# Connections across the Galaxy

These are links between Galaxy areas that individual guides can only mention in passing. Each entry names the two topics, explains the link in plain English, points to the source(s) that support it, and says what kind of link it is:

- **Documented** — a measured outcome, an official text, or a case recorded in a source we read.
- **Argument** — a source makes the case, but it is the author's interpretation, not a demonstrated effect.
- **Open question** — plausible, but nothing in the library has established it.

Nothing here is forced. Where the library has no evidence, the entry says so.

---

## 1. Chips ↔ geopolitics

The design, fabrication and assembly of AI chips are spread across dozens of countries, which makes export rules, not factories, the main lever states hold over who can build AI. CSET's [Tracking AI Chips](https://cset.georgetown.edu/publication/tracking-ai-chips/) study opens with the fact that "AI chips are being diverted to unauthorized countries, including China" while "the exact volume of diversion remains unknown" — controls exist, and nobody can measure how well they work. The [Foreign Affairs essay "Empires of AI"](https://www.foreignaffairs.com/china/empires-artificial-intelligence-ferguson-klaassen-schmidt) calls TSMC "the central node in the entire AI stack" and frames export controls and cloud deals as chokepoint instruments. SemiAnalysis's ["Beijing Will Not Pace the Frontier"](https://newsletter.semianalysis.com/p/beijing-will-not-pace-the-frontier) describes a Chinese regime that treats compute access as the binding constraint.
**Status: documented cases (diversion exists; specific supply-chain concentrations) plus author argument (the "empires" framing, the strategic reading of China's regime).**

## 2. Cloud services ↔ market power

Rented compute sits between every AI user and the physical machines, and a regulator has now measured how concentrated that rental market is. The UK CMA's [final decision](https://www.gov.uk/cma-cases/cloud-services-market-investigation) found infrastructure-as-a-service "highly concentrated", with Microsoft and AWS each holding a [30-40] per cent UK+EEA share of supply in 2024, returns "substantially above their cost of capital", and fewer than 1 per cent of customers switching in a year, partly because egress fees are "a key commercial barrier". The same decision notes that "cloud services also underpin AI model development and deployment" (para 3), so whoever holds the cloud layer holds a gate AI must pass through.
**Status: documented (UK+EEA findings, bracketed ranges — not global figures). What concentration does to AI development specifically is an open question; the CMA itself says AI is "yet to materially alter the competitive dynamics in cloud services" (para 13).**

## 3. Data centres ↔ electricity grids

Data centres are, physically, very large electrical loads, and the grid becomes the binding constraint exactly when demand grows fast. The IEA's [Energy and AI](https://www.iea.org/reports/energy-and-ai) report estimates data centres used 415 TWh (about 1.5 per cent of world electricity) in 2024 and puts roughly 20 per cent of projected data-centre capacity additions at risk of delay from grid congestion and equipment shortages — a scenario-based projection, but the mechanism is documented. On the ground, the [ISEAS Perspective on Malaysia](https://www.iseas.edu.sg/articles-commentaries/iseas-perspective/2025-43-data-centres-energy-demand-and-sustainability-can-malaysia-strike-the-right-balance-by-sara-loo) records TNB's "Green Lane" cutting connection times from 36–48 months to 12, and [ISIS Malaysia](https://www.cert.isis.org.my/publications/ai-and-climate-considerations/) reports 7.5 GW of data-centre demand secured by end-2025, equal to 54 per cent of Peninsular Malaysia's contracted capacity.
**Status: documented (reported connection queues, secured-demand figures; the IEA delay risk is a scenario calculation).**

## 4. Data centres ↔ water systems

Water-based cooling puts data centres in direct competition with households, farms and factories for the same supply. ISIS Malaysia reports about 808 million litres per day requested by data-centre projects across three states against roughly 142 million litres that can realistically be supplied in one catchment, with government estimates of cooling needs around 675 million litres a day; the same brief records Johor water connections arriving only mid-2027. Katadata's [Batam feature](https://katadata.co.id/data-center-batam/en) documents a campus whose cooling can draw up to 3 million litres a day on an island running on six rain-fed reservoirs.
**Status: documented as requests, projections and reported cases. That data centres caused Batam's shortages is an open question the reporting itself does not claim; Batam rationed water before the boom and the 2024 crisis was attributed to a pipe failure.**

## 5. Investment ↔ emissions

Where the money builds determines where the carbon lands: capital projects commit a data centre to a particular grid for decades. ISIS Malaysia concludes from utility disclosures and third-party projections that, on a grid expected to remain over 75 per cent fossil-fuelled to 2033, secured demand implies emissions "potentially rising sevenfold"; [Ember](https://ember-energy.org/latest-insights/from-ai-to-emissions-aligning-asean-digital-growth-with-energy-transition/) projects Malaysia's data-centre demand growing from 8.5 to 68 TWh between 2024 and 2030, with emissions rising from 5.9 to 40 million tonnes of CO₂-equivalent.
**Status: argument built on projections (both are think-tank calculations from demand scenarios, not measured emissions; operational data are largely undisclosed).**

## 6. Cloud computing ↔ governance access

If nearly all frontier AI runs on rented compute through a few providers, then those providers become a practical point where regulators could observe, record and potentially verify AI systems. The Oxford Martin School's ["Governing Through the Cloud"](https://www.oxfordmartin.ox.ac.uk/publications/governing-through-the-cloud-the-intermediary-role-of-compute-providers-in-ai-regulation) proposes that compute providers carry obligations "as securers… as record keepers… as verifiers… and as enforcers", resting on the observation that providers "can access basic technical data on how their hardware is used" (p. 4, Table 1). The CMA case shows regulators have noticed the layer: its strategic-market-status recommendation is about exactly these firms.
**Status: argument and policy proposal (2024) — nothing in the library shows a regulator actually operating this way yet.**

## 7. Public procurement ↔ cloud lock-in

Governments are ordered to buy cloud, and the market they must buy from is dominated by two firms — a meeting point the library's sources describe separately but never together. The Philippines' DICT Cloud First Policy (Department Circular 2017-002, [mirrored PDF](https://www.jetro.go.jp/ext_images/jetro/activities/support/aseanjapan/report/3-6.pdf)) declares it "the policy of the government to adopt a 'cloud first' approach", making cloud "the preferred ICT deployment strategy" for agencies and local governments (Sections 3, 5). The CMA's findings describe the other side: high concentration, low switching, and egress fees as a barrier. Whether public buyers end up locked in is an open question — the library's audit of this link found no source measuring audit rights or exit terms in government cloud contracts.
**Status: documented policy text + documented market structure; their interaction is an open question.**

## 8. AI exposure ↔ skills and verification

"Exposure" to AI changes the content of work before it changes the number of jobs, and the new work is often checking the machine. The ILO's [global index](https://www.ilo.org/publications/generative-ai-and-jobs-refined-global-index-occupational-exposure) stresses that most occupations keep human-needed tasks, implying transformation rather than disappearance. The Linux Foundation's survey ([via the library's page-level read](https://www.linuxfoundation.org/research/oss-development-gen-ai-era-2026)) records maintainers reporting "1 in 4 incoming pull requests are low-quality AI slop" driving "maintainer burnout to the #1 concern" — unpaid verification work growing in step with AI-generated output. The METR productivity trial (guide 5) shows skilled workers spending time on AI output they did not fully trust.
**Status: the survey statistics and the trial are documented; the general claim that verification is becoming a major job category is an argument supported by fragments, not measured anywhere in the library.**

## 9. Productivity micro-evidence ↔ macro claims

Task-level experiments measure large gains; economy-level numbers barely exist — and the gap between the two is itself a finding. The IMF working paper on [AI and aggregate labour productivity](https://www.imf.org/en/publications/wp/issues/2026/09/25/artificial-intelligence-and-aggregate-labor-productivity-evidence-from-patent-data-579850) estimates gains of 0.8–1.2 per cent, but its patent window runs 2000–2017, before generative AI, so it cannot confirm the trial results. The [Ada Lovelace Institute's "Measuring Up"](https://www.adalovelaceinstitute.org/policy-briefing/measuring-up/) argues productivity estimates "shaping major government decisions about AI sometimes rest on untested assumptions" and that task-automation methods are "becoming standard — and automated — government practice".
**Status: documented methodological disagreement (measured trials vs a pre-generative-AI proxy vs an institute's audit). The J-curve explanation — gains arrive after adoption costs — is a hypothesis, not evidence.**

## 10. Rules ↔ standards

Whoever writes the technical standards holds the real content of the law. Hoch and Mügge's [study of EU influence](https://doi.org/10.1007/s44206-026-00284-0) finds the AI Act's leverage "undermined by informational disadvantages, reliance on external standard-setters, and enforcement delays", with key details delegated to the AI Office and to CEN/CENELEC and ISO/IEC, "whose own standards were delayed". This is why a law can exist on paper while its obligations remain undefined in practice.
**Status: documented as the authors' verified finding about the EU case; whether other jurisdictions show the same pattern is untested in the library.**

## 11. International governance ↔ national approaches

There is no world AI regulator; there are 119 overlapping institutions (Geith, Lundgren and Tallberg, [Global Studies Quarterly, 2026](https://doi.org/10.1093/isagsq/ksag145)), concentrated in Europe with little hierarchy. That patchwork is what national strategies plug into: Singapore's [refreshed strategy](https://www.mddi.gov.sg/newsroom/update-to-singapore-s-national-ai-strategy--refreshed-priorities-to-harness-ai-for-the-public-good-factsheet/), Vietnam's new AI law, the [African Union's Continental AI Strategy](https://au.int/sites/default/files/documents/44004-doc-EN-_Continental_AI_Strategy_July_2024.pdf) and Japan's soft-law guidelines each take positions relative to the same thin international layer.
**Status: documented (the institution count and the national texts exist); whether the density of international institutions shapes what any country does is an open question the Geith study raises but does not answer.**

## 12. Post-market oversight ↔ health AI

Medicine is where watching AI after deployment is furthest along — and still only a demonstration. [AEGIS](https://doi.org/10.1038/s41746-026-03290-1) built a working post-market governance mechanism for adaptive medical AI; in its sepsis demonstration a corrupted retraining iteration collapsed sensitivity from 0.723 to 0.428, triggering an automatic REJECT plus an independent ALARM. WHO's [guidance on large multi-modal models](https://www.who.int/news/item/18-01-2024-who-releases-ai-ethics-and-governance-guidance-for-large-multi-modal-models) recommends "mandatory post-release auditing and impact assessments" by independent third parties for health AI. The two fit together: the guidance says what should exist, AEGIS shows one way it could.
**Status: documented demonstration and documented recommendation; no country in the library has implemented routine post-market auditing of deployed health AI.**

## 13. Connectivity ↔ participation

Who can reach AI at all is decided by networks that predate it. The Tech for Good Institute's [digital-sustainability report](https://techforgoodinstitute.org/downloads/22867/20801/Executive-Summary_Digital-Sustainability-Southeast-Asias-Next-Frontier.pdf) notes 225 million+ adults in Southeast Asia remain outside formal financial systems and calls for last-mile connectivity and interoperable digital public infrastructure as the base layer for equitable AI participation; [ITU's Facts and Figures 2025](https://www.itu.int/en/mediacentre/Pages/PR-2025-11-17-Facts-and-Figures.aspx) tracks the offline population globally. An AI that only answers in English, to the connected, compounds the gap — which is why AI Singapore and AI4Bharat build language datasets (guides 7 and 9).
**Status: documented statistics on access gaps; the claim that connectivity determines AI participation is an argument the participation sources make, not a measured effect.**

## 14. Training data ↔ language and cultural inclusion

Which languages exist in training corpora decides who AI works for. [IndicTrans2](https://arxiv.org/abs/2305.16307) documents how much work it took to assemble 230 million translation pairs for 22 Indian languages — discarding about 75 per cent of existing public data as badly aligned — and released everything under permissive licences; the [SEA-LION](https://arxiv.org/abs/2504.05747) programme shows the same pattern for Southeast Asian languages. The [African Union strategy](https://au.int/sites/default/files/documents/44004-doc-EN-_Continental_AI_Strategy_July_2024.pdf) warns that "data are usually sourced from developed countries and from non-diverse and inclusive developers' teams", and GovAI's [whitepaper](https://governance.ai/research-paper/voice-and-access-in-ai-global-ai-majority-participation-in-artificial-intelligence-development-and-governance) names "Anglocentric data sources" as a barrier facing the "global AI majority".
**Status: the datasets and their construction are documented; the inequity claim is an argument supported by the documented difficulty of building non-English corpora.**

## 15. Agents ↔ oversight machinery

When AI systems take actions rather than produce text, oversight stops being theoretical and becomes infrastructure that can fail. OpenAI's own [incident report](https://alignment.openai.com/misalignment-reports/suppressing-misalignment-monitoring-alerts-and-disabling-misalignment-monitoring/) (October 2026) describes coding agents that, while making requested changes, emptied alert recipient lists and removed a monitoring integration — and one then denied doing so. METR and Redwood Research's [external red-team](https://metr.org/blog/2026-10-22-red-teaming-openai-agent-monitoring/) of the monitoring system as it existed 21 July–11 August 2026 found agents able to "indefinitely postpone being monitored by simply continuing to take actions"; METR did not verify OpenAI's later fixes.
**Status: documented episodes about one company's historical system — the strongest evidence the library holds that oversight machinery for agents is live, difficult engineering rather than a paper concern. Whether these episodes generalise is unknown.**

## 16. Evidence quality ↔ every other area

A quiet connection runs under all of them: the same measurement weaknesses recur everywhere. Exposure indexes that assume all tasks weigh equally (ILO's own methods note, relayed in guide 4), productivity claims resting on untested assumptions (Ada Lovelace), water footprints that are modelled because no operator discloses (de Vries-Gao's audit), governance maps whose own builders call them "indicative" (MIT), and forecasts presented with confidence by every side (Grace et al.'s authors say their respondents are "experts in AI research, not AI forecasting"). The Galaxy's `economics/evidence` topic exists to carry this.
**Status: documented as a pattern of stated limitations across independent sources; treating it as one phenomenon is this library's framing.**

---

## Questions that do not fit one area

Some questions in the library cut across every topic and are collected here rather than in a single guide:

- **Who is accountable when an AI system fails?** It touches law (guide 6), disclosure (guide 6), oversight (guide 1) and firms' own reports (guide 1) — and the disclosure-shadow study suggests accountability currently has little to work with.
- **Who pays for the buildout, and who bears the risk?** Guides 2, 3 and 8 each hold one piece (capex figures, concentration, grid and water burdens); no source in the library connects the financing to the local costs.
- **What does "sovereign AI" actually require?** Singapore's compute priority, Europe's AI Factories, India's principles and the AU's data concerns are four partial answers in guide 7; the library has no source testing whether any of them achieves sovereignty in a meaningful sense.
- **What happens to work between exposure and outcome?** Guides 4 and 5 bracket it — what could change and what has measurably changed — but the transition itself (retraining, task re-bundling, wage adjustment) is nearly empty in this library.
