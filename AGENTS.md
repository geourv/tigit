# AGENTS.md

Guidance for agents working in this repository.

## Project

- Course: Tècniques d'informació geogràfica i turística.
- Acronym: TIGIT.
- Official URV course code: `21224102`.
- Degree: Grau en Gestió en Turisme i Hoteleria.
- Profile: `unaltremanual`.
- Default language: Catalan (`ca`).

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

## Build Checks

After structural content edits, run:

```bash
make build
```

Before committing visible content edits, run a browser preview:

```bash
make serve SITE_PROFILE=unaltremanual
```

Useful MCP checks from the `unaltraweb` factory:

```bash
make -C ../unaltraweb mcp-profile-check PROJECT=$PWD
make -C ../unaltraweb mcp-translation-plan PROJECT=$PWD
```
