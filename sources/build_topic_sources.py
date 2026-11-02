#!/usr/bin/env python3
"""Bridge catalogue.json + graph.json into galaxy.html: per-topic record lists with
honest read-depth labels. Idempotent — regenerates the TOPIC_SOURCES block in place.
Indexed-but-never-read records are labelled as absences, not judgements."""
import json, pathlib, re

root = pathlib.Path(".")
cat = json.loads((root/"sources/catalogue.json").read_text())
g = json.loads((root/"sources/graph.json").read_text())
gal = (root/"galaxy.html").read_text()

def tier(v):
    def has(*pats): return any(x in v for x in pats)
    if has("full text (arXiv HTML) read", "partial full text (arXiv HTML) read", "full PDF obtained", "FULL PDF read", "FULL TEXT read"):
        return ("F", "full or partial text read")
    if has("official statistics page"):
        return ("O", "official statistic (independently checked)")
    if has("verified at origin", "verified-at-origin", "executive summary read", "dataset page read", "publication page", "abstract read", "page read"):
        return ("V", "verified/read at origin (not full text)")
    if has("Discovery"):
        return ("D", "Discovery Engine snapshot (not human-verified)")
    if has("handoff"):
        return ("H", "handoff-verified metadata (not read)")
    if has("located via"):
        return ("S", "located via search (not read)")
    if has("metadata from", "index"):
        return ("L", "indexed only \u2014 not read")
    return ("?", "provenance unclear")

topics = {t["id"]: t["title"] for t in g["topics"]}
by_topic = {tid: [] for tid in topics}
mapped_records = 0
read_mapped = 0
for r in cat["records"]:
    tier_key, tier_label = tier(r["verification"])
    for tid in r.get("galaxy_topics", "").split(", "):
        if tid in by_topic:
            by_topic[tid].append({"id": r["id"], "title": r["title"], "url": r["url"],
                                  "tier": tier_key, "tierLabel": tier_label,
                                  "inst": r["institution"]})
            mapped_records += 1
            if tier_key in ("F", "V", "O"): read_mapped += 1

zero = [tid for tid, lst in by_topic.items() if not lst]
# sort each list: read tiers first (F,V,O), then others; then by title
order = {"F":0, "V":1, "O":2, "D":3, "H":4, "S":5, "L":6, "?":7}
for tid in by_topic:
    by_topic[tid].sort(key=lambda x: (order.get(x["tier"], 9), x["title"]))

data = {
    "built": "2026-11-02",
    "counts": {
        "records_total": len(cat["records"]),
        "records_mapped": len({r["id"] for r in cat["records"] if r.get("galaxy_topics","").strip()}),
        "topic_record_links": mapped_records,
        "read_mapped": read_mapped,
        "indexed_only_mapped": mapped_records - read_mapped,
        "topics_total": len(topics),
        "topics_with_records": sum(1 for lst in by_topic.values() if lst),
        "topics_without_records": len(zero),
    },
    "zeroRecordTopics": zero,
    "institutionAbsences": ("DAIR \u00b7 Harvard BKC formal papers \u00b7 ETH AI Center papers \u00b7 Cambridge LCFI items \u00b7 "
                            "DeepMind per-paper items \u00b7 Meta AI site papers \u00b7 Vector Institute index \u00b7 RIKEN AIP \u00b7 "
                            "Tsinghua KEG beyond GLM \u00b7 Oxford Ethics items"),
    "byTopic": by_topic,
}

# write durable JSON
(root/"sources/topic_sources.json").write_text(json.dumps(data, indent=1, ensure_ascii=False))

# inject/refresh the const inside galaxy.html's main script
block_start, block_end = "/* ==TOPIC_SOURCES_START== */", "/* ==TOPIC_SOURCES_END== */"
const = block_start + "\nconst TOPIC_SOURCES = " + json.dumps(data, ensure_ascii=False) + ";\n" + block_end
if block_start in gal:
    gal = re.sub(re.escape(block_start) + r".*?" + re.escape(block_end), const, gal, flags=re.S)
else:
    anchor = '"use strict";\n'
    assert gal.count(anchor) == 1
    gal = gal.replace(anchor, anchor + "\n" + const + "\n")
(root/"galaxy.html").write_text(gal)

read_labels = {"F":0,"V":0,"O":0}
print(f"topic_record_links={mapped_records}  topics_with_records={data['counts']['topics_with_records']}/{len(topics)}  zero={zero or 'none'}  read_mapped={read_mapped}")
