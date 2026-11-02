# Pre-study: existing maps and literature tools

Inspected directly on **1 November 2026** by fetching each site and reading what it says about itself. This is a comparison of what exists, so the Galaxy of AI project does not claim novelty without evidence. Everything below is from the linked page itself; quotes are exact phrases. Checked for the whole project, not re-verified daily.

---

## 1. MIT AI Governance Map

- **Direct source:** https://airisk.mit.edu/ai-governance
- **Function:** An interactive tool that classifies AI governance documents. It "classifies more than 1000 cases of AI risk governance and regulation by risk coverage, sector, scope, and other relevant dimensions," intended as "A common frame of reference for researchers, policymakers, and practitioners working on AI governance."
- **Scope:** Legal and governance documents drawn from CSET's ETO AGORA database ("a living collection of AI-relevant laws, regulations, standards, and other governance documents from the United States and around the world"). The team says most documents originate in the US and they are "actively working to expand coverage of other jurisdictions." Findings are "based on a snapshot of the dataset taken 23 March, 2026."
- **Dimensions:** Risk subdomains (MIT AI Risk Domain Taxonomy), sectors, AI lifecycle stages (OECD/NIST definitions), Hard Law / Soft Law / Other, technical scope, actors. Seven dashboards plus a prototype actor network graph.
- **Method:** LLM-based classification of AGORA documents. The related AI Risk Repository used systematic search (43 risk frameworks, 700+ risks) with "best fit framework synthesis."
- **Stated limitations:** Patterns "should be taken as indicative and will need to be validated through further analysis"; a "systematic validation study is ongoing"; LLM misclassifications handled by spot-checks; dataset skews US; the Repository relied on "a single expert reviewer" and its taxonomies "prioritize clarity and simplicity over nuance."
- **Access & reuse:** Free, no account. "Data from the MIT AI Risk Initiative is licensed under CC BY 4.0" — reuse allowed with attribution. Suggested citation: "Mapping the AI governance landscape: April 2026 update."
- **Maintainer:** MIT AI Risk Initiative / MIT FutureTech (contact airisk@mit.edu).
- **Relevance to Galaxy of AI:** Maps the *governance documents* layer only. It does not connect governance to physical infrastructure, jobs, or economics — which is where the Galaxy constellation aims.

## 2. OECD AI Policy Navigator

- **Direct source:** https://oecd.ai/en/dashboards/international
- **Function:** Dashboard of the OECD AI Policy Observatory, "a living repository from more than 80 jurisdictions and organisations" for browsing AI policies and initiatives with filters.
- **Scope:** International organisations/forums (African Union, ASEAN, Council of Europe, EU, G7, OECD/GPAI, UN, UNESCO, OAS, Arab League, APEC, IEEE, ISO); the wider portal covers risk and accountability, data and privacy, generative AI, future of work, AI incidents, AI in government, compute, health. Views: Overview / National / International / "All initiatives" sorted by start year.
- **Stated limitations:** Invites submissions for missing content ("Is your country working on AI policies and initiatives that we haven't listed?"), implying incompleteness. Methodology and data sources are not described on this dashboard page.
- **Access & reuse:** Free, no account. The page states no licence of its own; it links only to general OECD Terms & Conditions and gives a citation format: "Please cite as: OECD.AI (2025), OECD.AI Policy Navigator, accessed on 01/11/2026, https://oecd.ai/dashboards." **Reuse terms: unverified** — the licence page was not reachable in this pass (HTTP 404), so check before redistributing OECD content.
- **Maintainer:** OECD (intergovernmental organisation).
- **Relevance:** Tracks *policy initiatives* across jurisdictions, not connections between topics. A Galaxy node can link to it as an authoritative "who is governing what" reference.

## 3. OpenAlex Topics

- **Direct source:** https://help.openalex.org/data/topics/
- **Function:** Scholarly topic classification: "4 domains → 26 fields → 252 subfields → 4,516 topics." Each work gets "up to three topics automatically"; assignments roll up to authors, institutions and sources.
- **Method:** Topics came from clustering the citation network ("works that cite each other frequently land in the same cluster") with an LLM generating names/descriptions. Assignments are made by a fine-tuned "Qwen3-8B language model" reading title, abstract and source name (any language), trained on 2 million works labelled by Claude Opus 5.5. The `score` is the model's probability and is calibrated ("topics scored 0.9 are right about 90% of the time").
- **Stated limitations:** Topics are "inferred, not looked up" — predictions, not curated labels. "About 10% of works have no topic." Datasets/catalogue records also receive topics, which can inflate `works_count`. Classifier replaced October 2026; old assignments frozen as v2.0.0; precision deliberately preferred over recall.
- **Access & reuse:** Free API (`api.openalex.org/topics`, filterable; also a text-aboutness endpoint to classify your own text). "Code, model weights, training labels and evaluations are open" on GitHub. (OpenAlex data is generally CC0, but this specific page does not state it — verify on the OpenAlex licence page before relying on that.)
- **Maintainer:** OurResearch (the OpenAlex team).
- **Relevance:** This is what a *literature* layer of a knowledge map would rest on — but its topic links are machine-assigned predictions, which the Galaxy project must label as such.

