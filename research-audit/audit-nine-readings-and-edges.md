# Independent audit — nine Addendum-38 readings and two graph connections
Auditor: separate audit session, 4 November 2026. Workspace: research-audit/ only (no shared files edited).
Method: for each reading, the original accessible source was re-opened (archived PDF extraction in sources/pdfs/ where available; live page otherwise) and the specific stored claims, quoted passages, dates, geography, figures, methods and limits were checked against what the source actually says. Verdict classes: SUPPORTED (stored claims match the source as read), OVERSTATED (claim goes beyond the material read), FALSE (contradicted), INACCESSIBLE (could not be re-opened this audit), UNKNOWN (cannot be established from material read).

## Verdict summary

| # | Record | Verdict | Notes |
|---|--------|---------|-------|
| 1 | au-continental-ai-strategy | SUPPORTED with extraction caveats | Quotes verified modulo PDF-extraction spacing; date-of-adoption is search-derived |
| 2 | ilia-2025-exec-summary | SUPPORTED | All stored figures verified in the read text, incl. "19 countries" |
| 3 | uscopyright-ai-part2 | SUPPORTED | All four stored quotes verbatim in the executive summary |
| 4 | who-lmm-guidance | SUPPORTED WITH CORRECTIONS | Recommendation ≠ in-force law (supervisor-confirmed); one stored quote is a paraphrase |
| 5 | grace-ai-authors-2024 | SUPPORTED | All five stored figures verbatim in the abstract |
| 6 | crfm-foundation-models-report | SUPPORTED | All three stored passages verbatim in §1.1 |
| 7 | kapoor-normal-technology | SUPPORTED WITH CORRECTIONS | 6/7 quotes verbatim; one paraphrase-as-quote; truncation scope confirmed |
| 8 | india-niti-responsible-ai | SUPPORTED | Principles, constitutional framing, WEF/Microsoft credits verified |
| 9 | japan-ai-guidelines-business | SUPPORTED | All five stored facts verified in the MIC release; guidelines text remains unread |

## Per-reading detail

### 1. au-continental-ai-strategy (AU Continental AI Strategy, Jul 2024)
- Re-checked from the archived extraction (sources/pdfs/au-continental-ai-strategy.txt).
- Verified present: "There is also an AI divide between and within countries and globally" (found verbatim); "data are usually sourced from developed countries and from non-diverse and inclusive developers' teams" (found; the PDF extraction renders hyphenation with inserted spaces, e.g. "non -diverse", "people -centric" — the stored record uses cleaned hyphenation faithful to the printed text); GenAI risks sentence (disinformation/privacy/surveillance/copyright) found; "fifteen action areas" found; the first four action areas as stored match the text.
- Date check: the record's date field says "adopted at the AU Executive Council, Aug 2024". The PDF itself does not state an adoption date in the sections read; the August 2024 adoption comes from the AU document page (search-derived), not from the read material. Classify the adoption detail as UNKNOWN-from-material-read (supported by the AU page per search coverage).
- Geography: continental (55 AU member states implied, not counted in the read text) — the record does not claim a count. OK.
- Unread sections stated: pp. 7–66 (action-area detail, implementation) — correct.
- Overall: no factual overstatement found.

### 2. ilia-2025-exec-summary (ECLAC/CENIA ILIA 2025 executive summary)
- Verified verbatim in the archived extraction: "1.12% of global AI investment" (1 hit); "six times below" (1); talent gap "widened more rapidly since 2022" (1); "19 countries" (5 hits — the stored LIMITS line "19 countries covered" is supported by the read text, not just search).
- Coordination/financing credits (ECLAC division staff, CENIA, EU Global Gateway) verified on the copyright/credits page.
- Foreword authorship (José Manuel Salazar-Xirinachs) verified.
- Date: the exec summary is marked 2025; the third-edition history (2023/2024 editions) is in the prologue. No discrepancy.
- Overall: fully supported; the 184-pp main report remains unread as stated.

### 3. uscopyright-ai-part2 (US Copyright Office, Part 2: Copyrightability, Jan 2025)
- All four quotes stored in the record and edge verified verbatim in the executive summary: "resolved pursuant to existing law, without the need for legislative change"; "Copyright does not extend to purely AI-generated material, or material where there is insufficient human control over the expressive elements"; "prompts do not alone provide sufficient control"; "The case has not been made for additional copyright or sui generis protection for AI-generated content" (sui generis: 13 hits in the document).
- Preface facts verified (2023 initiative; March 2023 registration guidance; Aug 2023 Notice of Inquiry; "more than 10,000 comments… all 50 states and… 67 countries").
- Scope note stands: the training-data question is not Part 2's subject (it is deferred to a later part of the series) — the record states this correctly.
- Overall: fully supported.

