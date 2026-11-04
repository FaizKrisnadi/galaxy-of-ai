# Safe integration plan — bringing reviewed additions into the CURRENT Galaxy release
Written 4 Nov 2026 by the audit session. NO release file was edited in preparing this plan; everything below is a proposal for the release owner to apply.

## 0. What the current release actually is (verified 4 Nov)
Live release files: `redesign-preview/index.html` (34.6 KB, 4 Nov 02:08), `redesign-preview/galaxy.html` (663.8 KB, 4 Nov 02:08), `redesign-preview/data.js` (539.6 KB, 3 Nov 23:47), `redesign-preview/connection-evidence.js` (29.8 KB, 4 Nov 01:24), `redesign-preview/i18n.js`, `redesign-preview/translations.js` (80.6 KB), plus `assets/`.
- `data.js` sets `window.DATA` = { GALAXY: {sun, worlds[7: how, infrastructure, economics, society, governance, politics, environment]}, outlookAxes[6], futureQuestions[18], TOPIC_SOURCES, READING_NOTES, AUDIT_NOTES }.
- `TOPIC_SOURCES` inside data.js is the standard bridge schema (built/counts/zeroRecordTopics/institutionAbsences/byTopic) **at the 2 Nov interim state: 363 records, 899 topic-record links, 781 read-mapped, 36 topics**.
- `READING_NOTES` and `AUDIT_NOTES`: 359 entries each, keyed by record id, plain-English per-record summaries.
- `connection-evidence.js` sets `window.CONNECTION_EVIDENCE` = array of 65 edge objects {from, to, relation, kind, note} — exactly the pre-v0.8 graph (40 sourced / 25 association).
- Root `galaxy.html` also carries a TOPIC_SOURCES block, but it is NOT the live release.

**Verified deltas between the shared research files and the release:**
1. The 9 Addendum-38 records (au-continental-ai-strategy, ilia-2025-exec-summary, uscopyright-ai-part2, who-lmm-guidance, grace-ai-authors-2024, crfm-foundation-models-report, kapoor-normal-technology, india-niti-responsible-ai, japan-ai-guidelines-business) are absent from the release bridge, READING_NOTES, AUDIT_NOTES.
2. The 2 new topics (society/health, politics/copyright) are absent from the worlds' topic lists and the bridge.
3. The 2 new sourced edges are absent from CONNECTION_EVIDENCE (bridge: graph has 67 edges vs release 65).
4. Four PRE-EXISTING records lack READING_NOTES/AUDIT_NOTES entries even at the release state: aegis-postmarket, chincholikar-incident-disclosure, hoch-mugge-brussels, openai-long-horizon-safety.
5. Catalogue/graph now stand at 372 records / 38 topics / 67 links (checks pass; bridge 926 links, 792 read-mapped).

## 1. Preconditions
1. Land or coordinate the concurrent `research-guides/` work first — do not integrate while another session is writing.
2. Git baseline: commit or stash current modifications (the tree already carries the shared-file additions); record the three release files' current SHA-256 for rollback.
3. Apply the audit corrections FIRST (see audit-nine-readings-and-edges.md corrections queue): WHO quote wording + recommendation-scope, Kapoor "right analogy", AU adoption-date provenance, Japan Ver. 1.1 provenance. Integrating uncorrected text would bake the errors into the release.
4. Re-run `python3 sources/checks.py` and confirm ALL PASS before touching the release.

