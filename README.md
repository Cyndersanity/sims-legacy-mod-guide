# Sims 1 Legacy Collection – Modding Guide

A community-maintained guide for modding, customising and creating content for **The Sims Legacy Collection** – the 2025 25th anniversary re-release of The Sims 1 on Steam, EA App and Epic Games Store.

🌐 **Live site: [cyndersanity.github.io/sims-legacy-mod-guide](https://cyndersanity.github.io/sims-legacy-mod-guide/)**

---

## About the guide

This guide was built because the Legacy Collection has a slightly different folder structure, save location and tool compatibility compared to the original Complete Collection or disc versions – and most existing guides were written for one of those. This guide is specifically for Legacy Collection players on Windows, covering everything from installing your first mod through to creating custom content from scratch.

All content is based on community testing, verified tool compatibility checks, and direct research into what works (and doesn't) with the Legacy Collection as of 2026.

---

## What's covered

The guide has 20 pages, grouped into sections:

### Playing & modding
| Page | What it covers |
|------|---------------|
| `about-legacy.html` | What the Legacy Collection is, how it differs from older versions, the full expansion pack folder reference (EP1–EP7), technical changes (Vulkan renderer, new save location, no registry, encrypted config), in-game settings reference, and the full EA patch history |
| `whats-possible.html` | A clear breakdown of what can and can't be modded – engine limits, confirmed working features (edit_char, child ageing, resolution), Steam Deck compatibility, and graphics explained |
| `installing-mods.html` | Step-by-step installation for every file type, the correct folder paths for both Steam and EA App versions, CC file limits (objects, walls, skins, downloads folder size), and how to import/export lots and families |
| `download-sites.html` | 52 active CC and mod sites verified working in 2026 (in a scrollable table), archive resources, and community directories |
| `mod-list.html` | Quality-of-life mods, objects and furniture, debug and runtime tools (FaithBeam), and bug fixes – all with direct download links and install instructions |
| `cheats.html` | Every working cheat code including the debug cheats unlocked by FaithBeam's runtime patcher |

### Creating CC
| Page | What it covers |
|------|---------------|
| `making-cc.html` | Overview hub – how skins work in Sims 1, tools summary with Legacy Collection compatibility notes, links to all CC subpages |
| `making-clothing.html` | Custom body skins and outfits: body types, skin tones, filename format (B prefix system), step-by-step in GIMP, Feraligatr installer and manual registry fix routes |
| `making-heads.html` | Custom hair and face textures: C prefix system, Face Photo Wizard in The Sims Creator, skin tone versions |
| `making-walls-floors.html` | Wall coverings (.WLL), floor tiles (.FLR) via Home Crafter, and roof textures (.BMP) directly in GIMP |
| `making-objects.html` | Visual-only object retextures using Transmogrifier and IFF Pencil 2 – no BHAV scripting needed |
| `iff-hacking.html` | Creating gameplay mods from scratch: BHAV scripting, object hacking, custom careers, tool setup |
| `tools.html` | Every modding tool with download links and Legacy Collection compatibility notes – IFF Pencil 2, Transmogrifier (by Don Hopkins), Career Creator 3, FARx, FaithBeam, The Sims Creator, Home Crafter, Skin Doctor |

### Reference & help
| Page | What it covers |
|------|---------------|
| `terminology.html` | Plain-English definitions of CC, mod, hacking, IFF, FAR, BHAV, Vulkan, Maxis Match, buyable skins, Get Cool Stuff, and more |
| `cc-troubleshooting.html` | Fixing mods not loading, white blank skins, CC limits, old FAR-packed mods, registry fix, Feraligatr installer |
| `game-troubleshooting.html` | Vulkan errors, NVIDIA pixel issue, launch crashes, multi-monitor problems, Simscord and community help |

### Site
| Page | What it covers |
|------|---------------|
| `search.html` | Full-text keyword search across all 20 pages |
| `updates.html` | Public roadmap – what's in progress, planned, and being considered |
| `contact.html` | Google Form for corrections, missing mods, broken links and suggestions |

---

## Site structure

Static HTML only – no framework, no build step, no dependencies. Deployed directly via GitHub Pages from the root of the repository. All CSS is inline per-page. All JavaScript is inline and vanilla.

```
/
├── index.html                  Homepage with quick-navigation grid
├── about-legacy.html
├── whats-possible.html
├── installing-mods.html
├── download-sites.html
├── mod-list.html
├── cheats.html
├── making-cc.html              CC creation hub
├── making-clothing.html        CC subpage
├── making-heads.html           CC subpage
├── making-walls-floors.html    CC subpage
├── making-objects.html         CC subpage
├── iff-hacking.html
├── tools.html
├── terminology.html
├── cc-troubleshooting.html
├── game-troubleshooting.html
├── search.html
├── updates.html
├── contact.html
├── 404.html
├── sitemap.xml
├── robots.txt
└── nav_builder.py              Maintenance script – see below
```

---

## Navigation structure

The site uses a horizontal scrolling nav bar on desktop and a slide-in drawer on mobile (opened via the "Menu ☰" button). The desktop nav also has a ☰ button in the bar for users who prefer the drawer.

Nav is organised into dropdowns:

- **Mods / CC** – What's Possible, Installing Mods, Mod Download Sites, Must-Have Mods
- **Create CC** – Overview, Making Clothing, Making Hair & Heads, Making Walls & Floors, Object Retextures, IFF Hacking, Tools
- **Troubleshooting** – CC Issues, Game Issues
- **Site Info** – Roadmap, Contact

---

## Design system

The site uses a consistent set of CSS custom properties defined in every page's `<style>` block:

| Variable | Value | Used for |
|----------|-------|----------|
| `--cream` | `#F5F2E8` | Page background |
| `--green` | `#3BAE5C` | Primary brand colour, buttons, links |
| `--green-dark` | `#1A5229` | Headings, nav, footer |
| `--green-pale` | `#E6F5EB` | Card backgrounds, hover states |
| `--gold` | `#E8B84B` | Warning callouts |
| `--teal` | `#3AADA8` | Info callouts |
| `--red` | `#D94F4F` | Error callouts |
| `--ink` | `#1C2B1F` | Body text |

**Fonts:** Paytone One (headings), Nunito (body), IBM Plex Mono (code) – all loaded from Google Fonts.

**Callout convention:**
```html
<div class="callout teal">ℹ️ Info note</div>
<div class="callout gold">⚠️ Warning</div>
<div class="callout red">🚨 Critical warning</div>
<div class="callout green">✅ Tip or confirmation</div>
```

**Step-by-step lists:**
```html
<div class="steps">
  <div class="step">
    <div class="step-num"></div>
    <div class="step-body"><h4>Step title</h4><p>Step content.</p></div>
  </div>
</div>
```

**Tables** must always be wrapped in `.table-wrap`:
```html
<div class="table-wrap">
  <table>...</table>
</div>
```

---

## Adding or editing pages

### Editing existing content

Each page is self-contained HTML. Open the file in any text editor and edit the content inside `<main class="content">`. The CSS and nav are in the same file.

### Adding a new page

1. Copy an existing page (e.g. `about-legacy.html`) as a starting point
2. Update the `<title>` tag, `<h1>`, `.page-eyebrow`, and `.page-sub` to match the new page
3. Replace the content inside `<main class="content">` with your new content
4. Update the nav across all pages – run:
   ```bash
   python nav_builder.py --all
   ```
   Or manually add the new page's link to the nav-inner and drawer blocks in every HTML file
5. Add the page to `sitemap.xml`
6. Update the search index in `search.html` (the `INDEX` const at the top of the inline `<script>`)

### Updating the nav

The `nav_builder.py` script regenerates the nav block across all pages from a single source of truth. Run it any time you change the nav order, add a page, or rename a link:

```bash
python nav_builder.py --all
```

If you only need to update specific pages:
```bash
python nav_builder.py --pages about-legacy.html tools.html
```

---

## Contributing
---

## Contributing

The easiest way to flag something is via the **contact form on the live site** – it goes straight into a spreadsheet reviewed when the guide is next updated.

If you prefer GitHub:
- **Issues** – for broken links, factual errors, missing mods, or suggestions
- **Pull requests** – for direct corrections or additions

Useful contributions:
- Broken or dead links (especially in the 52-site active sites table)
- Mods that should be on the must-have list (include name, creator and download link)
- Corrections to install paths or tool instructions
- New information about Legacy Collection compatibility with tools or mods

---

## Notes

- Not affiliated with EA, Maxis, or any mod creator
- All external links verified as of April 2026 – use the contact form to flag anything broken
- Google Analytics (G-8ZDF0Q80RR) tracks visitor numbers only – no personal data collected
- The guide covers the Windows version of the Legacy Collection only. Mac version behaviour may differ.
