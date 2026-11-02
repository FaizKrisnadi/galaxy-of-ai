# PDF full-text reads (page-numbered extraction, 1 Nov 2026)

Tooling: pypdf 6.10.0 (runtime provided by supervisor). All three PDFs downloaded from official sources, checksummed (SHA-256 recorded in sources/pdfs/), and converted to page-numbered text (`sources/pdfs/*.txt`). Extraction quality: high (Oxford 55 pp / 0 near-empty; ISIS 36 pp / 3 near-empty; IEA 304 pp / 5 near-empty). **Unread pages are stated per document.** Principle: author conclusions are author conclusions; scenario projections are not forecasts; nothing below is presented as independently validated.

---

## 1. IEA — Energy and AI (2025)
**Version:** IEA (2025), Energy and AI, IEA, Paris. Published 10 Apr 2025. CC BY 4.0. PDF 304 pages (SHA-256 3956b80152d4aac6b659a09d…).
**Pages read:** Executive summary **pp. 13–17** (complete); Annex A methodology **pp. 255–257** (start). **Unread:** pp. 1–12 (framing), 18–254 (all six chapters incl. "Energy demand from AI" body, AI-for-energy chapters, security/climate chapters, country notes), 258–304 (rest of Annex A, Annex B definitions, Annex C references).
**Executive summary (pp. 13–17), exact passages:**
- p.14: "Data centres accounted for around 1.5% of the world's electricity consumption in 2024, or 415 terawatt-hours (TWh). The United States accounted for the largest share… (45%), followed by China (25%) and Europe (15%)."
- p.14: "Data centre electricity consumption is set to more than double to around 945 TWh by 2030… AI is the most important driver of this growth."
- p.14: "By the end of the decade, the country [US] is set to consume more electricity for data centres than for the production of aluminium, steel, cement, chemicals and all other energy-intensive goods combined."
- p.14: "Base Case sees global data centre electricity consumption rising to around 1 200 TWh by 2035."
- p.14: "Half of the global growth in data centre demand is met by renewables… Natural gas expands by 175 TWh… Nuclear contributes about the same amount… The first small modular reactors come online around 2030."
- p.15: "around 20% of planned data centre projects could be at risk of delays" (grid strain); "50% of data centres under development in the United States are in pre-existing large clusters".
- p.15: sensitivity cases — "the range of data centre electricity demand across our cases spans from 700 to 1 700 TWh" by 2035; High Efficiency Case 20% below Base in 2035.
**Methods (Annex A, p.255):** bottom-up model from Lawrence Berkeley National Laboratory; central input = annual server shipments (IDC 2019–2028 projections triangulated with Omdia, SemiAnalysis, Borderstep, Gartner, Koomey, Shehabi et al.); three data-centre archetypes (enterprise, colocation/service provider, hyperscale); technical characteristics based on US estimates (Shehabi et al. 2024) assumed constant across types; transmission network excluded from data-centre modelling.
**Nature of claims:** the 945/1,200 TWh numbers are **Base Case scenario projections**, not observations; the 415 TWh 2024 figure is a modelled estimate (LBNL-based), not a metered total. Author conclusions, within stated uncertainty.
**Galaxy:** how/inference ↔ environment/energy (graph edge grounded here); infrastructure/electricity; environment/energy; infrastructure/centres.