### 4. who-lmm-guidance (WHO LMM guidance, 18 Jan 2024) — CORRECTIONS REQUIRED
- Verified verbatim in the news release: "over 40 recommendations"; "mandatory post-release auditing and impact assessments"; "automation bias"; "diagnosis and clinical care"; "perform well-defined tasks with the necessary accuracy and reliability"; "meet ethical obligations and human rights standards"; release date 18 January 2024; publication link present.
- **Quote-accuracy correction (required):** the stored record and edge note render the disaggregation phrase as "disaggregated by user type (e.g., age, race, disability)". The release's actual wording is "published with outcomes disaggregated by **the type of user** (e.g., age, race, disability)". Meaning-preserving but presented as a quote — correct the quotation marks to the actual wording.
- **Scope correction (required, per supervisor's independent check):** the news release RECOMMENDS that governments introduce mandatory auditing for large-scale deployments; it does NOT establish that such a legal requirement is already in force anywhere. Both the record and the society/health→governance/postmarket edge must keep the recommendation attribution ("WHO recommends…") and must not be read as describing existing law. In-force post-market obligations for medical AI exist in other instruments (the library's eu-mdr-pms-2017 record covers the EU MDR regime) — any integration should keep these distinct.
- The "~98 pp" guidance length in the record's type field is search-derived, not read — mark UNKNOWN-from-material-read.
- Overall: supported as a recommendation with the two corrections above.

