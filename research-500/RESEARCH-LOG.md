# Research expansion log — November 2026 ("research-500")

**What happened:** a catalogue-deepening pass for the Galaxy of AI research library.
**Catalogue: 390 → 904 records — 514 new sources** (`checks.py` passes; `catalogue.csv` matches `catalogue.json`; `galaxy.html` untouched per the redesign freeze).

## Reconciliation (user-prompted, 5 Nov ~06:45–06:55 WIB)
The earlier lead counts were inconsistent: a loose substring match ("lead" matching "leaderboard", "lead author") gave 41; a stricter pass gave 23. Every record was reclassified by what its verification string actually evidences. Corrections made:
- 7 Crossref-harvested records relabelled to disclose that only the first ~600 characters of the publisher abstract were read (as delivered by the API), not the whole abstract (noy-zhang, ayers, crompton-burke, baidoo-anu, ding-peft, gawlikowski, rudolph).
- brazil-pbia-2024-2028 relabelled from "Metadata only (lead)" to SECONDARY-READ (the NIC.br observatory overview was read; the gov.br primary document was not).
- xia-genai-motivation-meta confirmed as a lead (search-result summaries only; abstract never read).
- No reading is inferred from the mere presence of an OpenAlex abstract: API-ABSTRACT classification is applied only where the abstract text was actually retrieved and read (directly in the curator's digests, or per the Global South agent's documented workflow); OpenAlex records lacking abstracts were never recorded.

**Reconciled totals (514 new records):**
- 367 read at origin (page/abstract/full-text at the source, its mirror, or an archive copy)
- 121 abstract-read via API records (OpenAlex 113, Crossref 7 [truncated ~600 chars, disclosed], Europe PMC 1)
- 7 secondary-source reads (a summary/analysis about the source read; primary gated — each disclosed)
- 19 metadata-only leads (nothing read; exact failures stated) — jftc, nhtsa, tironi-albornoz, unesco×3, wef, therabot, electricity-maps, ema-singapore, occto, batch3-publicsector×4, aouad, bullock-2019, crs-water, xia
- Read at some level: 495; not read: 19.

## Post-500 continuation (5 Nov, 06:35–07:25 WIB, +14 records: 890 → 904)
OpenAlex budget reset at midnight UTC allowed two more clusters: agriculture (6 — Dhillon smallholder review; Choruma SSA scoping review; Dibbern/Embrapa drivers-and-barriers; Musanase Rwanda crop recommender; Mhlanga & Ndhlovu Africa adoption; Hasan Bangladesh ensemble) and low-resource languages (8 — LLaMA; Qwen3; Code Llama; continual-learning survey; hallucination survey; Faiss; Gallegos bias survey; PaLM 2 — the canonical gap LLaMA itself had still been missing). All abstract-level reads via OpenAlex records; merges validated; backup at 904.

## API-harvest extension session (5 Nov, ~05:55–06:40 WIB; +98 records, 792 → 890)
To reach the 500-new target, a bulk-harvest layer was added: an OpenAlex API harvester (`research-500/scripts/openalex_harvest.py`) that retrieves works with publisher-deposited abstracts, reconstructs them, dedupes against the catalogue, and prints a digest the curator reads before writing each record. Verification label used: "Abstract read via OpenAlex/Crossref API record 2026-11-05 (publisher abstract); full text not read; link = DOI at origin." Crossref's API (publisher-deposited abstracts) supplemented OpenAlex when its anonymous budget ran out mid-session.
- **Clusters harvested (direct):** labour (Czarnitzki German firm productivity IV; Autor NBER 32140; IMF Gen-AI SDN; Bick/Deming adoption; Eisfeldt firm values; de Ridder AER intangibles; Stephany AI-skills +21% wages; Zarifhonvar; Zirar; Shen&Zhang China robots; Filippi review), productivity/using (Dwivedi 43-expert; Kosmyna EEG "cognitive debt"; Bankins; Budhwar; Zhou&Lee PNAS Nexus creativity; Garibay HCAI; Wach; Feuerriegel), health (TRIPOD+AI; Singhal MultiMedQA; Kung USMLE; RETFound; Hager MIMIC Nature Medicine "not ready for autonomous clinical decision-making"), governance/standards (Díaz-Rodríguez trustworthy-AI; Ali XAI; FUTURE-AI 117-expert/50-country; Gupta GenAI-cyber; Aldoseri), models/evals (Zhao LLM survey; Gemini; GPT-4o system card; Qwen TR; Chang eval survey; Yao security; Mamba; GPT-4 TR; APT; SAM; weak-to-strong; Toolformer; ToT; Voyager; Med-PaLM 2; GraphCast; GAIA; LiveBench; AgentDojo; TheAgentCompany; WIMBD; DeepSeek-R1 probe), education (Chan×3 Hong Kong studies; Walter; Crompton&Burke 138-study PRISMA; Baidoo-Anu; Annapureddy 12 competencies; Morandini; Poláková 19k-organisations job-ads; Rudolph), trust (Goldstein influence ops; Ferrara; Kaur deepfakes; Noy&Zhang Science 453-person RCT; Ayers JAMA empathy; Gawlikowski uncertainty; Ding PEFT), economy (ITU; ILO WESO; OECD DEO; Du digital-infrastructure divide).
- **Global South background subagent:** ~1,950 works examined across 24 OpenAlex batches; 45 written (12 Africa, 8 SE Asia, 6 South Asia, 7 LatAm, 6 Middle East, 6 Global South-broad), all abstracts read from stored OpenAlex records; 5 had an unparsed topic shorthand, fixed to valid topic ids before final merge; 40+5 integrated (batch6-globalsouth.json). The agent documented OpenAlex's anonymous-budget exhaustion mid-run (resets midnight UTC).
- **Incremental saves + validation after every merge:** backups at 884 and 890; checks.py passed throughout.
- **Session totals:** 98 integrated; 0 leads; 26 candidates deduped out (already covered by earlier agents).

