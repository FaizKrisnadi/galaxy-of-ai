# Milestone report — Galaxy of AI, first constellation

**Date:** 1 November 2026 · **Status:** bounded milestone complete, stopping here for independent supervisor review. Nothing has been published, shared or uploaded; no one was contacted; nothing was spent; no other project was touched.

---

## 1. What was delivered

| File | What it is |
|---|---|
| [START-HERE.md](START-HERE.md) | **Pre-existing — untouched.** The project's starting outline. |
| [CONTEXT.md](CONTEXT.md) | **Pre-existing — untouched.** Vision, known findings, mistakes to avoid. |
| [PRE-STUDY.md](PRE-STUDY.md) | New. Direct inspection notes on every comparable tool and source: function, scope, method, stated limitations, access & reuse terms, with exact links and quotes. |
| [constellation.html](constellation.html) | New. The first constellation: one self-contained HTML file. Open it in any browser — double-click or `File → Open`. No framework, no build step, no accounts, no paid APIs, no external assets; the page itself loads nothing from the internet. |

## 2. What the prototype does

- **AI at the centre**, with 8 surrounding nodes: Data & compute, Data centres, Electricity, Water/land & neighbours, Economics, Jobs & AI exposure, Governance, Human oversight.
- **13 labelled connections in three honest types**, shown in the legend and on every line:
  - **topic link** — "these subjects are related", never "this causes that" (10 edges);
  - **fact (sourced)** — something documented, with the source one click away (3 edges: data centres sized in megawatts; documented 2026 oversight incidents; Census findings on AI-exposed graduates);
  - **open question** — genuinely unsettled (2 edges: how much electricity AI uses worldwide; local data-centre effects case by case).
- **Click any node** → a short plain-English explanation (2–4 sentences), a "Handle with care" box stating the limitations in the source's own terms, its connections with type badges, and source links.
- **Three path buttons** re-trace the three exploration paths from START-HERE.md; "Show everything" resets.
- The map scales to fit the window; all nodes stay visible without scrolling.

## 3. Pre-study: what was directly inspected (all on 1 Nov 2026)

Every entry records function, scope, method, stated limitations, access & reuse, with quotes — see [PRE-STUDY.md](PRE-STUDY.md) for details.

- **MIT AI Governance Map** — 1,000+ governance documents, LLM-classified, US-skewed, snapshot 23 Mar 2026; data CC BY 4.0.
- **OECD AI Policy Navigator** — policy initiatives across 80+ jurisdictions; methodology not described on the dashboard page; **licence could not be verified** (terms page 404) — flagged, not assumed.
- **OpenAlex Topics** — 4,516 machine-assigned scholarly topics; predictions, calibrated scores; ~10% of works unclassified; open code/labels.
- **ArusGrid** — independent SEA/Gulf/India data-centre project tracker; evidence tiers, dated sources, banned aggregator reports; admits systematic MW undercounting; CC BY-NC 4.0.
- **Epoch AI Data Centers** — global AI-optimised data-centre database built partly from satellite imagery and permits; estimates ~46% (30–78% CI) coverage of global AI compute; no reuse terms stated on the page.
- **Katadata (Batam)** — 18 data centres planned/building on a rain-fed-reservoir island; flagship could use ~3m litres/day; by 2032 ten facilities ≈ 8% of current supply; the report itself does **not** claim a specific facility caused household shortages (2024 crisis blamed on a pipe leak).
- **ISEAS Perspective 2025/43 (Sara Loo)** — Malaysia: projected >5,000 MW data-centre demand by 2035 (~40% of Peninsular capacity); 5.9 GW secured maximum demand called "hazardously high"; single-author commentary, views not the institute's.
- **ISIS Malaysia "AI and Climate Considerations"** — GPU racks 60 kW+ vs 5–10 kW traditional; water requests ~808m L/day vs ~142m L/day realistically supplyable; source data "deliberately opaque"; some interview findings cannot be corroborated.
- **Open Knowledge Maps** — visual literature clustering via BASE; CC BY 4.0, open source, no accounts.
- **Not inspectable this session, recorded as such:** Connected Papers (fetch declined by the user); the two prior literature-map leads on ScienceDirect (Elsevier sign-in redirect) and MDPI (HTTP 403) — only abstract-level descriptions exist from earlier checks; **no content from them is used anywhere**.

## 4. What is new vs. already known (per CONTEXT.md)

- **Already known, now verified with direct inspection:** all eight tools/sources above; the two unreadable leads re-confirmed as unreadable.
- **New in this milestone:** (a) the pre-study comparison table with access/reuse terms in one place; (b) the first constellation itself — the *joined-up, labelled* view across these domains for one learner; (c) working local prototype, tested.
- **Explicitly not claimed:** no novelty for the galaxy idea, no gap claims, no PhD thesis, no causal claims, no claim that any specific query ran at any specific facility, no exhaustive literature synthesis.

## 5. Testing — what actually works

Automated browser checks (Playwright + Chrome for Testing, headless): **19/19 passed, zero console errors.**

- Renders 9 nodes and 13 edges; hub is AI; map fits the visible area with no node outside the frame.
- Every one of the 9 nodes opens a panel with the right heading, ≥1 source link, a care box and its connections.
- Selection highlighting dims non-neighbours correctly (checked on "Data centres").
- All three path buttons highlight their chains; reset restores the default view.
- All external links carry `rel="noopener"`; page loads no external resources (works offline; links open only when clicked).

Fixes made during testing: canvas now scales to the window (was cut off on the right); "rules demand checkers" label moved off the Human oversight node; IEA link added to the default panel's open-questions list.

## 6. Limitations (honest list)

1. **Small by design.** 9 nodes / 13 edges is a sketch, not a map of the field. START-HERE.md areas like politics, law, environment and institutions exist here only inside other nodes' text.
2. **Hand-authored layout.** Node positions and edges were chosen by me, not derived from data. Different reasonable arrangements exist.
3. **Summaries, not full-text studies.** Node text summarises the linked sources (verified this session or in the 31 Oct handoff pass). I have not read the full Census, IMF or ISEAS PDFs, and the METR/OpenAI items are summarised from their public write-ups as characterised in the handoff. Check originals before relying on any specific figure.
4. **Dated numbers.** Sources carry their own dates (ISEAS Jun 2025, ISIS Jun 2026, Census Sep 2026, METR describing a pre-21 Jul 2026 system). Figures will age; each panel says what its source is and when.
5. **Reuse terms partly unverified.** OECD licence page unreachable; Epoch AI page states no terms; Connected Papers and the two literature-map leads unreadable. Nothing has been redistributed, so nothing hinges on this yet — but check before any reuse beyond linking.
6. **Known readability nits left as-is:** edge labels are small at typical window sizes (browser zoom works); on very narrow screens the panel stacks below the map.
7. **No persistence or editing UI.** There is no way to add nodes in the browser — changes are made by editing the file. That is deliberate for a first sketch.

## 7. Suggested next steps (for the supervisor to choose from — nothing started)

1. Review the constellation's *content* (wording, node choice, whether the fact/unknown labels sit right) before any more nodes are added.
2. Add the politics/law and environment branches, reusing the ISEAS/ISIS material already inspected.
3. If wanted later: a second constellation for one real project case (e.g., a Batam facility) — only with newly verified sources, keeping "no facility-level claims without evidence".

**Stopping here for independent review, as instructed.**