### 5. grace-ai-authors-2024 (Grace et al., Thousands of AI Authors, 2024)
- All five stored figures verified verbatim on abstract page 1: "2,778" (5 hits); "50% by 2047" with the 13-years-earlier comparison; "37.8% and 51.4%" ≥10% extinction-level outcomes; "68.3%" net optimists with 48% of them ≥5% to extinction; 2116 full-automation figure (3 hits).
- v2 date "30 Apr 2024" visible on the PDF first page — matches the record.
- Survey body/questionnaire unread, as stated. Author list spot-checked (Grace, Stewart, Sandkühler, Thomas, Weinstein-Raun…; Brauner is listed among co-authors — the record's shortened author string is consistent).
- Overall: fully supported; the forecasts-are-opinions caveat is present in the record and must be preserved.

### 6. crfm-foundation-models-report (Bommasani et al., 2021)
- All three stored passages verified verbatim in §1.1: "sociological inflection point around the introduction of BERT"; "unprecedented level of homogenization… adapted from one of a few foundation models"; the leverage/liability sentence including "inherit the same problematic biases of a few foundation models"; cross-modality list (text/images/speech/tabular/protein/molecules/RL) verified.
- 214 pages, 0 near-empty — extraction quality good; body unread as stated.
- Overall: fully supported as a partial read.

### 7. kapoor-normal-technology (Kapoor & Narayanan, Apr 2025)
- Live re-verification against knightcolumbia.org: 6 of 7 stored quotes FOUND verbatim ("We articulate a vision of artificial intelligence (AI) as normal technology"; "capability-reliability gap"; the exam construct-validity sentence; "AI safety is not a model property"; systemic risks "become far more important than the catastrophic ones"; "reducing uncertainty as a first-rate policy goal").
- **Quote-accuracy correction (required):** the stored edge/record quote "The correct analogy is nuclear power, not nuclear weapons" does not appear verbatim — the essay says the "right analogy is nuclear power". Correct the quotation.
- Truncation scope confirmed independently: the page cuts off mid-sentence inside Part IV ("So, c…"), so Part IV onward remains unread — matching the record's stated scope.
- No PDF link visible on the page — the record's access line already reflects an online read.
- Overall: supported with one quote correction and the truncation scope confirmed.

### 8. india-niti-responsible-ai (NITI Aayog, Feb 2021)
- Verified verbatim in the archived extraction: the six principles ("Principle of Safety and Reliability", "Principle of Equality", "Inclusivity and Non-discrimination", "Privacy and security", "Transparency", "Accountability"); constitutional grounding including "Constitutional morality"; acknowledgements naming WEF C4IR (Kay Firth Butterfield, Arunima Sarkar) and "Legal inputs enabled by Microsoft".
- Geography/date: India, February 2021 — correct. 64 pp, 8 near-empty pages.
- Body detail (per-principle discussion) unread, as stated.
- Overall: fully supported as a partial read.

### 9. japan-ai-guidelines-business (MIC/METI, Apr 2024)
- Live re-verification against the MIC (Soumu) English release: all five stored facts FOUND — "3947 opinions were submitted"; consultation window 20 Jan–19 Feb 2024; unified guidelines by merging/updating existing ones for "a wide range of AI business actors"; the AI Strategy Council's "Tentative Summary of AI Issues" compiled 26 May 2023 as trigger; title "AI Guidelines for Business (Ver. 1.0)". Release date 19 April 2024 confirmed.
- The METI English page returned HTTP 403 to the public fetcher (consistent with the record's access note); the guidelines PDF still returns HTML to direct fetch — NOT bypassed. The guidelines' action-item text remains unread (record states this).
- The record's mention of Ver. 1.1 (Mar 2025) is search-derived, not read — mark UNKNOWN-from-material-read.
- Overall: supported at press-release level, as stated.

## The two graph connections (v0.8)

### society/health → governance/postmarket (sourced)
- WHO passage: verified except the disaggregation wording (paraphrase issue above) and with the scope correction (WHO recommends; not an in-force requirement — keep "should introduce" framing, per supervisor check).
- AEGIS half: AEGIS was independently read in full on 2 Nov (Addendum 36) and verified as a proof-of-concept post-market governance mechanism for adaptive medical AI; the edge note's "proof-of-concept, per its authors, not a clinical evaluation" matches AEGIS's stated limitation verbatim.
- Direction check: health → postmarket ("health AI needs watching after deployment") matches both sources' content. SUPPORTED, with the two wording corrections to apply in the next sanctioned edit.

### politics/copyright → governance/rules (sourced)
- USCO passage: all four quotes verbatim (verified above). Direction ("copyright questions fit inside existing law") matches the executive summary's first bullet. No causal claim is made. SUPPORTED as stored.

## Corrections queue (for the next sanctioned edit of shared files; NOT applied in this audit)
1. who-lmm-guidance record + society/health→governance/postmarket edge: replace "disaggregated by user type" with the release's "disaggregated by the type of user", and add "WHO recommends; not established as an in-force requirement" scope wording.
2. kapoor-normal-technology record + any note quoting it: replace "The correct analogy is nuclear power, not nuclear weapons" with "the right analogy is nuclear power".
3. au-continental-ai-strategy record: mark the Aug-2024 adoption date as search-derived (not read from the PDF).
4. japan-ai-guidelines-business record: mark Ver. 1.1 (Mar 2025) as search-derived.
5. REPORT-5 Addendum 38 / handoff: correct the "Africa and Latin America gaps closed / zero coverage" claim (see gaps file).

## Overclaim correction — "Africa and Latin America gaps closed"
Addendum 38's batch rationale stated the library had zero regional coverage for Africa and Latin America. That was wrong in the strict sense. Prior Africa-related records already in the 363-record baseline include: otis-kenya-2023 (field study of GenAI impact on Kenyan entrepreneurs), copperbelt-air-2026 (Copperbelt pollution), plus Africa-relevant international-body records (ICANN/IGF footprints, GSMA WRC-23, ITU submarine-cable body, Access Now shutdowns, APC community networks, UNU e-waste). Prior Latin-America-related records include: souza-lithium-triangle-2025 (field-level lithium review), singh-aya-2024 (Aya multilingual dataset incl. African and Spanish languages), pew-global-2025 and edelman-flash-2025 (global surveys covering the regions). What was genuinely missing — and what Addendum 38 actually added — was CONTINENTAL/REGIONAL POLICY-LEVEL sources (the AU strategy; the ECLAC index). The corrected statement: "the library lacked continental/regional policy and index sources for Africa and Latin America; field-level and country-level records already existed." Remaining genuine regional gaps after the additions: field-level African AI-labour and infrastructure studies beyond the existing records, Latin American country-level adoption/evaluation studies, and any Africa- or LatAm-authored evaluation research (the library's health and evaluation records remain predominantly North American, European and East-Asian).