## 2. Oxford Martin School — Governing Through the Cloud (2024)
**Version:** 13 Mar 2024 policy paper; Heim, Fist, Egan, Huang, Zekany, Trager, Osborne & Zilberman; open PDF 55 pages (SHA-256 b8b0b59eacd579461b9d8443…). Note: "being an author does not imply agreement with every claim" (authorship note, p.2).
**Pages read:** Executive summary **pp. 3–5** (complete, incl. Table 1 of the four capacities); §1.4 Limitations and Future Research Directions **p. 10**; §2.1 supply-chain framing **pp. 10–11**; table of contents. **Unread:** pp. 6–9, 12–55 (detailed capacity chapters — Security, Record Keeping, Verification incl. workload classification/compute accounting, Enforcement — the full US case study §4, conclusions, annexes).
**Key content (page-referenced):**
- p.3: proposal is "not intended to replace existing regulations on AI developers but rather to complement them"; focus on frontier AI "narrows the regulatory scope to the smaller set of key customers".
- p.4 (Table 1): the four capacities with definitions and examples — Security (prevent model/IP theft; protect large-scale deployments), Record Keeping ("selective collection… of high-level information of a compute provider's infrastructure usage"), Verification (confirm compliance with compute-threshold reporting; verify licences), Enforcement ("Restriction or limitation of compute access… for non-compliant customers"; "Disable AI systems that demonstrate activity that is undesirable, uncontrollable, or in violation of regulations").
- p.4: technical feasibility — providers "can access basic technical data on how their hardware is used"; workload detection/classification and compute quantification "likely" possible; verifying training-data type or specific evaluation runs "is not currently possible without direct access to customer code and data"; confidential computing may enable more later.
- p.5: EO 14110 already implements record-keeping roles (KYC for foreign customers; reporting of foreign training runs); extending to domestic customers + verification/enforcement would build "a comprehensive compute oversight scheme".
- p.10 (§1.4 Limitations, exact): "Our discussion is not a comprehensive policy blueprint ready for implementation"; internationalisation "is not explored in detail, especially the legal aspects"; reporting requirements "must be carefully weighed against the potential for misuse or government overreach"; frontier focus "simplifies the regulatory landscape" (GDPR protects natural persons, fewer constraints on juridical persons).
**Galaxy:** governance/procurement, governance/standards, infrastructure/chips, how/using.

## 3. ISIS Malaysia — AI and Climate Considerations (2026)
**Version:** 9 Jun 2026; Zaikariah (ISIS Malaysia) & Loo (ISEAS/Anthesis); PDF 36 pages (SHA-256 aed940b1f4a976d02558e441…). Foreword by Datuk Prof Dr Mohd Faiz Abdullah (ISIS Executive Chairman).
**Pages read:** authorship/foreword **pp. 3–4**; executive summary **p. 6** (start); findings §3.2 "Do the climate and environmental costs add up?" and §3.3 governance **pp. 13–15**. **Unread:** §1–2 detail (pp. 7–12 incl. methods exposition of the 15 interviews), §4–6 (pp. 16–35, compromises/opportunities/recommendations), references p. 36; 3 near-empty pages (section dividers).
**Key content (page-referenced):**
- p.4 (Foreword): framing — "AI Nation by 2030" vs net-zero 2050; "Policymaking in this area therefore cannot merely be driven by optimism or alarmism."
- p.6 (Exec summary): "Malaysia's increasing adoption and construction of AI infrastructure undermines its ability to effectively pursue climate and environmental goals"; "governance architecture lacks capacity to manage data centre growth and operations." — author conclusions.
- p.13–14: TNB Q4 FY2025 analyst briefing — 35 projects in operation; 7.5 GW cumulative maximum demand secured; load utilisation 405 MW (Dec 2024) → 850 MW (Dec 2025); = 16% of total generation capacity and "54% of Peninsular Malaysia's total contracted capacity (13.8GW)", up from 43% the previous year; "hazardously high".
- p.14: installed renewables 31% (Dec 2025); Ember: 9→68 TWh (2024–30), ~30% of national consumption; "emissions potentially rising sevenfold"; needs 6–8 GW new capacity by 2030 (~40–54% increase on 15 GW gas); NETR 70% RE-by-2050 target vs Ember's ~52% generation share estimate.
- p.14: water — GPT-3 training ≈5.4m litres; global AI water withdrawal 4.2–6.6 bn m³ by 2027; Johor projects wait until mid-2027.
- p.14–15: SPAN — ~808m L/day requested across Johor/Selangor/Negeri Sembilan, only under 20% (~142m L) "can be realistically supplied"; cooling ≈675m L/day (~700,000–800,000 households).
- p.15 (§3.3): governance "fragmented, voluntary and, as stakeholder interviews corroborate, insufficiently matched to the scale and pace".
**Methods (from p.2/page-level; details in unread §1–2):** 15 anonymised stakeholder interviews (Mar–Apr 2026) across four countries, five sectors.
**Limits:** author conclusions ("undermines") rest on projections (Ember/TNB) + interviews; operational data "generally not publicly disclosed"; interview findings partly unverifiable; recommendations (§6) unread in this pass.
**Galaxy:** environment/energy, environment/goals, infrastructure/water, economics/investment, governance/rules.

