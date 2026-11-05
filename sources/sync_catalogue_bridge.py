#!/usr/bin/env python3
"""Refresh the catalogue bridge without modifying galaxy.html or guessing reading depth."""
import json
from datetime import date
from pathlib import Path

root = Path(__file__).resolve().parent
catalogue = json.loads((root / 'catalogue.json').read_text())['records']
path = root / 'topic_sources.json'
bridge = json.loads(path.read_text())
old = {r['id']: r for rows in bridge['byTopic'].values() for r in rows}
topics = {key: [] for key in bridge['byTopic']}
unmapped = []
for record in catalogue:
    ids = [x.strip() for x in record.get('galaxy_topics', '').split(',') if x.strip()]
    for tid in ids:
        if tid not in topics:
            unmapped.append((record['id'], tid))
            continue
        existing = old.get(record['id'], {})
        topics[tid].append({
            'id': record['id'], 'title': record['title'], 'url': record['url'],
            'tier': existing.get('tier', '?'),
            'tierLabel': existing.get('tierLabel', 'Reading depth: see the source note'),
            'inst': record.get('institution', ''), 'date': record.get('date', ''),
            'description': record.get('relevance', ''),
            'verification': record.get('verification', ''),
        })
if unmapped:
    raise SystemExit(f'Unknown topic references: {unmapped!r}')
for rows in topics.values():
    rows.sort(key=lambda r: r['title'].casefold())
links = sum(map(len, topics.values()))
mapped = {r['id'] for rows in topics.values() for r in rows}
read_links = sum(r['tier'] in ('F', 'V', 'O') for rows in topics.values() for r in rows)
indexed_links = sum(r['tier'] == 'L' for rows in topics.values() for r in rows)
bridge.update(built=date.today().isoformat(), byTopic=topics,
              zeroRecordTopics=[k for k, v in topics.items() if not v])
bridge['counts'] = {'records_total': len(catalogue), 'records_mapped': len(mapped),
                    'topic_record_links': links, 'read_mapped': read_links,
                    'indexed_only_mapped': indexed_links, 'topics_total': len(topics),
                    'other_or_unknown_mapped': links - read_links - indexed_links,
                    'topics_with_records': sum(bool(v) for v in topics.values()),
                    'topics_without_records': sum(not v for v in topics.values())}
path.write_text(json.dumps(bridge, ensure_ascii=False, indent=1) + '\n')
print(f'{len(mapped)}/{len(catalogue)} catalogue records mapped across {links} links; new reading tiers left unspecified')
