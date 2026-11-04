# Librarian expansion batch — 4 November 2026

Baseline: 363 records (verified), graph v0.7.1 (36 topics, 65 links). This batch: 9 new readings, 2 new topics (society/health, politics/copyright), 2 new sourced edges, graph v0.8 (38 topics, 67 links).

## Batch 1 — Africa & Latin America (regional gaps)
1. **AU Continental AI Strategy** (Jul 2024; 66 pp; exec summary pp. 3–6 + five focus areas read; implementation unread). People-centric development framing; risks named (non-diverse data sourcing, discrimination, indigenous knowledge, GenAI disinformation/privacy/surveillance/copyright); "AI divide between and within countries"; 15 action areas starting with governance/regulations and public-sector adoption. [au.int PDF](https://au.int/sites/default/files/documents/44004-doc-EN-_Continental_AI_Strategy_July_2024.pdf)
2. **ILIA 2025 Executive Summary** (ECLAC + CENIA; EU-financed; 17 pp read; 184-pp report unread). Region has 6.6% of global GDP, 8.8% of population, **1.12% of global AI investment**; regional average six times below global investment intensity per GDP per capita; talent-outflow gap widening since 2022; Brazil/Costa Rica reversing inertia; new "quality of use" metrics (traceability, explainability, sensitivity testing). [CEPAL page](https://www.cepal.org/en/publications/84471-latin-american-artificial-intelligence-index-ilia-2025-executive-summary)

## Batch 2 — Health & copyright (topic gaps; new topics created)
3. **US Copyright Office, Part 2: Copyrightability** (Jan 2025; preface + 8-bullet exec summary + intro read; body unread). "Questions of copyrightability and AI can be resolved pursuant to existing law"; no copyright in purely AI-generated material; prompts alone insufficient; no case for new sui generis rights. [copyright.gov PDF](https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-2-Copyrightability-Report.pdf)
4. **WHO LMM guidance** (Jan 2024; news release read at origin; ~98-pp guidance not opened). 40+ recommendations; five health-application areas; mandatory post-release auditing by independent third parties with disaggregated outcomes. [WHO news](https://www.who.int/news/item/18-01-2024-who-releases-ai-ethics-and-governance-guidance-for-large-multi-modal-models)

## Batch 3 — Futures & competing views
5. **Grace et al., Thousands of AI Authors on the Future of AI** (2024; abstract read). 2,778 publishing researchers: 50% chance of full outperformance by 2047 (13 years earlier than their 2022 survey); 37.8–51.4% give ≥10% to extinction-level outcomes; broad agreement on prioritising risk research. Forecasts = expert opinion.
6. **Bommasani et al., On the Opportunities and Risks of Foundation Models** (2021; §1.1 + contents read; 214-pp body unread). Foundation-model homogenisation = high leverage + shared-bias liability, across modalities.
7. **Kapoor & Narayanan, AI as Normal Technology** (Apr 2025; read online to Part IV). Control/capabilities/diffusion principles; capability-reliability gap; benchmarks lack construct validity; systemic risks "far more important than the catastrophic ones"; resilience-first policy. The library's deliberate counter-frame to catastrophic framing.

## Batch 4 — Asia beyond SEA
8. **NITI Aayog, Responsible AI Part 1** (Feb 2021; principles + context read). Six principles grounded in Indian constitutional rights; WEF C4IR knowledge partner; "legal inputs enabled by Microsoft" (provenance flag). [niti.gov.in PDF](https://www.niti.gov.in/sites/default/files/2021-02/Responsible-AI-22022021.pdf)
9. **Japan AI Guidelines for Business Ver. 1.0** (Apr 2024; official MIC press release read; guidelines PDF gated). Unified soft-law guidelines after 3,947 public comments; response to generative-AI proliferation.

## New topics & edges (supported only)
- **society/health** ("Health & medicine") — created for WHO; edge society/health → governance/postmarket [sourced: WHO "mandatory post-release auditing" + AEGIS as the medical demonstration].
- **politics/copyright** ("Copyright & creative work") — created for USCO; edge politics/copyright → governance/rules [sourced: "resolved pursuant to existing law"].

## Access failures
- ICHEI SEA-universities PDF: server timeouts ×2 (recorded as an access-failure record on 2 Nov; unchanged).
- METI press release 403 / METI guidelines PDF returned HTML — Soumu English release used instead; guidelines text still unread.
- Kapoor & Narayanan: capture truncated at Part IV (policy section incomplete).

## Integration state
- catalogue.json/catalogue.csv: 372 records. Ledger: 9 rows appended. PDFs + extractions archived in sources/pdfs/.
- graph.json v0.8 rebuilt from build_graph.py (38 topics, 67 links; topics.csv/topic_links.csv regenerated).
- TOPIC_SOURCES block in galaxy.html rebuilt via the project's build_topic_sources.py (marker-bounded; UI code untouched).