## Extraction quality & failures
- All three PDFs converted without page errors; 8 near-empty pages total (dividers/covers).
- Figures/charts are not in extracted text (captions only) — numeric readings above come from body text, not chart interpolation.
- No pages were skipped silently: page ranges read vs unread are listed per document above.

---

## 1b. ISIS Malaysia — AI and Climate Considerations (36 pp) — FULL PDF obtained; deepened read (2 Nov 2026)
**Newly read this pass:** methods and limitations **pp. 7–8** (exact: "such data remain deliberately opaque"; interview findings "used to frame analytical questions, rather than make definitive claims"; AI racks 60kW+ vs 5–10kW; "AI data centres typically require liquid or immersion cooling systems, rather than the air-cooling infrastructure of their traditional counterparts"; the disconnect argument — buildout supports "GPU-intensive workloads of global technology companies engaged in LLM training and inferencing" while AI-RMap priorities are flood forecasting, public health, traffic management); recommendations **pp. 29–30** (standardised REC framework; workload disclosure modelled on the EU Energy Efficiency Directive; nationally beneficial uses — flood forecasting, river monitoring; standing technical working group with a water/climate subcommittee "tasked with linking data centre water approvals to catchment-level supply assessments"). **Still unread:** pp. 9–12 (§2.1–2.3 detail), pp. 16–28 (§4 compromises, §5 opportunities). Endnotes pp. 30–32 scanned (sources include IEA, Loo 2025, Li et al. water footprint, Khazanah Research Institute).

