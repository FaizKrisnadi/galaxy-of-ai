#!/usr/bin/env python3
"""Basic integrity checks for the Galaxy of AI research foundation files."""
import json, csv, sys, pathlib, re
ok = True
src = pathlib.Path("sources")
cat = json.loads((src/"catalogue.json").read_text())
g = json.loads((src/"graph.json").read_text())
recs, topics = cat["records"], {t["id"] for t in g["topics"]}

# 1 duplicate ids / urls
ids = [r["id"] for r in recs]
dups = {i for i in ids if ids.count(i) > 1}
print(f"1. records: {len(recs)}; duplicate ids: {sorted(dups) or 'none'}"); ok &= not dups
urls = [r["url"] for r in recs]
du = {u for u in urls if urls.count(u) > 1}
print(f"2. duplicate urls: {sorted(du) or 'none'}"); ok &= not du

# 2 broken topic refs in links
bad = [e for e in g["topic_links"] if e["from"] not in topics or e["to"] not in topics]
print(f"3. topic_links: {len(g['topic_links'])}; broken refs: {len(bad)}"); ok &= not bad

# 3 topics have >=1 domain; domains valid
doms = set(g["domains"])
bad2 = [t["id"] for t in g["topics"] if not t["domains"] or set(t["domains"]) - doms]
print(f"4. topics: {len(g['topics'])}; topics w/o valid domain: {bad2 or 'none'}"); ok &= not bad2
multi = [t["id"] for t in g["topics"] if len(t["domains"]) > 1]
print(f"   multi-domain topics: {len(multi)}/{len(g['topics'])}")

# 4 sources: url + date + verification present; galaxy_topics valid
miss_url = [r["id"] for r in recs if not r.get("url","").startswith("http")]
miss_date = [r["id"] for r in recs if not r.get("date")]
miss_ver = [r["id"] for r in recs if not r.get("verification")]
badt = [(r["id"], t) for r in recs for t in r.get("galaxy_topics","").split(", ") if t and t not in topics]
print(f"5. sources missing url: {miss_url or 'none'}; missing date: {miss_date or 'none'}; missing verification: {miss_ver or 'none'}")
print(f"6. source->topic refs broken: {badt or 'none'}")
ok &= not (miss_url or miss_ver or badt)

# 5 access-tier counts
from collections import Counter
tiers = Counter()
for r in recs:
    v = r["verification"]
    def has(*pats): return any(x in v for x in pats)
    if has("full text (arXiv HTML) read", "partial full text (arXiv HTML) read", "full PDF obtained", "FULL PDF read", "FULL TEXT read"): tiers["F full/partial-text read"] += 1
    elif has("verified at origin", "verified-at-origin", "executive summary read", "dataset page read", "publication page", "abstract read", "page read"): tiers["V verified/read at origin"] += 1
    elif has("Discovery"): tiers["D DiscoveryEngine-snapshot"] += 1
    elif has("handoff"): tiers["H handoff-verified"] += 1
    elif has("located via"): tiers["S search-located"] += 1
    elif has("official statistics page"): tiers["O official-statistics (Faiz-verified)"] += 1
    elif has("metadata from", "index"): tiers["L list-metadata/index"] += 1
    else: tiers["OTHER"] += 1
vread = sum(1 for r in recs if any(x in r["verification"] for x in ("verified at origin","verified-at-origin","executive summary read","dataset page read","publication page","abstract read","page read")) and "not read" not in r["verification"] and "not opened" not in r["verification"])
print(f"   records with read-related phrases (heuristic, not proof of reading): {vread}")

# 6 csv consistency
with (src/"catalogue.csv").open() as f:
    rows = list(csv.DictReader(f))
fields = rows[0].keys() if rows else []
expected = [{k: str(r.get(k, "")) for k in fields} for r in recs]
match = rows == expected
print(f"8. catalogue.csv rows: {len(rows)}; fields match json: {match}")
ok &= match

print("\nRESULT:", "STRUCTURAL CHECKS PASS (source claims not verified)" if ok else "CHECKS FAILED")
sys.exit(0 if ok else 1)
