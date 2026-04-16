# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A static HTML guide for modding **The Sims Legacy Collection** (2025), deployed from the repo root via GitHub Pages (Jekyll). There is **no build step, no framework, no package manager, no tests**. Every page is a standalone `.html` file that links to one shared `style.css`.

Live site: https://cyndersanity.github.io/sims-legacy-mod-guide/

## Commands

```bash
# Preview locally (relative paths work; opening files directly also works)
python -m http.server 8000

# Sync footer across every page after changing FOOTER_LINKS
python nav_builder.py --all

# Update a single page or list of pages
python nav_builder.py <file.html>
python nav_builder.py --pages a.html b.html
```

`nav_builder.py` currently **only rewrites the `<footer>` block**. The nav bar is inline JS-driven dropdowns rendered per-page — the script does not regenerate it despite the `PAGES` dict still being defined. When adding a new page or renaming a nav entry, copy the `<nav>…</nav>` block from a sibling page and edit by hand, then run `nav_builder.py --all` to sync footers.

## Architecture

### Page anatomy (every `.html` in the root follows this)

1. `<head>`: Google Fonts preconnect, `<link rel="stylesheet" href="style.css">`, a page-local `<style>` block for anything not in the shared stylesheet, and the Google Analytics snippet (ID `G-8ZDF0Q80RR`) inlined in every page.
2. `<nav>`: full dropdown bar + mobile drawer, duplicated inline on each page. Adding/renaming a nav link means editing every HTML file (or copying from a freshly-edited sibling).
3. Page content using the shared component patterns below.
4. `<footer>`: managed by `nav_builder.py` — do not hand-edit unless you intend to diverge.

### Shared CSS system (`style.css`)

All colour, spacing, radius, shadow, and font tokens are CSS variables in `:root` (e.g. `--green-dark`, `--cream`, `--font-head`). Prefer the variables over hex literals so palette changes stay one-line. Page-local `<style>` blocks should only define page-specific layout, not redefine tokens.

### Shared components (use these; don't invent new ones)

- **Callouts**: `<div class="callout teal|gold|red|green">…</div>` for info / warn / critical / tip
- **Steps**: `<div class="steps"><div class="step"><div class="step-num"></div><div class="step-body">…</div></div></div>` — `step-num` is auto-numbered via CSS counters
- **Accordion cards**: `.ref-card` + `.ref-head` (with inline `onclick` toggle) + `.ref-body`; one `<button class="expand-all" onclick="toggleAll(this)">` per section to expand/collapse just that section's cards
- **Tables**: always wrap in `<div class="table-wrap">…</div>` for horizontal overflow on mobile
- **File paths**: wrap in `<code>` (e.g. `<code>\\Downloads\\</code>`)
- **Example prefixes**: always `<strong>Example:</strong>`

The canonical component reference with live demos, colour swatches, and copy-pasteable markup is `_dev/style_guide_v6.html` — open it in a browser and copy from it rather than guessing. Jekyll excludes `_dev/` from the published site because of the underscore prefix.

### Page groupings

Hub pages link out to their sub-pages:

- `making-cc.html` → `making-clothing.html` (→ `clothing-retextures.html`, `clothing-meshes.html`) and `making-heads.html` (→ `head-retextures.html`, `head-creation.html`)
- `making-objects.html` → `object-retextures.html`, `object-creation.html`
- `iff-hacking.html` → `iff-simple-edits.html`, `iff-advanced.html`

When adding content, decide first whether it belongs on the hub or a sub-page; the hubs are intentionally kept as overviews (concepts + links out), not deep tutorials.

### Routing / deployment quirks

- GitHub Pages serves from the repo root on `main`. There is no `.nojekyll`, so Jekyll runs. Any folder or file starting with `_` is excluded (that's why `_dev/` works as a dev-only area).
- `sitemap.xml` and `robots.txt` are hand-maintained — add new pages to `sitemap.xml` when you create them.
- `search.html` does full-text client-side search; it has its own fetch/index logic embedded inline.

## Content rules (from README)

- **Accuracy first** — every claim should trace to Maxis docs, a named tool's docs, or verified community testing. Don't invent tool behaviour.
- **Beginner-friendly** — explain *why*, not just *what*.
- **Do not change without discussion**: career list and transfer loop data, the skin-prefix table, tool capability descriptions (e.g. TMog handles sprites; IFF Pencil does not). These are cross-referenced against multiple sources and casual edits tend to reintroduce long-standing misconceptions.

## Conventions worth knowing

- British English spelling throughout (`customise`, `colour`, `behaviour`).
- Emoji prefixes on nav links and section headings are part of the visual system — match existing usage rather than dropping or swapping them.
- When wiring a new interactive toggle, prefer the existing `toggleAll` / accordion pattern over adding a new one; all interactivity is inline `onclick` or small `<script>` blocks at the end of `<body>` — there is no module system.
