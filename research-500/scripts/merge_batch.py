#!/usr/bin/env python3
"""Merge subagent candidate JSON files into the Galaxy of AI catalogue.

Deduplicates against existing records AND within the batch by:
  - record id
  - exact URL (normalised: lowercase, trailing slash stripped)
  - DOI (from doi.org URLs and from any DOI-looking strings in url)
  - normalised title (case/punctuation-insensitive)

Input: research-500/agent-outputs/<glob>.json — each file a JSON array of records with fields:
  id, title, authors, date, institution, type, url, galaxy_topics, access, verification, relevance
Records flagged "lead": true are integrated with their stated metadata-only depth.

Usage: python3 research-500/scripts/merge_batch.py 'research-500/agent-outputs/batch1-*.json'
"""
import json, csv, re, sys, glob, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
SRC = ROOT / "sources"
CAT = SRC / "catalogue.json"
CSVF = SRC / "catalogue.csv"
GRAPH = SRC / "graph.json"

graph = json.loads(GRAPH.read_text())
VALID_TOPICS = {t["id"] for t in graph["topics"]}


def norm_title(t):
    t = t.lower()
    t = re.sub(r"[^a-z0-9 ]", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def norm_url(u):
    return u.strip().rstrip("/").lower()


def extract_dois(u):
    dois = set()
    if "doi.org/" in u:
        dois.add(u.split("doi.org/")[-1].rstrip("/").lower())
    for m in re.findall(r"10\.\d{4,9}/[^\s\"^,]+", u):
        dois.add(m.rstrip(".").lower())
    return dois


def load():
    cat = json.loads(CAT.read_text())
    recs = cat["records"]
    have_ids = {r["id"] for r in recs}
    have_urls = {norm_url(r["url"]) for r in recs}
    have_titles = {norm_title(r["title"]) for r in recs}
    have_dois = set()
    for r in recs:
        have_dois |= extract_dois(r["url"])
    return cat, recs, have_ids, have_urls, have_titles, have_dois


def slugify(title):
    s = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    return s[:60]


def main(pattern):
    cat, recs, have_ids, have_urls, have_titles, have_dois = load()
    before = len(recs)
    files = sorted(glob.glob(pattern))
    if not files:
        print("no files matched", pattern)
        return 1
    stats = {"files": 0, "candidates": 0, "integrated": 0, "dup_url": 0, "dup_title": 0,
             "dup_doi": 0, "dup_id": 0, "invalid": 0, "leads": 0, "bad_topic": []}
    for fp in files:
        try:
            cands = json.loads(pathlib.Path(fp).read_text())
        except Exception as e:
            print(f"!! {fp}: unparseable JSON: {e}")
            stats["invalid"] += 1
            continue
        if not isinstance(cands, list):
            print(f"!! {fp}: not a JSON array")
            stats["invalid"] += 1
            continue
        stats["files"] += 1
        for c in cands:
            stats["candidates"] += 1
            missing = [k for k in ("title", "authors", "date", "institution", "type",
                                   "url", "galaxy_topics", "access", "verification",
                                   "relevance") if not c.get(k)]
            if missing:
                print(f"   invalid (missing {missing}): {str(c.get('title'))[:60]}")
                stats["invalid"] += 1
                continue
            url = c["url"].strip()
            if not url.startswith("http"):
                print(f"   invalid (url not http): {c['title'][:60]}")
                stats["invalid"] += 1
                continue
            gt = c["galaxy_topics"]
            if isinstance(gt, list):
                gt = ", ".join(str(t) for t in gt)
            topics = [t.strip() for t in gt.split(",") if t.strip()]
            bad = [t for t in topics if t not in VALID_TOPICS]
            if bad:
                stats["bad_topic"].append((c["title"][:50], bad))
                stats["invalid"] += 1
                continue
            nu, nt = norm_url(url), norm_title(c["title"])
            nd = extract_dois(url)
            if nu in have_urls:
                stats["dup_url"] += 1
                continue
            if nt in have_titles:
                stats["dup_title"] += 1
                continue
            if nd & have_dois:
                stats["dup_doi"] += 1
                continue
            rid = (c.get("id") or slugify(c["title"])).strip()
            rid = re.sub(r"[^a-z0-9-]", "-", rid.lower())
            base = rid
            n = 2
            while rid in have_ids:
                rid = f"{base}-{n}"
                n += 1
            rec = dict(id=rid, title=c["title"].strip(), authors=c["authors"].strip(),
                       date=c["date"].strip(), institution=c["institution"].strip(),
                       type=c["type"].strip(), url=url,
                       galaxy_topics=", ".join(topics), access=c["access"].strip(),
                       verification=c["verification"].strip(),
                       relevance=c["relevance"].strip())
            recs.append(rec)
            have_ids.add(rid)
            have_urls.add(nu)
            have_titles.add(nt)
            have_dois |= nd
            stats["integrated"] += 1
            if c.get("lead"):
                stats["leads"] += 1
    cat["counts"]["total"] = len(recs)
    CAT.write_text(json.dumps(cat, indent=1, ensure_ascii=False) + "\n")
    # rewrite CSV with identical field order
    fields = list(recs[0].keys())
    with CSVF.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in recs:
            w.writerow({k: str(r.get(k, "")) for k in fields})
    print(f"\nfiles: {stats['files']}  candidates: {stats['candidates']}")
    print(f"integrated: {stats['integrated']}  (leads: {stats['leads']})")
    print(f"excluded: dup_url {stats['dup_url']}, dup_title {stats['dup_title']}, "
          f"dup_doi {stats['dup_doi']}, invalid {stats['invalid']}, dup_id-recycled (n/a)")
    if stats["bad_topic"]:
        print("bad topics:", stats["bad_topic"][:10])
    print(f"catalogue: {before} -> {len(recs)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "research-500/agent-outputs/*.json"))
