# Empirical AI Health Evaluation Studies — Research Audit

Curated 2026-11-04 for the Galaxy of AI library. Scope: original, accessible empirical studies evaluating AI in clinical settings (trials, prospective validations, real-world deployments, one systematic review). All items checked against `sources/catalogue.json` (ids/titles/DOIs): no overlap with existing records (`aegis-postmarket`, `who-lmm-guidance`, `holtzman-redberg-pms-2025`, `eu-mdr-pms-2017`). All DOIs grepped in catalogue.json: 0 hits.

---

## 1. LLM influence on physician diagnostic reasoning (RCT, US)

- STATUS: READ-abstract (full text via PMC)
- TITLE: Large Language Model Influence on Diagnostic Reasoning: A Randomized Clinical Trial
- AUTHORS+INSTITUTION: Ethan Goh (MBBS, MS) et al. — Stanford Center for Biomedical Informatics Research / Clinical Excellence Research Center, Stanford University
- DATE: 2024-10-28
- VENUE: JAMA Network Open 7(10):e2440969 (open access, CC license)
- URL: https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2825395 | https://pmc.ncbi.nlm.nih.gov/articles/PMC11519755
- READ SECTION: full text (methods + results + limitations)
- METHOD: Single-blind randomized clinical trial (Nov 29–Dec 29, 2023). 50 US-licensed physicians (26 attendings, 24 residents; internal medicine, family medicine, emergency medicine); 244 completed cases (125 LLM group, 119 control) across 6 clinical vignettes, 60 minutes. Intervention: ChatGPT Plus (GPT-4) plus conventional resources vs conventional resources only. Third exploratory arm: GPT-4 alone.
- FINDING: Physicians + LLM median diagnostic reasoning score per case "76% (IQR 66%–87%)" vs physicians + conventional resources "74% (IQR 63%–84%)"; adjusted difference "2 percentage points (95% CI, −4 to 8; P = .60)" — not significant. LLM alone scored "92% (IQR 82%–97%)", "16 percentage points" above the conventional-resources group "(95% CI, 2–30; P = .03)". Time per case did not differ significantly (adjusted difference −82 s; 95% CI −195 to 31; P = .20).
- LIMITS (stated): single LLM; no prompt-engineering training for participants; inconsistent enforcement of LLM use; only 6 vignettes; vignette format omits patient interviewing, data collection, real clinical context. Authors note results do not support autonomous LLM diagnosis without physician oversight.
- TOPIC CONNECTIONS: how/evaluation — a benchmark-style RCT showing vignette scores do not translate into human+AI gains; governance/oversight — the human-with-tool group did not beat humans alone, so oversight design (how clinicians actually use LLM output) is the binding constraint; society/health — direct evidence on diagnostic care quality.

## 2. MASAI trial — AI-supported mammography screening (RCT, Sweden)

- STATUS: READ-abstract (PubMed abstract, full "Findings" section)
- TITLE: Screening performance and characteristics of breast cancer detected in the Mammography Screening with Artificial Intelligence trial (MASAI): a randomised, controlled, parallel-group, non-inferiority, single-blinded, screening accuracy study
- AUTHORS+INSTITUTION: Veronica Hernström et al. (senior author Kristina Lång) — Diagnostic Radiology, Translational Medicine, Lund University; Skåne University Hospital, Malmö, Sweden (plus Cancer Registry of Norway co-author)
- DATE: 2025-02-03 (epub); issue 2025-03
- VENUE: The Lancet Digital Health 7(3):e175–e183 (open access, CC BY 4.0); ClinicalTrials.gov NCT04838756
- URL: https://pubmed.ncbi.nlm.nih.gov/39904652/ (DOI 10.1016/S2589-7500(24)00267-X)
- READ SECTION: abstract (background/methods/findings/interpretation), full numbers
- METHOD: Randomised, controlled, non-inferiority, single-blinded screening-accuracy study within the Swedish national screening programme at four sites in southwest Sweden (Malmö, Lund, Landskrona, Trelleborg). 105,934 women randomised 1:1 (Apr 12, 2021–Dec 7, 2022) to AI-supported screening (Transpara v1.7.0, ScreenPoint Medical, used to triage exams to single or double reading and flag findings) or standard double reading.
- FINDING: Cancer-detection rates "6·4 per 1000 (95% CI 5·7–7·1)" (AI group, 338 cancers among 53,043) vs "5·0 per 1000 (4·4–5·6)" (control, 262 cancers among 52,872), "a ratio of 1·29 (95% CI 1·09–1·51; p=0·0021)". Recall ratio "1·08 (95% CI 0·99–1·17; p=0·084)" and false-positive ratio "1·01 (0·91–1·11; p=0·92)" — not significantly higher. Positive predictive value of recall ratio "1·19 (95% CI 1·04–1·37; p=0·012)". "61 248 screen readings in the intervention group and 109 692 in the control group, resulting in a 44·2% reduction in the screen-reading workload." Extra detected cancers were "mainly small lymph-node negative cancers" (58 more T1, 46 more node-negative).
- LIMITS: single region/country and one vendor AI version; screening-accuracy outcomes only (no mortality data in this paper); interval-cancer and sensitivity results awaited at publication. Association between earlier detection and long-term benefit not established here.
- TOPIC CONNECTIONS: society/health — the first full-scale RCT of AI in population screening; how/evaluation — model of a trial embedded in a real national programme rather than a retrospective dataset; governance/postmarket — 44% workload shift and AI triage to single reading show deployment changes the system being regulated, requiring outcome monitoring after go-live; governance/oversight — AI deciding which exams get single human reading is a re-allocation of human oversight with measured (non-inferiority) safety bounds.

