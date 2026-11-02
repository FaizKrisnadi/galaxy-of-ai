# Milestone 2 repair report — supervisor-directed fixes

**Date:** 1 November 2026 · **Status:** repair pass complete, stopping for review. No publishing, no spending, no contact, no edits outside this project.

## 1. Urgent fix: planets stacking top-left at ~1280×739

**Root cause (found, not guessed):** `relayout()` had two cooperating defects. (a) In list/narrow mode it wrote `left:0;top:0` onto the planet buttons, and the wide branch never restored real coordinates — so any single narrow measurement (e.g. an in-app panel whose width changes without firing `window.resize`) left all planets stacked at the top-left forever. (b) Container resizes in embedded webviews often fire no `resize` event at all, so nothing re-ran.

**Fixes in galaxy.html:**
- Planet positions are now **derived from orbit data on every layout pass** (`applyPositions`); no stale coordinates can persist.
- Added a **ResizeObserver** on the map container plus `orientationchange`, alongside the existing `resize` listener.
- List mode clears inline transforms and never writes them back (a second bug my first fix introduced was caught by the re-run tests: the "park the planet" branch re-applied transforms in list mode and broke the mobile rows — fixed and re-tested).

## 2. Planets now visibly orbit the sun

- Each planet sits on its drawn ellipse (ring + angle in data) and **drifts slowly along it** — one lap ≈ 2.7 minutes (~10–15 px per 1.5 s at 1280×739: visible but calm). All planets share one angular speed, so their spacing never changes.
- **Reduced motion:** with `prefers-reduced-motion: reduce`, planets are static (verified 0.0 px movement); preference changes are honoured live.
- Labels stay readable and clickable while moving (click + keyboard verified); mobile list mode remains static rows.

## 3. Real rendered checks (not just in-bounds tests)

Playwright + Chrome for Testing, **21/21 pass, zero page/console errors**:

- **1280×739 (Faiz's size):** 7 planets, spread 675 px, min centre distance 135 px, **pairwise bounding-box overlaps: none**; every planet sits on its drawn orbit (worst deviation 0.000 of ring radius); drift verified (10.7 px/1.5 s); re-audited after drift (min distance 138 px, no overlaps). Screenshot inspected: whole galaxy visible, labels complete.
- **Narrow→wide without reload** (the exact stacking scenario): still 7 distinct planets, no overlaps.
- **1512×860:** same audit passes (min distance 164 px); screenshot inspected.
- **390×844 mobile:** list mode, 0 px horizontal overflow, 7 distinct rows in order; screenshot inspected.
- **Height-aware scaling added:** short desktop windows now scale the galaxy to fit both dimensions, so no label clips at the bottom edge (found on the 1280×739 screenshot and fixed).
- **Interaction with moving planets:** click and keyboard (Tab→sun, Enter, Esc) verified; world/topic/card flows unchanged.
- Earlier suite semantics still covered: all 28 topic cards, cross-world jumps, spoke cleanup, sources https + `noopener`.

## 4. Other supervisor-directed fixes (from the prior review, completed)

1. **`constellation.html` restored** — it now leads to the current galaxy (instant redirect + visible links), with **`constellation-v0.1.html` preserved unchanged**. Verified over HTTP: all three files return **200** (`python3 -m http.server`), and a real browser navigation of `http://127.0.0.1:8799/constellation.html` lands on `galaxy.html`.
2. **Data-centre card corrected:** states many centres house ordinary cloud/web services while a subset is built for AI; IT load in MW is explained as **rated power demand, "a measure of demand, not of electricity consumed over time"**; cooling described as air/water/hybrid depending on system, climate and site. Card text asserted in automated checks.
3. **Central explanations audited against their cited sources:** the basic-AI cards (AI, Models & training, Data) had wrongly cited OpenAlex Topics / OECD Navigator, which do not explain how models work. They now cite IBM's verified plain-language explainer explicitly labelled **"Further reading"**; the inference card's IEA link and the evaluation card's Huang et al. preprint are likewise relabelled as further reading / an example. No conceptual link is presented as established merely because two topics co-occur in a source. The IBM page was fetched and verified this session and is recorded in PRE-STUDY.md §6b with its limitations (vendor page, introductory).
4. **Footer removed:** the user-facing HTML/framework/version footer is gone; only the one-line legend remains.
5. **Navigation/language unchanged and re-verified** (keyboard + mobile checks above).

## 5. Files

- `galaxy.html` — repaired (layout engine, orbits, card corrections, further-reading labels, footer removed).
- `constellation.html` — restored as a small pointer page to the current galaxy.
- `constellation-v0.1.html`, `START-HERE.md`, `CONTEXT.md`, `REPORT.md`, `REPORT-2.md` — untouched.
- `PRE-STUDY.md` — one section added (§6b, IBM explainer record).
- New: this report.

## 6. Limits of this pass

- Orbital motion is uniform and circular-parameterised on the drawn ellipses — decorative calm, not a simulation.
- The 160 s period is a chosen aesthetic value.
- Verified in Chromium (in-app webviews are also Chromium-based here); other engines untested.
- The redirect page requires the file to sit next to `galaxy.html` (relative link), which is how the project is laid out.

Stopping here for supervisor review.
