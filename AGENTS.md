# AGENTS.md

Guidance for agents working in this repository.

## Project

- Course: Tècniques d'informació geogràfica i turística.
- Acronym: TIGIT.
- Official URV course code: `21224102`.
- Degree: Grau en Gestió en Turisme i Hoteleria.
- Profile: `unaltremanual`.
- Default language: Catalan (`ca`).

## Collaboration Workflow

- Read `.github/CONTRIBUTING.md` before creating a branch or editing files.
- Before editing locally, run the MCP control plane's read-only checkout preflight in the primary mutable checkout. Keep one active editing session per repository and use its `exec` wrapper when a process-held cooperative lease is required.
- For MCP-backed work, request `unaltraweb` as the one top-level MCP and let the control plane select its declared dependency closure. Pass the consumer root through `MCP_CONSUMER_WORKSPACE`.
- Never create, switch to, move, prune, repair, or remove linked worktrees as part of an editing session.
- Inspect `site_context`, `site_doctor`, the language policy, the active profile, and `manual_authoring_capabilities` before editing manual content.

## Editorial Workflow

- Draft and revise the Catalan source first.
- Read `context/writing-profile.md` before drafting or substantially revising chapters.
- Use `content_status: draft`, `review`, or `approved` in meaningful manual pages and chapters.
- Do not create or update Spanish/English translations while Catalan content is still changing.
- Run the unaltraweb MCP `translation_plan` before publication; translate only approved Catalan sources.
- Keep Moodle-specific dates, deadlines and grading operations out of the manual unless the user explicitly asks to publish a stable policy.
- Before any content commit or publication, serve the site locally and wait for the human author to review it in a browser and explicitly approve the rendered result.

## Course Manual Shape

- The manual is the shared document for students and all teachers.
- Integrate theory and practice in the same flow: data, Excel, visual semiology, cartography, QGIS, Inkscape and final synthesis.
- Write chapters so a theory teacher and a lab teacher can both see their responsibilities.
- Prefer narrative, explanatory sections over executive-summary bullets. Use lists only when they genuinely help with instructions, criteria, or inventories.
- Chapter 0 is the orientation chapter: move general explanations about how the manual works, how Moodle relates to the course, and how theory/practice are integrated into that chapter rather than overloading the cover page.
- Prefer phase-based structure over week-based structure. Moodle owns the calendar.
- Mark assessment material as draft until the user confirms it is ready for the official teaching guide.

## Figure Backgrounds And Pending Zoom Review

- Historical decision, 2026-09-24: defer individual fixes until shared opacity support was available. On 2026-10-26 the author accepted the exact first figure batch in TIGIT #23, including white opaque backgrounds; this supersedes the deferral for that batch. The scaffold update remains deferred by explicit author decision.
- `unaltraweb` MCP 0.7.3 `image_background_check` has now been exercised successfully. It warns about alpha and unverifiable images; it does not automatically repair figures or require white in every context.
- The audit covered 230 versioned SVG/PNG assets, including 190 figures referenced by the manual: 133 were opaque, 44 SVGs had substantial transparent areas, and 13 figures had only peripheral transparency, shadows, or minor antialiasing. Alpha alone is not a readability defect.
- The earlier zoom reproduced readability problems for the KDD and PlantUML folder tree: its translucent overlay and cloned image could lose ancestor-dependent background styles. Backgrounds must belong to the image itself.
- The first batch adds a full-viewBox KDD background, regenerates the donut and word cloud from their QMD sources, and uses author-owned `.edited.svg` backgrounds for the timeline, Gantt and folder tree. Native diagram originals remain byte-identical. See `context/figure-plan.md` for checks and provenance.
- [x] Agent review of the first batch: 21 browser zoom checks across light, dark and cafe, desktop/mobile inspection and selected PDF pages. The word cloud and companion bars retain bounded-raster alpha only in the outer one-pixel band (0.1445% of each sample); their interiors are opaque and the zoom backgrounds remain white.
- [x] Author browser/PDF approval of the revised chapter and first figure batch received on 2026-11-10: «Aprovo i integra». The author authorized the focused content commit/PR and integration; see TIGIT #23 and `context/figure-plan.md`. The chapter remains `draft`.
- [x] The follow-up in TIGIT #35 covers 44 figures with interior transparency, including palettes, UTM and eye/retina. It adds paper and viewport backgrounds to 39 SVG sources, reconciles/regenerates the palette source, and preserves four PNG originals inside self-contained opaque SVG variants. Internal layer transparency and original diagram geometry are preserved.
- [x] Agent review of #35: 44 fully opaque Chromium samples, 132 light/dark/cafe zoom probes with identical pixels over magenta/green underlays, seven mobile chapter checks and selected PDF pages. See `context/figure-plan.md` for source/runtime checks and provenance.
- [x] Author browser/PDF approval of #35 received on 2026-11-11: «Aprovo i integra», after confirming a single asset and fixed background per figure across all themes. The author authorized commit, PR, integration and branch cleanup. The rendered Catalan content remains `draft`.
- Use authoritative sources for generated outputs; preserve meaningful internal transparency such as the layers in `assets/img/gis/gis-layer-overlay.svg`. Preserve original diagrams and the provenance of author-owned edited variants. Do not change the shared renderer inside this consumer.

## Build Checks

After structural content edits, run:

```bash
make build
```

Before committing visible content edits, run a browser preview:

```bash
make serve
```

Run the MCP `site_check` before `build_site`. Use `profile_check` and `translation_plan` before publication; keep factory `build`, `check`, and `smoke` operations in the factory checkout.