## 3. Prospective AI chest X-ray validation for TB and abnormalities (Zambia)

- STATUS: READ-abstract (full text via PMC)
- TITLE: Prospective Multi-Site Validation of AI to Detect Tuberculosis and Chest X-Ray Abnormalities
- AUTHORS+INSTITUTION: Sahar Kazemzadeh (BS) et al. — Google, Mountain View, CA; study clinics in Lusaka, Zambia
- DATE: 2024-09-26 (PMC version 2025-01-16)
- VENUE: NEJM AI 1(10), DOI 10.1056/aioa2400018; preregistered NCT05139940
- URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC11737584
- READ SECTION: full text (methods, results, limitations)
- METHOD: Prospective, multi-site observational validation (Nov 2021–Feb 2023) at three clinics in Lusaka, Zambia (Chawama, Kanyama, Chainda). 1,932 adults enrolled; 1,827 evaluated for the TB AI (10.5% TB positive; 35.5% HIV positive); reference standard sputum culture/Xpert Ultra; comparator 10 India-based radiologists blinded to the reference standard.
- FINDING: TB AI AUC "0.87 (95% CI 0.84–0.90)". High-sensitivity threshold: sensitivity "87% (82–92)", specificity "70% (67–72)"; balanced threshold: "78% (72–84)" / "82% (81–84)". Radiologists: mean sensitivity "76% (71–83)", mean specificity "82% (77–85)". At the high-sensitivity threshold AI beat radiologists on sensitivity (difference 11%, P<0.001) but was not noninferior on specificity (difference −12%, P=1); at the balanced threshold noninferior on both. Against WHO targets (90%/70%), "specificity target met, sensitivity target not met"; no radiologist met the sensitivity target (best: 84%). HIV-positive subgroup AUC "0.83 vs 0.90" HIV-negative. Abnormality AI: AUC "0.97 (0.96–0.98)".
- LIMITS (stated): no single threshold let both AI and radiologists meet WHO sensitivity targets — country-/institution-specific threshold customization may be needed; a shared CXR machine at two sites produced grid-like artifacts, and site-level differences made attribution difficult. Lower performance in the HIV-positive subgroup.
- TOPIC CONNECTIONS: society/health — rigorous evaluation of diagnostic AI in a high-burden, low-resource setting; how/evaluation — preregistered prospective validation against culture reference and WHO target product profiles; governance/postmarket — found deployment-specific failure modes (scanner artifacts, subgroup performance) that only surface in the field, i.e., the case for post-deployment monitoring; governance/oversight — head-to-head against human readers defines what role the AI can hold in triage.

## 4. Ambient AI scribes and clinician burnout (multisystem QI study, US)