## Cumulative reading depth (500 new records — RECONCILED 5 Nov ~06:50 WIB)
An earlier count of "41 leads" used a loose substring match (matching "leaderboard", "lead author") and was wrong; a stricter pass then under-counted. Final reconciliation classified every record by what its verification string actually evidences:
- **367 read at origin** — page/abstract/full-text reads at the source, its official mirror, or an archive copy (by curator or area agents)
- **107 abstract-read via API records** — publisher abstracts as delivered by OpenAlex (100), Crossref (6) or Europe PMC (1), each linked to its origin DOI. Provenance label states the mechanism. 7 Crossref records were read at the ~600-character truncation the API returned — now disclosed in their verification strings. Where an OpenAlex record lacked an abstract, the work was NOT recorded.
- **7 secondary-source reads** — a summary/analysis page about the source was read while the primary stayed gated (e.g., Brazil PBIA via the NIC.br observatory; Pakistan policy via the ISSI brief; Moffatt v Air Canada holdings via the ABA analysis) — each disclosed in its verification
- **19 metadata-only leads** — nothing read (each states the exact failure: JFTC, NHTSA, Tironi & Albornoz, UNESCO×3, WEF, Therabot, Electricity Maps, EMA Singapore, OCCTO, batch3-publicsector×4, Aouad, Bullock 2019, CRS water FAQ, Xia meta-analysis)
Total read at some level: 481; not read: 19.

## Continuation session (5 Nov, 05:38–06:08 WIB, direct work)
After the first four batches (365 integrated), a final direct session added **37 more** (755 → 792) without subagents, working straight from verified URLs in 2-fetch rounds: NIST GenAI Profile, IEA grids report, UNEP AI end-to-end note, Council of Europe Framework Convention (CETS 225), OECD AI Principles (2024 update), WIMBD, LiveBench, AgentDojo, TheAgentCompany, GAIA, GPT-4 Technical Report, Mamba, APT, Segment Anything, weak-to-strong, Toolformer, Tree of Thoughts, Voyager, Med-PaLM 2, DeepSeek-R1 (probe confirmed), GraphCast (correct ID via search), IrokoBench, AceGPT, Jais, PhoGPT/ILIA/Airavata (earlier), AU Continental AI Strategy, Philippines NAISR 2.0, Thailand National AI Strategy, Pakistan National AI Policy (official PDF unfetchable — verified via ISSI brief), Singapore NAIS 2.0, Getty v Stability judgment page, FTC 6(b) report, ISO/IEC 42001, EU AI Act Article 72 guide, Bartz v. Anthropic settlement, de Vries-Gao Patterns water/carbon study, USGS BLM siting report, IPIE 2024-elections database, International IDEA LatAm information-integrity, Pew public-vs-experts + 25-country global, Ipsos AI Monitor 2025, MIT NANDA GenAI Divide (mirror-provenance caveat), npj human-LLM-collaboration meta-analysis, WHO 2021 ethics guidance, ILO WESO Trends 2025, ITU Facts & Figures 2026, OECD DEO Vol.2, MLE-bench. Saves were incremental (backups at 755/766/771/768/788/790/final). Dedup continued to work: 26 of 45 direct candidates this session were dropped as already-covered by earlier agents (incl. Luccioni FAccT, IEA minerals, WHO LMM 2025, Dolma/FineWeb, USCO Part 2, FDA PCCF, DeepSeek-R1, Gemini 1.5 — all found by agents first).

