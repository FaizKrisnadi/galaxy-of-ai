#!/usr/bin/env python3
"""Merge institution-list harvest (read 2026-11-01) into the catalogue.
All records from this pass are access-tier 'L' (metadata from the institution's own
listing page, read this session; abstract NOT read) unless noted."""
import json, pathlib

p = pathlib.Path("sources/catalogue.json")
cat = json.loads(p.read_text())
R = cat["records"]
have = {r["id"] for r in R} | {r["url"] for r in R}
L = "metadata from institution list, read 2026-11-01 (abstract not read)"

def add(id, title, authors, date, inst, typ, url, topics, access, verif, relevance):
    global R
    if id in have or url in have: print("skip dup:", id); return
    R.append(dict(id=id, title=title, authors=authors, date=date, institution=inst, type=typ,
                  url=url, galaxy_topics=topics, access=access, verification=verif, relevance=relevance))
    have.add(id); have.add(url)

EP="Epoch AI"; EPN="CC BY (per Epoch data index: free to use/distribute/reproduce with attribution)"
add("epoch-ai-data-centers-db","AI data centers (open database)",EP,"updated 2026-11-01",EP,"open dataset + explorer", "https://epoch.ai/data/ai-data-centers","infrastructure/centres, economics/investment","downloadable data; licence stated on index page",L,"Open database estimating compute, power and construction timelines from satellite and permit data. Companion to the methodology record.")
add("epoch-ai-models-db","AI models database (3,700+ models, 1950-today)",EP,"updated 2026-10-31",EP,"open dataset + explorer","https://epoch.ai/data/ai-models","how/models, how/evaluation",EPN,L,"Large historical model database; supports training-compute and scale trend work.")
add("epoch-chip-sales","AI chip sales",EP,"updated 2026-10-21",EP,"open dataset","https://epoch.ai/data/ai-chip-sales","infrastructure/chips, politics/chips",EPN,L,"Estimates compute, power and spending from financial reports and disclosures.")
add("epoch-gpu-clusters","GPU clusters database (500+ clusters)",EP,"updated 2026-03-13",EP,"open dataset","https://epoch.ai/data/gpu-clusters","infrastructure/centres, infrastructure/chips",EPN,L,"Over 500 GPU clusters/supercomputers for AI training and inference.")
add("epoch-ml-hardware","Machine learning hardware (180+ accelerators)",EP,"updated 2026-10-30",EP,"open dataset","https://epoch.ai/data/machine-learning-hardware","infrastructure/chips",EPN,L,"Specs of deep-learning-era accelerators.")
add("epoch-chatgpt-usage","ChatGPT usage (YouGov panel metadata)",EP,"updated 2026-10-01",EP,"open dataset","https://epoch.ai/data/chatgpt-usage","how/inference, society/trust",EPN,L,"Aggregate metadata from recorded ChatGPT histories of 5,000 US panelists (Dec 2022-Dec 2025); privacy-relevant provenance documented by Epoch.")
add("epoch-polling","Polling on AI usage at work",EP,"updated 2026-08-14",EP,"open dataset","https://epoch.ai/data/polling","society/skills, economics/jobs",EPN,L,"How employed Americans use AI at work, across demographics.")
add("epoch-trends","Trends in AI",EP,"living",EP,"analysis series","https://epoch.ai/trends","how/evaluation, economics/productivity",EPN,L,"Ongoing quantitative trend analyses (compute, data, performance).")

