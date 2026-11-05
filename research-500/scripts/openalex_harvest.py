#!/usr/bin/env python3
"""OpenAlex harvest for Galaxy of AI research-500.

Queries OpenAlex for recent (2023+) AI-related works, reconstructs publisher
abstracts, dedupes against the current catalogue, and prints a readable digest
so the curator can read abstracts and compose relevance fields.

Usage: python3 openalex_harvest.py <cluster> [page]
Clusters are defined in CLUSTERS below.
"""
import json, re, sys, urllib.request, urllib.parse, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]

CLUSTERS = {
    "labour":      ("artificial intelligence labor market jobs employment wages", "economics/jobs"),
    "productivity":("generative AI productivity firms workers experiment", "economics/productivity, how/using"),
    "health":      ("large language models clinical medicine diagnosis patients", "society/health"),
    "energy":      ("data centers energy consumption water artificial intelligence electricity", "environment/energy, infrastructure/centres"),
    "governance":  ("artificial intelligence governance regulation policy act", "governance/rules, politics/national"),
    "education":   ("generative AI education students teachers learning outcomes", "society/skills, society/participation"),
    "agents":      ("LLM agents benchmark evaluation tool use autonomous", "how/agents, how/evaluation"),
    "misinfo":     ("AI-generated misinformation deepfakes detection elections", "society/trust"),
    "public":      ("algorithmic decision-making government public services citizens", "governance/discretion, governance/procurement"),
    "skills":      ("AI skills workforce training reskilling literacy", "society/skills, economics/jobs"),
    "healthlmic":  ("artificial intelligence diagnosis low-resource settings healthcare developing countries", "society/health, society/participation"),
    "copyright":   ("generative AI copyright training data intellectual property creative", "politics/copyright, how/data"),
    "infra":       ("data center siting community land use local impact", "infrastructure/land, environment/resources"),
    "invest":      ("artificial intelligence investment venture capital capital expenditure infrastructure", "economics/investment"),
    "agri":        ("artificial intelligence agriculture smallholder farmers developing countries extension", "economics/productivity, society/participation"),
    "lowres":      ("large language models low-resource languages multilingual benchmark translation", "how/models, society/participation"),
    "gridml":       ("machine learning electricity load forecasting smart grid renewable integration", "infrastructure/grids, environment/energy"),
    "aiforsci":     ("machine learning protein structure prediction drug discovery materials science", "how/models, society/health"),
    "embodied":     ("robotics foundation models embodied AI manipulation vision-language-action", "how/models, how/agents"),
    "speech":       ("speech recognition low-resource languages ASR multilingual models", "how/models, society/participation"),
    "surveillance": ("facial recognition policing bias surveillance automated", "society/trust, politics/accountability"),
    "fintech":      ("AI credit scoring financial inclusion machine learning lending", "economics/ownership, society/participation"),
    "supplychain":  ("artificial intelligence supply chain resilience logistics optimization", "economics/productivity"),
    "coding":       ("code generation large language models developer productivity experiment", "how/agents, economics/productivity"),
    "moderation":   ("AI content moderation platform governance harmful content", "society/trust, governance/rules"),
    "climateml":    ("machine learning climate modeling extreme weather prediction adaptation", "environment/goals, how/models"),
}


def norm_title(t):
    t = t.lower()
    t = re.sub(r"[^a-z0-9 ]", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def load_dedup():
    cat = json.loads((ROOT / "sources/catalogue.json").read_text())
    titles = {norm_title(r["title"]) for r in cat["records"]}
    urls = {r["url"].rstrip("/").lower() for r in cat["records"]}
    dois = set()
    for r in cat["records"]:
        if "doi.org/" in r["url"]:
            dois.add(r["url"].split("doi.org/")[-1].rstrip("/").lower())
        for m in re.findall(r"10\.\d{4,9}/[^\s\",]+", r["url"]):
            dois.add(m.rstrip(".").lower())
    return titles, urls, dois


def abstract_from_inv(inv):
    if not inv:
        return None
    pos = {}
    for w, idxs in inv.items():
        for i in idxs:
            pos[i] = w
    return " ".join(pos[i] for i in sorted(pos))


def fmt_date(w):
    d = w.get("publication_date") or ""
    return d or str(w.get("publication_year", ""))


def pick_url(w):
    doi = w.get("doi") or ""
    if doi:
        return doi
    oa = (w.get("best_oa_location") or {}).get("landing_page_url")
    return oa or w.get("primary_location", {}).get("landing_page_url") or ""


def main(cluster, page=1):
    if cluster not in CLUSTERS:
        print("unknown cluster", cluster)
        return
    q, default_topics = CLUSTERS[cluster]
    titles, urls, dois = load_dedup()
    params = {
        "search": q,
        "filter": "from_publication_date:2023-01-01,type:article|preprint|report",
        "per_page": "50",
        "page": str(page),
        "sort": "cited_by_count:desc",
    }
    url = "https://api.openalex.org/works?" + urllib.parse.urlencode(params)
    import time
    data = None
    for attempt in range(5):
        try:
            with urllib.request.urlopen(url, timeout=60) as r:
                data = json.loads(r.read().decode())
            break
        except urllib.error.HTTPError as e:
            if e.code in (429, 503) and attempt < 4:
                wait = 20 * (attempt + 1)
                print(f"(rate-limited; waiting {wait}s)", file=sys.stderr)
                time.sleep(wait)
            else:
                raise
    if data is None:
        print("failed after retries")
        return
    shown = 0
    for w in data.get("results", []):
        ab = abstract_from_inv(w.get("abstract_inverted_index"))
        if not ab or len(ab) < 200:
            continue
        title = (w.get("title") or "").strip()
        if not title:
            continue
        nt = norm_title(title)
        if nt in titles:
            continue
        wurl = pick_url(w)
        wl = wurl.rstrip("/").lower()
        doi = (w.get("doi") or "").replace("https://doi.org/", "").lower()
        if wl in urls or (doi and doi in dois):
            continue
        auths = w.get("authorships") or []
        names = [a.get("author", {}).get("display_name", "") for a in auths[:3]]
        insts = []
        for a in auths[:1]:
            for i in (a.get("institutions") or [])[:2]:
                insts.append(i.get("display_name", ""))
        src = (w.get("primary_location") or {}).get("source") or {}
        venue = src.get("display_name", "")
        shown += 1
        print(f"\n[{shown}] {title}")
        print(f"    by {', '.join(n for n in names if n)}{' et al.' if len(auths) > 3 else ''} | {fmt_date(w)} | {venue or '; '.join(insts)} | cited {w.get('cited_by_count', 0)} | OA {bool((w.get('open_access') or {}).get('is_oa'))}")
        print(f"    URL: {wurl}")
        print(f"    TOPICS(default): {default_topics}")
        print(f"    ABSTRACT: {ab}")
    print(f"\n== cluster '{cluster}' page {page}: showed {shown}, pool {data.get('meta', {}).get('count', '?')}")


if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 1)
