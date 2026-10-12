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

## Pending Follow-up: Figure Transparency

- Author decision, 2026-09-24: defer individual figure fixes until the planned `unaltraweb` solution arrives through the scaffold and the MCP warns when adding figures with alpha transparency. Treat this as pending integration, not an already available capability.
- The audit covered 230 versioned SVG/PNG assets, including 190 figures referenced by the manual: 133 were opaque, 44 SVGs had substantial transparent areas, and 13 figures had only peripheral transparency, shadows, or minor antialiasing. Alpha alone is not a readability defect.
- The current zoom uses a translucent overlay and clones the image outside its figure container, so ancestor-dependent background styles can be lost. This was reproduced in the browser for the KDD and the PlantUML folder tree.
- [ ] After integrating the provider update, verify the scaffold changes and MCP alpha warnings, then review zoom readability in light, dark, and cafe themes. Start with `assets/img/data-sources/kdd-dikw-cycle.svg` and `assets/diagrams/reproducible-project-structure.puml.svg`.
- [ ] Also check `assets/img/data-visualization/housing-donut-tarragones-2021.svg`, `assets/img/data-visualization/word-cloud-accommodation-names-vila-seca.svg`, `assets/img/color-cartography/palette-reference-swatches.svg`, the UTM diagrams, and the eye/retina figures.
- [ ] Only if the shared solution is insufficient, revisit the affected figures individually. Use their authoritative sources for generated outputs; preserve meaningful internal transparency such as the layers in `assets/img/gis/gis-layer-overlay.svg`.
- If individual fixes become necessary: the KDD needs a background covering its nonzero `viewBox` (`40 106 1390 798`); the donut and word-cloud R sources can export with `ggsave(bg = "white")`. The palette-swatches Quarto source already declares a white background, but the current cropped SVG lacks it, so reconcile source and output before regenerating.

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