## 1c. ISEAS Perspective 2025/43 — Sara Loo (13 pp) — FULL PDF read, all pages (2 Nov 2026)
**Version:** ISEAS Perspective 2025/43, 12 June 2025, ISSN 2335-6677; open PDF from iseas.edu.sg. Institute disclaimer: "ISEAS – Yusof Ishak Institute accepts no responsibility for facts presented and views expressed."
**Pages read:** all 13.
**Key page-anchored content beyond the earlier page-summary:**
- p.2: >5,000 MW by 2035 = "40 per cent of Peninsular Malaysia's present power capacity, or 11.1 per cent of Malaysia's projected power capacity in 2035"; load 405 MW = 3% of TNB supply vs 5.9 GW secured = 43% — "hazardously high".
- p.3: PM Anwar's selective-FDI stance; IEA: a typical AI data centre "uses as much power as 100,000 households at present, while the largest centres currently being constructed will consume 20 times that amount"; "computational power needed for sustaining AI's growth is doubling roughly every 100 days".
- p.4: Johor >1.6 GW total supply (2024); AirTrunk 150 MW + 270 MW scalable; Yondr 300 MW at Sedenak; Johor DC capacity 10 MW (early 2021) → 1.3 GW (Nov 2024) → 2.7 GW expected (2027).
- p.5: TNB Green Lane Pathway — "connected three times faster… reducing the implementation period of 36 to 48 months, to 12 months"; DESAC 21 projects, RM113.8bn; Knight Frank table (Johor live 396.9 MW / pipeline 898.7 MW); "The inference phase accounts for approximately 60–70 per cent of overall machine learning-related energy use and 20–40 per cent in the training phase"; use-phase GHG 95 MtCO2e (2020) ≈ 3× production stage.
- p.6: Georgia case — 80% of 8,200 MW growth tied to data centres; residential bills +US$43/month; Senate Bill 34; collateral rule; TNB tariff 39.95 → 45.62 sen/kWh (+14.2%); capex to RM26.5bn (RP4).
- p.7: PUE ≤1.4 for >21 MW hyperscalers — "many points are framed as recommendations rather than enforceable regulations"; NAIO CEO: "we haven't come to a landing yet"; greenwashing risk.
- p.8: AirTrunk 30 MW VPPA; RE matching ≠ renewable powering; JHB1 solar-ready roof 1 MW = "a mere 2 per cent of its current phase's energy needs"; RE 8.3% of TNB generation (2023); SAC charges 45 vs 25 sen/kWh; Bridge DC 400 MW CRESS.
- p.8 solar-land illustration — "10 acres/MW → 5.9 GW would need 59,000 acres, over 60 per cent of Johor's landmass of 96,680 acres": **CONTRADICTED by official statistics (2 Nov 2026)**. DOSM gives Johor 19,166 km² (2020) ≈ 4.736 million acres, so 59,000 acres ≈ 239 km² ≈ **1.25%** of the state. Do not repeat the ISEAS claim. Also: the 10 acres/MW assumption (an ISEAS endnote citing a US county example) and the 5.9 GW sizing are NOT validated as adequate for 24-hour demand; 5.9 GW is secured maximum demand — a committed reservation, not continuous draw.
- p.9: recommendations — full cost of service / differential pricing (>21 MW); lifecycle assessment; "more proactive, enforceable guidelines".
- pp.10–11: Johor state planning guidelines + MIDA DESAC PUE/CUE/WUE tables (grid emission factors 0.758/0.425/0.198 GgCO2/GWh).
- Endnote 13 (p.12): "Estimating energy capacities with accuracy and consistency remains a challenge due to differing levels of transparency and reporting strategies across firms."
**Limits:** single-author commentary; institute disclaimer; industry data (DCByte/Knight Frank) without full live/pipeline breakdowns.
**Galaxy:** infrastructure/electricity, infrastructure/land, environment/energy, governance/oversight (enforceable-guidelines argument).

---

## 1d. ILO WP140 — deepened read (2 Nov 2026, pass 2): methods, assumptions, limitations
**Newly read:** §3.4 Survey design limitations (**paper pp. 18–19 = PDF pp. 21–22**) and the surrounding sampling detail.
**What exposure can and cannot tell us (exact passages):**
- Self-assessment design: "tasks of managers are assessed by individuals working as managers, tasks of professionals are assessed by professionals" — and therefore "the sample may not represent the entire working population, and interpretability of opinions on the automation potential is limited to comparisons within each 1-digit group" (p. 19).
- Familiarity imbalance: "We also expect an imbalance of understanding and experience with tasks and GenAI across different occupational groups" (p. 19); mitigations: an introductory GenAI prompt for respondents plus a parallel expert survey with manual adjudication of drastic discrepancies.
- Sample attrition disclosed: 57,400 observations from 1,640 respondents; 105 participants removed as insufficiently credible (<50% task rankings); 1,167 "don't know" rankings excluded — and "don't know" answers "occur twice as frequently in manual or technical fields" (Groups 3, 7, 8, 9) — i.e., attrition is concentrated in exactly the lower-exposure groups.
- Interpretation guardrails (pp. 46–48, read in pass 1): exposure ≠ actual impact; static snapshot; few fully automatable jobs.
**Unread:** pp. 20–45 (per-gradient figures 18–19 detail), annex pp. 51–68 (4-digit exposure table, sampling formula, questionnaire).
**Galaxy note:** the jobs↔national graph link was DOWNGRADED from sourced to association on this basis — the paper documents gradients and recommends policy processes; it does not document actual national policy responses.