- STATUS: READ-abstract (PubMed abstract, full results)
- TITLE: Use of Ambient AI Scribes to Reduce Administrative Burden and Professional Burnout
- AUTHORS+INSTITUTION: Kristine D. Olson et al. — Yale School of Medicine / Yale New Haven Health-Yale Medicine, with CHRISTUS Health, MemorialCare Health System, The Christ Hospital Health Network, Sutter Health, University of Chicago, RWJBarnabus Health; one co-author from Abridge AI, Inc (the platform vendor)
- DATE: 2025-10-01
- VENUE: JAMA Network Open 8(10):e2534976 (open access)
- URL: https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2839542 | https://pubmed.ncbi.nlm.nih.gov/41037268/
- READ SECTION: abstract (importance/objective/design/results/conclusions)
- METHOD: Quality improvement study with preintervention and 30-day postintervention surveys of the same ambient AI scribe platform (Abridge), across 6 academic and community-based US health systems, Feb 1–Oct 31, 2024. 451 clinicians enrolled; 272 completed both surveys (60.3%); 263 analyzed. Primary outcome: self-reported burnout (hierarchical logistic regression); secondary: cognitive task load, attention, after-hours documentation time.
- FINDING: Burnout "decreased significantly from 51.9% to 38.8% (odds ratio, 0.26; 95% CI, 0.13-0.54)". On 10-point scales: note-related cognitive task load difference "2.64 [0.13] points"; ability to provide undivided attention "2.05 [0.18]"; time spent documenting after hours "0.90 [0.19]" hours. Patient understandability of care plans from notes moved "−0.44 [0.17]" (significant decrease as reported).
- LIMITS: pre/post design with no control group — association, not causal proof; self-reported outcomes; voluntary participation and 39.7% non-completion; single vendor platform; vendor co-authorship visible in author list; 30-day window.
- TOPIC CONNECTIONS: society/health — clinical workforce wellbeing as a health-system outcome of AI deployment; how/evaluation — real-world multisystem evaluation, but also an example of weak (non-randomized) evidence being widely cited; society/participation — patient understandability of AI-drafted notes measured as an outcome, touching on patient-facing effects; governance/postmarket — deployed at scale across systems before controlled outcome evidence existed.

## 5. Systematic review/meta-analysis of generative AI diagnostic performance vs physicians