## Method
- Six area subagents per batch for batches 1–3 (concurrency-limited to one at a time; the fourth batch ran directly instead).
- Every record: original URL, publication date, authors, institution, type, plain-English summary with key findings/methods/limits attributed to the source, and an exact `verification` string stating what was read and when (2026-11-04/05) and what was NOT read.
- Inaccessible pages (403s, JS/WAF gates, paywalled abstracts, bot-blocks) were kept as **leads** labelled "Metadata only (lead)" — 41 of 365. Nothing unread is presented as read.
- Deduplication: normalised title, URL and DOI against all 390 pre-existing records and within each batch (`research-500/scripts/merge_batch.py`). 3 duplicates excluded across merges; a further 12 direct-pass candidates were dropped as duplicates of better-read records found by earlier agents.

## Batches
| Batch | Areas | Candidates | Integrated | Notes |
|---|---|---|---|---|
| 1 | how-AI-works; infrastructure+environment; economics; governance/law; society/health/education; global South + geopolitics | 131 | 130 | 9 leads |
| 2 | how (scaling/interpretability/reasoning); infra (grids/regions/LCA); economics (VC/trade/adoption); governance (elections/privacy/criminal justice); society (creative/gender/indigenous/youth + SEA education gap); datasets/trackers | 130 | 130 | 12 leads; ICHEI SEA report found to be already catalogued |
| 3 | safety/security/watermarking; chips/industrial policy; sectors (finance/agri/public services/SME); public-sector practice (registers, Robodebt/SyRI, participation) | 88 | 87 | 5 leads; 1 dup excluded |
| 4 (direct) | national governance (EO 14110/14179, EU AI Act, NIST RMF, Singapore NAIS 2.0, China GenAI measures, Indonesia Stranas KA), Getty v Stability, FTC 6(b), ISO 42001, ILIA 2025, regional LLMs (PhoGPT/Airavata/Jais), ITU, MLE-bench, Bullock lead, OECD DEO | 30 | 18 | 12 dropped as duplicates; 2 leads |

## Reading depth (first 402 new records — superseded by the reconciliation above, retained for provenance)
- 379 records read at abstract level or better
  - fuller reads: full texts, translations, executive summaries, page-anchored passages, official overview pages
  - abstract/page-level reads
- Leads and classification now follow the reconciled four-way scheme: READ-ORIGIN / API-ABSTRACT / SECONDARY-READ / LEAD.

## Full-text highlights (beyond abstracts)
EO 14110 full text; EO 14179 full text; China GenAI Interim Measures full translation; China AI-labelling Measures full translation; G7 Hiroshima Code (8pp); UNGA resolution text; OECD Gov-with-AI foreword+exec; ASEAN sustainable-DC guide exec pp.1–5; Getty v Stability judgment page (205pp PDF unread — flagged); Thomson Reuters v Ross opinion pp.1–3; USCO Part 3 selected pages (prior session).

## Known gaps and open items
- Thinnest new-record growth: infrastructure/land (5), infrastructure/grids (5), environment/goals (4), politics/copyright (4) — existing records cover them, but new depth was limited by access failures and the research budget.
- Blocked-at-origin (retry candidates): WEF Future of Jobs, UNESCO main site (RAM tracker, AI competency framework), JFTC competition report, NHTSA SGO, OECD WP93 (long-standing), Electricity Maps portal, EMA Singapore, ISEAS annexes, CMA appendices L–Q, CRS water FAQ, de Vries Joule, Bullock 2019/2020 (Sage/IOS gates), RAND federal-siting report, congress.gov/USGS mirrors, moitt.gov.pk PDF (application/pdf unfetchable by tooling).
- The **500-new-source target was reached** (890 catalogue records): batches 1–3 via area subagents (347), batch 4 direct (18), the OpenAlex/Crossref API harvest + a Global South background agent (+98), and the earlier continuation direct passes (+37). Constraints encountered along the way: subagent concurrency (one at a time), OpenAlex anonymous-budget exhaustion mid-session (resets midnight UTC), Semantic Scholar 429s, and per-site blocks listed above.

## Files
- `research-500/agent-outputs/batch{1,2,3}-*.json` — subagent candidate files (source of truth for merges)
- `research-500/direct/batch4a.json`, `batch4c.json` — direct-research records
- `research-500/scripts/merge_batch.py` — dedup/merge/validation used for every integration
- `research-500/backups/` — catalogue snapshots at 755, 766, 771, 768, 788, 790, final(792)
- `research-500/existing-sources-compact.txt`, `dedup-keys.json` — dedup aids (refreshed at 520/650)

**Standing rules honoured:** no publication, no deploys, no paid services, no outreach, no edits to `galaxy.html` or other projects; graph.json untouched (no new topic links asserted beyond what sources support). No git commit made (work preserved via backups; say the word if a commit is wanted).