## 2b. SciTech Asia — AI literacy and Thai workforce readiness (23 pp) — FULL PDF read (2 Nov 2026, pass 2)
**Version:** Science & Technology Asia 30(3), July–September 2025, pp. 209–231; Kaewsawad (NIDA) & Duda (AGH Kraków); CC BY-NC-ND 4.0; co-financed by EU Horizon Europe (project 101086381, "Overcoming Digital Divide in Europe and Southeast Asia").
**Newly read:** §3 Study (**pp. 7–8**: research questions; Thai-language online survey "distributed via professional and industry networks, as well as social media platforms"; no explicit screening questions — demographic data and employment-based exclusions used instead; hypotheses H1–H14 under a modified UTAUT framework); §4 Analysis opening (**p. 12**: SEM measurement-model assessment — internal consistency, convergent and discriminant validity); §6 Conclusion (**pp. 21–22**); Limitation (**p. 22**).
**Key content (exact):** AI literacy "can significantly reduce anxiety (β = −0.892, p < 0.001)"; effort expectancy → acceptance (β = 0.370); ten of fourteen hypotheses validated. Conclusion: AI literacy "does not follow a predictable sectoral pattern" — agriculture/food showed unexpectedly strong literacy while IT showed "more moderate readiness levels"; "Policymakers and industry leaders should… avoid the one-size-fits-all approach". Limitation: "relatively limited sample size of only 318 respondents"; online distribution "could potentially cause sampling bias or underrepresentation of certain groups"; "caution should be exercised when deducing these results as the entirety of the Thai workforce."
**Unread:** §2 literature review detail (pp. 4–7), §4.2–4.4 result tables (pp. 14–19), §5 discussion (pp. 20–22).
**Galaxy:** society/skills, economics/jobs — plus this pass grounds the correlation-vs-causation framing: the β coefficients are survey associations (SEM paths), not causal effects.

---

## 3b. Oxford Martin — Governing Through the Cloud (55 pp) — DEEPENED read (2 Nov 2026, pass 2)
**Newly read:** §2.1–2.2 governance capacities (**pp. 10–15**, incl. Figure 5 flows and §2.2.2 record keeping); §4.1–4.1.3 US case study (**pp. 31–33**).
**Key content (exact):** record keeping "allows more visibility into the developments of AI generally, helps link customers and their usage to real-world actors, and enables post-incident attributions and forensics" (p. 14); providers "remain vulnerable to malicious cyber actors and can be the subjects of successful cyber attacks" (p. 14); EO 14110 uses Defense Production Act authority to require reporting of "clusters capable of collectively providing more than 10 20 OP/s with more than 100 Gbit/s networking bandwidth" and IEEPA authority for foreign-customer KYC (p. 31); "There is currently no explicit authority that requires compute providers to stop a foreign customer training a frontier model that might be used maliciously in the future" (p. 32); "it falls short of a comprehensive oversight scheme" (p. 32); domestic-developer KYC expansion proposed (p. 32).
**Still unread:** pp. 6–9, 12–13, 16–30 (§2.2.2–2.2.4 detail, §3 verification/compute accounting, §2.2.4 enforcement), 34–55 (§5 recommendations, conclusion).

