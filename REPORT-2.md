# Milestone 2 report — Galaxy of AI v0.2

**Date:** 1 November 2026 · **Status:** milestone complete, stopping for supervisor review. No deployment, no paid services, no contact, no changes to other projects.

## What was built

**[galaxy.html](galaxy.html)** — a two-level explorable galaxy, one self-contained file (no framework, no accounts, nothing loaded from the internet):

- **Overview (uncluttered):** glowing AI sun + 7 planets on faint orbits with a starfield. No lines between planets, no visible labels beyond names and taglines.
  - How AI works · Physical infrastructure · Economics · People & society · Governance · Politics & law · Environment
- **Planet view:** click a planet → it becomes the centre with its topics around it. Back via the "← Galaxy" crumb, **Esc**, or the browser flow (focus returns to the planet you came from).
- **Topic cards:** click a topic → a panel with 2–4 plain-English sentences, one italic "Still unknown" line where honest, linked sources, and "Reaches into" cross-links that jump between worlds (e.g. Data centres → Economics·Investment; Jobs → Society·Public attitudes).
- **Minimal labelling:** one legend line — solid link = described by a linked source; dotted = a link worth exploring, not evidence. Heavy v0.1 warning boxes are gone; caveats live inside the prose.
- **28 topics across 7 worlds**, all sourced from material already verified in PRE-STUDY.md, the 31 Oct handoff pass, or inspected directly this session. No new searches were run.
- **Easy to extend:** all content sits in one `GALAXY` data object at the top of the script — adding a topic or world is adding an object.

## Corrections carried out (as directed)

1. **Water/cooling:** v0.1 implied all data centres need water. v0.2 says plainly: *not every data centre drinks water — some cool with air, others with water or hybrid designs; it depends on the cooling system, climate and site.* The sourced figures (Johor ~808m L/day requested vs ~142m supplyable, ISIS; Batam flagship ~3m L/day, Katadata) are presented as "where water is used".
2. **Census study:** verified directly at census.gov this session. v0.2 follows the abstract precisely: most AI-exposed **decile** of college majors; likelihood of **initial employment** −5 percentage points; **full-quarter initial earnings** −13%; effects attenuate with distance from entry but stay substantial. Explicitly framed: exposure ≠ job loss; a documented correlation, not proven cause.
3. **Proposed vs sourced:** dotted cross-links (3: data→participation, exposure→attitudes, preferences→national rules) are marked "worth exploring — not evidence"; all other links trace to a listed source.

## Evidence of testing (Playwright + Chrome for Testing)

**26/26 checks pass, zero console/page errors.**

- **Structure:** 1 sun + 7 planets + 3 orbit rings + 110 stars; every planet inside the visible area (no scrolling); 28/28 topic cards open with ≥1 https source, `rel=noopener` throughout.
- **Interaction:** world open/close, card open/close, cross-world jump switches the background world and clears the old world's spoke lines (a real bug found by screenshot and fixed).
- **Keyboard:** first Tab lands on the sun; Enter opens cards/worlds; Esc steps back down (card → world → overview); focus moves to the opened heading and returns to the triggering node; core button focused when a world opens.
- **Small screen (390×844):** list mode with large touch rows; 0 px horizontal overflow; card becomes a bottom sheet inside the viewport.
- **Visual inspection:** overview, world+card, and both mobile screenshots reviewed — galaxy feel, readable text, uncluttered.

Bugs found by testing and fixed: nodes missing coordinates (piled unpositioned, core intercepted clicks); leftover spoke lines when jumping between worlds; screenshot-order artefacts in the test itself (not page bugs).

## Preserved / changed files

- `constellation-v0.1.html` — v0.1 prototype, **renamed and preserved** (was `constellation.html`).
- `REPORT.md` (milestone 1), `START-HERE.md`, `CONTEXT.md`, `PRE-STUDY.md` — **untouched**.
- New: `galaxy.html`, this report.

## Actual limits

1. **Hand-made content, not a literature synthesis.** 7 worlds / 28 topics were chosen by me as a beginner's starting set; the politics/law and society worlds are meaningful but deliberately thin starting points.
2. **Summaries of sources.** Explanations summarise the linked pages (inspected directly) or the handoff's verified descriptions (Census now verified at source; IMF, Geith, Kim, Hoch & Mügge, SemiAnalysis, Lundgren & Tallberg, Culot, Ustenko, Linux Foundation, Anthropic, Chincholikar & Chawla are summarised from the handoff's 31 Oct verification pass — originals not opened this session). Figures can age; each card names its source.
3. **Two known readability trade-offs:** when a card is open it covers the right side of the map on desktop (close or Esc to continue — standard side-panel behaviour); edge "Still unknown" lines are one-sentence simplifications of genuinely complex debates.
4. **Static positions.** Planet and topic layouts are fixed coordinates scaled to the window; there is no physics, drag or zoom — deliberate, to stay simple.
5. **Reuse terms unchanged from PRE-STUDY.md** (OECD licence still unverified; Epoch terms not stated on its page) — nothing is redistributed, so nothing hinges on it yet.

**Next-step suggestions (not started):** review wording of the 28 topics; then, if approved, a third branch level only where a real question needs it.
