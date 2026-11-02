#!/usr/bin/env python3
import json, pathlib, csv, traceback, sys
p = pathlib.Path("sources/catalogue.json")
cat = json.loads(p.read_text())
R = cat["records"]; have = {r["url"] for r in R}
S = "located via targeted web search 2026-11-01 (official URL); landing page not fetched"
L = "metadata from institution list, read 2026-11-01 (abstract not read)"
V = "verified at origin 2026-11-01 (page/abstract read)"

def add(id,title,authors,date,inst,typ,url,topics,access,verif,relevance):
    assert id not in {r["id"] for r in R} and url not in have, f"dup {id}"
    assert isinstance(relevance,str) and relevance, f"missing relevance: {id}"
    R.append(dict(id=id,title=title,authors=authors,date=date,institution=inst,type=typ,url=url,
                  galaxy_topics=topics,access=access,verification=verif,relevance=relevance))
    have.add(url)

try:
    CH="Center for Human-Compatible AI, UC Berkeley"
    add("chai-managing-risks","Managing AI Risks in an Era of Rapid Progress","Bengio, Hinton, Yao, Song, Abbeel, et al.","2023","CHAI / UC Berkeley (multi-institution statement)","paper (arXiv 2310.17688)","https://arxiv.org/abs/2310.17688","governance/oversight, how/evaluation, politics/international","arXiv page (open)",L,"Landmark multi-author statement on AI risk governance in a rapid-progress era.")
    add("chai-tasra","TASRA: A Taxonomy of Societal-Scale Risks from AI","Andrew Critch & Stuart Russell","2023","CHAI / UC Berkeley","paper (arXiv 2306.06924)","https://arxiv.org/abs/2306.06924","how/evaluation, governance/rules, society/trust","arXiv page (open)",L,"Taxonomy framing societal-scale AI risk — conceptual grounding for the safety/risk vocabulary.")
    add("chai-control-roadmap","Control for Societal-scale Challenges: Road Map 2030","Anca Dragan, Andrew Alleyne, et al.","2023","CHAI / UC Berkeley + IEEE CSS","roadmap paper","https://ieeecss.org/control-societal-scale-challenges-road-map-2030","how/agents, infrastructure/grids","open page (IEEE CSS)",L,"Control-theory road map linking automation and societal-scale systems.")
    add("chai-teacher-selection-rlhf","Active teacher selection for reinforcement learning from human feedback","Freedman, Svegliato, Wray & Russell","2023","CHAI / UC Berkeley","paper (arXiv 2310.15288)","https://arxiv.org/abs/2310.15288","how/models, society/skills","arXiv page (open)",L,"RLHF method: selecting whose feedback teaches the model — human-role grounding.")

    CM="Block Center for Technology and Society, Carnegie Mellon University"
    add("cmu-transition-memo","The United States Government's Role in Harnessing Technology for Future Prosperity: A Transition Memorandum","Block Center authors (list page)","2024",CM,"policy memorandum (PDF)","https://www.cmu.edu/sites/default/files/cmu-block-center-site-files/documents/Block%20Center%202025%20Transition%20Memo%20(2).pdf","governance/procurement, politics/national","direct PDF (official site)",L,"CMU policy memo on government's technology role — procurement/state-capacity angle.")
    add("cmu-state-local-ai-guide","A Policy Maker's Guide to Artificial Intelligence for State and Local Governments","Block Center authors (list page)","2020",CM,"policy guide (PDF)","https://www.cmu.edu/sites/default/files/cmu-block-center-site-files/documents/Safe%20and%20Equitable%20AI%20for%20State%20and%20Local%20Governments.pdf","governance/procurement, governance/discretion","direct PDF (official site)",L,"Practitioner guide for sub-national AI adoption; pairs with AI Now's state/local toolkit.")

    AD="Ada Lovelace Institute"
    add("ada-minding-business","Minding your business",AD,"2026-10-22",AD,"policy briefing","https://www.adalovelaceinstitute.org/policy-briefing/minding-your-business/","economics/ownership, governance/rules","open site",L,"Newest Ada Lovelace briefing (abstract not read).")
    add("ada-uk-regulation-options","Making sense of the current options for AI regulation in the UK",AD,"2026-09-25",AD,"feature","https://www.adalovelaceinstitute.org/feature/ai-regulation-options-uk/","governance/rules, politics/national","open site",L,"Independent explainer of UK AI-regulation options.")
    add("ada-care-consideration","Care and consideration",AD,"2026-09-08",AD,"report","https://www.adalovelaceinstitute.org/report/care-and-consideration/","how/evaluation, society/participation","open site",L,"Publication screening and evidence-synthesis methods — evidence-infrastructure angle.")
    add("ada-measuring-up","Measuring Up",AD,"2026-05-11",AD,"policy briefing","https://www.adalovelaceinstitute.org/policy-briefing/measuring-up/","economics/productivity, governance/rules","open site",L,"Evaluates claims about AI and productivity in the UK public sector — counterweight to productivity hype.")
    add("ada-navigating-future","Navigating the future",AD,"2026-04-13",AD,"report","https://www.adalovelaceinstitute.org/report/navigating-the-future/","economics/jobs, society/skills","open site",L,"AI and young people's education-to-work transitions.")

    AI2="Allen Institute for AI (Ai2)"
    add("olmo-paper","OLMo: Accelerating the Science of Language Models","Dirk Groeneveld et al. (Ai2)","2024-02-01 (v4 2024-06-07; arXiv:2402.00838)","Ai2","paper (arXiv, CC BY 4.0) + open data/code/weights","https://arxiv.org/abs/2402.00838","how/models, how/data","arXiv open (CC BY 4.0 paper); model/data/code on GitHub and Hugging Face under separate licences",V,"'Competitive, truly Open Language Model' with open training data, training and evaluation code — the reference open-science counterpoint to closed frontier models.")
    add("olmo3-blog","OLMo 3 (blog release)","Ai2","2025-11",AI2,"model release (blog)","https://allenai.org/blog/olmo3","how/models","open blog release",S,"Compact dense 7B/32B models described as the 'most complete model pipeline ever released' — verify details on the blog before citing specifics.")

    AISG="AI Singapore (National Research Foundation)"
    add("sealion-paper","SEA-LION: Southeast Asian Languages in One Network","Raymond Ng et al. (AI Singapore)","2025-04-08 (v4 2025-10-30; arXiv:2504.05747; IJCNLP-AACL 2025)","AI Singapore","paper (arXiv, CC BY 4.0) + open weights","https://arxiv.org/abs/2504.05747","how/models, society/participation","arXiv open (CC BY 4.0 paper); open weights on Hugging Face (base-model licences apply)",V,"Open SEA-language models (11 languages incl. Indonesian, Malay, Thai, Tamil, Khmer) built via continued pre-training; released for the SEA community. Regional perspective on who AI languages serve.")
    add("sealion-seald-dataset","SEALD - Southeast Asian Languages in One Network Data","AI Singapore","living",AISG,"open dataset programme","https://aisingapore.org/aiproducts/southeast-asian-languages-in-one-network-data-seald","how/data","open dataset programme (official page; licence stated there)",S,"Regional data corpus underpinning SEA-LION - Southeast-Asian data-sovereignty angle.")

    add("deepmind-stealth-sa","Evaluating Frontier Models for Stealth and Situational Awareness","Mary Phuong, Roland S. Zimmermann, Ziyue Wang, David Lindner, Victoria Krakovna, Sarah Cogan, Allan Dafoe, Lewis Ho, Rohin Shah (DeepMind AGI safety team)","2025-05-02 (v4 2025-07-03; arXiv:2505.01420)","Google DeepMind","paper (arXiv)","https://arxiv.org/abs/2505.01420","how/evaluation, governance/oversight, how/agents","arXiv open (licence stated on the arXiv page)",V,"Scheming-evaluation suite (5 stealth + 11 situational-awareness tests) supporting 'a scheming inability safety case'; no concerning levels found in tested models - a passing result supports an inability claim only for those models. Note: DeepMind's own list showed 15 Jul 2026; arXiv v1 is 2 May 2025 (listing/artefact flagged).")

    LCFI="Leverhulme Centre for the Future of Intelligence, University of Cambridge"
    add("lcfi-repository","LCFI open-access publication collection (Cambridge Apollo)","LCFI","living",LCFI,"open-access repository collection (handle 1810/286662)","https://www.repository.cam.ac.uk/handle/1810/286662","society/trust, governance/rules","collection page: item list JS-only - entry point + permanent URI recorded",L,"Institutional entry point; items must be listed via the repository UI. Programme example: 'AI: Trust and Society'.")

    add("cmu-blockcenter-index","Block Center publications index","CMU Block Center","living",CM,"institutional index","https://www.cmu.edu/block-center/publications","governance/procurement","index page read 2026-11-01",L,"Listing verified: newest visible items are 2020-2024 policy PDFs; no 2026 items visible at harvest time.")
    add("eth-ai-center-index","ETH AI Center publications index","ETH Zurich AI Center","living","ETH Zurich AI Center","institutional index (JS-loaded list)","https://ai.ethz.ch/research/publications.html","how/models, how/evaluation","JS-only listing; entry point recorded",L,"Index located via search; JS-only render - no items extractable 2026-11-01. 145 professors (37 core + 108 associated, as of Jul 2026). Individual papers need another retrieval route (Scholar/faculty pages).")

    add("cifar-pcais-evaluation","Evaluation of the Pan-Canadian Artificial Intelligence Strategy","ISED Canada (government evaluation; CIFAR strategy)","2024-2026 (page undated)","ISED Canada / CIFAR","official government evaluation","https://ised-isde.canada.ca/site/audits-evaluations/en/evaluation/evaluation-pan-canadian-artificial-intelligence-strategy-20-1","politics/national, economics/ownership","official government page (open)",S,"Government evaluation of the national AI strategy behind Mila/Amii/Vector - institutional context for the Canadian ecosystem.")

    UCL="UCL Institute for Innovation and Public Purpose"
    add("ucl-iipp-netzero-dri","Public procurement for net-zero digital research infrastructure: a mission-oriented approach","UCL IIPP (policy report 2023/02)","2023-06",UCL,"policy report","https://www.ucl.ac.uk/bartlett/publications/2023/jun/public-procurement-net-zero-digital-research-infrastructure-mission-oriented-approach","governance/procurement, infrastructure/centres","open UCL publication page",S,"Mission-oriented procurement applied to digital research infrastructure - procurement-machinery grounding.")
    add("ucl-iipp-taxonomy","Mission-Oriented Procurement for Green Innovation: A new taxonomy","UCL IIPP","2026-06",UCL,"working paper","https://www.ucl.ac.uk/bartlett/publications/2026/jun/mission-oriented-procurement-green-innovation-new-taxonomy","governance/procurement, environment/goals","open UCL publication page",S,"2026 IIPP taxonomy linking procurement to green innovation.")

    add("nus-genai-cs-education","Reshaping Undergraduate Computer Science Education in the Generative AI Era","AI4SG Lab, NUS School of Computing","2026-05 (arXiv:2606.07545)","NUS School of Computing","paper (arXiv)","https://arxiv.org/html/2606.07545v1","society/skills, how/using","arXiv HTML (open)",S,"Regional university evidence on AI's effect on computing education - pairs with the verification-burden theme.")

except Exception:
    traceback.print_exc()
    sys.exit(1)

cat["counts"] = {"total": len(R)}
p.write_text(json.dumps(cat, indent=1, ensure_ascii=False))
with open("sources/catalogue.csv","w",newline="") as f:
    w = csv.writer(f)
    w.writerow(["id","title","authors","date","institution","type","url","galaxy_topics","access","verification","relevance"])
    for r in R:
        w.writerow([r["id"],r["title"],r["authors"],r["date"],r["institution"],r["type"],r["url"],r["galaxy_topics"],r["access"],r["verification"],r["relevance"]])
print("catalogue:", len(R), "records")
