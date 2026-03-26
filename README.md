# The Sims 1 Legacy Collection — Modding Guide

A community-maintained guide for modding and customising **The Sims Legacy Collection** (2025 re-release). Covers everything from installing your first mod to creating custom content from scratch.

🌐 **Live site: [cyndersanity.github.io/sims-legacy-mod-guide](https://cyndersanity.github.io/sims-legacy-mod-guide/)**

---

## What's in the guide

- **About the Legacy Collection** — what changed from the original, patch history, technical differences, in-game settings reference
- **What's Possible** — engine limits, confirmed working features, resolution & graphics explained
- **Installing Mods** — folder paths for Steam and EA App, file type reference, CC limits, importing lots and families
- **Download Sites** — active mod sites confirmed working in 2026, archive resources, Simblr tutorials
- **Must-Have Mods** — QoL hacks, bug fixes, objects, debug tools, careers, pets
- **Cheat Codes** — every working cheat including FaithBeam debug unlocks
- **Creating CC** — custom skins, clothing, body types, walls, floors, TSO conversions
- **IFF Hacking** — building gameplay mods and object hacks from scratch
- **Modding Tools** — every tool you need with download links
- **CC & Game Troubleshooting** — common issues with fixes, registry workaround, Vulkan errors
- **Terminology** — what CC, mods, IFF, FAR, Vulkan and more actually mean

---

## Structure

All pages are static HTML with no build step required. The site is deployed directly via GitHub Pages from the root of this repository.

```
/
├── index.html
├── about-legacy.html
├── whats-possible.html
├── installing-mods.html
├── download-sites.html
├── mod-list.html
├── cheats.html
├── making-cc.html
├── iff-hacking.html
├── tools.html
├── cc-troubleshooting.html
├── game-troubleshooting.html
├── terminology.html
├── updates.html
├── contact.html
├── search.html
├── 404.html
├── sitemap.xml
├── robots.txt
└── nav_builder.py     ← maintenance script for updating nav across all pages
```

### Updating navigation

If you add a page or change the nav order, run:

```bash
python nav_builder.py --all
```

This regenerates the nav block in every HTML file from a single source of truth.

---

## Contributing

Spotted something wrong? Found a mod that should be on the list? Two ways to help:

1. **Submit via the contact form** on the live site — goes straight to a spreadsheet I check when updating
2. **Open an issue or PR** on this repo

Corrections, broken links, missing mods, and new community resources are all welcome.

---

## Notes

- Not affiliated with EA or Maxis
- All external links verified as of March 2026 — if something's broken, please flag it
- Google Analytics (G-8ZDF0Q80RR) is used to track visitor numbers only
- Last updated: March 2026
