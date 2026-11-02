# Full-source reads: infrastructure, energy and political economy (1 Nov 2026)

> **FILE-CONTENT NOTICE (2 Nov 2026):** despite its name, this file does not contain catalogue guidance — its content is a truncated duplicate of `sources/notes/full-source-reads.md` (it stops before that file's SEA-batch section). The authoritative per-record catalogue is `sources/catalogue.json` / `catalogue.csv` (140 records; read-depth in each record's `verification` field; topic coverage via `build_topic_sources.py` → `topic_sources.json`). Read-depth notes live in `sources/notes/*.md`. The duplicate content below is preserved as-is; a future batch may restore proper catalogue guidance here. Flagged during the 2 Nov 2026 milestone (REPORT-5.md Addendum 28).

> **Superseded in part:** after this session's page/summary-level reads, the full PDFs of items 1 (IEA), 3 (ISIS) and 4 (Oxford) were downloaded, converted with pypdf, and read at page level — see **pdf-full-reads.md** (page-anchored passages). The IEA and ISIS notes here are superseded by the PDF reads; the Oxford item remains page+abstract level for content (PDF obtained, key pages read — see pdf-full-reads.md).

Reading levels are stated per item. Principle applied throughout: **author conclusions are reported as author conclusions** — they become "established" only through independent replication, which none of these items has.

---

## 1. IEA — Energy and AI (2025) — executive summary read (self-contained section)
**Version:** IEA (2025), Energy and AI, IEA, Paris; CC BY 4.0. Executive summary on the report page; full PDF not opened.
**Key figures (exact):** data centres ≈1.5% of world electricity in 2024 = 415 TWh (US 45%, China 25%, Europe 15%); ~12%/yr growth since 2017; "set to more than double to around 945 TWh by 2030"; ~1,200 TWh by 2035 Base Case; one-tenth of global demand growth to 2030 but >20% in advanced economies; "AI is the most important driver of this growth"; half of growth met by renewables (+450 TWh to 2035), gas +175 TWh (notably US), nuclear similar (China/Japan/US, SMRs ~2030).
**Uncertainty (stated):** case range "from 700 to 1 700 TWh" by 2035 (Lift-Off/Headwinds/High Efficiency; High Efficiency 20% below Base in 2035) — drivers: adoption speed, capability/productivity, efficiency gains, bottlenecks.
**Limits:** executive summary only; the modelling chapters (which define the cases) were not read; projections are scenarios, not forecasts.
**Galaxy:** how/inference—environment/energy; infrastructure/electricity; environment/energy; economics/investment.

## 2. Epoch AI — AI Chip Users explorer (dataset page + FAQ read)
**Version:** updated 2026-09-09; ZIP/CSV downloadable; CC BY 4.0.
**What it measures:** compute used (not owned) by OpenAI, Anthropic, Google DeepMind, Meta Superintelligence Labs, SpaceXAI, in H100e. Method (exact): "We divide the peak number of dense 8-bit operations (FP8 or INT8) each chip can perform by the Nvidia H100's corresponding spec, and then multiply this ratio by the number of chips."
**Uncertainty:** Monte Carlo 90% CIs; "there is also some guesswork involved"; "substantially uncertain, especially for Meta Superintelligence Labs and Google DeepMind."
**Limits (stated):** usage ≠ ownership (Anthropic/OpenAI predominantly rent); parent-company compute not fully attributable to labs; US-centric coverage; per-lab numbers live in the chart/ZIP, not the page text.
**Galaxy:** infrastructure/chips; economics/ownership; economics/investment.

## 3. ISIS Malaysia — AI and Climate Considerations (publication page + executive summary read; full PDF located, not converted)
**Version:** 9 Jun 2026; authors Zayana Zaikariah & Sara Loo; PDF at cert.isis.org.my/wp-content/uploads/02-CERT-PUBLICATION-AICC-ADJ.pdf.
**Argument (author conclusion):** the data-centre boom "undermines its ability to effectively pursue climate and environmental goals"; the moratorium on non-AI data centres "cannot be practically enforced"; risk of "subsidis[ing] the computational needs of foreign corporations, without securing commensurate returns in local innovation capacity."
**Evidence:** 15 anonymised stakeholder interviews (Mar–Apr 2026) across Malaysia, Singapore, Indonesia, Philippines, five sectors; peer-reviewed research, government documents, industry reports. Figures: 38 projects with TNB ESAs totalling 5.9 GW (Dec 2024); 7.5 GW cumulative maximum demand secured by end-2025 = "54% of Peninsular Malaysia's total contracted capacity (13.8GW)"; >5,000 MW by 2035 (~40% of capacity); Ember 9→68 TWh (2024–30); emissions "potentially rising sevenfold" on a >75% fossil grid to 2033; cooling ≈675m L/day; ~808m L/day requested vs ~142m (<20%) supplyable; Johor water connections mid-2027.
**Limits (stated):** operational energy/water/emissions data "are generally not publicly disclosed by most companies operating in Malaysia"; interview findings are anonymised and partly unverifiable — the authors frame them as questions. The "undermines" claim is the authors' argument built on projections and interviews, not a measured causal result.
**Galaxy:** environment/energy, environment/goals, infrastructure/water, economics/investment, governance/rules.

## 4. Oxford Martin School — Governing Through the Cloud (publication page + abstract read; PDF located, NOT read — PDF conversion unsupported by tooling this session)
**Version:** 13 Mar 2024; Heim, Fist, Egan, Huang, Zekany, Trager, Osborne & Zilberman; Oxford Martin AI Governance Initiative; open PDF (direct URL preserved in the catalogue).
**Argument (author proposal):** compute providers should carry legal/ethical obligations as regulatory intermediaries in four capacities — "as securers… as record keepers… as verifiers… and as enforcers" — with technical feasibility assessed "in a targeted and privacy-conscious manner" (providers can already see workload type and compute consumed from non-confidential data).
**Case study:** US EO 14110 record-keeping requirements; proposes adding verification/enforcement roles.
**Limits:** policy analysis/proposal, not an evaluation; "internationalization will be key to effective implementation"; core tension "balancing confidentiality and privacy with risk mitigation". Full PDF unread — content beyond the abstract/summary is unverified here.
**Galaxy:** governance/procurement, governance/standards, infrastructure/chips, how/using.

## Correction applied to the DeepMind record (same principle)
The DeepMind full-text read (see full-paper-reads.md) is relabelled **PARTIAL** (appendices A, C–H and B.1.5 truncated). Its closing claim — "current models do not pose severe risks from scheming" — is the **authors' conclusion within their proposed safety-case framing** (assumptions: oversight strength, four-month successor scope, no anti-sandbagging measures). It is recorded as a proposed safety case, **not validated safety**, and not as an established fact.