## 2. Steps (each independently revertible)
**Step A — regenerate the bridge for data.js.** Run the project bridge (`python3 sources/build_topic_sources.py` writes topic_sources.json and the root-galaxy block) and copy the fresh JSON object into data.js's `TOPIC_SOURCES` key, replacing the 2 Nov object. Expected new counts: records_total 372, topic_record_links 926, read_mapped 792, topics_total 38. Keep `institutionAbsences` only if re-derived (it is stale: written before the interim 216-record expansion — recommend re-deriving from the catalogue before display).
**Step B — add the two topics to the worlds.**
- society world, append after "trust": {id:"health", title:"Health & medicine", tagline:"where AI meets care", body:[2–4 short <p> blocks summarising: WHO LMM guidance (40+ recommendations; five application areas; mandatory post-release auditing recommended — a recommendation, not an in-force rule), AEGIS proof-of-concept, Takita 2025 meta-analysis caveat (pooled generative-AI diagnostic accuracy 52.1%, worse than expert physicians, 76% high risk of bias)]}. Reference readings: who-lmm-guidance, aegis-postmarket, plus the source-pack health studies once reviewed.
- politics world, append after existing topics: {id:"copyright", title:"Copyright & creative work", tagline:"who owns AI outputs", body:[USCO Part 2 bullets: existing law suffices; no copyright in purely AI-generated material; prompts alone insufficient; no new sui generis right; human authors keep copyright in perceptible contributions]}. Reference reading: uscopyright-ai-part2.
- Note the worlds' topic ids are unprefixed (e.g. "attitudes") while graph/bridge ids are prefixed ("society/health") — replicate the release's own convention when adding.
**Step C — add the reading notes.** Add READING_NOTES + AUDIT_NOTES entries for the 9 new records AND the 4 missing pre-existing ones (aegis-postmarket, chincholikar-incident-disclosure, hoch-mugge-brussels, openai-long-horizon-safety), using each record's `relevance`/`verification` text compressed to the release's plain-English note style (~600–1,200 chars). Include the corrections from the audit (WHO wording/scope; Kapoor wording).
**Step D — add the two edges.** Append to `window.CONNECTION_EVIDENCE` the two objects copied verbatim from sources/graph.json topic_links (from/to/relation/kind/note), after applying the audit corrections to the WHO note.
**Step E — translations.** `translations.js` translates world/topic titles. Add per-language entries for "Health & medicine" and "Copyright & creative work" (Indonesian drafts: "Kesehatan & kedokteran", "Hak cipta & karya kreatif") or confirm the documented English fallback; the file header states untranslated library content remains in English.
**Step F — no changes expected** to outlookAxes/futureQuestions (they reference existing topics), index.html, galaxy.html UI code, or i18n.js. Verify by diff that these files are byte-identical after integration.

## 3. Tests (run after each step; all must pass before shipping)
T1. `node -e "const d=require('./data.js')"` equivalent or a headless parse: data.js and connection-evidence.js parse without error.
T2. Bridge parity: every catalogue.json record id appears in TOPIC_SOURCES.byTopic under each of its galaxy_topics; counts object equals checks.py output (372 / 926 / 792 / 38 / 38).
T3. Topic integrity: each world's topic ids + domain prefix exist in graph.json topics (38); no duplicate topic id within a world; society/health and politics/copyright each have ≥1 mapped record (who-lmm-guidance; uscopyright-ai-part2).
T4. Edge parity: CONNECTION_EVIDENCE has exactly the 67 graph.json edges, same from/to/kind; no duplicates.
T5. Notes parity: every record id has a READING_NOTES entry (372/372) and an AUDIT_NOTES entry; spot-read 5 for tone (plain English, no causal overclaims).
T6. Translations: new topic titles resolve in each language file or fall back to English without key errors in console.
T7. Browser smoke test (manual, per release): load redesign-preview/index.html → open the society planet → Health & medicine topic renders with its readings → politics planet → Copyright & creative work renders → open one new reading's note → connection inspector lists the 2 new edges → no console errors → astronaut/guide and AI test flows still work.
T8. Rollback check: restoring the three recorded SHA-256 file versions returns the release to the pre-integration state.

## 4. Explicit non-goals
Do not touch: root galaxy.html in the same change, research-guides/, connection-map-preview/, connection-preview/, .wrangler/, any shared catalogue/graph file during integration (the plan assumes shared files are already final), and no git operations from the research sessions.