- STATUS: READ-abstract (full text via PMC; consistent across three fetches)
- TITLE: A systematic review and meta-analysis of diagnostic performance comparison between generative AI and physicians
- AUTHORS+INSTITUTION: Hirotaka Takita et al. — Department of Diagnostic and Interventional Radiology, Graduate School of Medicine, Osaka Metropolitan University, Osaka, Japan
- DATE: 2025-03-22
- VENUE: npj Digital Medicine 8:175 (open access); PROSPERO CRD42023494733
- URL: https://www.nature.com/articles/s41746-025-01543-z | https://pmc.ncbi.nlm.nih.gov/articles/PMC11929846/
- READ SECTION: full text (methods, results, limitations)
- METHOD: Systematic review and meta-analysis (PRISMA-DTA) of studies validating generative AI on diagnostic tasks, June 2018–June 2024; 18,371 records screened, 83 studies included (71 peer-reviewed, 12 preprints; 17 with physician comparisons). Most-evaluated models: GPT-4 (54), GPT-3.5 (40); most common specialty: general medicine (27); tasks mostly free text (73 studies).
- FINDING: Pooled AI diagnostic accuracy "52.1% (95% CI 47.0–57.1%)". AI vs physicians overall: "no significant difference" (physicians "9.9% higher; 95% CI −2.3 to 22.0%; p = 0.10"). Vs non-expert physicians: "0.6% higher" for AI ("95% CI −14.5 to 15.7%; p = 0.93"). Vs expert physicians: AI "significantly worse" (difference "15.8%; 95% CI 4.4–27.1%; p = 0.007"). Quality: "63/83 (76%)" studies at high risk of bias; publication bias suggested (Egger's p = 0.045).
- LIMITS (stated): moderate unexplained heterogeneity; missing demographic data limits generalizability; AI "may perform worse in complex real-world scenarios (e.g., with EHR data)"; training-data opacity made external-validation classification uncertain; urology finding rests on a single large study; publication bias risk. Most included studies are vignette/text tasks, not deployed systems.
- TOPIC CONNECTIONS: how/evaluation — the reference meta-picture of what generative-AI "accuracy" claims are built on and how weak most validation studies are; society/health — pooled evidence on diagnostic performance relative to clinicians; governance/rules — the 76% high-risk-of-bias finding is an argument for minimum evidence standards before clinical claims are made; governance/postmarket — the gap between benchmark and real-world (EHR-context) performance motivates post-deployment evaluation.

## 6. Real-time deep-learning diabetic retinopathy screening in Thailand (prospective cohort)

- STATUS: READ-abstract (PubMed abstract, full numbers)
- TITLE: Real-time diabetic retinopathy screening by deep learning in a multisite national screening programme: a prospective interventional cohort study
- AUTHORS+INSTITUTION: Paisan Ruamviboonsuk et al. — Rajavithi Hospital, Bangkok, Thailand, with Google co-authors (funding: Google and Rajavithi Hospital)
- DATE: 2022-03-07 (epub); issue 2022-04
- VENUE: The Lancet Digital Health 4(4):e235–e244 (open access, CC BY-NC-ND 4.0); Thai Clinical Trials Registry TCRT20190902002
- URL: https://pubmed.ncbi.nlm.nih.gov/35272972/ (DOI 10.1016/S2589-7500(22)00017-6)
- READ SECTION: abstract (background/methods/findings/interpretation), full numbers; declared COI section
- METHOD: Prospective interventional cohort study deploying a deep-learning system into Thailand's national diabetic retinopathy screening programme at nine primary care sites. 7,940 patients screened for inclusion Dec 12, 2018–Mar 29, 2020; 7,651 (96.3%) analyzed. Real-time AI interpretation and referral recommendations; regional retina specialists over-read every image as a safety mechanism. Performance vs adjudicated reference standard by fellowship-trained retina specialists.
- FINDING: For vision-threatening diabetic retinopathy, AI "accuracy of 94·7% (95% CI 93·0-96·2), sensitivity of 91·4% (87·1-95·0), and specificity of 95·4% (94·1-96·7)". Over-reading specialists: accuracy "93·5 (91·7-95·0; p=0·17)", sensitivity "84·8% (79·4-90·0; p=0·024)", specificity "95·5% (94·1-96·7; p=0·98)". PPV "79·2 (95% CI 73·8-84·3)" vs "75·6 (69·8-81·1)" for over-readers; NPV "95·5 (92·8-97·9)" vs "92·4 (89·3-95·5)". 2,412 patients (31.5%) referred.
- LIMITS: all images also over-read by specialists, so autonomous (unassisted) programme performance was not tested; Google employees among authors holding Alphabet stock (declared); data from 2018–2020 with an earlier-generation system; interpretation notes that "socioenvironmental factors and workflows must be taken into consideration" in LMIC programmes.
- TOPIC CONNECTIONS: society/health — evidence that AI screening can match specialists in LMIC primary care where specialists are scarce; society/participation — integration into a national public programme reaching rural primary care sites raises access and inclusion questions; governance/oversight — the human over-read layer was the deployed safety control; how/evaluation — prospective, registry-linked, real-workflow evaluation rather than retrospective accuracy claims.

## 7. LLM preconsultation chatbot for primary-to-specialist care (RCT, China)

- STATUS: READ-abstract (journal-page abstract, full text incl. trial registration ID)
- TITLE: An LLM chatbot to facilitate primary-to-specialist care transitions: a randomized controlled trial
- AUTHORS+INSTITUTION: Xinge Tao et al. — School of Population Medicine and Public Health, Chinese Academy of Medical Sciences & Peking Union Medical College, Beijing, China (co-authors from The First Affiliated Hospital of Guilin Medical University and others)
- DATE: 2026-01-19
- VENUE: Nature Medicine (open access); Chinese Clinical Trial Registry ChiCTR2400094159
- URL: https://www.nature.com/articles/s41591-025-04176-7
- READ SECTION: full abstract (journal meta description = complete abstract text)
- METHOD: RCT of "PreA", an LLM chatbot co-designed with local stakeholders to do history-taking, preliminary diagnoses, and test ordering ahead of specialist consultation. "2,069 patients (1,141 women; 928 men)" randomized to PreA-only, PreA with staff support (PreA-human), or no PreA (No-PreA) before specialist consultation; "111 specialists from 24 medical disciplines across two health centers".
- FINDING (as stated in abstract): PreA-only "significantly reduced physician consultation duration (28.7% reduction; 3.14 ± 2.25 min) compared to the No-PreA group (4.41 ± 2.77 min; P < 0.001)"; "physician-perceived care coordination (mean scores 113.1% increase; 3.69 ± 0.90 versus 1.73 ± 0.95; P < 0.001)"; "patient-reported communication ease (mean scores 16.0% increase; 3.99 ± 0.62 versus 3.44 ± 0.97; P < 0.001)". "Equivalent outcomes between the PreA-only and PreA-human groups confirmed the autonomous operation capability." "Co-designed PreA outperformed the same model with additional fine-tuning on local dialogues across clinical decision-making domains."
- LIMITS: two health centers in one country; primary endpoints are process and perception measures (consultation duration, coordination, communication), not clinical outcomes or diagnostic accuracy; abstract does not report safety events or mis-referral rates; the unusual "113.1%"/"16.0%" percentage phrasing is as printed in the abstract and should be checked against the full tables before citing numerically.
- TOPIC CONNECTIONS: society/health — patient-facing LLM reshaping the primary-to-specialist pathway in a resource-limited setting; society/participation — co-design with local stakeholders is the study's central claim ("co-design ... compared to passive local data collecting" was more effective), and patients used the tool autonomously; how/evaluation — a registered three-arm RCT of an LLM in live care flow; governance/oversight — the PreA-human arm equivalence finding is precisely the evidence used to argue humans can be removed from the loop, an oversight decision that needs scrutiny.

## 8. Therabot — generative AI therapy chatbot RCT (US)

- STATUS: LEAD (abstract not directly read — see failure note)
- TITLE: Randomized Trial of a Generative AI Chatbot for Mental Health Treatment
- AUTHORS+INSTITUTION: Michael V. Heinz et al. — Dartmouth College (Geisel School of Medicine), per publisher and Dartmouth press release
- DATE: 2025-03 (per publisher/press coverage)
- VENUE: NEJM AI, DOI 10.1056/AIoa2400802
- URL: https://ai.nejm.org/doi/full/10.1056/AIoa2400802
- READ SECTION: none — direct fetches failed (NEJM AI returns HTTP 403 / Cloudflare challenge; not indexed on PubMed Central; Semantic Scholar API returned HTTP 429 rate-limit on repeated attempts). Secondary description via Dartmouth press release only: first RCT of a fully generative-AI therapy chatbot reporting symptom improvements for major depressive disorder, generalized anxiety disorder, and eating-disorder risk vs waitlist control. Numbers NOT verified — do not cite figures from this entry without reading the paper.
- METHOD: (unverified) RCT of the Therabot generative-AI therapy chatbot vs waitlist control.
- FINDING: not verified at abstract level.
- LIMITS: unknown until read; waitlist-controlled design visible in coverage.
- TOPIC CONNECTIONS: society/health — mental-health care delivered by an LLM agent; governance/oversight — autonomous therapeutic conversation raises oversight questions if verified; how/evaluation — candidate for the "clinical trial of LLM-based advice" slot alongside Goh and Tao.

---

## Additional leads (found, not read)

- LEAD: Final MASAI trial results, The Lancet (Jan 2026) — reported improved sensitivity and reduced interval cancers at further follow-up (per EurekAlert/ASCO Post coverage). Would supersede/extend item 2. Not read: paywalled/press-release only in this pass.
- LEAD: Oxford study on risks of LLM chatbots giving medical advice (University of Oxford news, 2026-02-10, https://www.ox.ac.uk/news/2026-02-10-new-study-warns-risks-ai-chatbots-giving-medical-advice) — reports wrong diagnoses and impacts on self-assessment/urgency perception. Venue and abstract unverified; not read.
- LEAD: AIRIS-TB population-scale chest X-ray AI evaluation, npj Digital Medicine 2025 (https://www.nature.com/articles/s41746-025-01832-7) — reportedly evaluated on >1 million CXRs (AUC 98.51%, FNR 1.57% per search snippet). Overlaps topically with item 3; not read, numbers unverified.

## Honest note on failures and limits

- PubMed via the standard fetcher returned a cookie-notice shell for two queries; the alternate web reader succeeded, and one fetch per page was then verified. Europe PMC rendered only navigation. NEJM AI (Therabot) is fully blocked to my fetchers (403/Cloudflare), so item 8 is a lead, not a read; Semantic Scholar was rate-limited (429) on every attempt.
- Reading depth is abstract-level (plus, where noted, PMC full text for Goh, Kazemzadeh, Takita). I did not verify tables, supplementary materials, or protocols; quoted numbers are exactly as they appear in the abstracts/pages read. The Tao et al. percentages ("113.1%", "16.0%") are odd as printed and flagged above.
- Two of eight studies (Kazemzadeh, Ruamviboonsuk) have vendor (Google) authors and funding, and one (Olson) has the scribe vendor in the author list; COI positions are stated where I saw them declared, but I did not audit COIs beyond the abstract/declaration pages.
- Selection is convenience-based from open-access venues; negative or null deployment studies are likely underrepresented in what I surfaced. No causation is claimed anywhere from pre/post or association designs (Olson in particular is pre/post without a control arm).
- Dedupe performed against catalogue.json by title keyword grep and exact DOI grep for all 8 DOIs (0 hits each); graph.json topic ids confirmed as the labels used above.
