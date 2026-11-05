#!/usr/bin/env python3
"""Refresh local preview reading snapshots without overwriting editorial notes."""
import json
import pathlib
import re

root = pathlib.Path(__file__).resolve().parent
bridge = json.loads((root.parent / 'sources/topic_sources.json').read_text())
data_path = root / 'data.js'
raw = data_path.read_text()
data = json.loads(raw.removeprefix('window.DATA=').rstrip(';\n'))

# Muse's newer public-release snapshot may have hand-written notes absent from
# this preview. Prefer them to the catalogue fallback, while retaining any
# pre-existing preview-specific notes.
public = (root.parent / 'public-release/index.html').read_text()
for name in ('READING_NOTES', 'AUDIT_NOTES'):
    match = re.search(r'^const ' + name + r'\s*=\s*(\{.*\});\s*$', public, flags=re.M)
    if match:
        for rid, note in json.loads(match[1]).items():
            if not data[name].get(rid) or any(
                record['id'] == rid and data[name][rid] == record.get('description' if name == 'READING_NOTES' else 'verification')
                for entries in bridge['byTopic'].values() for record in entries
            ):
                data[name][rid] = note

# Existing hand-written notes remain authoritative; catalogue material fills gaps.
for entries in bridge['byTopic'].values():
    for record in entries:
        rid = record['id']
        if not data['READING_NOTES'].get(rid) and record.get('description'):
            data['READING_NOTES'][rid] = record['description']
        if not data['AUDIT_NOTES'].get(rid) and record.get('verification'):
            data['AUDIT_NOTES'][rid] = record['verification']
data['TOPIC_SOURCES'] = bridge
encoded = lambda value: json.dumps(value, ensure_ascii=False, separators=(',', ':'))
data_path.write_text('window.DATA=' + encoded(data) + ';\n')

galaxy_path = root / 'galaxy.html'
galaxy = galaxy_path.read_text()
galaxy, count = re.subn(r'(/\* ==TOPIC_SOURCES_START== \*/\s*const TOPIC_SOURCES\s*=\s*).*?(;\s*/\* ==TOPIC_SOURCES_END== \*/)', lambda m: m[1] + encoded(bridge) + m[2], galaxy, count=1, flags=re.S)
if count != 1:
    raise ValueError('Could not locate the galaxy source snapshot')
for name in ('READING_NOTES', 'AUDIT_NOTES'):
    pattern = r'(^const ' + name + r'\s*=\s*).*?(;\s*$)'
    galaxy, count = re.subn(pattern, lambda m: m[1] + encoded(data[name]) + m[2], galaxy, count=1, flags=re.M)
    if count != 1:
        raise ValueError(f'Could not locate {name}')
galaxy_path.write_text(galaxy)
print(f"Synced {bridge['counts']['records_mapped']} catalogue records across {bridge['counts']['topic_record_links']} topic links")