CS="CSET, Georgetown University"
add("cset-redteaming-reporting","Systematizing the Reporting of AI Red-Teaming","Ji, Shea-Blymyer, Beavan & Yee","2026-10",CS,"report","https://cset.georgetown.edu/publication/systematizing-the-reporting-of-ai-red-teaming/","governance/oversight, how/evaluation","metadata from CSET list",L,"How red-teaming results are reported — connects independent testing to oversight practice.")
add("cset-tracking-chips","Tracking AI Chips","Feldgoise, Miller & Dohmen","2026-09",CS,"report","https://cset.georgetown.edu/publication/tracking-ai-chips/","politics/chips, infrastructure/chips","metadata from CSET list",L,"Chip tracking relevant to export-control enforcement.")
add("cset-stem-talent","How Global Talent Pathways Shape U.S. STEM Award Achievement","Thinnyun, Beavan & Arnold","2026-09",CS,"data brief","https://cset.georgetown.edu/publication/how-global-talent-pathways-shape-u-s-stem-award-achievement/","economics/jobs, society/skills","metadata from CSET list",L,"Workforce/talent pathways evidence.")
add("cset-semi-workforce","Strengthening the U.S. Semiconductor Manufacturing Workforce","Karsten & Koslosky","2026-09",CS,"report","https://cset.georgetown.edu/publication/strengthening-the-u-s-semiconductor-manufacturing-workforce/","economics/jobs, infrastructure/chips","metadata from CSET list",L,"Chip-manufacturing workforce constraints — supply-chain grounding.")
add("cset-ai-competition","Artificial Intelligence in Competition","Andrew Lohn","2026-09",CS,"report","https://cset.georgetown.edu/publication/artificial-intelligence-in-competition/","economics/ownership, governance/rules","metadata from CSET list",L,"AI and competition policy — market-power grounding.")
add("cset-cyber-compliance","Outpaced: AI and Policy's Role in Transforming Cybersecurity Compliance","Katherine Carroll","2026-08",CS,"report","https://cset.georgetown.edu/publication/outpaced-ai-and-policys-role-in-transforming-cybersecurity-compliance/","governance/standards, governance/postmarket","metadata from CSET list",L,"Compliance machinery under AI change — standards/audit access.")
add("cset-coalition-ops","Coalition Operations","Probasco, Mayo & Kahn","2026-09",CS,"report","https://cset.georgetown.edu/publication/coalition-operations/","politics/international, how/agents","metadata from CSET list",L,"AI in military coalition settings — international/security angle.")

HAI="Stanford HAI"
add("hai-ai-index-2026","AI Index Report 2026","AI Index Steering Committee (Stanford HAI)","2026",HAI,"annual report (free to read; independent initiative)","https://aiindex.stanford.edu/ai-index/2026-ai-index-report","how/evaluation, economics/productivity, governance/rules","landing page read 2026-11-01; report not opened this session",L,"Rigorous annual measurement across R&D, performance, economy, education, policy; notes 'data transparency is declining' — a stated measurement limit.")

OA="OpenAI"
add("openai-long-horizon-safety","Safety and alignment in an era of long-horizon models",OA,"2026-07-20",OA,"company research/position post","https://openai.com/index/safety-alignment-long-horizon-models/","governance/oversight, how/agents","metadata from OpenAI safety index",L,"Company framing of safety for long-horizon agentic models; provider-authored.")
add("openai-pacing-cyber","Pacing model development in an era of cyber-critical capabilities",OA,"2026-08-18",OA,"company policy post","https://openai.com/index/pacing-model-development-cyber-capabilities/","politics/national, how/agents","metadata from OpenAI safety index",L,"Developer posture on capability pacing for cyber-relevant capability.")
add("openai-oss-safeguard","gpt-oss-safeguard technical report",OA,"2026 (date not shown on listing)",OA,"technical report","https://openai.com/index/gpt-oss-safeguard-technical-report/","how/evaluation, governance/oversight","metadata from OpenAI safety index",L,"Open-weights safeguard model technical report; provider-authored.")
add("openai-sora2-card","Sora 2 System Card",OA,"2026 (date not shown on listing)",OA,"system card","https://openai.com/index/sora-2-system-card/","how/evaluation, society/trust","metadata from OpenAI safety index",L,"System cards are self-published evaluations — privileged access, selection risk.")
add("openai-research-index","OpenAI research index (product-announcement heavy)","OA","living",OA,"publication index","https://openai.com/research/","how/models","index page read 2026-11-01",L,"Listing read: dominated by product launches (GPT-6.x etc.); system cards and safety posts live under /safety/. Recorded as the entry point; individual research papers need targeted retrieval.")

