# Compiled supplementary source pack — 4 November 2026
Compiles the three pack files into one list. Every READ item had its abstract/summary opened this session; spot-checks of the subagent's two sampled studies (Takita; Kazemzadeh) were re-verified line-by-line by the audit session via PMC. Leads are separated and must not be cited until read. No causal claims are made beyond what the sources state. Counts: **14 READ + 6 LEADS = 20 items** (within the 12–20 bound).

## A. Empirical AI health evaluation (7 READ + 1 LEAD + 3 LEADS)
Detail in agent-health-evals.md (written by the health subagent; two studies independently re-verified by the audit session — marked ✓ below).

| # | Study | Venue/Year | Key verified figure | Topic connections |
|---|-------|-----------|---------------------|-------------------|
| 1 ✓ | Goh et al., LLM influence on diagnostic reasoning (RCT, 50 physicians, 244 cases) | JAMA Network Open 2024 | Physicians+GPT-4 76% vs conventional 74% (P=.60); GPT-4 alone 92% | how/evaluation, governance/oversight, society/health |
| 2 ✓ | Hernström et al., MASAI mammography screening RCT (105,934 women) | Lancet Digital Health 2025 | Detection 6.4 vs 5.0/1000 (ratio 1.29, p=0.0021); workload −44.2% | society/health, how/evaluation, governance/postmarket, governance/oversight |
| 3 ✓ | Kazemzadeh et al., prospective AI chest X-ray TB validation, Lusaka Zambia (1,932 adults; 10.5% TB+; 35.5% HIV+) | NEJM AI 2024 | AUC 0.87 (0.84–0.90); HIV+ subgroup 0.83 vs 0.90; sensitivity target vs WHO not met at any shared threshold | society/health, how/evaluation, governance/postmarket |
| 4 | Olson et al., ambient AI scribes across 6 US systems (pre/post; 272 completing) | JAMA Network Open 2025 | Burnout 51.9%→38.8% (OR 0.26); vendor co-author visible; not causal | society/health, how/evaluation, society/participation |
| 5 ✓ | Takita et al., meta-analysis of generative-AI diagnostics (83 studies) | npj Digital Medicine 2025 | Pooled accuracy 52.1% (47.0–57.1); vs experts −15.8% (p=0.007); 76% high risk of bias | how/evaluation, society/health, governance/rules |
| 6 | Ruamviboonsuk et al., AI diabetic-retinopathy screening in Thailand's national programme (7,651 analysed) | Lancet Digital Health 2022 | Accuracy 94.7% vs specialist over-readers; over-read safety layer retained | society/health, society/participation, governance/oversight |
| 7 | Tao et al., PreA LLM preconsultation chatbot RCT, China (2,069 patients; 111 specialists) | Nature Medicine 2026 | Consultation duration −28.7% (P<0.001); co-design beat fine-tuning (authors' claim); process endpoints only | society/health, society/participation, governance/oversight |
| 8 | LEAD: Heinz et al., Therabot mental-health RCT | NEJM AI 2025 | Not read (403/Cloudflare; press coverage only) — do not cite figures | society/health |
| 9–11 | LEADS: final MASAI Lancet results (2026); Oxford chatbot-advice study (2026); AIRIS-TB population-scale CXR (npj 2025) | — | Not read; numbers unverified | — |

## B. Field-level Africa (4 READ + 1 LEAD)
Detail in agent-africa-field.md (written directly by the audit session after the assigned subagent failed).

| # | Source | Read scope | Key content | Topic connections |
|---|--------|-----------|-------------|-------------------|
| 12 | CIPIT, The State of AI in Africa Report (2025, 70 pp) | exec summary + contents | Kenya/SA/Nigeria/Ghana strides; "shift from consumption to creation"; uneven progress (electricity, regulation, skills) | politics/national, infrastructure/centres, society/skills, governance/rules |
| 13 | GIZ, Invisible Workers, Visible Harms (2026, 43 pp) | opening + scope + Ghana case pointers | Data-work foundations; Kenya/Ghana/Nigeria/SA principal markets; ~150 Meta content moderators in Ghana (litigation reported) | economics/jobs, society/participation, politics/accountability |
| 14 | Pidoux et al., Mapping Data Labour Supply Chain in Africa (arXiv, 10 pp) | abstract | Data labour spans 43 of 55 African countries; 17 major firms; n=81 union-participatory questionnaire; precarity | economics/jobs, society/participation, politics/accountability |
| 15 | Adelani et al., IrokoBench (arXiv, 26 pp) | abstract | Human-translated benchmark, 17 African languages (AfriXNLI/AfriMGSM/AfriMMLU); LLM capability limits in low-resource languages | how/evaluation, how/data, society/participation |
| 16 | LEAD: Isagah, AI Readiness in Africa (ACM 2024) | — | 403 to public fetcher; TOE-framework readiness study per search | — |

## C. Field-level Latin America (3 READ + 2 LEADS)
Detail in agent-latam-field.md (written directly by the audit session after a second subagent failure).

| # | Source | Read scope | Key content | Topic connections |
|---|--------|-----------|-------------|-------------------|
| 17 | CENIA, Latam-GPT official page | landing page in full | "A language model made in Latin America, for Latin America"; regional model effort; details (size/languages/release) search-derived only | how/models, politics/national |
| 18 | Fundar (Argentina), AI value-chain column | page in full (Spanish) | Data-centre-only focus "resignarse a no competir en otros segmentos"; >25 AI bills since 2024, none approved; CAMIA/IDB loan never executed | politics/national, infrastructure/centres, governance/rules, economics/investment |
| 19 | Fairwork (Oxford spinout) | organisational site in full | Five principles, /10 scoring; 2025 reports for Argentina, Brazil, Colombia, Ecuador, Paraguay, Uruguay; country scores unverified on page | economics/jobs, governance/rules, society/participation |
| 20 | LEADS: Brookings Latam-GPT-sovereignty analysis; Argentina DC-pipeline figures (BNamericas/Industrial Info) | — | Not read; figures unverified | — |

## Pack-level limits
- All reads are abstract/exec-summary/page level; no full-paper verification beyond the two PMC spot-checks.
- Venue mix: 7 health studies are peer-reviewed (one vendor co-authored; COIs noted per source); CIPIT/GIZ/Fundar/Fairwork are institutional reports or columns (advocacy-adjacent); the two arXiv items are preprints.
- Geographic intent met for health (Sweden, US ×3, Zambia, Thailand, China, Japan-review) and for Africa/LatAm fieldwork, but the health set remains majority-North-American by first-author institution.
- No causation inferred anywhere; pre/post and association designs are labelled as such (Olson especially).
- Subagent failures: two of three assigned subagents failed on concurrency limits; their slices were completed directly by the audit session in the same exclusive files.