## 4b. CSET — Tracking AI Chips (101 pp) — FULL PDF obtained; executive summary read (2 Nov 2026)
**Version:** Feldgoise, Miller & Dohmen, September 2026, CSET Georgetown; open PDF (SHA-256 7299dddf25334e566e9aa85b…).
**Sections read:** Executive summary **pp. 2–4** complete. **Unread:** body chapters pp. 5–81 (location-verification approaches, trilateration appendix, cost-benefit modelling, case study detail).
**Methods:** evaluation of location-verification approaches against four criteria (verifiability, accuracy, security, repeatability) with cost modelling across "more than ten million simulated scenarios".
**Findings (exact):** "It is indisputable that AI chips are being diverted to unauthorized countries, including China."; ping-based location verification (PLV) + physical inspections most feasible; PLV cost $3.1–28.8M/yr owned landmarks (0.5–7.2% of BIS FY2026 budget); "physical inspections never achieved higher detections-per-cost than a PLV system". **Five limitations:** post-hoc detection only; offline-chip ambiguity; adversarial obfuscation; ~20-mile geolocation floor; end-user blindness.
**Recommendations:** firmware-based signing; data-centre chips under strictest rules only; BIS-certified third-party operators; global scope; BIS resourcing ("the utility of a PLV system is limited by BIS's capacity to pursue those leads").
**Galaxy:** politics/chips, infrastructure/chips, governance/oversight.

## 4c. Stanford HAI — AI Index Report 2026 (425 pp) — FULL PDF obtained; front matter read (2 Nov 2026)
**Version:** ninth edition; canonical PDF hai.stanford.edu/assets/files/ai_index_report_2026.pdf (SHA-256 fff5ac1df971cee7daf847fa…). pypdf surrogate-encoding issues sanitised during extraction.
**Sections read:** Top Takeaways lineup + introduction + co-chairs' message **pp. 2–5**. **Unread:** chapter bodies pp. 12–385 (nine chapters), appendices.
**Key content (exact, pp. 4–5):** "Generative AI hit nearly 53% population-level adoption within three years"; "global corporate investment more than doubled in 2025"; organizational adoption 88%; "Benchmarks are saturating, frontier labs are disclosing less, and independent testing does not always confirm what developers report"; EU AI Act prohibitions vs US deregulation; "more than half of newly adopted national AI strategies came from developing countries"; "The data does not point in a single direction."
**Limits:** front matter only — chapter-level statistics unverified here; the report itself notes data-transparency decline.
**Galaxy:** how/evaluation, economics/productivity, governance/rules, politics/national.

## 4d. OpenAI — gpt-oss-safeguard technical report (page read, 2 Nov 2026)
Two open-weight reasoning safeguard models (120b/20b) "post-trained from the gpt-oss models", "trained to reason from a provided policy in order to label content under that policy"; Apache 2.0 + usage policy. Stated limits: not for end-user interaction; safety metrics describe chat behaviour; no additional bio/cyber training data. Provider-authored; open weights permit third-party verification.
**Galaxy:** how/evaluation, governance/oversight.

---

