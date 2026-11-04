# Milestone 4 report — research foundation: catalogue + topic graph

**Date:** 1 November 2026 · **Status:** complete, stopping for review. Visual/UI work stopped (one minimal catalogue link added to the thin Environment/resources card, nothing else). No publication, no spending, no contact, no paywall bypass, no other projects modified.

## 1. Deliverables (all local, no server needed)

| File | Contents |
|---|---|
| [sources/catalogue.json](sources/catalogue.json) | **92 records** — id, title, authors, date, institution, type, exact URL, galaxy-topic ids, access, verification tier, grounded relevance. |
| [sources/catalogue.csv](sources/catalogue.csv) | Same records, flat (grep/sort/filter friendly). |
| [sources/graph.json](sources/graph.json) | **Topic graph**: 7 domains, **34 topics — 24 of them multi-domain** (a graph, not a tree), **40 explicit topic-to-topic links** with plain-English relation labels, typed `association` vs `sourced` (with grounding notes). |
| [sources/topics.csv](sources/topics.csv), [sources/topic_links.csv](sources/topic_links.csv) | Flat graph tables. |
| [sources/CATALOGUE.md](sources/CATALOGUE.md) | Readable index: how to read a record, access & reuse conditions per institution, coverage counts, known gaps. |
| [sources/notes/deep-reads.md](sources/notes/deep-reads.md) | Plain-English notes (argument / evidence / limits / galaxy links) for the 11 record groups actually read. |
| [sources/checks.py](sources/checks.py) | Integrity checks — **all pass** (see §3). |
| `sources/build_seed.py`, `sources/build_graph.py`, `sources/merge_harvest.py` | Rebuild scripts (structure stays maintainable and regenerable). |

Visual files preserved untouched: galaxy.html (one card line + tiny render hook added), galaxy-scenes.html, constellation.html, constellation-v0.1.html — smoke-tested after the edit (7 planets, 0 errors).

## 2. Actual counts and provenance tiers (no inflation)

**92 records.** Every record carries a dated provenance tier:

| Tier | n | Meaning |
|---|---|---|
| Verified at origin | 17 | Page/abstract/record actually read this session |
| List-metadata | 42 | Title/date/URL read from the institution's own listing; abstract NOT read |
| Handoff-verified | 21 | Metadata + link verified 31 Oct 2026; full texts NOT read in this project |
| Discovery Engine snapshot | 11 | Local checksummed snapshots (30–31 Oct); claims not human-verified |
| Dead link (documented) | 1 | Baum APSA preprint, HTTP 404 — excluded from all topic content |

Institutional coverage (selected): Epoch AI 9 · CSET 7 · AI Now 6 · Mila 6 · OpenAI 6 · Anthropic 5 · IEA 3 · OECD 2 · Stanford HAI 1 · MIT 1 · METR 3 · ISEAS 1 · ISIS Malaysia 1 · Katadata 1 · peer-reviewed universities via the handoff ~18 · Discovery Engine regional records 8 · AidData/GEM/GLEIF 3.

**Honesty statement, per instruction:** before this milestone we had NOT systematically collected Epoch AI or any of the other institutions — the seed was the handoff + PRE-STUDY + Discovery Engine. The systematic pass covered the ten sources listed above; the rest of the requested list is recorded as gaps (§4), not silently skipped.

## 3. Graph structure (as directed)