## 4. Data-centre trackers

### 4a. ArusGrid

- **Direct source:** https://arusgrid.com/methodology
- **Function:** "An independent tracker of the data center buildout, project by project." Name from "arus," Malay/Indonesian for current.
- **Scope:** Southeast Asia, the Gulf and India; full depth in Malaysia, Singapore, Indonesia, Thailand, Vietnam, the Philippines, UAE, Saudi Arabia, India; China entered October 2026, India on 27 September 2026 (58 projects). Inclusion: 20 MW planned/built IT load, or smaller with a confirmed hyperscaler/AI tenant. Tracks lifecycle stage, builder/funder/operator/buyer, IT load, capital and power costs. Cancelled projects stay in the dataset but are excluded from totals.
- **Method:** Megawatts always mean IT load; unknown figures stay blank. Every stage change needs "a dated source." Evidence tiers (verified/corroborated/sourced/thin), AI-readiness tiers, chip export-control access tiers, seven-gate "build odds," cost estimates from the Turner & Townsend index — all computed by fixed rules. "Aggregator market reports are banned as facility sources." Each batch gets an adversarial fact check; audit tables show claim error rates of roughly 4–10% for country passes and 24–38% for builder/infrastructure facts before correction, with "zero fabricated sources" found.
- **Stated limitations:** Live MW "systematically undercount[ed]"; vacancy known for only six of 16 markets; roughly half of facilities lack usable capital figures; Vietnam at lower confidence; the build-odds method "has not yet been tested against outcomes"; Gulf figures understate reality due to disclosure gaps.
- **Access & reuse:** Free site; dataset and visualisations licensed **CC BY-NC 4.0** (attribution, non-commercial; commercial licence separate). Dataset updated daily on GitHub. No named maintainer on the page. Corrections: corrections@arusgrid.com.
- **Relevance:** The closest existing thing to the Galaxy's "data centres → place" path, but project-by-project rather than conceptual — it does not map ideas or governance.

### 4b. Epoch AI — Data Centers database

- **Direct source:** https://epoch.ai/data/data-centers-documentation/methodology
- **Function & scope:** Database of "AI-optimized" data centers, mostly US-based but expanding globally, limited to facilities "operational in 2024 or later (with some exceptions)"; planned projects included only if construction has started. Tracks IT power capacity, AI compute (H100-equivalents), total facility power, construction timelines and capital-cost estimates. "Compute" means AI-chip capacity at a site, not all computing. Estimated coverage: "46% as of November 1, 2026 (90% CI: 30% to 78%)" of global deployed AI compute.
- **Method:** Three-phase pipeline — discovery (news, announcements, third-party databases, satellite imagery); research (commercial satellite imagery from SkyWatch/Vantor/Airbus/Google Earth/Sentinel-2, air-quality and building permits, tax abatements, company disclosures; facilities identified by cooling equipment, backup generators and substations); analysis (a cooling model estimating IT power from fan count/size/floorspace, peak PUE defaults of 1.2 for hyperscalers / 1.4 otherwise, a chip model with a one-quarter sales-to-deployment lag, and cost-per-Watt of "$38B capital cost per gigawatt of IT power").
- **Stated limitations:** Obscure or smaller (<100 MW) centers may be missed; permit plans can shrink, expand or stall; ownership/tenant arrangements are often secret; cooling-model errors historically ranged "77% and 118%" of reference values, with 80% of IT-power estimates within 1.4× of actual.
- **Access & reuse:** Free to read. **No licence/reuse terms stated on the methodology page** (only a site copyright notice) — check the site's terms before redistributing Epoch data.
- **Maintainer:** Epoch AI (research non-profit).
- **Relevance:** Complements ArusGrid: global, AI-specific, estimate-based (satellite/permit inference) rather than SEA/Gulf/India project journalism with evidence tiers. Both are honest about undercounting.

## 5. Regional reading on data centres (inspected 1 Nov 2026)