AN="Anthropic"
add("anthropic-agents-judgment","How AI agents shape experts' judgment calls",AN,"2026-10-27",AN,"company research post","https://www.anthropic.com/research/agents-judgment-calls","how/agents, society/skills","metadata from Anthropic research index",L,"Agents and expert judgment — relevant to discretion and verification topics.")
add("anthropic-ukaisi-assessment","An alignment assessment of the UK AISI cybertesting incident",AN,"2026-10-23",AN,"company research post","https://www.anthropic.com/research/alignment-assessment-ukaisi","governance/oversight, how/evaluation","metadata from Anthropic research index",L,"Company assessment of a third-party cyber-testing incident; provider-authored.")
add("anthropic-unintended-actions","Investigating unintended model actions in our evaluations and internal use",AN,"2026-10-09",AN,"company research post","https://www.anthropic.com/research/investigating-unintended-model-actions","governance/oversight, how/agents","metadata from Anthropic research index",L,"Internal investigation of unintended actions — parallels the OpenAI October 2026 incident record.")
add("anthropic-cyber-assessment","An alignment assessment of recent cybersecurity incidents",AN,"2026-09-09",AN,"company research post","https://www.anthropic.com/research/alignment-assessment-cybersecurity-incidents","society/trust, governance/oversight","metadata from Anthropic research index",L,"Provider-authored incident assessment; corroboration needed for external use.")

DM="Google DeepMind"
add("deepmind-publications-index","Google DeepMind publications index (267 items)","DM","living",DM,"publication index (paginated)","https://deepmind.google/publications/","how/models, how/agents, how/evaluation","index page read 2026-11-01; individual paper URLs not exposed in listing extraction",L,"Recent relevant items seen: 'Evaluating frontier models for stealth and situational awareness' (2026-07-15), 'Economic Policy for AGI' (2026-09-16), 'Architectural Backdoors for Within-Batch Data Stealing' (2026-09-22). Retrieve exact paper URLs before citing.")

IEA2="IEA"
add("iea-energy-and-ai","Energy and AI",IEA2,"2025-04-10",IEA2,"flagship report (CC BY 4.0, free PDF)","https://www.iea.org/reports/energy-and-ai","infrastructure/electricity, environment/energy, environment/goals","report page read 2026-11-01; PDF not opened this session",L,"Global/regional modelling of AI electricity demand and supply sources; chapters on demand, supply, security, climate. Key source for Energy & emissions grounding.")
add("iea-key-questions","Key Questions on Energy and AI",IEA2,"2026-04-16",IEA2,"flagship report","https://www.iea.org/reports/key-questions-on-energy-and-ai","infrastructure/electricity, environment/energy","listed on IEA Energy and AI page; not opened this session",L,"Follow-up flagship that supplies the IEA tracker's data; underlying source for the data-centre electricity tracker.")

AIN="AI Now Institute"
add("ainow-landscape-2025","Artificial Power: 2025 Landscape Report",AIN,"2025-06-03",AIN,"report (independent, critical perspective)","https://ainowinstitute.org/publications/research/ai-now-2025-landscape-report","governance/rules, economics/ownership, politics/international","metadata from AI Now list",L,"Independent critical framing of AI power concentration.")
add("ainow-dc-toolkit","North Star Data Center Policy Toolkit: State and Local Policy Interventions","AIN","2026-04-01",AIN,"report/toolkit","https://ainowinstitute.org/publications/data-center-policy-guide","infrastructure/land, governance/procurement, environment/resources","metadata from AI Now list",L,"State/local interventions against 'rampant AI data center expansion' — directly relevant to land/permits and place.")
add("ainow-nuclear","Fission for Algorithms: The Undermining of Nuclear Regulation in Service of AI",AIN,"2025-11-11",AIN,"report","https://ainowinstitute.org/publications/fission-for-algorithms","environment/energy, governance/rules","metadata from AI Now list",L,"Energy-regulation stress from AI demand — independent watchdog angle.")
add("ainow-kill-chain","Anatomy of an AI Kill Chain (with Airwars)",AIN,"2026-07-28",AIN,"analysis","https://ainowinstitute.org/publications/anatomy-of-an-ai-kill-chain","politics/international, how/agents","metadata from AI Now list",L,"Critical analysis of military AI chains — independent perspective on agents in conflict.")
add("ainow-double-agents","Double Agents: Defensive AI Agents Magnify Cyber Risks",AIN,"2026-07-08",AIN,"research","https://ainowinstitute.org/publications/double-agents","how/agents, society/trust","metadata from AI Now list",L,"Critical counterpoint to defensive-AI-agent narratives.")
add("ainow-europe-industrial","Redirecting Europe's AI Industrial Policy",AIN,"2024-10-15",AIN,"report","https://ainowinstitute.org/publications/research/redirecting-europes-ai-industrial-policy","politics/national, economics/ownership","metadata from AI Now list",L,"Critical European industrial-policy analysis.")

