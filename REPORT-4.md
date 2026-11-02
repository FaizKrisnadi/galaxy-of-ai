# Milestone 3 report — deepened, connected, in-canvas galaxy

**Date:** 1 November 2026 · **Status:** complete, stopping for review. No publishing, no spending, no outreach, no other projects touched.

## Version links (all local files)

| File | What it is |
|---|---|
| [galaxy.html](galaxy.html) | **Current version** — one canvas: planets orbit the sun; clicking a planet expands its topics **in place**, with connection lines; everything else stays as dimmed context. |
| [galaxy-scenes.html](galaxy-scenes.html) | **Preserved snapshot** of the previous working version (separate planet scenes), byte-identical to the pre-rework file (SHA verified). Linked from the legend ("classic separate-scene view"). |
| [constellation.html](constellation.html) | Pointer page → current galaxy (HTTP-verified 200 + redirect in the previous pass). |
| [constellation-v0.1.html](constellation-v0.1.html) | The original nine-node prototype, preserved. |
| [galaxy.html](galaxy.html) content basis | CONTEXT.md + PRE-STUDY.md + the 31 Oct handoff; no discovery was redone. |

## 1. Deepening (Faiz's four paths) — now 34 topics

- **AI basics → using AI:** added **Agents & doing tasks** (agents act in sequences and need monitoring machinery — METR red-team + OpenAI incident, both previously verified) and **Using AI in organisations** (adaptation with human review — Turobov & Coyle's 63-UN-document study; OECD WP 93's 14-country review).
- **Infrastructure → electricity, water, investment:** added **Grids & critical infrastructure** (Pursiainen et al.: path-dependent, uneven adaptation of EU critical-infrastructure governance).
- **Economics → evidence and limits:** added **Reading the evidence** — a beginner's methods card (records vs self-reports, correlation vs causation, working paper ≠ settled result), explicitly tied back to the Census, IMF and Linux Foundation items it discusses.
- **Governance → institutions to oversight:** added **Watching AI after deployment** (AEGIS post-market monitoring demonstration, limits stated) and **Officials & discretion** (Anastasopoulos's normative argument, labelled as argument not measurement).
- **Enriched existing cards:** Human oversight gained METR's viewer-tampering demonstration (with observed-vs-proof-of-concept distinction); Public attitudes gained Flanders & Nungsari's WVS Wave 8 finding (40,960 respondents, tech-optimism anchor, cross-sectional caveat); Skills & verification gained the Indonesian civil-servant dataset labelled "dataset, not findings" (Southeast Asia interest).
- Within-world chains added and drawn: models→data→inference→agents/evaluation; centres→electricity→grids, centres→water, land→centres; evidence↔jobs/productivity; rules→standards, procurement→post-market→oversight, discretion→oversight.

## 2. Source audit (concrete additions, checks, access limits)

**Verified at origin this session:** Turobov & Coyle (CC BY, open access), METR 6 Oct post, Flanders & Nungsari (arXiv), Ginting dataset (CC BY, survey record read). **DOI resolves, abstract bot-gated, statements follow the 31 Oct verified handoff:** Pursiainen (Springer), AEGIS (Nature), Anastasopoulos (Wiley 403). **Dropped rather than weakly sourced:** Baum (APSA) — the handoff's link is now HTTP 404 and no precise replacement URL could be verified, so state-official perceptions are omitted. All card statements were written against these verified descriptions; no numbers or findings were added beyond them. Full record in PRE-STUDY.md §6c–6d.

## 3. In-canvas expansion (the new interaction, built on the same content)

- Click a planet → it pins, its topics fan out around it **inside the same canvas** (pulled toward the sun and clamped so nothing leaves the canvas), with spokes, within-world topic lines (solid = sourced, dotted = proposed), and the **other six planets dimmed but still on their orbits as context**.
- Click a topic → card + **connections made visible**: connected topics glow (including back-links), others soften, and **cross-world lines are drawn from the topic to the target planets** — Faiz's "galaxy of connected knowledge, not just topic cards".
- Follow a "Reaches into" link (or click a dimmed planet) → the new world expands in the same canvas. Collapse via the planet, the "← Collapse" chip, or Esc; the galaxy resumes orbiting.
- The sun, planets, orbiting motion, reduced-motion behaviour, keyboard flow and mobile list mode are preserved. Inter-planet arcs hide while a world is focused (they would only add clutter there).

## 4. Verification (Playwright + Chrome for Testing — **36/36, zero page errors**)

Faiz's requested flow, executed in a real browser: **expand infrastructure** (6 topics in-canvas, 6 spokes + 5 topic lines, other planets dimmed, arcs hidden) → **inspect data-centre connections** (card with 3 sources + 6 cross-links; 4 connected topics lit; **cross-world lines to Economics/Environment/Politics planets drawn**) → **follow into economics** (switches expansion in place, card = Investment) → **collapse** (canvas restored, arcs back, focus returned) → **open sources** (https + noopener verified on deepened cards) → **resizing** (expanded layout refits 1512→1280 with all topics inside the canvas; 1280×739 and 1512×860 planet audits pass; narrow→wide regression: **planets never stack**). Also verified: Esc card→collapse ordering, keyboard (Tab sun → planets → topics → cards), mobile 390px (6 stacked topic rows, bottom-sheet card, collapse button), and that galaxy-scenes.html still opens its infrastructure scene with all 6 topics. Screenshots inspected at each step.

**Bugs caught and fixed during the pass:** a corrupted edit (section-comment anchors matched CSS comments, injecting the engine into the stylesheet) — recovered from the snapshot and redone with unique anchors; three stale test expectations corrected by computing them from the data.

## 5. Remaining gaps and limits

1. **Three abstracts not re-read** (Springer/Nature/Wiley gates) — those three cards rest on the 31 Oct handoff pass; flagged in PRE-STUDY.md.
2. **Baum (state-official perceptions) omitted** — dead link, no verifiable replacement.
3. **Expanded topics can slightly overlap dimmed context planets** at some orbit positions — intentional hierarchy (topics bright, context at 25% opacity), not yet geometry-avoided.
4. **The focused planet's orbit is paused** while expanded (its neighbours too) — motion resumes on collapse; this is what keeps the expanded graph readable and non-drifting.
5. **34 topics is still a curated sketch**, not a literature synthesis; politics/law and society remain thinner than the four deepened paths.
6. **Single engine testing** (Chromium); in-app webviews here are Chromium-based.
7. The overview's 14 inter-planet arcs are tooltips-only (no click); they duplicate information visible when expanding — kept faint by design.

Stopping here for supervisor review.
