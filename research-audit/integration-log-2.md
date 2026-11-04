# Integration log 2 — source-pack deepening into catalogue + release (4 Nov 2026, second session)
Supervised milestone: integrate the verified source-pack readings (research-audit/source-pack-2026-11-04.md) into the shared catalogue AND the redesign-preview release. All changes uncommitted (no git operations per instruction).

## Reading-level verification performed before integration
- 5 health abstracts independently re-verified this session by the audit session (not the subagent): Goh and Tao via direct publisher-page fetches (exact figures confirmed on-page: '76% (IQR, 66%-87%)… 74%', '2,069 patients', '28.7% reduction'); Hernström, Olson, Ruamviboonsuk via the Europe PMC API (title/journal/year/methods match; abstract text retrieved). Combined with the earlier PMC spot-checks (Takita, Kazemzadeh), all 7 health studies have been independently re-verified against originals.
- The 4 Africa items were read directly by the audit session (CIPIT exec summary, GIZ framing + Ghana case, Pidoux abstract, IrokoBench abstract — extractions archived in sources/pdfs/).
- The 3 LatAm items were read directly by the audit session (Latam-GPT page, Fundar column in Spanish, Fairwork organisational site).
- Dedupe: 0 DOI/URL/title overlaps with the 372-record baseline (checked before adding).

## Catalogue additions (14 records; 372 → 386)
- Health (7): goh-llm-diagnostic-rct (F, PMC full text), hernstrom-masai-2025 (V, abstract via Europe PMC), kazemzadeh-zambia-tb-2024 (F, PMC full text + re-verified), olson-ambient-scribes-2025 (V, abstract), takita-genai-meta-2025 (F, PMC full text + re-verified), ruamviboonsuk-thailand-dr-2022 (V, abstract), tao-prea-chatbot-2026 (V, publisher page).
- Africa (4): cipit-state-ai-africa-2025 (V, exec summary + structure), giz-invisible-workers-2026 (V, opening + key passages), pidoux-data-labour-africa-2025 (V, abstract), irokobench-2024 (V, abstract).
- Latin America (3): latamgpt-cenia (V, official page), fundar-argentina-ai-2025 (V, page in full, Spanish), fairwork-latam-2025 (V, organisational site).
- Reading-depth labels are per-record in the verification fields; blocked items (Therabot, Isagah ACM) remain LEADS in research-audit/source-pack-2026-11-04.md and were NOT added.

## New sourced edges (3; graph v0.9, 70 links) — each with exact supporting passages in the edge note
1. society/health → how/evaluation — Takita pooled accuracy 52.1% (76% high risk of bias) + Goh RCT non-transfer (P=.60). Claim is about evidence quality, not that health AI fails.
2. how/evaluation → society/participation — IrokoBench: 'low-resource languages… often evaluated only on basic text classification tasks due to the lack of appropriate or comprehensive benchmarks'. The paper does not claim benchmark access causes inclusion (labelled).
3. economics/jobs → society/participation — Fairwork five principles incl. 'Fair Representation — Support for workers' voice, organising, and good-faith negotiation' across six Latin American countries (2025 reports). Country scores not verified on the page read (labelled).

## Release integration (backups: research-audit/backups-2026-11-04/; pre-integration SHAs recorded)
- data.js: TOPIC_SOURCES → 386-state bridge (973 topic-record links, 816 read-mapped, 38/38 topics); READING_NOTES + AUDIT_NOTES extended by 14 entries each (372→386).
- galaxy.html: same four consts spliced (TOPIC_SOURCES, READING_NOTES 372→386, AUDIT_NOTES 372→386, RESEARCH_LINKS 67→70). GALAXY world topic items for health/copyright: redundant hand-added sources arrays REMOVED (they duplicated bridge URLs with different canonical forms, causing a visible double-reading on the map panel — found in browser verification).
- connection-evidence.js: 67→70 edges.
- translations.js: unchanged from the previous milestone (Indonesian entries for health/copyright already present; other languages on documented English fallback).

## i18n stall fix (narrow, release-owner sanctioned by this milestone)
- Diagnosis: the map's translation walker scheduled refreshes via requestAnimationFrame only; when the tab is backgrounded the rAF pauses, `queued` stays true, and every later schedule() call is a no-op — newly rendered panels keep English labels even though the dictionary (verified live on the page) has the Indonesian strings. A manually translated node persists, confirming data presence.
- Fix (one line in i18n.js): schedule() now also sets a 150 ms setTimeout fallback so a queued refresh always eventually runs: `requestAnimationFrame(refresh); setTimeout(refresh,150)`. refresh() is idempotent (queued=false at entry, originals WeakMap preserves first-seen text).
- Verification: after the fix, switching language to Bahasa Indonesia via the release's own selector translated the frame (`documentElement.lang="id"`), world and topic labels rendered Indonesian ("Sikap publik…", "Kesehatan & kedokteran", "Hak cipta & karya kreatif"), and the Copyright topic panel rendered the USCO reading in full. i18n.js parse-checked with node.

## Validation
- checks.py ALL PASS (386 records, 70 links, 0 broken refs, CSV=JSON, 38/38 topics).
- Parity suite T1–T6 + T7 ALL PASS at the 386-state: bridge parity per record per topic; world topics == graph topics; CONNECTION_EVIDENCE == graph == RESEARCH_LINKS (70); notes cover 386/386 in all four stores; no stale 36-topic counts; WHO wording corrected everywhere; NITI seven-principles text present; no duplicate Health readings (T6d); id translations present (T7).
- node eval: galaxy.html consts parse; GALAXY worlds society:5 / politics:5; bodies intact after the sources-array removal.
- Real browser flows: Health topic page in the Catalogue view renders all 9 society/health readings (7 pack + AEGIS + WHO) with notes and depth details; Copyright topic 1 reading (USCO) with note; Indonesian mode renders translated world and topic labels with the fix; map page-side check: the app's own builder produces 9 readings for society/health in the live page; jobs-topic filter finds the GIZ report.
- Map-panel visual nuance: on the galaxy.html map, the Health topic panel opened with title but the readings list required the panel's own detail toggle ("Show topic details"); the app's builder output was verified page-side (9 readings) so the data is present — noted as an interaction detail, not a data gap.

## Failures and limitations
- Subagent: both Africa and LatAm subagents failed on concurrency limits (previous milestone); no subagents used this session — the work was done directly.
- Therabot (NEJM AI) remains a blocked LEAD (403/Cloudflare); Isagah (ACM) remains a 403 LEAD; Brookings/Argentina-pipeline figures remain unverified leads.
- The map-panel readings list requires the "Show topic details" toggle in the galaxy.html experience — interaction detail, verified page-side.
- The institutionAbsences string in build_topic_sources.py still needs re-derivation (queued in the handoff).
- ruamviboonsuk-thailand-dr-2022 (2022) slightly predates the 2023–2026 window preference; included deliberately for LMIC geography.