### 5a. Katadata — "A Digital Boom in a Thirsty City" (Batam)
- **Direct source:** https://katadata.co.id/data-center-batam/en (byline Rezza Aji Pratama; part of "Dark Side of The Boom", a 14-outlet Asian media collaboration initiated by Internews' Earth Journalism Network; no explicit publication date on page)
- **What it reports:** At least 18 data centres planned or being built in Batam (~1.26 million people, "relies entirely on six rain-fed reservoirs"). Flagship: NeutraDC–Nxera's US$600m, 56 MW project in Kabil Industrial Park (Telkom Indonesia 60%, Singtel/Nxera 35%, Medco Power 5%), first phase online "early 2026", potentially using 3 million litres of water daily. Nine more planned in Nongsa Digital Park SEZ; by 2032 ten facilities could need ~32 million litres/day — "about 8.4% of the current total supply", enough for 320,000 people. Meanwhile 18 "stress areas" already face rationing and fixing infrastructure needs ~Rp1.4 trillion (US$85m), 74% of BP Batam's budget; a national funding request was rejected.
- **What it does NOT claim:** It does not claim data centres caused the 2024 Teluk Mata Ikan crisis (blamed on a pipe leak) and does not assert that any specific facility caused particular household shortages. It includes industry counterpoints (efficient cooling designs) and closes on an open question: who gets prioritised in a drought.
- **Evidence base:** Named interviews (NeutraDC-Nxera CEO, BP Batam officials, residents, NGO, polytechnic), BP Batam figures, water-per-MW estimates attributed to David Mytton (Imperial College London), WHO's 100 L/person/day guideline.
- **Relevance:** The strongest local-case reading for the Galaxy's "data centres → place" connection — and a model of careful reporting: it shows expansion and stress side by side without claiming causation.