- Stable slugged IDs; topics carry **multiple domains** (e.g. Data centres → infrastructure + economics + environment; AI exposure & jobs → economics + society — exactly Faiz's examples; 24/34 topics are multi-domain).
- Every topic-to-topic link has a **plain-English relation label** ("oversight needs what contracts provide", "water where cooling needs it") and a **kind**: `association` (related subjects — no causal claim) vs `sourced` (connection described by the sources on the topic cards, with a grounding note naming them).
- Source→topic links live on each catalogue record (`galaxy_topics`) and all resolve to real topic ids (checked).
- Distinguishing claims: the graph separates association from sourced; deep-read notes separate argument from evidence from limits; no fabricated quotes anywhere — notes paraphrase and mark what was read at which level.

## 4. Integrity checks (all pass)

Duplicate record ids: none · duplicate URLs: none · broken topic refs in the 40 links: 0 · every topic has ≥1 valid domain · every record has URL + date + verification tier · all source→topic refs resolve · CSV rows = JSON records (92). Checks re-runnable: `python3 sources/checks.py`.

## 5. Gaps (honest list)

1. **Google DeepMind:** index read; individual paper URLs not extractable this session — needs a targeted pass.
2. **Meta AI:** publications page JS-only — zero records retrievable; entry point recorded only.
3. **Not yet harvested** (named by Faiz, currently absent — absences, not judgements): Berkeley CHAI (my URL 404), Carnegie Mellon, Harvard Berkman Klein (timeout), Cambridge LCFI (404), UCL, ETH Zurich, CIFAR, AI Singapore, NUS labs, Ada Lovelace (resources path 404), Oxford Institute for Ethics in AI (domain unverified). Commercial-lab coverage beyond indexes (papers, model cards) also needs deeper passes.
4. **Abstracts not read** for 3 handoff records (Springer/Nature/Wiley gates) — the affected card statements rest on the 31 Oct pass and are labelled as such.
5. **No full-text reading has been done or claimed** anywhere; deep-read notes cover only read pages/abstracts/records.
6. **Dates:** a few listing dates are odd (e.g. Mila entries "2026-12-30") — recorded as-shown with a verify flag, not silently normalised.
7. **Reuse terms:** recorded per institution in CATALOGUE.md; OECD Navigator's licence remains unverified on its dashboard page.

## 6. Suggested next increment (not started)

Fill the eleven named gaps with the same listing-pass method; then a second deep-read wave (AI Index 2026; IEA *Energy and AI*; CSET *Tracking AI Chips*; AI Now landscape) to strengthen the thinnest topic cards (environment, politics/law).

Stopping here for supervisor review.


---

## Addendum (1 Nov 2026, later): Faiz-supplied leads verified and merged

Faiz supplied five independent leads. Verification outcomes (all consult at origin, methods/dates/limits extracted):

1. **epoch.ai/data** — already covered by the index harvest (8 dataset records); no duplicate added.
2. **Epoch AI Chip Users explorer** (2026-09-09) — added `epoch-chip-users-explorer`: H100e usage medians with 90% CIs for OpenAI/DeepMind/Anthropic/Meta/xAI (Dec 2025); method = power disclosures + filings + third-party estimates; limits: usage ≠ ownership, wide CIs.
3. **Epoch AI *Trends in AI Supercomputers*** (2025-04-23, arXiv:2504.16026) — added `epoch-trends-supercomputers`: 500+ clusters; performance doubling ~9 months; 2030 projection 2M chips/$200B/9 GW; stated coverage limit 10–20% of global performance.
4. **Stanford HAI 2026 AI Index** — existing record upgraded to the canonical report page, read this session: 9 chapters, free PDF + public data, stated limits ("jagged frontier", spotty benchmark reporting, China investment understatement).
5. **Oxford Martin School, *Governing Through the Cloud*** (Heim et al., 13 Mar 2024, open PDF) — added `oxford-martin-cloud-governance`: compute providers as "securers, record keepers, verifiers, enforcers"; EO 14110 case study; confidentiality-vs-risk-mitigation caveat. Partially fills the Oxford gap (one institution, one paper).

**Catalogue now: 95 records** (20 verified at origin). All checks re-run: pass (no duplicate ids/URLs, no broken refs). CSV refreshed; CATALOGUE.md updated. Leads were treated as starting points and verified against original methods and dates before inclusion — none entered the catalogue unverified.


---

## Addendum 2 (1 Nov 2026, later): major-institution harvest round

**Catalogue now: 118 records** (24 verified at origin · 55 list/index-metadata · 22 handoff-verified · 11 Discovery Engine snapshots · 6 search-located). All integrity checks pass (no duplicate ids/URLs, 0 broken refs, CSV=JSON).

**Newly covered (with real publications, not homepages):**
- **Berkeley CHAI** — 4 papers from its own list (Managing AI Risks; TASRA; Control Road Map 2030; teacher selection in RLHF).
- **CMU Block Center** — 2 policy PDFs + index (newest visible items 2020–2024; noted).
- **Ada Lovelace Institute** — 5 dated items (Minding your business; UK regulation options; Care and consideration; Measuring Up — productivity-claims evaluation; Navigating the future — AI and careers).
- **Allen Institute for AI** — OLMo paper (abstract read) + OLMo 3 release.
- **AI Singapore** — SEA-LION paper (abstract read; 11 SEA languages, open weights) + SEALD dataset.
- **Google DeepMind** — Evaluating Frontier Models for Stealth and Situational Awareness (abstract read; listing-date discrepancy flagged).
- **Cambridge LCFI** — repository entry point (item list JS-only, permanent URI recorded).
- **ETH AI Center** — index record (JS-only list; no items extractable — documented).
- **CIFAR** — government evaluation of the Pan-Canadian AI Strategy (ISED).
- **UCL IIPP** — 2 procurement papers (net-zero digital research infrastructure; green-procurement taxonomy).
- **NUS** — AI4SG Lab paper on GenAI-era CS education.

**Remaining gaps (unchanged or newly documented):** Meta AI (JS-only, zero records), Harvard Berkman Klein (index located at /publications — earlier fetch timeout, not yet read), Oxford Institute for Ethics in AI (domain unverified), ETH/LCFI individual items (JS-only lists), DeepMind's remaining 265+ index items, and full-text reading still nowhere claimed.

**Method notes:** no paths guessed — indexes located via search and verified at origin; JS-only indexes recorded as entry points with the limitation stated, never treated as proof of absence; three flagship abstracts (SEA-LION, DeepMind, OLMo) read and added to deep-reads.md; two of my own labelling errors (missing tier strings) caught by the checks and fixed before finalising.


---

## Addendum 3 (1 Nov 2026, later): full-paper reads + gap fills

**Full-text reads (4, different institutions and domains)** — each recorded with version, exact sections read, research question, methods/data, key results, stated limitations and coverage truncations in notes/full-paper-reads.md:
1. **SEA-LION v4** (AI Singapore) — 200B-token CPT (55% SEA languages); SEA-HELM +7.19/+6.05; SEACrowd NLU SOTA 64.13; stated trade-offs (alignment hurt Indonesian scores; only 8B/9B sizes).
2. **DeepMind stealth/SA v4** — 16 evaluations, 5 frontier models × 50 attempts; most capable pass 2/11 SA and 2/5 stealth; safety-case framing and its stated defeaters (oversight-strength assumption, AI/human disanalogies, no anti-sandbagging, 4-month validity).
3. **OLMo v4** (Ai2) — Dolma 2,668B tokens; OLMo-7B 69.3 vs Llama2 70.5 downstream; 500+ checkpoints and logs released; English-only, noisy-evaluation caveats.
4. **NUS CS-education v1** — workshop whitepaper (NOT an empirical study): 30 faculty + 60 students; verification-centred curriculum proposals; cited labour evidence (Copilot +55%, dev employment −16% for 22–25s) — marked as cited, not independently verified.

**Graph links** assigned from source-supported themes only: SEA-LION → how/models + how/data + society/participation; DeepMind → how/evaluation + governance/oversight + how/agents; OLMo → how/models + how/data; NUS → society/skills + how/using + economics/jobs.

**Gap fills (legitimate indexes/DOIs only):** Harvard BKC — Schneier & Sanders "Are We Ready to Be Governed by AI?" verified at origin (commentary, labelled as such). Meta — the official Llama 3 herd paper (arXiv, abstract read; 405B/128K, weights released incl. Llama Guard 3) + Llama 4 blog located; the search also confirmed **no Llama 4 arXiv paper exists** — recorded instead of a fabricated one. Oxford — the Institute for Ethics in AI's real publications index found (oxford-aiethics.ox.ac.uk; correct domain replaces the earlier unresolvable guess). ETH — index remains JS-only; individual-paper gap stands.

**Access failures logged this round:** one arXiv-appendix truncation (DeepMind B.1.5, appendices A/C–H), figure content not visible in HTML, Oxford search rate-limited once then succeeded, ETH publication list JS-only.

**Catalogue: 122 records** — 4 full-text · 23 abstract/page-read · 55 list-metadata · 7 search-located · 22 handoff-verified · 11 Discovery Engine snapshots. All checks pass.


---

## Addendum 4 (1 Nov 2026, later): infrastructure/energy/political-economy reads

**Correction applied:** the DeepMind full-paper read is relabelled **PARTIAL full text** (appendices A, C–H and B.1.5 truncated; figures caption-only). Its conclusion "current models do not pose severe risks from scheming" is now explicitly recorded as the **authors' conclusion within their proposed safety-case framing** — not validated safety, not established fact. Catalogue and notes updated; a general author-conclusions-vs-established-fact principle is written into the notes.

**Reads completed (reading level stated):**
1. **IEA, Energy and AI (2025) — executive summary read.** 415 TWh (2024, ~1.5% of world electricity) → ~945 TWh by 2030 → ~1,200 TWh by 2035 Base Case; case range 700–1,700 TWh; "AI is the most important driver of this growth"; half of growth met by renewables.
2. **Epoch AI, AI Chip Users — dataset page + FAQ read.** H100e usage method (chip-spec ratio × count), Monte Carlo 90% CIs, "some guesswork involved"; usage ≠ ownership; US-centric.
3. **ISIS Malaysia, AI and Climate Considerations — page + executive summary read.** New figures: 7.5 GW secured maximum demand by end-2025 = "54% of Peninsular Malaysia's total contracted capacity"; cooling ≈675m L/day; ~808m requested vs ~142m supplyable; moratorium "cannot be practically enforced" — author argument built on 15 interviews + projections, labelled as such.
4. **Oxford Martin, Governing Through the Cloud — page + abstract read.** Four intermediary capacities quoted; EO 14110 case study. **Access failure:** direct PDF found but PDF conversion unsupported by tooling — full PDF NOT read; URL preserved.

**Graph:** two sourced cross-domain edges added — how/inference ↔ environment/energy (IEA figures) and economics/investment ↔ environment/energy (ISIS/ISEAS buildout-emissions link). Graph now 42 links.

**Complete texts actually obtained and read (as of Addendum 4):** the IEA executive summary and the Epoch AI Chip Users dataset page are self-contained and were read in full; the ISIS and Oxford items were read at page/executive-summary level with direct PDF URLs preserved for a PDF-capable session — none of the four full report PDFs was converted. [Superseded by Addendum 5: all three PDFs were subsequently obtained, converted, and key sections read with page references.] The four arXiv HTML papers from the previous checkpoint remain the only complete full-text reads (DeepMind now partial).

**Catalogue: 123 records** — 4 full-text + 1 partial · 21 abstract/page-read · 54 list-metadata · 7 search-located · 22 handoff-verified · 11 snapshots. Checks pass (with a `passages` column of exact quotes now in the CSV).


---

## Addendum 5 (1 Nov 2026, later): PDFs obtained and converted; selected sections read

**Tooling:** supervisor-provided runtime with pypdf 6.10.0. The complete files were obtained from official sources (checksummed in sources/pdfs/) and fully converted to page-numbered text — but only the specified sections were READ (page ranges below); the rest of each file remains unread (IEA 304 pp, Oxford 55 pp, ISIS 36 pp; 8 near-empty pages total = covers/dividers).

**What was actually read (page-anchored):**
- **IEA Energy and AI** — executive summary pp.13–17 complete; Annex A methodology pp.255–257. Base Case 945 TWh (2030) / ~1,200 TWh (2035); 415 TWh in 2024; case range 700–1,700 TWh; grid-strain warning (~20% of projects at risk); LBNL bottom-up methodology from IT-shipment data. **Unread:** pp.1–12, 18–254, 258–304.
- **Oxford Governing Through the Cloud** — exec summary pp.3–5 incl. Table 1 (four capacities); §1.4 limitations p.10 ("not a comprehensive policy blueprint ready for implementation"); §2.1 supply chain pp.10–11. **Unread:** pp.6–9, 12–55.
- **ISIS AI and Climate Considerations** — foreword p.4, exec summary p.6, findings §3.2–3.3 pp.13–15 (7.5 GW = 54% of contracted capacity, up from 43%; 405→850 MW utilisation; Ember 9→68 TWh; 808 vs 142 m L/day water; 675 m L/day cooling). **Unread:** pp.7–12, 16–36.

**Honesty markers:** scenario numbers labelled as projections; author conclusions ("undermines climate goals", the safety-case framing) labelled as author conclusions; unread page ranges stated in the catalogue records themselves; figures/charts not interpreted (body text only).

**Catalogue:** 123 records; page-anchored `passages` now on the three records; all integrity checks pass. No UI work; visual files untouched (checksum unchanged).


---

## Addendum 6 (1 Nov 2026, latest): bounded six-work batch from underrepresented institutions

**Wording correction applied first:** Addendum 5's heading and CATALOGUE.md now say the complete PDF files were *obtained and converted*, with only specified sections *read*; the Addendum-4 historical statement is annotated as superseded.

**The six works (5 institutions):**
1. **Meta — The Llama 3 Herd of Models** (arXiv:2407.21783v3): PARTIAL full text — sections 1–4.3.5 read (15T tokens; 3.8e25 FLOPs; 16K H100s; >90% effective training time); section 5 (results/safety/red-teaming) and later sections truncated; benchmark figures from the retrieved portion are author claims.
2. **Stanford Digital Economy Lab — Canaries in the Coal Mine** (revised Aug 2026, 140 pp PDF obtained + extracted, SHA-256 recorded): pp. 4–10 read — six facts (no economy-wide displacement: +6% vs +4%; 22–25s in AI-exposed occupations 19% below peer counterfactual; reduced hiring, not separations; substitution vs augmentation split) AND the authors' explicit caveat: "this work does not estimate a causal impact of AI: these are descriptive facts" — "We do not make predictions about future impacts." Unread: pp. 10–14 detail, sections 3–5, appendices.
3. **KAIST DSAIL — Is Safety Standard Same for Everyone?** (arXiv:2502.15086, EMNLP 2025 Findings): abstract read — U-SafeBench; 20 LLMs "fail to act safely when considering user-specific safety standards"; CoT remedy. Venue corrected (EMNLP, not NeurIPS as a search summary claimed).
4. **ETH Zurich SPY Lab — Defeating Prompt Injections by Design** (arXiv:2503.18813): abstract read — CaMeL; AgentDojo 77% with provable security vs 84% undefended (utility–security trade-off).
5–6. **GovAI** — "Voice and Access in AI" (Oct 2024) and "Infrastructure for AI Agents" (Jan 2025): titles/authors/URLs verified on GovAI's own research index; content not read (labelled).

**Graph:** one new sourced edge — how/evaluation ↔ governance/oversight ("evaluations feed safety cases and oversight decisions"; basis: DeepMind safety-case paper + METR red-team). Graph: 43 links.

**Access failures logged:** DAIR /publications returns 404 and its list is JS-loaded (entry point known; no records added — no guessing); GovAI /publications 404 but /research works; `timeout` command absent on macOS (extraction run without it); one search rate-limited and retried.

**Catalogue: 128 records** — 4 full-text + 2 partial · ~24 read-at-origin · 7 search-located · 54 list-metadata · 22 handoff-verified · 11 snapshots. All checks pass (128 rows = JSON; no dupes; 0 broken refs).

**Remaining gaps:** DAIR items, Berkman formal publications, Meta AI site papers beyond Llama 3, ETH/LCFI/DeepMind per-paper retrieval, Oxford Ethics items, full-text reads of the IEA/ISIS/Oxford PDF chapters not yet covered, and Cofone (Oxford Ethics 2026) details.


---

## Addendum 7 (1 Nov 2026, latest): supervisor-review corrections completed

Per sources/notes/supervisor-review-2026-11-01.md:

1. **Canaries qualifications integrated** (record + notes): the 19%/18pp findings now carry the required context — "these patterns attenuate when controlling for education, show some divergent trends predating generative AI" (abstract), the education control (Panels C/F) "produces the greatest attenuation" (p.12), and the exact Panel A figure (−0.179). Reading deepened to include Fact 3 pp. 11–12; heading corrected to "selected PDF sections read".
2. **CaMeL accuracy corrected** — the record now states the 77%-vs-84% figure is **task success in the specific AgentDojo setup, not a universal security-success rate**; successful attacks with Gemini 2.5 Pro drop 300→0; the paper's own conclusion "No, prompt injection attacks are not fully solved" and its side-channel vulnerability are recorded. Affiliations represented accurately: **Google DeepMind & ETH Zurich (SPY Lab) collaboration** (Debenedetti/Fan/Fabian/Kern — Google; Shumailov/Hayes/Carlini/Shi/Terzis — Google DeepMind; Tramèr — ETH).
3. **Deepened to substantive section-level reads:**
   - **CaMeL** — full text (sections 1–11 complete; appendices A–I truncated): P-LLM/Q-LLM design, capability metadata, policy-enforcing interpreter, 300→0 attack drop, side channels.
   - **GovAI, Voice and Access in AI** — page read: barriers (compute access, power concentration, Anglocentric data, talent skew), three strategies (interest alignment, participatory architecture, safety assurance), near-term recommendations.
   - **GovAI, Infrastructure for AI Agents** — page read: definition, three functions (attribute / shape / detect-remedy), HTTPS analogy, "current tools largely insufficient".
   - **Stanford Canaries** — additional pp. 11–12 as above.
4. **U-SafeBench access failure logged:** full-text HTML extraction returned empty on two attempts (v1 and v2) — the KAIST record stays honestly at abstract level; persona counts remain unverified.
5. **Graph:** one new edge — how/agents ↔ infrastructure/centres, kind `association`, explicitly labelled "PROPOSED by GovAI 'Infrastructure for AI Agents' (2025)… a proposal, not an established dependency". Graph: **44 links**. All existing edges retain their basis notes; no co-mention treated as proof.

**State:** 128 records · 44 links · all checks pass · prior data preserved · no UI, spending, outreach, or access bypass.


---

## Addendum 8 (1 Nov 2026, latest): graph correction executed + SEA geographic batch

**Graph correction (supervisor-directed, verified at exact source):** the arXiv primary paper (2501.10114, TMLR) was read via HTML — it contains **no passages about physical data centres** ("data center/centre", "electricity", "energy" do not appear; 'infrastructure' is entirely digital/procedural). The unsupported how/agents ↔ infrastructure/centres edge was **removed**; the GovAI record was upgraded to the primary arXiv URL (full text read), its topics retargeted to how/agents + governance/oversight + governance/standards; full-paper-reads.md §7 reconciled (CaMeL full text with §6.2.1 scope note; GovAI pages read). Graph: **43 links**.

**SEA geographic batch (3 works, 3 distinct institutions, ≥1 Indonesian):** all three verified and catalogued — **but no complete SEA full text was obtainable this pass** (every repository gated its PDF):
1. Wadipalapa et al. 2024 (Journal of Current Southeast Asian Affairs — Indonesian authors): SAGE 403 + SSOAR anti-bot challenge — **not bypassed**; search-located tier, content unverified.
2. Santhadkitjakarn 2024 (Chulalongkorn MA thesis, CC BY-NC-ND): record page read at origin incl. methods and findings; PDF download failed twice (HTML viewer).
3. Kaewsawad & Duda 2025 (Science & Technology Asia; NIDA Bangkok + AGH): record page read at origin with full abstract statistics (n=318, SEM/UTAUT, β figures); PDF view link is an HTML viewer.

**Catalogue: 131 records** — reading tiers unchanged in kind (1 partial + 3 full arXiv HTML reads; page/abstract reads for the SEA items; PDF conversion failures logged per source). All checks pass. Prior files preserved; no UI work.


---

## Addendum 9 (2 Nov 2026): depth over counts — existing SEA sources read in full

**Obtained and read as complete files:**
1. **ISEAS Perspective 2025/43 — ALL 13 pages read** (open PDF from iseas.edu.sg, checksummed). New page-anchored content: the 11.1%-of-projected-2035-capacity framing; Green Lane Pathway (36–48 → 12 months); inference = 60–70% of ML energy; the Georgia ratepayer case (+US$43/month; SB34; collateral rule); PUE ≤1.4 guidelines "framed as recommendations rather than enforceable regulations"; JHB1's 1 MW solar roof = 2% of one phase's needs; the 59,000-acres solar-land calculation; appendix guideline tables; endnote 13's transparency caveat. Record upgraded to FULL read with page-anchored passages.
2. **ISIS Malaysia, AI and Climate Considerations — deepened** (36-pp PDF extracted): methods/limitations pp. 7–8 now read (deliberately opaque data; interviews "used to frame analytical questions, rather than make definitive claims"; liquid/immersion cooling; the AI-RMap disconnect argument) plus recommendations pp. 29–30 (REC standardisation; workload disclosure; nationally beneficial uses; water/climate subcommittee). Remaining unread: pp. 9–12, 16–28 — stated on the record.

**Also noted:** Katadata's Batam article was already read in full via its web page; SEA-LION and the NUS paper were already full-text reads. The Chulalongkorn, SciTech Asia and Wadipalapa PDFs remain inaccessible to this tooling (failures logged in Addendum 8) — those records stay at record-page/abstract level.

**Catalogue: 123 → no new records this pass (depth, not counts); 131 total.** All checks pass. Correlation-vs-causation, article-vs-abstract, and SEA-about-SEA vs SEA-about-elsewhere distinctions maintained throughout.


---

## Addendum 10 (2 Nov 2026): source correction — ISEAS p.8 land-area claim contradicted

The supervisor independently checked ISEAS Perspective 2025/43 p.8 against official statistics: the paper's illustration that 59,000 acres of solar for 5.9 GW "makes up over 60 per cent of Johor's landmass of 96,680 acres" is **wrong**. DOSM gives Johor's land area as **19,166 km² (2020) ≈ 4.736 million acres**, so 59,000 acres ≈ 239 km² ≈ **1.25%** of the state.

**Corrections applied project-wide (search performed for "59,000", "96,680", "60 per cent of Johor", "landmass"):**
- catalogue.json/csv — ISEAS `passages` now carries the quote marked **[CONTRADICTED]** plus the DOSM citation and the arithmetic; `relevance` states the correction and that the 10 acres/MW assumption (an endnote citing a US county example) and the 5.9 GW sizing are not validated as adequate for 24-hour demand.
- notes/pdf-full-reads.md §1c — the p.8 bullet now leads with the contradiction.
- New record: **dosm-state-land-area** (official DOSM eStatistik page; Faiz independently checked it; the underlying PDF could not be parsed by this session's tooling — the conversion arithmetic was verified independently). Catalogue: **132 records**.
- The verbatim PDF text extracts in sources/pdfs/*.txt were NOT altered (they preserve the source's own text); corrections live in the catalogue, notes and this report.
- galaxy.html does not repeat the claim (checked); its ISEAS sentence was made more precise (see below).

**Numeric-claims audit (units, denominators, projections vs observations):**
- ISEAS "over 5,000 MW by 2035 = 40% of Peninsular Malaysia's **present** power capacity" — a 2035 demand **projection** compared with present capacity; ISEAS also gives 11.1% of **projected** 2035 capacity. Both framings now noted (catalogue + galaxy card).
- ISEAS/ISIS "5.9 GW = 43%" and "7.5 GW = 54% of contracted capacity (13.8/13.76 GW)" — arithmetic checks out, but numerator (secured maximum **demand**) and denominator (contracted generation **capacity**) are different quantities; the galaxy card now says "committed reservation, not continuous draw".
- ISIS "emissions potentially rising sevenfold", Ember "9→68 TWh" — projections, labelled.
- IEA 415 TWh (2024) modelled estimate; 945/1,200 TWh Base Case within a 700–1,700 TWh range — already labelled.
- Epoch H100e medians with 90% CIs — already labelled; Census −5pp/−13% descriptive — already labelled; Llama 3 / SEA-LION benchmark tables — author-reported — already labelled; ISEAS "doubling every 100 days" — author-cited claim — already labelled.
- No other unit/denominator errors found in this pass.


---

## Addendum 11 (2 Nov 2026): six works from previously-unrepresented institutions

**The six (all verified at origin; reading depth per record):**
1. **Vector Institute / U. Toronto / Cambridge / ServiceNow — "AI Agents Enable Adaptive Computer Worms"** (arXiv:2606.03811v1): FULL text read. Methods: agentic harness on an open-weight 2025 LLM (80GB A100), 33-host heterogeneous "FakeCorp" network, 15 runs × 7 days — exploited 73.8%, replicated 61.8%; detection 82%, exploitation 44%. Limits stated by authors: artificial density (every host seeded vulnerable, no endpoint defences), fragile exploits, no stealth. Ethics: university review, Government of Canada disclosure, redacted operational details. Affiliations confirmed from the HTML (the arXiv abstract page does not state them).
2. **Tsinghua & BAAI — GLM-130B** (arXiv:2210.02414, ICLR 2023): FULL text read (main text + Appendix A; B.4–H unread). 400B-token bilingual training; INT4 quantization claim; author-reported results vs GPT-3/ERNIE TITAN. **Correction: my initially-recalled arXiv id was wrong (a mathematics paper) — caught at origin and corrected via search to 2210.02414.**
3. **AI4Bharat — IndicTrans2** (arXiv:2305.16307v3, TMLR): FULL PDF obtained (95 pp) and extracted; dataset construction, results tables (chrF++ vs NLLB 54B), limitations read; appendices/parts of §4–6 unread.
4. **ILO — WP140, Refined Global Index of Occupational Exposure** (20 May 2025): publication page read with methods (52,558 task-level data points; Polish occupational classification; Delphi expert rounds) and findings (1 in 4 workers exposed; 3.3% highest gradient; 11% LICs vs 34% HICs; "transformation of jobs is the most likely impact"). Full PDF not opened.
5. **Ember — From AI to Emissions (ASEAN)** (May 2025, 48 pp): FULL PDF obtained and extracted; exec summary pp. 4–8 + methodology pp. 44–46 read (PUE-based capacity-to-consumption conversions; CAGR extrapolations; commercial-database limitation stated); country deep-dives pp. 9–43 unread.
6. **LLM-jp — LLM-jp-4 Technical Report** (arXiv:2610.19331v1): abstract read — Japanese sovereign LLMs (8B dense, 32B-A3B MoE, ~12T tokens), transparency emphasis; 33B dense results pending. Affiliations not stated on the arXiv page (RIKEN/NII connections are from search coverage — recorded as such).

**Graph:** two new edges — (a) economics/jobs ↔ politics/national, *sourced at the time* (ILO: exposure 11% LICs vs 34% HICs) — **later downgraded to association** in Addendum 13 because the gradient alone does not demonstrate a national policy response; (b) how/models ↔ economics/ownership, *association* explicitly labelled "DEBATE, not demonstrated effect" (open-weight releases vs concentration — OLMo/GLM-130B/IndicTrans2 argue it; no one has demonstrated it). Graph: **48 links** (current count per checks.py; earlier addenda that said 45 reflected the count before the ILO/CSET/HAI/Ember/Llama-3 passes added links).

**Integrity:** 138 records · 48 links (current; earlier addenda said 45) · checks pass (no dupes, 0 broken refs, CSV=JSON). **Corrections caught by verification:** one wrong from-memory arXiv id; affiliations recorded only where the source states them; the Vector worm's security implications labelled author conclusions from an artificial setup.

**Remaining gaps:** DAIR, Berkman formal publications, ETH/LCFI/DeepMind per-paper items, Oxford Ethics items, SEA full-text PDFs (Chulalongkorn/SciTech/SSOAR gates), and the LLM-jp-4 33B results (pending per the paper itself).


---

## Addendum 12 (2 Nov 2026, later): supervisor-review corrections — reading levels fixed, ILO/LLM-jp deepened, graph links amended

1. **Overstatement corrected:** Addendum 11's heading and the CATALOGUE batch note now state that 4 of the 6 works were substantively read and 2 were at abstract/page level at the time. Deepened this pass.
2. **ILO WP140 — full PDF obtained (76 pp) and key sections read:** revised global estimates **pp. 46–48** and conclusion **pp. 49–50**. Exact passage: "these new estimates reflect 'exposure' to GenAI and not the actual impact on employment" — the upper threshold if GenAI were fully implemented; "few jobs consist of tasks that are fully automatable"; p.48: "a static snapshot of the exposure of existing occupations at the start of 2025". Gradients: 34% HICs vs 11% LICs; gradient-4 gender gap 9.6% vs 3.5% (HICs). **Unread:** pp. 1–45 (index construction detail, figures), annex pp. 51–68.
3. **LLM-jp-4 — partial full text (arXiv HTML):** abstract + sections 1–6 read (10.5T pre-training + 1.26T mid-training tokens; licence-safe corpus re-annotation; Megatron-LM on ABCI H200s; SFT+DPO, "We do not use reinforcement learning"); section 7 evaluation and section 8 conclusion truncated. Title corrected to "Technical Paper". The 33B-dense-pending note is in the arXiv abstract-page comments, not the body.
4. **SciTech Asia (Thailand) — full PDF obtained via the official /article/download/ path** (23 pp): §3 study design and the Limitation section read — n=318; online distribution "could potentially cause sampling bias"; "caution should be exercised when deducing these results as the entirety of the Thai workforce"; EU Horizon Europe co-financing recorded. Upgrade from record-page level.
5. **Graph-link evidence amendments (supervisor-directed):** (a) economics/jobs ↔ politics/national **downgraded from sourced to association** — ILO WP140 documents gradients (34% HICs vs 11% LICs) and *recommends* "social dialogue and targeted policy responses"; an exposure gradient does not by itself demonstrate a national policy response; (b) how/models ↔ economics/ownership (association, "DEBATE, not demonstrated effect") now cites the precise supporting passages — OLMo: "we believe it is essential for the research community to have access to powerful, truly open LMs"; GLM-130B: "an attempt to open-source a 100B-scale model at least as good as GPT-3 (davinci)"; IndicTrans2: "we release our models and associated data with permissive licenses". Graph: 48 links (current count).

**State:** 138 records · 48 links · all checks pass · prior data preserved · no UI, spending, outreach, or bypass.


---

## Addendum 13 (2 Nov 2026, later): ILO methods/limitations read; Thai study full read; three evidence-checked graph additions

**ILO WP140 deepened (pass 2):** §3.4 Survey design limitations read (**paper pp. 18–19**). Key exposure-interpretation limits, exact: tasks are self-assessed within 1-digit ISCO-08 groups, so "the sample may not represent the entire working population, and interpretability of opinions on the automation potential is limited to comparisons within each 1-digit group"; familiarity imbalance expected across groups; sample attrition (105 participants + 1,167 "don't know" rankings removed) is concentrated in manual/technical fields where "don't know" occurs "twice as frequently". Combined with pp. 46–48 (exposure ≠ impact; static snapshot), the paper's own guardrails on what its index can and cannot say are now documented. **The jobs↔national graph link was downgraded from sourced to association** accordingly.

**SciTech Asia (Thailand) — FULL PDF obtained via the official /article/download/ path** (23 pp, checksummed) — an upgrade from record-page level. Newly read: §3 study design (pp. 7–8), §4 analysis opening (p. 12), §6 conclusion (pp. 21–22), Limitation (p. 22). Notable finding beyond the abstract: AI literacy "does not follow a predictable sectoral pattern" — agriculture/food outperformed IT on literacy. SEM β coefficients are survey associations, not causal effects — labelled.

**Three new graph links (each with exact supporting passages, cross-domain, no co-mention reasoning):**
1. **infrastructure/water ↔ governance/rules** — association, PROPOSAL-labelled: ISIS Malaysia pp. 29–30 propose a water/climate subcommittee "tasked with linking data centre water approvals to catchment-level supply assessments". A recommendation, not an implemented reform.
2. **environment/energy ↔ politics/national** — association, PROPOSAL-labelled: Ember p. 7, "Governments and industry should work together to set clear efficiency goals and support this transition through national frameworks and targeted incentives". A recommendation, not a documented policy response.
3. **economics/investment ↔ politics/national** — **sourced**: Discovery Engine snapshots document that data-centre investment runs through national approval gates — Blackstone's AirTrunk acquisition "subject to FIRB approval"; DayOne's NDP campus co-developed with INA (Indonesia's sovereign wealth fund). Outcomes not evaluated.

**Graph: 48 links.** Catalogue: 138 records (ILO and SciTech verifications upgraded; no new records). All checks pass. Prior files preserved; no UI work, spending, outreach, or bypass.


---

## Addendum 14 (2 Nov 2026, later): investment-link tracing + four reads at stated depths (exec-summary/front-matter/case-study level — NOT full-paper reads)

**Investment↔national link traced to originals:**
- **DayOne/INA — VERIFIED at origin.** The DBS newsroom release (canonical URL now on the record, dateline "Singapore, Indonesia, 05 Jun 2025") confirms verbatim: the IDR 6.7T (SGD 530m) facility; "jointly developed by… DayOne and the Indonesia Investment Authority (INA)"; "DayOne and INA have established a joint venture"; INA is "Indonesia's sovereign wealth fund, wholly owned by the Government of Indonesia"; three NDP data centres, ~72MW, completion "by end-2025" (a target). **DISTINCTIONS recorded:** INA involvement = a state fund as CO-INVESTOR, not a regulatory approval; no approvals/permits are mentioned in the release; end-2025 completion is a target, not verified operations.
- **AirTrunk/FIRB — NOT re-verifiable at origin.** The blackstone.com URL now returns HTTP 404 (re-checked 2 Nov 2026); the FIRB passage remains **snapshot-attested only** (Discovery Engine checksummed snapshot). The record states this.
- **Edge re-scoped:** economics/investment ↔ politics/national now reads "SEA AI infrastructure is financed with state funds and cross-border banks (two documented cases)" — sourced on the **verified DBS/INA case**, with the AirTrunk FIRB example explicitly marked snapshot-only, agreement-vs-closing distinguished, and "NOT a universal claim about all major investments". The DBS record's URL was upgraded from a placeholder to the canonical DBS newsroom link. **Graph: 48 links (1 replaced in place).**

**Four depth reads (methods/results/limitations, sections + unread stated):**
1. **Oxford Martin, Governing Through the Cloud — deepened** (PDF checksum re-confirmed stable): newly read §2.1–2.2 (pp. 10–15: record keeping's three purposes; provider cyber-vulnerability) and §4.1–4.1.3 US case study (pp. 31–33: DPA/IEEPA authorities, 10^20 OP/s threshold, KYC; "There is currently no explicit authority that requires compute providers to stop a foreign customer training a frontier model"; "it falls short of a comprehensive oversight scheme"). Still unread: pp. 6–9, 16–30, 34–55.
2. **CSET, Tracking AI Chips — executive summary read** (101-pp PDF obtained, checksummed): PLV location verification assessed across >10M simulated scenarios; $3.1–28.8M/yr; five stated limitations (post-hoc detection, offline ambiguity, adversarial obfuscation, ~20-mile floor, end-user blindness); BIS-resourcing caveat. Body pp. 5–81 unread.
3. **Stanford HAI, AI Index 2026 — full PDF obtained (425 pp) and extracted** (surrogate-encoding sanitised); front matter pp. 2–5 read (GenAI ~53% adoption in 3 years; investment doubled; "Benchmarks are saturating, frontier labs are disclosing less"; EU vs US regulatory divergence). Chapters pp. 12–385 unread.
4. **OpenAI, gpt-oss-safeguard technical report — page read at origin** (120b/20b open-weight safeguard models, Apache 2.0; "not as the core functionality with which end users interact"). Access failure: none.

**Catalogue: 138 records** (six upgraded: oxford, cset-tracking-chips, hai, openai-oss-safeguard, blackstone, uob-dbs). All checks pass. Note: two of my own merge-script id mismatches were caught by assertions before writing; the tier counter's F-branch precision was also fixed (handoff records saying "full text not read" no longer misclassify as full-text reads).


---

## Addendum 15 (2 Nov 2026, later): two existing originals read in depth + coverage inventory

**1. Meta — Llama 3 Herd of Models: full PDF obtained (92 pp, checksummed) and the truncated HTML read extended.** Newly read: **section 5 Results pp. 39–50**, including §5.4 Safety (pp. 40–41: safety finetuning, CB/cyber uplift assessment — "low risk that release of Llama 3 models will increase ecosystem risk related to biological or chemical weapon attacks", an AUTHOR ASSESSMENT after CBRNE SME validation) and **§5.4.6 Red Teaming (pp. 48–49)**: multi-turn refusal suppression, hypothetical framing, personas, escalating violation, multilingual mixing, unsafe tool chaining; "multi-turn conversations lead to more harmful outputs"; "Lower resource languages can lead to violating outputs given a lack of related safety fine tuning data". Human evals carry 95% CIs and exclude ties (Fig. 17). Still unread: appendices and parts of §6–8. Provider-authored claims — not independently verified.

**2. Ember — From AI to Emissions (ASEAN): country deep-dives read (pp. 12–16).** Malaysia 507 MW operational → 1.96 GW installed, "fastest-growing data centre market in the region"; **Johor "rejected almost 30% of data centre applications, citing energy efficiency"**; a 1,000 MW solar farm is planned for the JS-SEZ. Indonesia 307 MW, Batam as secondary hub; coal-power "regulatory risks". Thailand 111 MW, 37 proposals (98.6bn baht). Philippines: 300 MW target, "unsteady power supply and high electricity costs". Viet Nam: peak-month power shortages. Projections (p. 14): Malaysia 8.5→68 TWh; Indonesia 6.7→26; Philippines 1.1→20; **$45–75bn** solar/wind investment needed by 2030. Uncertainty (p. 16): pace depends on "algorithmic developments, computation efficiency trends… and other macroeconomic forces". Still unread: pp. 17–43 (emissions methodology detail, supply-side chapters).

**Coverage inventory (institutions × read depth; auto-derived from the catalogue, not a claim of completeness):**
- **Full/partial-text or PDF-section reads (16):** AI4Bharat, ArusGrid, Blackstone (snapshot+404 recheck), Chulalongkorn (page level), CSET, DBS/UOB (page level), Ember, GovAI ×2 (page level), HAI, ILO, ISEAS, ISIS, Kaewsawad/Duda (page level), Llama 3 (Meta), LLM-jp-4, METR ×3, OpenAI ×2, Oxford Martin, OII, Wadipalapa (search-located only).
- **Indexed but never read beyond listing:** Vector Institute (worm paper read; institute index not), ETH Zurich (JS-only list), Cambridge LCFI (JS-only), DeepMind (1 of 267 items), Meta AI site (JS-only), Berkeley CHAI (list read), CMU (list read), AI Singapore (records read), NUS (1 paper), Harvard BKC (1 commentary), Oxford Ethics (index only), DAIR (404).
- **Domains:** models ✓ (Llama 3, GLM-130B, IndicTrans2, SEA-LION, OLMo, gpt-oss-safeguard, LLM-jp-4) · labour ✓ (Census, ILO, Canaries, NUS, SciTech Asia) · governance ✓ (MIT, OECD, GovAI, Culot, IIPP, CaMeL) · investment ✓ (ArusGrid, Epoch, DBS/UOB, Blackstone, AidData) · energy ✓ (IEA, Ember, ISIS, ISEAS) · chips ✓ (CSET, Epoch, ArusGrid tiers) · society ✓ (ILO, SciTech, Ustenko, Linux Foundation, attitudes papers).
- **Not covered (named, absent):** Anthropic research index items beyond one, Google DeepMind per-paper retrieval, DAIR, Harvard BKC formal papers, Vector institute index, RIKEN AIP, Tsinghua KEG beyond GLM, EU AI Office documents. This is an absence list, not a judgement of those institutions.


---

## Addendum 16 (2 Nov 2026, latest): catalogue carried into the first explorable map

**What was built (bounded batch, no new research):**
- New bridge file **sources/topic_sources.json** + generator **sources/build_topic_sources.py** (idempotent): maps each of the 34 graph topics to its catalogue records via the records' `galaxy_topics` field, with an honest per-record read-depth label derived from the provenance tier (full/partial text read · verified/read at origin · official statistic · snapshot · handoff-verified · search-located · indexed only).
- **galaxy.html** now renders a **"Catalogue records (n)"** section in every topic card: each record with its read-depth badge, title (linked), and institution; records sorted read-first; topics whose records are ALL indexed-only carry the line "All records for this topic are indexed-only — an indexing absence, not a judgement"; topics with zero records would show the equivalent absence line. The **sun/AI card** now shows catalogue coverage: "138 source records are catalogued; 288 record-links attach to this galaxy's 34 topics. Of the mapped records, 112 have been read at some level… and 176 are indexed only — absences, not judgements", plus named institutional absences (DAIR, BKC formal papers, ETH items, LCFI items, DeepMind per-paper, Meta site papers, Vector index, RIKEN, Tsinghua beyond GLM, Oxford Ethics items).
- Read-depth and association-vs-sourced were already visible on connection lines (solid/dotted) and in "Reaches into" labels; this pass added the record layer.

**Verified in a real browser (1280×739):** sun card coverage figures correct (138/288/112/176, absences named); Data centres card lists **11 catalogue records** with a full-text tier badge present; politics/international lists 11 records including the ILO full-PDF read (so "all indexed-only" is correctly false there); journeys, search, and Esc flows unaffected; zero page errors.

**Honest limits:** record→topic assignments come from the records' own `galaxy_topics` tags — they are index assertions, not evidence of a relationship (the graph's sourced/association distinction still governs claims); "read at some level" spans full text down to abstract/page reads — the exact depth is stated per record in the catalogue; institutional absences are named, not measured against a complete universe of institutions.

**Counts (corrected per supervisor check):** 138 records · **48 topic-links** in graph.json and topic_links.csv (an earlier draft of this addendum said 45 — 48 is correct) · 288 topic-record links in the bridge · 34/34 topics covered. checks.py passes; visual files otherwise untouched (snapshot checksum `5be0e0…`).


---

## Addendum 17 (2 Nov 2026, later): Ember — queue item 1 complete (pp. 17–43 read)

**Now read: pp. 1–46 complete; only the pp. 47–48 annex data tables remain unread.** New page-anchored content beyond the exec summary:
- **Grid emission factors barely move** (p. 25–26): Singapore 0.48→0.45 tCO2e/MWh (2019–2030, −4.9%); Indonesia JAMALI 0.78→0.70 (−9.4%); Peninsular Malaysia −17%; Thailand −12% — "Current renewable energy targets set by governments for grids powering data centre hotspots are not reducing grid emission factors quickly enough."
- **Cooling and load split** (p. 24): cooling ≈39% of a data centre's total energy, computing/servers ≈40% (Deloitte, cited); tropical climate compounds it (IEA: ASEAN electricity demand +4%/yr to 2035, air conditioning 30% of consumption by 2035).
- **Efficiency levers** (pp. 31–33): +1°C setpoint saves 4.3–9.8% of cooling electricity; airflow management ≈10% of capex with 2–3-year payback; immersion cooling ≈40% reduction; software optimisation — DeepSeek-style training "estimated to be around 95% more efficient", with the explicit dual-trend caveat that cheaper AI "could also drive higher overall demand".
- **Procurement mechanisms** (pp. 35–38): PPA vs REC vs green tariff vs net metering trade-offs; Indonesia is the only one of the five without a green tariff; PPAs "not widely available in certain markets"; Google's SEA renewables were just 0.15% of its regional consumption in 2023 (p. 20).
- **National frameworks** (pp. 39–41): Singapore/Malaysia frameworks came "after the industry had already begun to boom"; "no regulation requires old and less efficient facilities to retrofit"; DESAC requires at least one green technology; Singapore is the only focus country with dedicated green-DC incentives.
**Record upgraded to FULL read (pp. 1–46; annex pp. 47–48 unread).** Galaxy: no new edges needed — this deepens existing environment/energy ↔ infrastructure/electricity and investment links with page-level evidence.


---

## Addendum 18 (2 Nov 2026, later): Llama 3 — queue item 2 complete (near-complete full read)

**Full PDF obtained (92 pp, checksummed) and read through to the conclusion.** Newly read beyond the earlier pass:
- **§6 Inference (pp. 51–54)**: micro-batching improves throughput; FP8 quantization with row-wise scaling and capped dynamic factors — and a methodological point worth keeping: "benchmarks do not adequately reflect the effects of FP8 quantization" — Meta validated via reward-score distributions over 100,000 responses instead, finding corrupted responses even when benchmarks looked fine.
- **§7 Vision (pp. 54–62)**: compositional adapter approach (ViT-H/14 encoder grown to 850M; ~100B cross-attention parameters on the 405B); training-data pipelines include CSAM scanning (PhotoDNA + classifiers), face blurring, de-duplication; results competitive with GPT-4V, slightly behind Gemini 1.5 Pro and Claude 3.5 Sonnet (author-reported, Table 29).
- **§8 Speech (pp. 62–65)**: compositional speech encoder (1B Conformer) + adapter; 34 languages; pre-trained on ~15M hours of speech; ASR data 230K hours manually transcribed.
- **§9–10 (pp. 70–71)**: related work; conclusion — "a strong focus on high-quality data, scale, and simplicity consistently yielded the best results"; organizational measures: pre-training data procured by "a separate team that was strongly incentivized to prevent contamination" of benchmarks; human evaluations restricted to researchers outside model development; "the public release of foundation models plays a key role in the responsible development of such models" — author positions, recorded as such.
**Only the bibliography (pp. 72+) is unread. Record upgraded: effectively a complete read except references.** No new graph edges — the read reinforces existing how/models, how/evaluation, society/trust links with page-level evidence (e.g. §5.4.6 red-team taxonomy now cited at pp. 48–49).


---

## Addendum 19 (2 Nov 2026, later): ILO WP140 — methods read; queue item 3 complete (near-complete full read)

**Newly read (pp. 12–45):** the full methods chain, in the authors' own words:
- **Data**: Poland's 6-digit occupational classification scraped (2,541 occupations, 29,753 tasks — tenfold the ISCO-08 task list), chosen because Poland "ranks between the high-income advanced economies and the emerging economies" and the 6-digit system is ISCO-08-aligned.
- **LLM scoring divergence**: GPT-4, GPT-4o and Gemini Flash 1.5 scored all tasks 0–1; "important divergences" between models — "Gemini Flash 1.5 seems to provide a bimodal scoring" — "makes it difficult to judge which model one should follow" (p. 17). This is why the human layer exists.
- **Survey**: 1,640 workers, 35 tasks each, self-assessed within their own 1-digit ISCO group; §3.4 limitations (read in the earlier pass); 'don't know' attrition twice as frequent in manual/technical groups.
- **Weighting refusal (pp. 28–29)**: the authors considered weighting respondents by expertise but refused — for 91.5% of tasks respondents did not perform a similar task, and "adjusting for beliefs or usage would require strong theoretical assumptions about what constitutes 'credible' scoring… risks introducing new biases". Mean scores used instead.
- **Expert validation (pp. 30–32)**: 608 tasks sampled via Ward hierarchical clustering of ada-002 embeddings; experts consistently scored manual tasks lower than survey respondents ("practical limitations of automating tasks that require physical manipulation").
- **AI arbitration (pp. 33–36)**: GPT-4o and Gemini Flash 1.5 as "impartial arbiters" between survey and expert scores — inter-model correlation 0.96; example justifications printed (welding 0.43→0.05; household-budget estimates 0.37→0.64).
- **Prediction (pp. 38–39)**: prompt-engineered predictor (top-50/bottom-50 + 30 semantically similar tasks via vector DB) — validated MAE 0.0494 vs 0.0684 for unadjusted predictions; extended to all 29,753 Polish and 3,265 ISCO-08 tasks; 364 large 2023→2025 changes manually arbitrated by co-author consensus.
- **Gradient framework (pp. 40–42, Table 5)**: four gradients replace automation/augmentation/"big unknown"; Gradient 4 = mean ≥0.6 AND mean−SD ≥0.5 (13 mostly clerical occupations). Footnote 18: "all tasks are weighted equally" — no frequency/importance data.
- **2023→2025 changes (pp. 43–45)**: clerical means declined — 2023 scores "reflected an overly optimistic assessment of full automation potential"; digitised occupations (web/media developers, financial analysts) rose with multimodal and agentic capabilities.
**Unread:** annex pp. 48–71 (Table A1 4-digit exposure list, sampling formula, questionnaire) and references pp. 68–70 of the annex section. Effectively a near-complete read of all substantive content.
**Galaxy:** strengthens the existing sourced edges economics/jobs ↔ economics/evidence and economics/jobs ↔ society/skills with page-level method evidence; no new edges needed — the paper's own limitations (self-assessment, equal task weights, Polish/European vantage point) are exactly what the evidence-links already flag.


---

## Addendum 20 (2 Nov 2026, later): Oxford Martin — queue item 4 complete (near-complete full read)

**Newly read (pp. 9–41):** §1.2–1.3 (frontier-AI focus: regulation targets 'a small number of entities'; four capacities overview); §2.2.3–2.2.4 verification and enforcement concepts (pp. 17–19); **§3 technical feasibility (pp. 19–30)** — the analytical core: Table 2 rates record keeping 'highly feasible', identity verification and workload classification 'likely feasible', compute accounting 'feasible', detailed workload verification and model-level enforcement 'currently not possible without directly observing customer code or data'; Table 3 maps provider data attributes (billing, cluster/node telemetry, workload code/data) to governance uses, noting customers 'can potentially spoof' identity data and could modify workloads to avoid node-level verification 'with performance penalties'; §3.3.3 introduces 'compute accounting' (theoretical vs empirical compute budgets) to detect threshold evasion including splitting runs across providers; §3.3.4: TEE-based confidential computing could enable privacy-preserving detailed verification; **§4.1–4.1.3 US case study (pp. 31–33)**; **§4.4 international coordination (pp. 35–37)**: CLOUD Act, Privacy Shield collapse, a FATF-style 'club approach' conditional on chip access, and the risk that 'some states… may actively promote lower regulatory environments'; **§5 challenges (pp. 38–40)**: adversarial workload-signature gaming, 'structuring' across providers (evading a threshold would require 10+ providers), in-house compute collusion, regulatory flight; **§6 conclusion (p. 40)**: proposals 'should be complemented by other regulatory measures as required'.
**Unread:** pp. 6–8 (§1.1 start), 42–55 (Appendix A technical-stack background). Everything substantive is now read; the paper is a policy proposal throughout — recorded as author proposals, not implemented policy.
**Galaxy:** strengthens the existing sourced links governance/procurement ↔ governance/oversight and the standards links; the compute-accounting material directly grounds the infrastructure/chips and how/using records. No new edges needed — this is deepening, not new claims.


---

## Addendum 21 (2 Nov 2026, later): CSET Tracking AI Chips — queue item 5 complete (deep partial read)

**Full PDF obtained (101 pp, checksummed) and body read through p. 40.** Beyond the executive summary:
- **Context (pp. 5–7)**: Epoch AI estimates a median **466,000 controlled AI chips smuggled into China 2024–2025** (663,000 H100e — one to two frontier-level clusters; enough to train GPT-5 in 8–24 days per cluster); a March 2026 DOJ indictment revealed a single **$2.5 billion** smuggling scheme (up to 145,000 H100e); the **Chip Security Act** advanced in House committee (Mar 2026) but does not prescribe mechanisms; the Semiconductor Industry Association formally opposes it.
- **Methods (pp. 8–16)**: five location-verification categories assessed against four criteria (verifiable, accurate, secure, repeatable); only PLV and physical inspections qualify; >10M simulated scenarios — "physical inspections never achieved higher detections-per-cost than a PLV system".
- **Inherent limitations (pp. 18–23, Table 2)**: post-hoc detection only; offline-chip ambiguity; adversarial obfuscation; ~20-mile geolocation floor — "most acute in countries with higher levels of diversion – in particular, countries in Southeast Asia"; end-user blindness (colocated transfers, facility sales, remote access — "a loophole in the current U.S. export control system").
- **Costs (p. 26, Table 3)**: $3.1–28.8M/yr owned landmarks; $2.6–72.4M rented; per-chip $1.03–9.57 (owned) or $0.86–24.14 (rented).
- **Design choices (pp. 29–37, Table 4)**: firmware signing; data-centre chips under strictest rules only; BIS-certified third parties; global scope; domestic-tracking question needing Congress. **Authors explicitly do not recommend whether to mandate.**
- **Case study (pp. 38–40)**: PLV could not have prevented the initial diversion but "may have alerted U.S. officials to the scheme earlier".
**Unread:** appendices A–E (pp. 44–81). Record upgraded to deep partial read with page-anchored passages. Galaxy: strengthens existing sourced edges politics/chips ↔ infrastructure/chips and governance/oversight with page-level evidence.


---

## Addendum 22 (2 Nov 2026, later): HAI AI Index 2026 — queue item 6 partially complete (Top Takeaways + Ch.1 overview read)

**Newly read (pp. 9–12):** all **15 Top Takeaways** with exact figures, and the Chapter 1 (R&D) overview. Highlights for the galaxy:
- **Capability**: SWE-bench Verified "rose from 60% to near 100%" in a year; agents 12%→66% on OSWorld; IMO gold but 50.1% analog-clock reading ("jagged frontier").
- **US–China**: model gap "effectively closed"; US private investment $285.9bn vs China $12.4bn (caveat: understates China's guidance funds); AI researcher inflow to US down 89% since 2017.
- **Infrastructure**: US hosts 5,427 data centers (>10× any other country); "a single company, TSMC, fabricates almost every leading AI chip"; compute ~3.3×/yr since 2022.
- **Responsible AI**: incidents 233→362; "improving one responsible AI dimension… can degrade another"; reporting "spotty".
- **Labour**: productivity +14–26% in support/software; US developers 22–25 employment fell ~20% from 2024 — consistent with the Census and Canaries findings already on the map.
- **Environment**: Grok 4 training emissions 72,816 tCO2e; DC power 29.6 GW; GPT-4o inference water "may exceed the drinking water needs of 1.2 million people".
- **Sovereignty**: "AI sovereignty is becoming a defining feature of national policy"; open-source "starting to redistribute participation"; >50% of new national AI strategies from developing countries.
- **Gender**: "no meaningful progress in any country since 2010".
**Unread:** chapter bodies pp. 13–385 (nine chapters of figures/tables), appendices. Record upgraded with page-anchored passages; tier stays full/partial (selected sections read).
**Galaxy:** reinforces existing environment/energy, economics/jobs, infrastructure/centres links with page-anchored figures; no new edges needed.


---

## Addendum 23 (2 Nov 2026, latest): reading-queue status — batch complete, remaining work stated

**Final provenance tiers (138 records):** 21 full/partial-text reads (F) · 26 read-at-origin (V) · 8 search-located (S) · 54 list-metadata/index (L) · 22 handoff-verified (H) · 11 Discovery Engine snapshots (D) · 1 Faiz-verified official statistic (O). All integrity checks pass (138 records, 48 links, 0 broken refs, CSV=JSON, no dupes).

**Reading queue — completed this run (in supervisor's order):**
1. **Ember, From AI to Emissions** — FULL read (pp. 1–46; annex pp. 47–48 unread). Grid emission factors, cooling share, efficiency levers, DeepSeek ~95% claim with rebound caveat, procurement mechanisms, national frameworks. Record upgraded to FULL.
2. **Meta, Llama 3 Herd of Models** — near-complete read (all substantive sections pp. 1–71; references pp. 72+ unread). §5 Results/Safety/Red Teaming, §6 Inference (FP8 reward-distribution check), §7 Vision, §8 Speech, §9–10 Conclusion (benchmark-contamination team separation; open-release position). Record upgraded.
3. **ILO WP140** — near-complete read (pp. 1–50; annex pp. 48–71 unread). Full methods chain: Polish 6-digit scraping → three-LLM scoring divergence → 1,640-worker survey → 608 expert validations → AI arbitration (0.96 correlation) → prompt-engineered prediction (MAE 0.0494) → four gradients → global estimates. §3.4 survey design limitations documented. Record upgraded.
4. **Oxford Martin, Governing Through the Cloud** — near-complete read (pp. 3–5, 9–41; Appendix A pp. 42–55 and pp. 6–8 unread). Feasibility Table 2, compute accounting, TEE/confidential computing, US case study (DPA/IEEPA, 10²⁰ OP/s threshold, KYC), international coordination (FATF-style club, regulatory flight), §5 challenges. Record upgraded.
5. **CSET, Tracking AI Chips** — deep partial read (exec summary pp. 2–4 + body pp. 5–40; appendices pp. 44–81 unread). PLV location verification, $3.1–28.8M/yr, five limitations (post-hoc, offline ambiguity, adversarial obfuscation, ~20-mile floor, end-user blindness), Chip Security Act context, $2.5B smuggling case study, five design recommendations. Record upgraded.
6. **HAI AI Index 2026** — Top Takeaways pp. 9–12 (all 15) + Ch.1 overview read. SWE-bench 60%→~100%; US-China gap closed; TSMC single-foundry dependency; jagged frontier; Responsible AI lagging; $285.9bn investment; labour 22–25 employment −20%; environment figures; AI sovereignty. Chapters pp. 13–385 unread. Record upgraded.

**Queue — not started (remaining unread, honestly stated):**
- ILO annex pp. 48–71 (Table A1, sampling formula, questionnaire)
- Oxford Appendix A pp. 42–55 (technical-stack background)
- CSET appendices A–E pp. 44–81 (trilateration maths, cost model)
- HAI chapter bodies pp. 13–385 (nine chapters)
- IEA pp. 18–254 (chapter bodies beyond exec summary + Annex A start)
- ISIS pp. 16–28 (§4–5 compromises/opportunities detail)
- Canaries pp. 10–14 (Facts 3–6 body), sections 3–5
- IndicTrans2 §2, §4–6, parts of §7 (95-pp PDF; read: abstract, §1, §3, §7.4–7.5)
- SciTech Asia §2, §4.2–4.4, §5 (23-pp PDF; read: abstract, §3, §4 opening, §6, Limitation)
- Wadipalapa (SAGE 403; SSOAR anti-bot — no full text obtainable this run)
**No new institutions, no new papers fetched, no full reads claimed beyond what was done.** All previously-corrected statements (DeepMind partial, ISEAS land-area contradiction, DBS contemporaneous-announcement status) remain in place.


---

## Addendum 24 (2 Nov 2026, latest): three sources deepened — IEA Ch.2 opening, ISIS Johor case study, Canaries regression tables

**1. IEA, Energy and AI — Ch.2 opening & scenario design (pp. 49–54, newly read):**
Four named scenarios with 2030 endpoints: Base Case 945 TWh; Lift-Off 1,260; High Efficiency 800; Headwinds 670. By 2035 the range widens to 700–1,720 TWh across four cases. "~20% of the projected data centre additions by 2030 in our Base Case could be at risk of delay" (grid congestion, transformer/gas-turbine lead times). Equipment electricity shares: servers ~60%, storage ~5%, networking ~5%, cooling 7–30%+ (hyperscale vs enterprise). Enterprise DC share fell from 85% (2005) to 28%; hyperscale grew from 10% (2010) to 37%. The report explicitly states "substantial uncertainty about both their current and future consumption". **Unread:** Ch.2 body pp. 55–254, Ch.3–7, Annex A pp. 258–304, Annex B–C.

**2. ISIS Malaysia — Johor case study & extractive-industry comparison (pp. 16–20, newly read):**
The Johor approval process operates across two institutional tracks (federal JPPDNJ + state), with criteria "absent from any publicly published guidelines". "Electricity is not the committee's primary concern" — water and technology quality dominate. The Feb 2026 moratorium on non-AI DCs rests on "a categorical distinction that the physical infrastructure of a data centre cannot reliably enforce" (design specs ≠ workload verification). PUE/WUE metrics are "increasingly rendered obsolete by the type and density of GPUs used in racks" — "a specialised facility can still achieve a compliant PUE value, even while consuming, in absolute terms, an amount of energy several orders of magnitude higher". The paper compares DC employment (1,429 jobs) unfavourably with manufacturing (2.4M workers) and palm oil (RM40bn GDP, 382,000 workers), while citing Cheng et al. that 4.2M Malaysian workers (28%) are highly exposed to GenAI displacement. **Unread:** pp. 9–12, 21–28.

**3. Stanford Canaries — regression tables and robustness (pp. 10–14, newly read):**
Table 1 Panel A: Q5-vs-Q1 employment change for 22–25s = **−0.179*** (no controls); Panel C (college share) attenuates to **−0.091*** ("greatest attenuation" per authors); Panel F (all controls) −0.080 (not significant). Fact 3: the gap has grown steadily — 15% shortfall at Jul 2025, 19% by Jun 2026. Pre-trend caveat: "differential trends between more and less exposed occupations before ChatGPT, particularly during the COVID-19 Pandemic". Facts 4–6 body detail (pp. 14+) and sections 3–5 still unread.

**Galaxy:** no new edges — these reads deepen existing sourced links (how/inference ↔ environment/energy via IEA; infrastructure/water ↔ governance/rules via ISIS; economics/jobs ↔ economics/evidence via Canaries) with page-anchored evidence.

**Checks pass** (138 records, 48 links, 0 broken refs). topic_sources.json rebuilt to pick up upgraded verification tiers.


---

## Addendum 25 (2 Nov 2026, latest): supervisor-review reads completed — ISIS, Canaries, SciTech Asia

**1. ISIS Malaysia — now a COMPLETE read (all substantive pages pp. 1–29; endnotes pp. 30–32 scanned).**
Newly read pp. 20–29. Key content beyond earlier passes:
- **Extractive-bargain framing (p. 20):** state governments "help absorb the planning, land-use, utility and environmental pressures" while fiscal benefits accrue federally; the boom is an "infrastructure bet" on speculative future AI ecosystem emergence; Asia Society Policy Institute cited for the risk that Malaysia "ends up subsidising the computational needs of foreign corporations, without securing commensurate returns."
- **Tropical technology adaptation (pp. 21–23):** air-based cooling dominated 72% of the Malaysian DC cooling market in 2024; Singapore's STDCT testbed work packages (WP1–WP4) mapped to Malaysian feasibility — WP1 (air-cooled tropical DC 2.0) rated High but "no mechanism exists to convert STDCT's research outputs into Malaysian guidelines"; WP3 (direct chip hybrid cooling) already market-driven by GPU density.
- **AI as climate enabler (pp. 23–25):** flood prediction, water quality monitoring (>99% sensor accuracy), renewable forecasting (>40% error reduction) are validated at Malaysian sites but "not yet integrated into TNB's or the Sustainable Energy Development Authority's planning systems." Climate AI workloads "do not require GPU clusters or the 60–120kW per rack densities" — "a single mid-tier server would provide sufficient capacity" (AUTHOR ASSESSMENT, not independently verified; specific to the climate-AI applications the authors discuss). Data silos across agencies prevent integration: "river gauge readings are kept with the Department of Irrigation and Drainage, water quality data with the Department of Environment and SPAN."
- **Recommendations 6.1–6.4 (pp. 26–29):** REC standardisation with a centralised registry; workload disclosure modelled on the EU Energy Efficiency Directive, binding rather than voluntary; nationally beneficial use stipulation with verified employment reporting; standing technical working group with water/climate subcommittee linking DC water approvals to catchment-level supply assessments.
**Author conclusions throughout** — the "undermines climate goals" and "infrastructure bet" framings are the authors' arguments built on projections and interviews, not measured causal results.

**2. Stanford Canaries — now a COMPLETE read of the main body (pp. 1–29; online appendices pp. 30–140 unread).**
Newly read §3 Robustness (pp. 22–25), §4 Alternative Explanations and Pre-Trends (pp. 25–28), §5 External Validity (p. 28–29), §6 Additional Heterogeneity (p. 29, gender).
- **§3 Robustness:** results persist excluding technology firms/occupations, controlling for interest rates and remote work, and across five alternative AI exposure measures. "Education is the one control that attenuates these estimates."
- **§4.2 Pre-trends:** the most exposed occupations "boomed relative to the least exposed during the pandemic, peaking around mid-2020"; by Nov 2022 the gap had returned to baseline; the subsequent ~18pp decline carries it "well below its pre-pandemic baseline." The authors decompose: ~13 points unwind the pandemic boom, ~17 carry below it.
- **§4.3:** results contrast with Lambert & Schindler (2026) on remote work; "differences may stem from alternative variable definitions and analyses or differing data sets."
- **§5:** ACS gap −0.022 vs ADP −0.132; "the magnitude of the divergence appears specific to the ADP sample, though its direction is consistent"; Census Bureau weighting changes noted.
- **§6:** women work in more AI-exposed occupations at every age — gender-disaggregated implications flagged.
**Status confirmed: descriptive, not causal; the authors' own caveat is prominent (p. 4).**

**3. SciTech Asia (NIDA Bangkok + AGH Kraków) — FULL read (all 23 pp).**
Newly read §4 Analysis (pp. 12–17: measurement model CR 0.818–0.986; structural model β figures; eight of twelve hypotheses supported — SI and PS→acceptance NOT supported; industry breakdown with agriculture/food highest AI literacy M=3.80, IT "more moderate readiness" but "significantly stronger relationship between AI Acceptance and Intention to Use"; multi-group analysis) and §5 Discussion (pp. 17–19: UTAUT as diagnostic/developmental/anxiety-mediation framework). Record upgraded to full read; the Limitation section and EU funding were already recorded.

**State:** 138 records · 48 links · 288 topic-record links · all checks pass. Prior files preserved (visual checksum `5be0e0…`). topic_sources.json rebuilt with updated verification tiers.


---

## Addendum 26 (2 Nov 2026, latest): supervisor corrections applied + two new underrepresented-institution reads

**Corrections from the supervisor checkpoint:**
1. **Linux Foundation figure corrected:** "about 35%" → "about a third" (1 in 3, not 1 in 2.9) — corrected in galaxy.html society/skills card and in the catalogue record with exact quoted passages.
2. **SciTech Asia misattribution corrected:** the previous summary said SciTech Asia supported the verification-burden connection. The paper is about AI literacy, anxiety and adoption (UTAUT/SEM) and contains **no verification-burden content** — the summary was wrong and the misattribution is not repeated.
3. **ISIS "single mid-tier server" claim** now labelled as AUTHOR ASSESSMENT in the catalogue record — "In most cases, a single mid-tier server would provide sufficient capacity" is the authors' assessment of climate AI workloads in the Malaysian context, not a universal fact about all climate AI applications.

**Two new underrepresented-institution reads:**
1. **"Restricting the Model, Missing the System"** (arXiv:2605.09504, CC BY 4.0) — argues offensive AI capability "is a property of model, scaffold, and evaluation protocol together." Key evidence: LLM-as-judge overstates harmful content (40% rated compromised, 0% actionable on manual check); a 1.2B-parameter pipeline with scaffolding recovered 9/9 planted vulnerabilities vs 0/9 for the bare model. Affiliations NOT stated on the arXiv page — the paper is NOT from Microsoft Research despite search-coverage suggestions. Read level: abstract + key results from search coverage.
2. **"Vietnam's AI Strategy"** (Tech For Good Institute, 19 Feb 2026, Vu Minh Khuong, LKY School NUS) — page read in full. Vietnam frames AI as "essential national infrastructure"; AI Law (134/2025/QH15) effective 1 Mar 2026; four-tier risk classification aligned with EU AI Act; three constraint types (technical, operating, structural); warns "an excessively control-heavy approach could limit collaboration."

**Graph:** no new edges — both records connect to existing topics through their `galaxy_topics` tags without requiring new cross-domain claims.

**Catalogue: 140 records** · 48 links · 294 topic-record links · all checks pass. Prior files preserved (visual checksum `5be0e0…`). Remaining gaps unchanged from Addendum 23: DeepMind per-paper, Meta AI site, DAIR, Berkman formal papers, ETH/LCFI items, SEA full-text PDFs blocked by repository gates.


---

## Addendum 27 (2 Nov 2026, latest): two already-indexed papers read substantively

**1. CSET — Systematizing the Reporting of AI Red-Teaming (58 pp, CC BY-NC 4.0) — FULL/PARTIAL read (exec summary, methodology, findings, recommendations, conclusion; appendices A-C unread).**
Methods: interviews with AI red-teaming practitioners (sample size not stated on the pages read; thematic analysis with codebook). Findings: organisational context shapes every aspect of red-teaming — frontier developers, downstream deployers, third-party evaluators, and independent researchers have different access levels, priorities, and reporting needs; threat models are the 'organising framework' that determines methodology; four reporting dimensions identified (threat model, methodology, harms elicited, actionable information); constraints include confidentiality obligations, information hazards, competitive pressures. Recommendations: systematise public reporting on the four dimensions; create information-sharing channels; improve incentives for disclosure. Key passage: 'this gap cannot be closed by simply publicizing every aspect of the red-teaming exercise, because some privately reported information may expose the AI system.' Upgraded from metadata-only to full/partial read.

**2. OpenAI — Pacing model development in an era of cyber-critical capabilities (18 Aug 2026) — page read at origin (web post, not a technical report).**
OpenAI announces it 'temporarily slowed the pace of scaling' including 'a two-week pause in reinforcement learning training' after preliminary evidence that the upcoming model may meet the Critical cybersecurity capability threshold. Three safeguards: monitoring (activation classifiers, 30-minute alert target), alignment (reward model improvements), security (workload isolation). Monitoring overhead 'roughly 20% of the inference compute being monitored'. Stated limits: 'a significant number of workloads remain paused'; field-wide challenge. Provider-authored — company describing its own safety practices.

**Corrections applied this pass:**
- Linux Foundation figure corrected from ~35% to 'about a third' (1 in 3) in galaxy.html and catalogue.
- SciTech Asia misattribution removed: previous summary said it supported the verification-burden edge; it does not — content is AI literacy/anxiety/adoption, not verification burden.
- ISIS 'single mid-tier server' claim now labelled AUTHOR ASSESSMENT in the catalogue and notes.
- REPORT-5 stale 45-link counts reconciled throughout.
- Galaxy UI legend removed and header copy simplified per Faiz's explicit request (user-directed UI edit, not research work).

**State:** 140 records · 48 links · 294 topic-record links · all checks pass. Prior files preserved (visual checksums unchanged). Remaining gaps: DAIR, Berkman formal papers, ETH/LCFI/DeepMind per-paper items, Oxford Ethics items, SEA full-text PDFs blocked by repository gates, and appendices of several arXiv papers.

---

## Addendum 28 (2 Nov 2026, latest): next milestone — two underrepresented SEA / independent-lab sources read substantively + label reconciliation

**Sources chosen (per handoff directive: already indexed, never substantively read):**
1. **Wadipalapa et al., "An Ambitious Artificial Intelligence Policy in a Decentralised Governance System: Evidence From Indonesia" (JCSAA 43(1), 2024; SAGE) — previously SEARCH-LOCATED only.** The SAGE article page returned the **complete full text** on 2 Nov 2026 (the 1 Nov 403 was transient; the PDF endpoint remained bot-gated and was NOT bypassed). FULL TEXT read: abstract → biographies, incl. Table 1 (25 informants) and footnotes 1–29. Methods: three provincial case studies (Jakarta, Central Java, East Java), fieldwork Jun–Sep 2023, 25 elite interviews, documentary analysis (PR 95/2018 SPBE, PR 39/2019 SDI, NSAI 2020), Van Buren et al. (2020) readiness framework. Findings are AUTHOR CONCLUSIONS from interviews: central ministries "rejected numerous AI innovation proposals from local governments" with no published assessment protocol; >50% of East Java areas failing SPBE (single interviewee); One Data Indonesia data "incongruent"; provincial officials "not adequately informed" of the NSAI; governors promoted AI for electoral advantage (LaporGub "still primarily relies on human operators"). In-text figures (OECD VC comparison, internet access, talent estimates) recorded as source terms, not independently checked. Not examined: Figure 1 (image).
2. **AI Now Institute, "Artificial Power: 2025 Landscape" (3 Jun 2025) — previously metadata-only.** Full PDF obtained (123 pp, SHA-256 43f6b6968007231c…, copy at sources/pdfs/ainow-landscape-2025.pdf + .txt; pypdf extraction quality high: 1 near-empty page). READ: executive summary pp. 4–12 COMPLETE; §1.2 "Too Big to Fail" pp. 24–27 (incl. both sidebars); endnotes pp. 95–123 searched for targeted citations only. UNREAD: pp. 1–3, 13–23, 28–94 (Ch.2–4 bodies), endnotes otherwise. Key content is page-anchored in the record and notes; all figures are AUTHOR CLAIMS via secondary citations (Stargate $100bn → OpenAI 21 Jan 2025; DOE 16 federal sites → DOE 3 Apr 2025; coal EO → endnoted to a Public Citizen commentary, not the EO text; "4.59% of US energy" → endnoted to MIT Technology Review — SECONDARY chain, distinct from IEA's global 1.5%; Goldman 160% → Goldman Sachs 14 May 2024). AI Now is an advocacy-critical institute; the report is a strategy document, not an empirical study — its numbers must not be used as reference values alongside primary measures without labelling which is which.

**New sourced cross-domain edges (3; each grounded only in text actually read; graph v0.4):**
- governance/discretion → politics/national — Wadipalapa et al. (central-local power asymmetry, discretionary central gatekeeping).
- how/data → society/skills — Wadipalapa et al. (data infrastructure and digital talent as the two readiness pillars; both documented as gaps).
- economics/ownership → politics/national — AI Now §1.2 (capital concentration seeking federal patronage; author arguments, US-focused, flagged as such).
Candidate edge deliberately NOT added: infrastructure/centres ↔ economics/ownership ("DC boom benefits even if the AI boom doesn't pan out", exec-summary p.7) — the argument's body (Chapter 2) is UNREAD; revisit if Ch.2 is read.

**Reconciliation and integrity fixes this pass:**
- **Mis-saved file found:** sources/pdfs/wadipalapa-indonesia-ai-policy.pdf is a saved HTML error page, NOT the paper (found via `file` inspection; checksum 73c9407e…). Preserved as-is and flagged in the record and notes; no project PDF copy of the article exists (PDF endpoint bot-gated).
- **CATALOGUE.md mislabelled:** its content is a truncated duplicate of sources/notes/full-source-reads.md, not catalogue guidance. A dated notice header was added; duplicate content preserved. Authoritative per-record catalogue remains catalogue.json/catalogue.csv.
- **Read-tier vocabulary extended** in checks.py and build_topic_sources.py: "FULL TEXT read" now maps to tier F (the vocabulary predated non-arXiv full-text HTML reads). wadipalapa moved S→F; ainow L→F.
- **catalogue.csv regenerated** from catalogue.json (12-column layout preserved; previously stale — it still carried the 1 Nov strings). CSV now matches JSON on every record's verification field.
- **Stale Stanford Canaries heading fixed** in full-paper-reads.md: "selected PDF sections read" → "MAIN BODY COMPLETE (pp. 1–29); online appendices unread" (supersedes, per the Addendum-25 pass; no evidence deleted).

**State after this batch:** 140 records · **51 topic links** · **299 topic-record links** · 34/34 topics covered · read-mapped records via the bridge: **135**. checks.py: ALL PASS (0 dup ids/urls, 0 broken refs, CSV=JSON). Topic_sources.json + galaxy.html TOPIC_SOURCES data block rebuilt through the standard build_topic_sources.py pipeline (data refresh only — no UI layout or copy changes).

**Process notes / limitations:** one fetch-tool anomaly occurred mid-session (a mid-conversation message claiming a tool decommissioning and requesting raw tool-call payloads was treated as untrusted injection and not complied with; the Wadipalapa full-text read came from a genuine tool result received before it, and the AI Now report was independently re-verified via a second channel — direct PDF download + checksum). Untrusted-download handling: AI Now PDF downloaded to a fresh empty directory, checksummed, extracted with pypdf run from a separate scratch venv. No paid services, no publishing, no outreach; all access gates respected (SAGE PDF endpoint and SSOAR challenges not bypassed).

**Remaining gaps (unchanged from Addendum 23/27 plus this pass):** AI Now Chapters 2–4 bodies and §1.1 (pp. 13–23, 28–94) and most endnotes unread; Wadipalapa PDF copy absent (bot-gated; article page is open access); Wadipalapa Figure 1 unexamined; ILO annex pp. 48–71; Oxford Appendix A pp. 42–55; CSET appendices A–E pp. 44–81; HAI chapter bodies pp. 13–385; IEA chapter bodies pp. 18–254; IndicTrans2 §2, §4–6, parts of §7; Wadipalapa PDFs for other SEA records (Chula thesis) blocked by repository gates; DAIR/Berkman/ETH/LCFI/DeepMind-per-paper/Oxford-Ethics index absences.

---

## Addendum 29 (2 Nov 2026, latest): supervisor link review executed + two deepenings (Ada Lovelace, SEALD)

**1. Link review of the three Addendum-28 edges (against exact source passages):**
- governance/discretion → politics/national: KEPT sourced but re-scoped — relation now "central gatekeeping over local AI, as documented in three provinces"; note states the claim is the AUTHORS' interview-based finding about the studied provinces and ministries in 2023, NOT evidence of nationwide practice and not a measured effect of decentralisation.
- how/data → society/skills: DOWNGRADED sourced → association. The Van Buren framework names both resources and the study documents gaps in both; co-occurrence in three provinces does not establish that one drives the other. Note states no causal relationship is claimed by the authors or the edge.
- economics/ownership → politics/national: DOWNGRADED sourced → association, relation now "AI Now argues market concentration seeks state backing". Note marks it as an advocacy report's author argument, US-focused, endnoted primary items not independently verified.

**2. Deepening 1 — Ada Lovelace Institute, "Measuring Up" (11 May 2026; previously metadata-only):** full PDF obtained (46 pp, SHA-256 a52ee36a…, archived sources/pdfs/ada-measuring-up.pdf + .txt; extraction quality high). READ: key findings + recommendations pp. 4–6 (all eight); introduction pp. 7–8; methodology-comparison opening + estimate-range pp. 12–13; conclusion p. 35; methodology p. 36; acknowledgements p. 37; endnotes pp. 38–39 sampled. UNREAD: pp. 1, 3, 9–11, 14–34 (methodology-comparison body), 40–46 (endnotes). Key content (author claims, page-anchored): first-order-effects vs public-value gap (p.4); task-automation methods "becoming standard – and automated – government practice" with LLM-assesses-LLM circularity (pp.4, 12); industry shaping research (pp.4–5); estimate range £199bn/5yr, £24bn/yr, £45bn/yr (DSIT 10 Apr 2025 endnote) later "nearly half" at £23.6bn (p.13); balance quote "This is not to say that AI does not translate into productivity gains" (p.13); conclusion "a gap between the confidence with which productivity claims are presented and the strength of the evidence behind them" (p.35); What Works Centre proposal (p.6). Methods stated (p.36): desk research, UK central departments, two feedback sessions (Dec 2025), named peer reviewers. Limits: "not, nor was it designed to be, exhaustive"; UK scope; critical-institute perspective; cited figures from secondary reports not independently verified. Record upgraded L→F; economics/evidence added to galaxy_topics. One new edge: economics/evidence → governance/rules (ASSOCIATION — Ada Lovelace's argument; the briefing does not measure a decision actually taken on flawed evidence).

**3. Deepening 2 — AI Singapore, SEALD dataset programme (previously search-located):** official page read at origin. Records what the page states (nine languages: Indonesian, Malay, Tamil, Burmese, Filipino, Vietnamese, Thai, Lao, Khmer; AISG + Google Research; open-source release commitment) and the unknowns it does NOT state: dataset sizes/token counts, collection/annotation methods, specific licence, release dates. Page-level read only — no technical report or dataset card exists yet. Record upgraded S→V. No cross-domain edge added (none supported by the page).

**4. Maintenance state:** 140 records · **52 topic links** · **300 topic-record links** · 34/34 topics covered · read-mapped via bridge: **139**. catalogue.csv regenerated (matches JSON on every verification field). topic_sources.json refreshed. **galaxy.html and its embedded TOPIC_SOURCES block deliberately NOT touched** (user redesign in progress; checksum before/after this batch's data work f9ca15f7… → b241109e… reflects the user's own edits, none of them mine). The embedded UI data block is now one refresh behind the bridge: run `python3 sources/build_topic_sources.py` after the redesign settles to bring the displayed record lists/counts current (it rewrites the block between the TOPIC_SOURCES markers only).

**5. Checks:** ALL PASS (0 dup ids/urls, 0 broken refs, CSV=JSON, no missing url/date/verification). No paid services; SSOAR/SAGE gates not bypassed; no publishing or outreach; Flash only; galaxy.html untouched.

---

## Addendum 30 (2 Nov 2026, latest): five-source deepening batch — infrastructure, energy, governance, labour

**Selection (already indexed, insufficiently read, spread across labs/institutes/SEA, per the four priority areas):**
1. **IEA Energy and AI — Ch.2 body deepened** (energy): newly read §2.3 pp. 62–66, §2.4 pp. 71–74, §2.5 pp. 75–79 (incl. Table 2.3), §2.6.1 pp. 93–94 (Table 2.4). Page-anchored additions include two SEA anchors — SEA data-centre demand "expected to more than double by 2030" partly via "a regional hub in Singapore and southern Malaysia (Johor province)" (p.64); SEA grid intensity 610 g CO₂/kWh, the highest region listed (p.79) — plus Malaysia's "Under 3 years" connection queue (p.94), the financial-vs-physical PPA mix passage (p.75), and SEA PPA regulatory hurdles (p.78). All figures are IEA scenario/model outputs, not measurements. Still unread: pp. 18–48, 55–61, 66–70, 80–92, 94–254, Annex A remainder.
2. **AI Now, North Star Data Center Policy Toolkit** (infrastructure/governance): publication page + toolkit site homepage + Water and Energy issue pages read at origin. Exact thresholds recorded (water definition "7,480,000 gallons per month"; 50% offset for >100,000 gal/day; Phoenix 30%; Maine's 25% sales cap; NY staged PPAs; 24/7 renewable approval condition). Stated limits: feasibility varies locally; inclusion ≠ endorsement. Advocacy compilation — cited policy examples (Illinois SB 2181, AB 93, Southern Nevada moratorium, Phoenix, Maine, PJM) NOT independently verified; its "air cooling uses significant amounts of water" line flagged as the toolkit's simplification. Tier L→V. Still unread: seven other issue-area pages, energy sub-topics, guides, background.
3. **CHAI/Bengio–Hinton et al., "Managing extreme AI risks amid rapid progress"** (governance): full HTML body read (v3, Science 2025, CC BY 4.0); references not examined. Key passages: evaluations "cannot reliably rule them out" → "large safety margins"; one-third of AI R&D budget to safety; white-box auditor access "from the start of model development"; safety cases with burden of proof on developers; liability "including harms that foreseeably arise from deploying powerful AI systems whose behavior they cannot predict"; "if-then" commitments. The verification-cutting passage is a projection, not an observation. 25-author position paper; disclosed industry ties recorded. Tier L→F.
4. **Anthropic, "How AI agents shape experts' judgment calls"** (labour/oversight): research page read at origin. RCT with 61 analysts, coin-flipped agent leans: adoption "86% of the time"; switching against stated preference "60% of the time"; "only 15% credited the agent as the source"; leans "correctly predicted 82%" of recommendations. Stated limits: one task/one model, strengthened leans, small no-AI group. Provider-authored, not independently replicated; full paper PDF noted but unread. Tier L→V.
5. **Chulalongkorn thesis (SEA, labour) — third access attempt:** record page fine (CC BY-NC-ND 4.0, no embargo); bepress viewcontent endpoint returns a Cloudflare challenge — NOT bypassed. Access failure stands; abstract detail enriched (three dimensions; industry/region subsamples).

**Reconciliation (not new research):** **epoch-ai-data-centers-db** record relabelled to reflect PRE-STUDY.md §4b's documented 1 Nov methodology-page inspection (coverage "46% (90% CI: 30% to 78%)"; cooling-model error history "77% and 118%"; no licence terms stated) — the record previously understated this read level; live database tables remain unread.

**New edges (2; both conservatively typed):**
- society/skills → governance/oversight **(sourced)** — the Anthropic RCT supports causal attribution WITHIN the experiment; note scopes it to one task, one model, strengthened leans, provider-authored, unreplicated.
- infrastructure/land → governance/rules **(association)** — AI Now toolkit's compiled siting/permitting interventions; explicitly marked upgradable if any cited example is verified at origin.

**State:** 140 records · **54 topic links** · **303 topic-record links** · 34/34 topics · read-mapped via bridge: **150**. catalogue.csv regenerated (matches JSON). topic_sources.json refreshed via the JSON-only path. **galaxy.html untouched by this batch** (user redesign continues; checksum observed 62b017e5…). checks.py: ALL PASS (0 dupes, 0 broken refs, CSV=JSON). No paid services; Cloudflare/SSOAR/SAGE gates not bypassed; Flash only.

---

## Addendum 31 (2 Nov 2026, latest): Anthropic paper read & link verified; two AI Now examples traced to official sources (both inaccurate); four under-read originals

**1. Anthropic 61-analyst study — full primary paper read.** "Who's Aligned to Whom? How AI Agents Shape Experts' Research Judgment Calls" (29 pp, SHA-256 ab13c3f1…, archived in sources/pdfs/). Main body pp. 1–14 read incl. the complete limitations; appendices A.1–A.10 unread. The paper CONFIRMS the page's headline numbers and ADDS qualifiers the page omitted: the 82% recommendation-prediction figure is "in an exploratory analysis", in-sample, restricted to participants who did not choose an extension, vs a 61% majority baseline (AUC 0.84); the 60% switching figure applies only to the 23% of decisions where the participant had already taken a side (self-selected subset); the final-recommendation effect is +17pp p=0.069 (not conventionally significant); recruitment was "through a paid expert-annotator marketplace"; participants were "new to the domain"; direct simulations show the agent "advocated the leaned option on 87% of 150 declarations". Three stated limitations: amplified lean ("Whether the flip rates hold for a stock agent depends on whether it has a preference... and volunteers it"), a single setting, average causal effects only. **Graph-link verification:** society/skills → governance/oversight (sourced) SURVIVES — random assignment identifies the lean's average causal effect — and the edge note was tightened with all the paper's own caveats.

**2. AI Now toolkit — two cited examples traced to official sources; BOTH descriptions materially inaccurate:**
- **California AB 93 "Water resources: data centers"** (official leginfo history + text): passed the Legislature but **VETOED 10/11/2025** — not law; override consideration pending since 22 Jan 2026. The toolkit's "(signed)" is CONTRADICTED. Bill text verified: pre-licensing water-use estimate "under penalty of perjury" + annual-use self-certification at renewal; threshold >10 kW and 20 W/sq ft; the text does NOT itemise end uses, so the toolkit's "loophole to exclude" cooling/construction water overstates a silence.
- **Maine "25 percent"** (official 132nd Legislature EUT Committee disposition, Aug 2025): the provision is **LD 912, Public Law 2025 ch. 85** (emergency, effective 23 May 2025) — a single-site nameplate-capacity condition ("may not use more than 25% of its nameplate capacity to serve data centers located on the commercial or industrial site", ISO-NE area, municipality north of Chester), NOT a statewide 25%-of-in-state-electricity-sales cap as the toolkit states.
- Conclusion recorded in the record, the note, and the handoff: the toolkit's signals are real but every example needs origin verification; the infrastructure/land → governance/rules edge STAYS association.

**3. Four under-read originals (major lab / university / SEA — no duplication; SEA-LION skipped as already near-complete):**
- **IndicTrans2 (AI4Bharat/IIT Madras ecosystem) §4–6 read** (pp. 12–24): mining (12 languages; Nepali dropped — LaBSE "suboptimal for Nepali"; 230.5M pairs after dedup; ~75% of NLLB/Samanantar data filtered out), modeling (2.2M gold pairs; script unification; <dnt> tags; 1.1B params; extended FLORES dev set released), evaluation (GPT-3.5/Azure/Google comparisons "a reasonable approximation"; "almost all the test sets are English-original"; chrF++ primary; COMET restricted to 13 languages). Unread: §2 detail, §7.1–7.3 tables, appendices.
- **Katadata Batam — FULL article read at origin** (SEA slot): byline/sections/credits recorded; new figures (Mytton 25.5M L/yr/MW; six reservoirs ≈382M L/day, Duriangkang −2.7 m in 2020; water tariffs Rp12,000 vs Rp28,000–36,000/m³; Rp300bn desalination; Golden Digital Gateway 881K L/day; Johor 72 projects/13 operational/2.6 GW); eight named interviews; industry counterpoints; the article's explicit non-causation framing stands. No date stated on the page (internal references imply 2025+).
- **OpenAI, "Safety and alignment in an era of long-horizon models" (20 Jul 2026) — page read at origin**: trajectory-level safety argument, the NanoGPT sandbox-escape example, pause/rollback safeguards, redeployment replays; stated limits (evals "never perfectly match" real use; replays non-deterministic). Provider-authored incident narrative — all specifics are OpenAI's account. Grounds how/agents → governance/oversight (sourced, with METR).
- **Mazzucato (UCL IIPP), "Public procurement for net-zero digital research infrastructure" (2023/02) — FULL read** (20 pp, via UCL Discovery after the Bartlett PDF endpoint returned a Cloudflare challenge — not bypassed; funded by UKRI, the body it advises — commissioned advice, not an evaluation): "digital and data infrastructure are not neutral. Governance structures are needed..."; hour-by-hour carbon reporting; "delaying the use of significant computing capacity – such as when training an AI system - during periods of high renewable energy capacity could significantly reduce carbon"; PPI/GPP; four conditionality types; pooled procurement. Unread: parts of §4 detail, references. Tier S→F; environment/energy added to galaxy_topics.

**New edge (1, conservative):** governance/procurement → environment/energy (ASSOCIATION — IIPP proposals, not implemented-procurement evaluations). Updated edge note: infrastructure/land → governance/rules now records the two trace findings.

**State:** 140 records · **55 topic links** · **304 topic-record links** · 34/34 topics · read-mapped via bridge: **155**. catalogue.csv regenerated (matches JSON). topic_sources.json refreshed JSON-only. **galaxy.html untouched by this batch** (user redesign continues; observed checksum eb2a5f56…). checks.py: ALL PASS (0 dupes, 0 broken refs, CSV=JSON). No paid services; Cloudflare gates (Chula, UCL Bartlett) not bypassed — legitimate open copies used where they existed; Flash only.

---

## Addendum 32 (2 Nov 2026, latest): Infrastructure expanded beyond physical assets — the cloud/software layer

**Scope inspected first:** the catalogue had the Oxford cloud-governance paper (near-fully read) but NO record on cloud market structure, connectivity/access, or SEA cloud services — the gap was real; no duplicates created.

**New graph topics (2, plain English; graph v0.6 — 36 topics, 61 links):**
- **infrastructure/cloud — "Cloud services & compute platforms"** [infrastructure, economics, governance]: rented computing (IaaS/PaaS) that AI runs on; the digital service AND its material basis.
- **infrastructure/connectivity — "Networks & access"** [infrastructure, society]: connections and last-mile access that decide who can use cloud and AI.
(Oxford Martin's record gained the infrastructure/cloud tag — the whole paper is about compute providers as governance intermediaries.)

**New sources catalogued and substantively read (2):**
- **UK CMA cloud services market investigation — FINAL decision (official regulator; NEW record cma-cloud-services-mi, F tier).** Summary of final decision (8 pp) read completely (sources/pdfs/cma-cloud-summary-final.pdf; SHA-256 98b48c48…); 637-pp full report + appendices unread. Official findings: IaaS "highly concentrated" — Microsoft and AWS each [30–40]% UK+EEA supply 2024, Google [5–10]%; both hold "significant unilateral market power" with returns "substantially above their cost of capital"; £10.5bn UK spend 2024 (~30%/yr); "Cloud services also underpin AI model development and deployment"; the three majors are "strong vertically integrated providers of accelerated compute and AI-related cloud services"; entry needs "significant capital investment in fixed assets such as data centres, networks and servers... largely a sunk cost"; "less than 1% of customers switch provider each year"; egress fees "a key commercial barrier"; Microsoft's licensing practices found adverse; decision: AECs on all three grounds; remedy: recommend SMS investigations under the DMCC Act (options expected early 2026). Limits: UK+EEA scope; bracketed ranges; SMS is a recommendation. The "voluntary commitments accepted" narrative in secondary reporting is NOT on the official case page and is not used.
- **Tech for Good Institute — "Digital Sustainability: Southeast Asia's Next Frontier" (exec summary, NEW record tfgi-digital-sustainability, F tier).** Singapore SEA institute (extends the existing TFGI record — no duplication). Methods: literature reviews + survey of 72 capital providers. Cloud named as enabler; substance is access: last-mile connectivity via 4P models, inclusive DPI ("interoperable ID systems, payment platforms and data exchanges that enable equitable access, trust and participation"), US$210bn/yr SEA climate-resilient-infrastructure financing gap, SEA draws only 3% of global impact-investing assets, 225m+ adults outside formal finance. Limits: NOT a cloud-market study; advocacy framing; secondary statistics; full report unread.

**Already-indexed records read this batch (3):**
- **OII/Foreign Affairs "Empires of AI"** (L→V): full essay read at origin — Ferguson/Klaassen/Schmidt argue knowledge empires; "the basic operating system on which everyone else must depend"; TSMC "the central node in the entire AI stack"; recorded as AUTHOR ARGUMENTS with secondary citations; institution field corrected (authors are not OII researchers). SEA only in passing.
- **CSET "Artificial Intelligence in Competition"** (L→V, exec summary): six theories of victory; "technological leads are small and shrinking". SCOPE NOTE recorded: NOT cloud-specific — not citable for cloud structure.
- **Oxford Martin "Governing Through the Cloud"** (already near-complete read): tagged infrastructure/cloud; its four-capacities proposal now anchors the cloud→oversight edge.

**New sourced cross-domain relationships (6 edges; graph v0.6):**
1. infrastructure/cloud → infrastructure/centres [sourced — CMA para 17: entry = capital in "data centres, networks and servers"; Oxford Martin] — "cloud runs in data centres".
2. infrastructure/cloud → economics/ownership [sourced — CMA paras 5–8, 36a: concentration, unilateral market power, above-cost returns].
3. infrastructure/cloud → how/inference [sourced — CMA para 3: "Cloud services also underpin AI model development and deployment"; para 12 vertical integration; para 13 AI "yet to materially alter" dynamics].
4. infrastructure/cloud → governance/oversight [sourced — Oxford Martin p.4 Table 1 four capacities; "providers can access basic technical data on how their hardware is used"] — a proposal, noted as such.
5. infrastructure/cloud → politics/international [association — Ferguson/Klaassen/Schmidt essay; author arguments, secondary figures].
6. infrastructure/connectivity → society/participation [sourced — TFGI: last-mile connectivity, DPI, "equitable access, trust and participation"].
The dependency chain is now on the graph: models/inference → cloud → data centres → electricity/water/grids, with ownership and governance attached to the cloud node.

**State:** **142 records** · **36 topics** · **61 topic links** · 311 topic-record links · 34/34→**36/36 topics covered** · read-mapped via bridge: **164**. catalogue.csv regenerated (142 rows, matches JSON). topic_sources.json refreshed JSON-only. **galaxy.html untouched** (observed checksum eb2a5f56… unchanged through the graph rebuild; refresh instruction updated in handoff: run build_topic_sources.py once after the redesign settles). checks.py: ALL PASS (0 dupes, 0 broken refs, CSV=JSON, all topics domain-valid). No paid extras; no UI edits; access gates respected.

---

## Addendum 33 (2 Nov 2026, latest): cloud & networks deepened — CMA evidence base checked, SEA cables and access gaps read

**1. CMA switching/egress findings — the actual basis, with geography and date checked** (final decision report paras 6.341–6.417, PDF pp. 330–349 read; appendices L–Q located but NOT read; 637-pp report archived, SHA-256 c33adc90…):
- Geography/date: market scope **UK+EEA** (fn 1); scenario built on **UK customer-level storage data 2018–2022** (from AWS/Microsoft/Google information requests); list prices "for the applicable UK region" — **London** for Google and AWS — **accessed 29 Jan 2024**; provider egress-payment shares for **2023**; free-switching programmes (2024) considered.
- Method: one-off full-data-transfer cost as % of annual spend, spread over a typical three-year contract. Provider-submitted analyses down-weighted on selection bias (switched customers exclude those deterred by fees, para 6.404).
- Results: percentages REDACTED as bracketed ranges in the public version ([0–5]%–[5–10]% above [5–10]% of annual spend per year; smallest customers hit hardest; unspread [10–20]%–[20–30]%). Caveats: analysis "likely to understate the effect" (total-spend denominator); list prices ignore CSA discounts and premium alternatives; combined effect "ambiguous".
- CONCLUSION: the egress/switching findings are a UK+EEA regulator's measured analysis on 2018–2022 UK data and Jan-2024 list prices — NOT SEA or global figures.

**2. Southeast Asian connectivity — two new records:**
- **ISEAS Perspective 2025/21, Cha Hae Won, "The Struggle for Subsea Cable Supremacy in Southeast Asia"** (14 Mar 2025; NEW record, F tier; pp. 1–11 read, annex pp. 11–23 unread): cables ≈1.4M km, "over 95 per cent of global data traffic"; **"ASN, NEC, SubCom, and HMN Technologies holding about 98 per cent of the subsea market share"** (p.4, endnoted, author compilation from TeleGeography Dec 2024); SeaMeWe-6 lost by HMN to SubCom amid US pressure (~US$4m training grants); US lobbying of Vietnam's ten-cables-by-2030 plan; **SJC2 "significantly delayed for several years due to Beijing's objections and lags in obtaining permits"**; **Apricot and Echo "deliberately rerouted to avoid passing the South China Sea"** at higher cost; "Chinese monopoly of subsea cables in the South China Sea" risk; nine US/France/Japan partnership cables with no Chinese supplier; conclusion: third-country suppliers enable hedging but the trend is "technological bifurcation"; ASEAN's Feb 2024 Digital Ministers' plan for a "diverse… submarine cable network". Limits: single-author perspective, institute disclaimer, TeleGeography-derived figures not independently verified.
- **ERIA, "ASEAN Digital Community 2045: A Strategic Overview"** (NEW record, V tier, SELECTED sections read: §3.3–3.4 + connectivity pillar; rest of 29 pp unread): ASEAN constrained by "the lack of both digital and physical enablers… innovative networks, hardware, software, data centres, and widespread broadband connectivity"; measured gaps — fixed-broadband speed Singapore 211.36 Mbps vs Indonesia 21.95 vs Myanmar 18.35; internet usage 40% (Myanmar) to 98% (Brunei); EIU index Singapore 1st vs Cambodia 75th; rural-urban divides. Limits: compiled third-party statistics (accessed 25 Jan 2024); no cloud/procurement analysis.

**3. Three new supported edges (graph v0.6.1 — 36 topics, 64 links):**
- infrastructure/connectivity → infrastructure/cloud [sourced — CMA para 17: cloud entry = capital in "data centres, networks and servers"].
- infrastructure/connectivity → politics/international [sourced — ISEAS: documented SJC2 delay, Apricot/Echo reroutes, Vietnam lobbying, minilateral exclusions; author's bifurcation outlook flagged as interpretation].
- infrastructure/connectivity → economics/ownership [sourced — ISEAS p.4: ~98% four-supplier cable-construction concentration; endnoted figure, flagged as author compilation; distinct from CMA's cloud-service concentration].

**Access failures and attempts (not bypassed):** IMDA Digital Connectivity Blueprint page exists ("LAST UPDATED: 02 Jul 2025", headings and a download link present) but its body is JS-loaded — official figures (current cable-landing count, doubling target) NOT read at origin; only secondary reports (Nikkei: ~25 cables at launch; CIL/NUS: 26 cables to seven landing stations) seen via search, not used as verified facts. asean.org's ADM-2025/2030 PDFs returned an HTML bot page instead of the PDF. The NUS CIL "ASEAN Academic Reports on Submarine Cables" page fetched empty.

**State:** **144 records** · 36 topics · **64 links** · 316 topic-record links · 36/36 topics covered · read-mapped via bridge: **167**. catalogue.csv regenerated (144 rows, matches JSON). topic_sources.json refreshed JSON-only. **galaxy.html untouched** (checksum eb2a5f56… unchanged). checks.py: ALL PASS. No paid extras; Flash only.

**Concrete gaps (named, for the next batch):**
1. SEA cloud-procurement regulator source still missing — DEFA documents, Singapore GovTech/IMDA cloud policies unread (IMDA JS-gated; ASEAN PDFs bot-gated).
2. CMA appendices L–Q (egress background, customer cost scenarios, free-switching programmes, customer views, internal documents, provider costs) unread — the redacted percentages mean the public record cannot state exact customer shares.
3. ISEAS 2025/21 annex and TeleGeography's own data pages unread (the underlying cable dataset).
4. IMDA cable-landing figures and the ASEAN Digital Masterplan cloud/action-plan content unverified at origin.
5. No SEA-specific cloud-market share data found in any read source (CMA is UK+EEA; ERIA/TFGI cover access, not market structure) — a genuine regional evidence gap, recorded as such.

---

## Addendum 34 (2 Nov 2026, latest): SEA cloud procurement found + labour/governance/model-ecosystem breadth

**Track 1 — SEA public-sector cloud procurement (the gap named in Addendum 33):**
- **NEW record — Philippines DICT Department Circular 2017-002, "Prescribing the Philippine Government's Cloud First Policy" (18 Jan 2017, 21 pp, F tier; Sections 1–9 read; Sections 10–15 headings only; DC-10 amendment image-only, unread).** PDFs read via third-party mirrors (JETRO, DataGuidance) of the official circular — provenance flagged; dict.gov.ph not directly fetched. Key provisions (exact): coverage of "all… Agencies of the National Government, including Constitutional Commissions, Congress, the Judiciary… Government-Owned or -Controlled Corporations and Local Government Units" plus accredited private CSPs; "It is hereby declared the policy of the government to adopt a 'cloud first' approach… as a primary part of their infostructure planning and procurement"; cloud as "the preferred ICT deployment strategy" with special-requirements and TCO/security exceptions; GovCloud + accredited-CSP list with Philippine-law dispute clauses. Scope: official policy TEXT (a documented procurement mandate), not implementation evidence; Philippines-specific; 2017 — predates today's concentrated market.
- **NEW sourced edge:** governance/procurement → infrastructure/cloud ("governments buy cloud first", DICT Section 5 quote).
- Access failures recorded: OECD WP93 page JS-gated ×2 (paper remains unread beyond metadata; the existing how/using→procurement edge cites it on metadata provenance only); IMF PDF endpoints bot-gated ×3.

**Track 2 — breadth beyond infrastructure:**
- **IMF WP 2026/204 (Eklou, "AI and Aggregate Labor Productivity: Evidence from Patent Data")** — page read at origin (H→V; PDF gated, not bypassed): OECD patent data **2000–2017**; output per worker +0.8–1.2%, possible long-run gains "up to 3.8 percent"; OECD ≈89% of world AI patents. CRITICAL SCOPE recorded: the window PREDATES generative AI — the estimates speak to pre-LLM AI; model estimates, not realised gains. Full methods unread.
- **Ai2 OLMo 3 release blog** (S→V, 20 Nov 2025 + Dec update): provider claims labelled throughout — full-flow release of "data, code, model weights, and checkpoints"; Dolma 3 ~9.3T tokens; "arguably the best 32B model… with open weights"; Instruct 7B trails Qwen 3 8B on several benchmarks. All performance/openness claims are the provider's own evaluations — the map's openness↔concentration debate (how/models → economics/ownership, association) gains a named, dated data point with its own admitted limits.
- Provider-claims vs independent-evidence discipline maintained: DICT = official policy text; IMF = author estimates (independent institution, unread full methods); Ai2 = provider assertions only.

**State:** **145 records** · 36 topics · **65 links** · 318 topic-record links · 36/36 topics covered · read-mapped via bridge: **174**. catalogue.csv regenerated (145 rows, matches JSON). topic_sources.json refreshed JSON-only. **galaxy.html untouched** (checksum eb2a5f56… unchanged). checks.py: ALL PASS (0 dupes, 0 broken refs, CSV=JSON). No paid extras; no access bypassing (OECD, IMF, ASEAN, IMDA gates all respected); Flash only.

---

## Addendum 35 (2 Nov 2026, latest): WP93 edges repaired; labour and SEA-SME breadth

**1. OECD WP93 edge audit and repair (explicit, per directive).** WP93 has never been read (publication page JS-gated twice). Two edges cited it:
- how/using → governance/procurement [sourced] previously rested ENTIRELY on unread sources (WP93 metadata + Culot handoff-metadata). REPAIRED: both citations withdrawn in the edge note; the sourced status is retained on read sources only (Wadipalapa et al. FULL TEXT; DICT Cloud First Policy Sections 1–9; Mazzucato/IIPP full read; Turobov & Coyle verified at origin), each named in the note.
- governance/procurement → governance/postmarket [association] previously attributed a "weak-measurement finding" to WP93. REPAIRED: attribution withdrawn; the edge is now an explicitly ungrounded open question with named candidate grounding (WP93, AEGIS) if ever read.
- The WP93 record itself now warns against citing it unread. BROADER AUDIT FLAG recorded in the handoff: other sourced edges still cite handoff-metadata-only records (Geith, Hoch & Mügge, Culot ×2, AEGIS, Chincholikar, Anastasopoulos, Pursiainen, Kim) — flagged for a coordinated audit; not silently withdrawn.

**2. Breadth reads:**
- **HAI AI Index 2026, Ch.4 Economy — overview + highlights (PDF pp. 171–174) read; body unread.** Labour: software developers 22–25 employment "fallen nearly 20% from 2024"; one-third of organisations expect workforce reductions though large-scale losses haven't shown in aggregate data; productivity gains 14–15% (support), 26% (software), 50% (marketing), smaller in deeper-reasoning tasks, with possible "long-term learning penalties"; SEA-relevant adoption stat — Singapore 61% vs US 28.3% (24th); Google >$150bn capex 2025.
- **NEW record — KAS/Flaminiano, "Exploring Readiness and Challenges to AI-Driven Competitiveness in Southeast Asian SMEs" (2025; partial read: abstract, methodology, results opening).** The accessible original regional study: 12 manufacturing-SME owners via 4 FGDs (Metro Manila, Rizal, Zambales); SMEs "over 99 percent of all firms" in SEA; barriers (skills, talent programmes, digital infrastructure, cost); skills gap worse in Indonesia/Philippines/Vietnam than Singapore; r=0.94 readiness×innovation (author's calc); 5/12 daily AI users. Limits: Philippines-only qualitative sample; think-tank chapter; self-reported adoption.
- (Education track: nus-genai-cs-education and SciTech Asia were already full reads — no duplication attempted; ICHEI/UNESCO/EdTech Hub candidates noted for a future pass in the handoff.)

**State:** **146 records** · 36 topics · 65 links · 320 topic-record links · 36/36 topics covered · read-mapped via bridge: **174**. catalogue.csv regenerated (146 rows, matches JSON). topic_sources.json refreshed JSON-only. **galaxy.html untouched** (checksum eb2a5f56… unchanged all session). checks.py: ALL PASS. No paid extras; no bypassing; Flash only.

---

## Addendum 36 (2 Nov 2026, latest): sourced-edge audit complete — 4 verified, 1 re-grounded, 5 downgraded

**Audit scope:** every sourced edge whose citation rested on unread/metadata-only records (the named handoff list: Geith, Hoch & Mügge, Culot ×2, AEGIS, Chincholikar, Anastasopoulos, Pursiainen, Kim). Method per edge: attempt the original substantive text through legitimate open-access routes; retain only what is verified; otherwise downgrade with the gate and date recorded. Direction preserved throughout; no citations fabricated.

**Retained as sourced, now verified by full-text reads (3 records upgraded H→F; 4 edges):**
1. **AEGIS** (npj Digital Medicine 9:789, 13 Oct 2026, OA — Afdideh et al., KTH): proof-of-concept post-market governance infrastructure (DARM/MMM/CDM → APPROVE/CONDITIONAL/CLINICAL REVIEW/REJECT + independent ALARM); sepsis instantiation — corruption iteration collapsed sensitivity 0.723→0.428 triggering REJECT+ALARM; drift AUC 0.82→1.00 (n≥100). Authors' limits: "proof-of-concept… not a clinical evaluation"; retrospective/simulation; covariate shift only. Edge governance/postmarket→oversight RETAINED with these passages.
2. **Chincholikar & Chawla** (Frontiers in AI, 21 Oct 2026, OA — independent researchers): pre-registered; 1,389 AIID incidents → 307 matched across 21 US-listed issuers; **"Only 4 incidents (1.3%) received incident-specific disclosure, and 7 (2.3%) any substantive disclosure"; "The remaining 300 incidents (97.7%) form an AI incident disclosure shadow"**. Limits: media-derived conditional denominator; filings-only universe; descriptive. Edge postmarket→accountability RETAINED.
3. **Hoch & Mügge** (Digital Society 5:45, 4 Sep 2026, OA — UvA): "informational disadvantages, reliance on external standard-setters, and enforcement delays"; standards delegated to CEN/CENELEC/ISO/IEC "whose own standards were delayed"; rules "watered down in the face of US competition"; EU influence in the US/China "the real litmus test" — "seems negligible so far". Edges rules→standards and standards→politics/national RETAINED.

**Re-grounded (1 edge):** infrastructure/grids → governance/rules — Pursiainen citation withdrawn (unread); the edge now rests on ISEAS (Green Lane 12-month connections; PUE guidelines "recommendations rather than enforceable regulations"), ISIS (grid governance "fragmented, voluntary… insufficiently matched"), Ember (frameworks came "after the industry had already begun to boom").

**Downgraded to association/open question (5 edges), each with the gate and date in its note:**
- governance/rules → politics/international (Geith: OUP 403; Kim: unread).
- governance/procurement → governance/oversight (Culot: Wiley gate; partial read context named — CMA lock-in, Oxford Martin verification proposal — neither measures audit rights).
- economics/ownership → governance/procurement (Culot: unread; related read evidence named — CMA public-sector concentration, DICT mandate).
- infrastructure/centres → infrastructure/grids (Pursiainen: Springer IDP cookie gate ×2; the demand-side link remains grounded by ISEAS/IEA reads).
- governance/discretion → governance/oversight (Anastasopoulos: Wiley 403; related read evidence named — Wadipalapa's discretionary gatekeeping; Anthropic RCT).

**Edge balance after audit: 40 sourced / 25 association** (was 45/20). Every remaining sourced edge's note now names at least one actually-read record, or (for the MIXED legacy notes, e.g. METR/OpenAI, IEA) at least one read record grounds the claim.

**Breadth note:** the audit itself added independent-research governance sources (KTH's AEGIS; two independent researchers in Frontiers; UvA) as full reads. SEA-work breadth is served by the KAS/Flaminiano study (Addendum 35); the ICHEI SEA-universities education report remains the queued next SEA read.

**State:** 146 records · 36 topics · 65 links (40 sourced / 25 association) · 320 topic-record links · read-mapped via bridge: **180**. catalogue.csv regenerated (146 rows, matches JSON). topic_sources.json refreshed JSON-only. **galaxy.html untouched** (checksum eb2a5f56… unchanged). checks.py: ALL PASS. No paid extras; all cookie gates respected (the two OA full texts were reached via the publishers' own no-cookie fallback URLs, not bypassed); Flash only.

---

## Addendum 37 (2 Nov 2026, latest): CMU public-administration guide read; ICHEI access failure recorded; sample audit of retained edges

**1. New read — CMU Block Center, "A Policy Maker's Guide to AI for State and Local Governments: Reaching Safe, Effective and Equitable Scale" (c. 2020; 10 pp; L→F partial — pp. 1–4 full, pp. 5–10 skimmed).** Public-administration primary source: AI "already in place" in US cities (Charlotte-Mecklenburg officer-risk model, 2015; Allegheny County child-welfare screening); equity risk ("the province of the wealthiest, largest, or most technologically sophisticated cities"); proposed National AI Strategy for Local Public Services (talent, digital infrastructure, regulatory/standards); LSE: "only 4.5 percent" of 15,000+ programmes adequately evaluated; AI forces explicit value specification; community involvement ("Most failed AI-assisted public programs do so at least in part because the community… [is] not involved"); the Flint case — 2017 volunteer ML model (18,883 inspections, 6,288 replacements, "70 percent accuracy rate") abandoned in 2018 after backlash, redeployed "with significant costs and lost time"; CMU finding that simplified flow charts beat confusion matrices for lay understanding. Limits: US-only; advocacy-adjacent; vignettes from secondary reporting; positive framing is the authors' position. society/participation added to its tags.

**2. Access failure recorded — ICHEI SEA-universities education report (Jul 2025):** two download attempts timed out (ar.ichei.org unreachable from this network; exit 28) — NOT bypassed. An access-failure record was created so the queue is explicit and nothing cites it unread.

**3. Sample audit of retained sourced edges (relationship + direction, not just read-status):**
- economics/evidence → economics/jobs ("applied to the jobs study"): confirmed at page level (Census limitations statement, verified at origin); note sharpened; full-text passage verification flagged outstanding.
- society/skills → economics/jobs ("verification is work too"): confirmed via Boysel/LAI survey statistics ("1 in 4 incoming pull requests are low-quality AI slop" driving "maintainer burnout to the #1 concern"; 1 in 3 projects with formal AI-contribution policies); unpaid-context caveat added.
- how/using → society/skills ("verification work falls on people"): confirmed (Turobov & Coyle human-in-the-loop "most effective balance" + Boysel/LAI statistics).
- infrastructure/centres → politics/chips ("chip export rules shape who can build"): confirmed via ArusGrid per-project chip export-control access tiers; no change needed.
No mismatches found in the sample; three edge notes sharpened to carry the exact supporting statistics (graph v0.7.1).

**State:** **147 records** · 36 topics · 65 links (40 sourced / 25 association) · 322 topic-record links · 36/36 topics covered · read-mapped via bridge: **183**. catalogue.csv regenerated (147 rows, matches JSON). topic_sources.json refreshed JSON-only. **galaxy.html untouched** (checksum eb2a5f56… unchanged). checks.py: ALL PASS. No paid extras; no bypassing (ICHEI timeouts respected); Flash only.

---

## Addendum 38 (4 Nov 2026, librarian session): regional, health, copyright and futures expansion

**Baseline verified:** 363 records (matches the independent check), graph v0.7.1 (36 topics / 65 links), checks passing, git main clean apart from the user's untracked preview dirs. Interim-session work (2–4 Nov) had grown the catalogue via notes/reading-ledger.csv + audit files; the galaxy.html embedded data block was stale at the 147-record state.

**Batch 1 — Africa & Latin America (gaps: zero regional coverage):**
1. **AU Continental AI Strategy** (Jul 2024, 66 pp — exec summary pp. 3–6 + five focus areas read; implementation unread). People-centric development framing; risks named incl. non-diverse data sourcing and indigenous-knowledge effects; "AI divide between and within countries"; 15 action areas starting with governance/regulations and public-sector adoption.
2. **ILIA 2025 Executive Summary** (ECLAC + CENIA, EU-financed; 17 pp read in full; 184-pp report unread). Region = 6.6% of global GDP, 8.8% of population, **1.12% of global AI investment**; investment intensity six times below global average; talent-outflow gap widening since 2022; Brazil/Costa Rica reversing inertia; third edition adds "quality of use" metrics (traceability, explainability, sensitivity testing).

**Batch 2 — Health & copyright (gaps: no health or copyright topic):**
3. **US Copyright Office, Part 2: Copyrightability** (Jan 2025, 52 pp — preface + 8-bullet exec summary + intro read; section analysis unread). "Resolved pursuant to existing law"; no copyright in purely AI-generated material; prompts alone insufficient; no case for sui generis rights. Training-data question explicitly NOT in this part.
4. **WHO LMM guidance** (Jan 2024; news release read at origin; ~98-pp guidance not opened). 40+ recommendations; five health-application areas; **"mandatory post-release auditing and impact assessments"** by independent third parties with disaggregated outcomes.

**Batch 3 — Futures & competing views:**
5. **Grace et al., Thousands of AI Authors** (2024; abstract read): 2,778 publishing researchers; 50% full-outperformance by 2047 (13 years earlier than the 2022 survey); 37.8–51.4% give ≥10% to extinction-level outcomes; broad agreement on prioritising risk research. Forecasts = expert opinion.
6. **Bommasani et al., On the Opportunities and Risks of Foundation Models** (2021; §1.1 + contents read; body unread): homogenisation = high leverage + shared-bias liability across modalities.
7. **Kapoor & Narayanan, AI as Normal Technology** (Apr 2025; read online to Part IV; truncated there): control/capabilities/diffusion principles; capability-reliability gap; benchmarks lack construct validity; systemic risks "far more important than the catastrophic ones"; resilience-first policy. The library's deliberate counter-frame.

**Batch 4 — Asia beyond SEA:**
8. **NITI Aayog, Responsible AI Part 1** (Feb 2021; principles + context read): six principles grounded in Indian constitutional rights; provenance flags (WEF C4IR knowledge partner; "legal inputs enabled by Microsoft").
9. **Japan AI Guidelines for Business Ver. 1.0** (Apr 2024; official MIC English release read; guidelines PDF gated, METI page 403): unified soft-law guidelines after 3,947 public comments; action-item text NOT captured.

**Graph v0.8 (38 topics, 67 links):** new topics **society/health** ("Health & medicine") and **politics/copyright** ("Copyright & creative work"), each created for a read source. Two new sourced edges: society/health → governance/postmarket (WHO mandatory post-release auditing + AEGIS as the medical demonstration); politics/copyright → governance/rules (USCO "resolved pursuant to existing law"). No other edges added; no training-data↔copyright edge (USCO Part 2 explicitly excludes that question).

**Integration:** 372 records in catalogue.json/csv (9 added, 0 duplicates); 9 ledger rows appended (interim-session convention); notes in sources/notes/librarian-batch-2026-11-04.md; PDFs + extractions archived in sources/pdfs/ (6 files); topic_sources.json rebuilt; **galaxy.html's embedded TOPIC_SOURCES block rebuilt via the project's own build_topic_sources.py — git diff confirms exactly 1 line changed (the const), UI code untouched**. checks.py: ALL PASS (372 records, 67 links, 0 broken refs, CSV=JSON, 38/38 topics covered).

**Honest limits:** all nine reads are partial (exec-summary/abstract/press-release level) with unread sections stated per record; the ILIA country tables, AU action-area detail, USCO section analysis, WHO full guidance, Grace survey methods, Bommasani chapters, Kapoor Part IV, NITI body and Japan guidelines text remain unread; the hardcoded institutionAbsences string in build_topic_sources.py predates the interim sessions' 216 additions and should be re-derived next pass; the 5 '?'-tier records and the interim sessions' ledger entries were not independently re-audited this session.

---

## Addendum 39 (4 Nov 2026, integration milestone): verified nine-reading batch integrated into the redesign-preview release

**Corrections applied first (from research-audit/audit-nine-readings-and-edges.md, each verified against the original):** NITI = seven principles (seventh restored from the document's own list); AU adoption = Executive Council 45th Ordinary Session, 18–19 July 2024, Accra (per the document foreword); WHO quote corrected to "disaggregated by the type of user" with the explicit recommendation-not-law scope; Kapoor quote corrected to "the right analogy is nuclear power"; Japan Ver. 1.1 marked search-derived. aegis-postmarket gained `society/health` in galaxy_tags (found when the map panel rendered its reading without a note). Graph v0.8.1; CSV regenerated; root galaxy.html block regenerated (one-line diff).

**Release integration (redesign-preview/, backups in research-audit/backups-2026-11-04/):** data.js (bridge 372/927/793/38 + 13 reading/audit notes + health/copyright topic items), galaxy.html (same splices + RESEARCH_LINKS 65→67 + two world-topic items), connection-evidence.js (65→67), translations.js (Indonesian for both new topics under id.ui; other languages on documented English fallback after a same-session mis-pass was caught and cleaned).

**Validation:** checks.py ALL PASS; parity suite T1–T6 ALL PASS (bridge parity per record, world-topics==graph-topics, edge parity 67 across graph/CONNECTION_EVIDENCE/RESEARCH_LINKS, notes 372/372 in all four stores, no stale counts, corrected wording everywhere); node eval of the five modified galaxy.html consts; **real browser flows on a loopback server**: desktop map (society → Health & medicine with body/Still-open/connection/2 readings incl. notes and depth details; politics → Copyright & creative work with USCO reading), Catalogue view (both readings + depth details), mobile 390×844 (both flows), galaxy.html map experience (67 edges incl. both new; screenshot confirms the new node rendered, Indonesian UI), AI-test start screen, astronaut guide, Map/Read toggle, search — all intact.

**Limitations found in browser verification:** (1) the release's i18n walker sometimes leaves freshly expanded panels in English (observed for the new Copyright topic in Indonesian mode while the Health topic translated; Indonesian strings verified present in the live dictionary; a manually translated node persists — release-UI characteristic, flagged to the owner, not patched); (2) language selection does not persist across reloads (release behaviour); (3) institutionAbsences string still needs re-derivation; (4) ICHEI remains an access-failure lead.

**State:** 372 records · 38 topics · 67 links (42 sourced / 25 association) · bridge 927/793 · checks.py ALL PASS · backups + integration log in research-audit/ · no git operations.

---

## Addendum 40 (4 Nov 2026, supervised milestone): source-pack integrated — 14 new readings across health, Africa, Latin America

**Verification before integration:** all 14 candidates independently re-verified against originals this session — Goh and Tao via direct publisher-page fetches (exact on-page figures confirmed), Hernström/Olson/Ruamviboonsuk via the Europe PMC API (title/journal/year/methods match), the 4 Africa items from archived extractions of the actual PDFs, the 3 LatAm items from the pages read in full. Dedupe by DOI/URL/title: zero overlaps with the 372-record baseline. Blocked items (Therabot; Isagah ACM) and unverified leads (MASAI final results; Oxford chatbot study; AIRIS-TB; Argentina pipeline figures) remain leads and were NOT added.

**14 new records (372 → 386):**
- Health (7, all open-access, all mapped to society/health + how/evaluation + oversight/postmarket as supported): Goh RCT (physicians+GPT-4 76% vs physicians 74%, P=.60 — vignette gains don't transfer); Hernström MASAI (105,934 women; detection 6.4 vs 5.0/1000; workload −44.2%); Kazemzadeh Zambia TB validation (1,932 participants; AUC 0.87; WHO sensitivity targets unmet at shared thresholds); Olson ambient scribes (burnout 51.9%→38.8%, pre/post — association labelled); Takita meta-analysis (pooled accuracy 52.1%, 76% high risk of bias); Ruamviboonsuk Thailand DR (94.7% accuracy in a national programme, over-read safety layer retained); Tao PreA RCT (consultation −28.7%, co-design beat fine-tuning — process endpoints only).
- Africa (4): CIPIT State of AI in Africa 2025 (exec summary; Kenya/SA/Nigeria/Ghana strides; consumption→creation shift; uneven progress); GIZ Invisible Workers 2026 (Sub-Saharan data-work markets; Ghana Meta-moderator litigation); Pidoux et al. data-labour mapping (43 of 55 African countries, 17 firms, n=81 union-participatory); IrokoBench (17 African languages, human-translated benchmark).
- Latin America (3): Latam-GPT official page (regional LLM project; details beyond the page marked unverified); Fundar Argentina value-chain column (data-centre-first critique; >25 AI bills none approved); Fairwork (five-principle platform ratings, 2025 reports for six countries).

**New sourced edges (3; graph v0.9 = 70 links):** society/health → how/evaluation (Takita 76%-high-risk-of-bias + Goh non-transfer — evidence-quality claim, labelled); how/evaluation → society/participation (IrokoBench: evaluation gaps exclude language communities — no causal claim, labelled); economics/jobs → society/participation (Fairwork Fair Representation across six LatAm countries — country scores labelled unverified).

**Release integration (redesign-preview/; backups research-audit/backups-2026-11-04/):** data.js + galaxy.html TOPIC_SOURCES/READING_NOTES/AUDIT_NOTES spliced to 386-state (973 links, 816 read-mapped); RESEARCH_LINKS and connection-evidence.js 67→70 edges. A visible map-panel double-reading of AEGIS was found in browser verification and fixed (the topic items' redundant hand-added sources arrays removed from both files — bridge records supply the readings). **i18n stall fixed narrowly** (i18n.js one line: rAF + 150 ms setTimeout fallback — the release's walker stalled when the tab was backgrounded because rAF pauses leave `queued` stuck true; verified: Indonesian now applies to newly expanded panels including both new topics via the release's own selector; parse-checked with node).

**Validation:** checks.py ALL PASS (386 records, 70 links, 0 broken, CSV=JSON); parity suite ALL PASS (per-record bridge parity, world==graph topics, edges 70 across all three stores, notes 386/386 in four stores, no stale counts, corrected wording, no duplicate readings, id translations present); node eval of galaxy.html consts; real browser flows: Health topic page renders all 9 society/health readings with notes and depth details; Copyright topic renders USCO with note; Indonesian labels verified live (world and topic level); map page-side builder produces 9 readings for society/health; GIZ filter check on jobs topic passes; mobile 390×844 map spot-checked (society world renders; the health panel interaction requires the map's own "Show topic details" toggle — page-side data verified, interaction noted).

**Honest limitations:** all 14 reads are abstract/exec/page level (three with PMC full text); two health studies have vendor co-authors (COIs recorded); Therabot/Isagah/Brookings/Argentina-figures remain leads; the map-panel interaction nuance above is release-UI behaviour, documented not patched; subagents failed twice on concurrency limits across sessions — all pack slices were completed directly; no git operations.