## 5. IEA — Energy and AI — Ch.2 body deepened (Addendum 30, 2 Nov 2026)
**Newly read:** §2.3 Outlook **pp. 62–66**; §2.4 ICT-sector implications **pp. 71–74**; §2.5 electricity supply **pp. 75–79** (incl. Table 2.3); §2.6.1 opening + Table 2.4 **pp. 93–94**. **Still unread:** pp. 18–48 (Ch.1 body), 55–61, 66–70 (sensitivity-case detail), 80–92 (supply-mix projections, Box 2.5), 94–254 (rest of §2.6.2+, Ch.3–7, country notes), Annex A remainder.
**Page-anchored additions beyond the exec summary:**
- p.62: Base Case drivers — server stock +60% by 2030 (a third from extended lifetimes); installed capacity ~100 → ~225 GW; accelerated-server capacity ~5× (8-accelerator servers can exceed 10 kW vs <2 kW for 2-accelerator).
- p.63: PUE 1.41 → 1.29 saves ~90 TWh (~30% cooling per unit IT electricity); 945 TWh by 2030 = just under 3% of global electricity (2024: 415 TWh ≈ 1.5%); 15%/yr growth >4× faster than all other sectors, yet "the data centre share in global electricity demand remains limited".
- p.64: accelerated servers ≈ half the net increase (conventional ~20%, other IT ~10%, infrastructure ~20%). **SEA anchor:** "A notable example is Southeast Asia, where electricity demand from data centres is expected to more than double by 2030, partially due to the presence of a regional hub in Singapore and southern Malaysia (Johor province)." US+China ≈ 80% of global growth (US +240 TWh/130%; China +175 TWh/170%; Europe +45 TWh/70%; Japan +15 TWh/80%).
- p.65: per-capita 2024→2030 — US ~540 → >1,200 kWh (order of magnitude above other regions); China ~70→~200; Europe ~100→165; India ~15. DCs <10% of global demand growth but "tend to concentrate in specific locations, making their integration into the grid potentially more challenging".
- p.71–72: ICT context — DCs ~360 TWh 2023 = one-third of ICT's >1,000 TWh (4% of global electricity); networks ~280; devices ~440; crypto ~125 TWh (outside ICT definition).
- p.72–74: edge AI — NPUs 1–5 W; edge shift "likely to reduce energy use in data centres with only a limited increase in energy use by devices" BUT gen-AI device sales may accelerate replacement cycles (+80%/yr to 2028, ~900m units per IDC) → manufacturing energy and e-waste; network energy use largely traffic-independent (Mytton, Lundén & Malmodin 2024).
- p.75: procurement — "the separation of renewable generation and data centre consumption often means other sources, like natural gas or coal, are used to meet physical electricity needs" (financial vs physical mix); hourly matching (Google; Microsoft–Constellation Three Mile Island 20-yr PPA, Sep 2024).
- p.76–77: Table 2.2 operator capacity/targets (Meta 9,780 MW, Google 8,960, Amazon 7,660, Microsoft 6,970; Tencent 12%, Baidu 5% current clean share); SMR plans "up to 25 GW" announced (mostly US); Fervo/Google 115 MW Corsac; Meta–Sage 150 MW.
- p.78: corporate PPAs ~120 GW operational (tech companies >30%; 2024 tech PPAs ≈ 20% of the 415 TWh); 75% of DC-operator operational PPA capacity in the US; **SEA anchor:** "While there has recently been an increase in announcements from other parts of the world, including Southeast Asia and India, significant regulatory hurdles continue to limit the deployment of PPAs."
- p.79: Table 2.3 — grid-connection CO₂ intensity "United States: 350, China: 600, **Southeast Asia: 610**, Europe: 240, World: 460" g CO₂/kWh; only utility solar PV (1–4 yr) and gas GT (1–3 yr) build within typical DC timelines.
- p.93–94: §2.6.1 — connection queues: "Malaysia Under 3 years" (IEA survey), Dublin "paused until 2030", Netherlands up to 10 years, North Virginia up to 7; moratoriums noted; supply CO₂ peaks 215–320 Mt (Base/HighEff/Headwinds) vs ~475 Mt plateau (Lift-Off).
**Nature:** all figures are IEA model outputs (Base Case projections) or cited survey values — not measurements; scenario, not forecast.
**Galaxy:** deepens existing sourced edges (how/inference↔environment/energy; infrastructure/centres↔infrastructure/grids; infrastructure/centres↔infrastructure/electricity) with page-level evidence; no new edges needed.

---