### 5b. ISEAS Perspective 2025/43 — Sara Loo, "Data Centres, Energy Demand and Sustainability: Can Malaysia Strike the Right Balance?"
- **Direct source:** https://www.iseas.edu.sg/articles-commentaries/iseas-perspective/2025-43-data-centres-energy-demand-and-sustainability-can-malaysia-strike-the-right-balance-by-sara-loo (published 12 June 2025; author: Associate Research Officer, Malaysia Studies Programme, ISEAS – Yusof Ishak Institute)
- **Main argument:** Malaysia "appears to have overcommitted to data centre expansion, especially in Johor, without sufficiently robust sustainability guidelines in place"; optimising PUE and encouraging renewables "runs the risk of greenwashing rather than achieving sustainable growth".
- **Key figures:** RM184.7bn (US$43.6bn) data-centre-related investment 2021–2024; projected data-centre energy use of over 5,000 MW by 2035 — "40 per cent of Peninsular Malaysia's present power capacity"; 38 projects signed electricity supply agreements with TNB; actual load Dec 2024 was 405 MW but secured maximum demand 5.9 GW (~43% of TNB's contracted capacity), which the author calls "hazardously high"; Johor holds close to 80% of live IT capacity (2024); renewables were 8.3% of TNB electricity (2023).
- **Stated limitations:** Analytical commentary; some figures (DCByte, May 2025) lack IT-capacity breakdowns; some claims rest on anonymised stakeholder interviews, presented as indicative; the institute "accepts no responsibility for facts presented and views expressed" (author's own).
- **Relevance:** Concrete, citable numbers for the AI → electricity connection in Southeast Asia; policy framing (full cost of service, lifecycle assessment, enforceable rules) links electricity back to governance.

### 5c. ISIS Malaysia / CERT — "AI and Climate Considerations"
- **Direct source:** https://www.cert.isis.org.my/publications/ai-and-climate-considerations/ (authors: Zayana Zaikariah, ISIS Malaysia, and Sara Loo, ISEAS–Yusof Ishak Institute / Anthesis Group; published 9 June 2026; policy paper with PDF)
- **Main argument:** Malaysia's "AI Nation by 2030" goal and its 2050 net-zero goal increasingly conflict; the data-centre boom serves mainly external commercial demand, and "the instruments meant to govern the boom were designed for a smaller scale of infrastructure."
- **Key figures:** Traditional data centres run 5–10 kW per rack vs 60 kW+ for AI-optimised ones; a GPU uses "five to ten times" the energy of a standard server chip; 143 projects approved 2021–June 2025 worth RM144.4bn; Ember projects data-centre demand rising from 9 to 68 TWh (2024–30), roughly 30% of national consumption; grid projected to stay over 75% fossil-fuel-dependent until at least 2033; of ~808 million litres/day of water requested in Johor, Selangor and Negeri Sembilan, only ~142 million litres "can be realistically supplied" (SPAN); Johor projects wait until mid-2027 for water.
- **Stated limitations:** Operational energy/water/emissions data are "deliberately opaque" and often unverifiable; some findings from 15 interviews across four countries "cannot be corroborated by published sources" and frame questions rather than definitive claims.
- **Relevance:** Connects the map's infrastructure nodes (electricity, water) directly to governance (verification, disclosure, REC accounting) — the same "oversight is infrastructure" theme as the AI side of the map.

## 6b. Educational explainer (inspected 1 Nov 2026, added during the repair pass)

### IBM Think — "What is artificial intelligence (AI)?"
- **Direct source:** https://www.ibm.com/think/topics/artificial-intelligence (authors Cole Stryker, Eda Kavlakoglu; IBM's public education platform)
- **What it covers (verified by direct fetch):** a plain-language definition — "Artificial intelligence (AI) is technology that enables computers and machines to simulate human learning, comprehension, problem solving, decision making, creativity and autonomy" — plus learning from data "without being explicitly programmed for specific tasks", and training/tuning/generation phases.
- **Why it is used:** the galaxy's basic-AI explanations (sun card, models & training, data) previously cited OpenAlex Topics and the OECD Navigator, which document *classification of research* and *policy initiatives* respectively — they do not explain how models work. This page is used as **"Further reading"**, clearly labelled, not as evidence for any factual claim.
- **Limitations:** it is a vendor education page that promotes IBM products alongside the content; it is introductory, not a research source.

## 6c. Deepening-pass sources (added 1 Nov 2026, access status recorded)

New sources brought into the galaxy during the deepening pass, each checked against the statement it supports:

**Verified directly at origin this session (abstract/record read):**
- **Turobov & Coyle, "Governing the evidence base"** (Data & Policy 8:e47, 2026) — https://doi.org/10.1017/dap.2026.10100 — **CC BY 4.0, open access.** Abstract confirms: 63 UN policy documents; four archetypes (expert, topic modelling, human-in-the-loop LLM, API automation); "the human-in-the-loop model offers the most effective balance". Supports the "Using AI in organisations" topic.
- **METR, "AI systems could cover up misbehavior"** (6 Oct 2026) — https://metr.org/blog/2026-10-06-ai-systems-could-cover-up-misbehavior/ — confirms the staging-viewer proof of concept ("we have not observed agents exploiting this in any of our evaluations"), the patch within one day, and the thesis that agent outputs are untrusted input and viewers are security-critical infrastructure. Supports the Human oversight and post-market topics.
- **Flanders & Nungsari, "Conditional Values"** (arXiv:2610.37197) — https://arxiv.org/abs/2610.37197 — abstract confirms provisional WVS Wave 8, 40,960 respondents, 24 country samples, tech optimism as strongest pooled predictor. Supports the Public attitudes topic. Cross-sectional caveat comes from the design, not the abstract.
- **Ginting et al. dataset** (Mendeley Data, DOI 10.17632/9b26sb2k4g.1) — **CC BY 4.0.** Record confirms 1,000 Indonesian civil servants, structured online questionnaire (Google Forms), 12 Mar–12 Jun 2026, Universitas Sumatera Utara; a dataset for analysis, not findings. Used as labelled "Further reading (dataset, not findings)".

**DOI resolves to the correct publisher, but the abstract was NOT re-read this session (bot/cookie gates); statements follow the 31 Oct handoff verification pass:**
- **Pursiainen, Rød & Johansson** (Eur. J. Security Research) — https://doi.org/10.1007/s41125-026-00115-w — Springer cookie gate.
- **Afdideh et al., "AEGIS"** (npj Digital Medicine) — https://doi.org/10.1038/s41746-026-03290-1 — Nature cookie gate.
- **Anastasopoulos** (Public Administration Review) — https://doi.org/10.1111/puar.70201 — Wiley returned HTTP 403.

**Dropped during verification:** the handoff's APSA preprint link for Baum, "Governing with Artificial Intelligence" now returns **HTTP 404**; a web search confirmed the preprint's existence but produced no precise working URL, so it is **not used anywhere** in the galaxy and its intended contribution (state-official perceptions) is omitted rather than weakly sourced.

## 6d. Literature mapping tools

### 5a. Open Knowledge Maps
- **Direct source:** https://openknowledgemaps.org/
- **Function:** Generates visual topic maps of research ("Get an overview - Find resources - Identify concepts") with thematic clusters.
- **Data source:** "Search more than 400 Million outputs in 400+ languages from over 11.000 sources (via BASE)" (base-search.net). PubMed and OpenAlex are **not** mentioned on the page.
- **Stated limitations:** Only "No hallucinations, results are based only on underlying metadata" — output quality depends on metadata quality; no other limitations listed.
- **Access & reuse:** Free, no accounts advertised. Content under "a Creative Commons Attribution 4.0 International License"; "Our software is open source and hosted on Github." Charitable non-profit funded by members (ETH Zurich, Harvard Library, ZBW) and funders (European Commission, Volkswagen Foundation, OpenAIRE). Organisations can buy "Custom Services" — but no paid APIs for normal users.
- **Relevance:** Closest analogue to the Galaxy's visual style (clustered node maps); confirms that simple visual mapping of literature is already well established.

### 5b. Connected Papers — **not inspected**
- A fetch of https://www.connectedpapers.com/about was declined in this session, so nothing is recorded about it here. It is widely known as a similarity-graph tool built on Semantic Scholar, but **that description is unverified in this project** and must not be cited from memory.

## 7. Comparison: what exists vs. what Galaxy of AI adds

| Tool / source | What it maps | Unit | Covers infrastructure/economics/jobs? | Reuse |
|---|---|---|---|---|
| MIT AI Governance Map | Governance documents | Documents/cases | No (governance only) | CC BY 4.0 |
| OECD AI Policy Navigator | Policy initiatives | Initiatives | "Compute" and "future of work" topics exist, but no connected map | Unverified on page |
| OpenAlex Topics | Scholarly subjects | Publications | As topics, yes — but machine-assigned predictions | Open code/labels; data broadly open |
| ArusGrid | Data-centre projects (SEA, Gulf, India) | Facilities | Yes — physical buildout, project by project | CC BY-NC 4.0 |
| Epoch AI Data Centers | AI-optimised data centres (global) | Facilities | Yes — power, compute, cost estimates | Not stated on page; check terms |
| ISEAS / ISIS Malaysia / Katadata | Regional analysis & reporting | Articles | Yes — Malaysia & Batam energy/water | Copyright of publishers; cite, don't republish |
| Open Knowledge Maps | Research literature | Papers clustered | No — whatever the search returns | CC BY 4.0, open source |
| **Galaxy of AI (this project)** | **Connections between AI and other domains, for one learner** | **Nodes + labelled edges with sources** | **Yes — as labelled topic links, not measured data** | Personal project; all sources linked |

**Prior literature-map leads not readable in this session.** Two earlier leads (a ScienceDirect article, https://www.sciencedirect.com/science/article/pii/S0161893826001092, and an MDPI article, https://www.mdpi.com/2076-3387/16/1/19) could **not** be read on 1 Nov 2026: ScienceDirect redirects to an Elsevier sign-in, and MDPI returned HTTP 403. Only abstract-level descriptions from earlier checks exist; no full-text review is claimed and no content from them is used in the constellation.

**Honest conclusion about novelty:** visual maps of AI governance (MIT), policy initiatives (OECD), scholarly topics (OpenAlex), data-centre projects (ArusGrid) and literature clusters (OKMaps) all already exist. What the Galaxy of AI first constellation can offer — and must state as its only difference — is a **beginner-oriented joined-up view**: one small map where a single learner can walk from AI to electricity, data centres, jobs and oversight with each link labelled as *topic link*, *factual claim*, or *unknown*, and each explanation short and source-linked. That is a personal learning aid, not a research instrument, and it is directly inspired by the tools above rather than replacing any of them.

## 8. Rules carried from START-HERE.md, CONTEXT.md and the research handoff

1. A connection means subjects are **related**; it does not mean one causes another. (START-HERE.md)
2. Never describe an association as causal, a benchmark as a deployment outcome, or an absence of public evidence as an absence of private action. (Handoff §0)
3. Machine-assigned topic links (OpenAlex-style) are predictions; label them.
4. Reported local effects (e.g., Katadata on Batam water) do not by themselves establish data-centre causation. (START-HERE.md)
5. Dated technical assessments (e.g., METR's red-team of 21 July–11 Aug 2026 systems) describe the system as it existed then, not now. (START-HERE.md, Handoff C1)
6. "AI exposure" does not mean job loss — it means how much of a job's tasks could be done or changed by AI. (CONTEXT.md)
7. Never claim a specific AI query ran at a specific facility without evidence; general inference chains are not case evidence. (CONTEXT.md)
8. The galaxy idea is not unprecedented — the tools above cover neighbouring ground; this project's only claim is a beginner-friendly joined-up view. (CONTEXT.md)
