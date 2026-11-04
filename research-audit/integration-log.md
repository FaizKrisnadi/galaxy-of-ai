# Integration log — verified nine-reading batch into redesign-preview (4 Nov 2026)
Supervised milestone executed by the audit session. Corrections from `audit-nine-readings-and-edges.md` were applied to shared files first, then the release data was regenerated and integrated. All changes uncommitted (no git operations per instruction).

## Shared files (corrections + one tag fix)
1. **india-niti-responsible-ai** — verification corrected: **seven** principles (the seventh, "protection and reinforcement of positive human values", verified in the document's own list; the earlier six-principle note arose from a truncated extraction view).
2. **au-continental-ai-strategy** — date field corrected to the document's own foreword: adopted by the AU Executive Council, **45th Ordinary Session, 18–19 July 2024, Accra** (the "Aug 2024" earlier note was the webpage posting date).
3. **who-lmm-guidance** — quote corrected to the release's "published with outcomes disaggregated **by the type of user**"; scope line added (WHO recommends mandatory post-release auditing; not established as an in-force requirement).
4. **kapoor-normal-technology** — quote corrected to the essay's "the **right** analogy is nuclear power".
5. **japan-ai-guidelines-business** — Ver. 1.1 (Mar 2025) marked search-derived/unknown-from-material-read.
6. **aegis-postmarket** — `society/health` added to galaxy_tags (justified: it is the medical-AI post-market demonstration on the health topic card; found missing when the map panel showed its reading without a note).
7. build_graph.py WHO edge note corrected (same wording/scope); graph v0.8.1 rebuilt (38 topics / 67 links); catalogue.csv regenerated; root galaxy.html TOPIC_SOURCES block regenerated via build_topic_sources.py (git diff: one line).
8. `build_topic_sources.py` "built" stamp made current (2026-11-04).

## Release files integrated (backups in research-audit/backups-2026-11-04/)
- **data.js**: TOPIC_SOURCES replaced with the 372-state bridge (927 topic-record links, 793 read-mapped, 38/38 topics); READING_NOTES + AUDIT_NOTES extended by 13 entries (9 new readings + 4 pre-existing records that lacked notes: aegis-postmarket, chincholikar-incident-disclosure, hoch-mugge-brussels, openai-long-horizon-safety); GALAXY.worlds: `society` gained the "health" topic item and `politics` the "copyright" topic item (id/title/tagline/body/unknown/sources, matching the release's own item shape).
- **galaxy.html**: embedded TOPIC_SOURCES/READING_NOTES/AUDIT_NOTES spliced to the same state (AUDIT_NOTES now 372, READING_NOTES 372); GALAXY worlds extended with the same two topic items (surgical JS-literal insertion after `trust` and `accountability`); embedded RESEARCH_LINKS extended 65→67 edges.
- **connection-evidence.js**: 65→67 edges (both new sourced edges, with the corrected WHO note).
- **translations.js**: Indonesian entries added for both new topic titles and taglines under `id.ui`; all other languages intentionally left to the release's documented English fallback (a first pass briefly added Indonesian strings to all languages — caught and removed in the same session; verified final state: id translated, others fallback).

## Validation performed
- **Scripted**: checks.py ALL PASS (372 records, 67 links, 0 broken refs, CSV=JSON, 38/38 topics); parity suite T1–T6 ALL PASS (JSON parses; every catalogue record mapped under each of its topics; world topics == graph topics; CONNECTION_EVIDENCE == graph edges == galaxy.html RESEARCH_LINKS (67); notes cover 372/372 in all four stores; no stale 36-topic counts; WHO wording corrected everywhere; NITI seven-principles text present).
- **node eval** of the five modified galaxy.html consts: JS parses; worlds show society:5 / politics:5; both new topic items intact (3-paragraph bodies, correct sources arrays).
- **Real browser flows (IAB, loopback server on 127.0.0.1:8642)**:
  - Desktop map (index.html → Galaxy view): society world expands showing **5 topics incl. "Health & medicine"**; topic panel renders the three-paragraph body, "Still open" box, the sourced connection "health AI needs watching after deployment", and both readings with full notes and "What was read" details; politics world shows **"Copyright & creative work"** with the USCO reading.
  - Catalogue view: People & society → Health & medicine renders both readings with notes and depth details.
  - Galaxy map experience (galaxy.html): loads with 67 connection edges incl. both new ones (page-side check); screenshot confirms the new "Kesehatan & kedokteran" node on the map, connected, with the topic panel rendering (Indonesian UI shown due to persisted language; the astronaut guide greeting also localized — existing controls intact).
  - Mobile (390×844): Galaxy view society→health flow and Catalogue flow both render the new topic and readings; existing mobile nav works.
  - Existing controls preserved: AI outlook test opens and reaches its start screen; astronaut guide present; language selector present; Map/Read toggle and line guide intact; search filter intact.
  - Tabs marked handoff; local test server left running on 127.0.0.1:8642 (stop with: `kill $(lsof -ti :8642)`).

## Known limitations found during browser verification
1. **Translation refresh quirk (pre-existing release behaviour, not caused by this integration):** in the galaxy.html map, an already-rendered topic panel can keep its English label after the language changes or after new expansion renders — observed for the new "Copyright & creative work" topic (Indonesian strings verified present in the live GALAXY_TRANSLATIONS dictionary; a manually translated node persists, so it is the release's i18n walker refresh, not missing data). The Health topic translated correctly in the same state. A clean reload can return the map to English (language persistence differs between index.html's selector and the map). Flag to the release owner; fixing it means editing i18n.js — outside research integration.
2. The data.js/galaxy.html bridge "built" stamp is now 2026-11-04; the institutionAbsences string in build_topic_sources.py predates the interim 216-record expansion and still needs re-derivation.
3. Root galaxy.html's TOPIC_SOURCES block was regenerated (one-line diff) but root galaxy.html is NOT the live release; both copies now agree at 372-state.