## 6. UK CMA — Cloud services market investigation, summary of final decision (8 pp) — FULL read (2 Nov 2026)
**Version:** official regulator decision; referred by Ofcom 5 Oct 2023; provisional 28 Jan 2025; final 31 Jul 2025; case closed. Copy: sources/pdfs/cma-cloud-summary-final.pdf (SHA-256 98b48c48…). **Unread:** the 637-page final decision report and its appendices (incl. Appendix D market structure, Appendix R market power); the case page (timeline) read.
**Page-anchored findings (official):**
- Definition (para 2): cloud = "access to shared computing resources on demand so that the customers do not need to own the underlying hardware and software" (IaaS + PaaS) — the digital-service/material-basis distinction in the regulator's own words.
- Market (para 3): UK customer spend £10.5bn (2024), ~30%/yr growth since 2020; "Cloud services also underpin AI model development and deployment."
- Concentration (paras 5–8): IaaS "highly concentrated" — Microsoft and AWS each [30–40]% (UK+EEA, 2024), Google [5–10]%; PaaS Microsoft [20–30]%, AWS [10–20]%; positions "likely to endure"; returns "substantially above their cost of capital".
- Vertical integration (para 12): "Microsoft, AWS and Google are all strong vertically integrated providers of accelerated compute and AI-related cloud services, including through partnerships with AI model developers. Other cloud providers are significantly weaker in this respect." AI "yet to materially alter the competitive dynamics" (para 13).
- Barriers (paras 17–19, 23–28): entry needs "significant capital investment in fixed assets such as data centres, networks and servers... largely a sunk cost"; "less than 1% of customers switch provider each year"; egress fees "a key commercial barrier"; technical differentiation; committed spend widespread but not currently harmful.
- Microsoft licensing (paras 30–36c): practices "adversely impacting the competitiveness of AWS and Google" — an AEC; relevant products listed (fn 2: Windows Server, SQL Server, Windows 10/11, Visual Studio, productivity suites).
- Decision (para 36): AECs from (a) concentration + barriers → "significant unilateral market power"; (b) switching/multi-cloud lock-in; (c) Microsoft licensing. Illustration: 5% above-competitive prices ≈ £500m/yr (fn 3).
- Remedy (paras 38–42): recommend the Board prioritise SMS investigations to consider designating Microsoft and AWS under the DMCC Act; options expected early 2026.
**Limits:** UK+EEA scope; bracketed share ranges; SMS is a recommendation, not a designation; secondary claims of "voluntary commitments accepted" are NOT on the official case page and are not used.
**Galaxy:** infrastructure/cloud (new topic), economics/ownership, governance/rules — grounds the new cloud topic's sourced edges (→ data centres, → ownership, → inference).

---

## 7. UK CMA — final decision report: egress/switching evidence base read (Addendum 33, 2 Nov 2026)
**Read:** the egress/switching analysis at paras 6.341–6.417 (PDF pp. 330–349) of the 637-pp final decision report (copy: sources/pdfs/cma-cloud-final-decision-full.pdf, SHA-256 c33adc90…). Appendices L–Q located but NOT read.
**Geography and date (checked):** market scope "UK+EEA" (fn 1); switching-cost scenario built on "UK customer-level data on the mean volumes of data they stored for each year from 2018 to 2022" (para 6.406a); list prices from provider websites "for the applicable UK region" — "London" for Google and AWS — accessed **29 Jan 2024** (fn 1679–1680); provider egress-payment shares reported for **2023** (paras 6.349–6.352); free switching programmes (2024) considered (para 6.344d).
**Method (paras 6.406):** one-off full-data-transfer scenario; cost as % of annual spend spread over a typical three-year contract. Provider-submitted analyses given less weight: those based on customers who actually switched "will tend to exclude any customers that found egress fees too high and were deterred from switching" (para 6.404) — a selection-bias critique.
**Results (percentages REDACTED as bracketed ranges in the public version):** [0–5]%–[5–10]% of customers would pay egress fees above [5–10]% of annual spend per year over a three-year contract; smallest customers (£1,000–£10,000/yr) face the highest proportional fees; up-front unspread: [10–20]%–[20–30]% would face >[5–10]% (paras 6.407–6.410).
**Caveats (paras 6.411–6.412):** the analysis "is likely to understate the effect of egress fees on switching" (total-spend denominator); list prices ignore discounts (CSAs) and premium alternatives; "the combined effect of these different factors is ambiguous".
**Bottom line for this project:** the switching/egress findings are a UK+EEA regulator's measured analysis on 2018–2022 UK customer data and Jan-2024 list prices — NOT Southeast Asian or global figures; exact percentages are confidential.