MI="Mila (Quebec AI Institute)"
add("mila-ecuas","ECUAS: metrics for principled evaluation of uncertainty-augmented systems","Estienne, Ernst, Vera, Piantanida & Ferrer","2026 (listing shows 2026-12-30; arXiv implies earlier — verify)",MI,"paper (openreview)","https://openreview.net/forum?id=O9u4lItD9K","how/evaluation","metadata from Mila list; URL on listing",L,"Uncertainty-aware evaluation for high-stakes decision-making.")
add("mila-gitchameleon","GitChameleon 2.0: Evaluating AI Code Generation Against Python Library Version Incompatibilities","Misra, Islah, May, Rauby, Wang, Gehring, Orvieto, Chaudhary, Muller, Rish, Kahou & Caccia","2026 (arXiv 2507.12367)",MI,"paper (arXiv)","https://doi.org/10.48550/arXiv.2507.12367","how/evaluation, society/skills","metadata from Mila list; arXiv DOI on listing",L,"Code-generation evaluation under version incompatibilities — practical verification grounding.")
add("mila-risk-rl","Reward Redistribution for CVaR MDPs using a Bellman Operator on L-infinity","Muni, Taboga, Derman, Bacon & Delage","2026 (arXiv 2602.03778)",MI,"paper (arXiv)","https://doi.org/10.48550/arXiv.2602.03778","how/models, how/agents","metadata from Mila list",L,"Risk-averse RL aimed at safety-critical applications.")
add("mila-sft-rotation","Rotation-Preserving Supervised Fine-Tuning","Jin, Ni, Li, Bacon, Hamdaqa & Precup","2026 (arXiv 2605.10973)",MI,"paper (arXiv)","https://doi.org/10.48550/arXiv.2605.10973","how/models","metadata from Mila list",L,"Fine-tuning degradation — training-methods grounding.")
add("mila-diffusion-policy","Adaptive Order Policies for Masked Diffusion","Mohamud, Hasan, Ravanelli & Bengio","2026 (arXiv 2606.00295)",MI,"paper (arXiv)","https://doi.org/10.48550/arxiv.2606.00295","how/models, how/agents","metadata from Mila list",L,"Policy learning for diffusion models — agent-style decision-making relevance.")
add("mila-speech-grounding","Listen First, Then Answer: Timestamp-Grounded Speech Reasoning","Jeong, Mousavi, Ravanelli & Subakan","2026 (arXiv 2603.19468)",MI,"paper (arXiv)","https://doi.org/10.48550/arXiv.2603.19468","how/models","metadata from Mila list",L,"Multimodal grounding example.")

OII="Oxford Internet Institute"
add("oii-empires-of-ai","Empires of AI (guest essay)","Ferguson, Klaassen & Schmidt (one OII doctoral researcher)","2026-10-20","OII / Foreign Affairs","opinion essay (press)","https://www.foreignaffairs.com/china/empires-artificial-intelligence-ferguson-klaassen-schmidt","economics/ownership, politics/international","listed on OII research page",L,"Independent critical perspective on AI power concentration; press essay, not peer-reviewed research.")
add("oii-research-page","OII research index (projects + press; publication list paginated)","OII","living",OII,"institutional index","https://www.oii.ox.ac.uk/research/","society/participation, governance/discretion","page read 2026-11-01; publication list itself not rendered in extraction",L,"Entry point recorded; the publication list needs targeted retrieval. Relevant theme: right to reasonable algorithmic inferences (project).")

cat["records"] = R
cat["counts"] = {"total": len(R)}
p.write_text(json.dumps(cat, indent=1, ensure_ascii=False))
print("catalogue records:", len(R))
