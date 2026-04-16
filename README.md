# Sims 1 Legacy Collection – Modding Guide

A community-maintained guide for modding, customising and creating content for **The Sims Legacy Collection** – the 2025 25th anniversary re-release of The Sims 1 on Steam, EA App and Epic Games Store.

🌐 **Live site: [cyndersanity.github.io/sims-legacy-mod-guide](https://cyndersanity.github.io/sims-legacy-mod-guide/)**

---

## About

This guide exists because the Legacy Collection has different folder structures, save locations and tool compatibility compared to the original Complete Collection or disc versions. Most existing modding guides were written for those older versions. This guide is specifically for Legacy Collection players on Windows, covering everything from installing your first mod through to creating custom content from scratch.

All content is based on community testing, verified tool compatibility checks, official Maxis design documents (98 PDFs published by Don Hopkins), and direct research into what works with the Legacy Collection as of 2026.

---

## Pages

The guide has **32 pages** grouped into sections:

### Playing & Modding
| Page | Description |
|------|-------------|
| `about-legacy.html` | History, technical changes (Vulkan renderer, new save location, no registry, encrypted config), expansion pack folder reference (EP1–EP7), patch history |
| `whats-possible.html` | Engine limits, what can and can't be modded, Steam Deck compatibility |
| `installing-mods.html` | Step-by-step installation for every file type, folder paths for Steam and EA App, CC limits |
| `download-sites.html` | 52 active CC and mod sites verified working in 2026 |
| `mod-list.html` | Quality-of-life mods, objects, debug tools (FaithBeam), bug fixes |

### Gameplay
| Page | Description |
|------|-------------|
| `cheats.html` | Every cheat code with expandable Tips & Tricks section, debug cheats via FaithBeam |
| `careers.html` | All 20 standard + Fame career tracks, promotion requirements, salary, career transfer loop with full transfer tables |

### Creating CC
| Page | Description |
|------|-------------|
| `making-cc.html` | Overview hub – how skins work, tools summary, links to all CC subpages |
| `making-clothing.html` | Clothing overview – how skins work, body types, dress style prefixes, filename format, xskin chain, and links to retexturing and mesh guides |
| `clothing-retextures.html` | Retexturing clothing – GIMP painting workflow, UV layout, backwards-text quirk, skin tone variants, indexed BMP conversion, TSC Wardrobe, getting into game |
| `clothing-meshes.html` | Custom clothing meshes – what a mesh is, mesh rules, Blender + TS1 Blender IO workflow, MilkShape + SKN2OBJ workflow, BodyWarp, accessories, UV mapping, testing |
| `making-heads.html` | Hair & Heads overview – how heads work, texture vs mesh, filename format, UV layout, links to retexturing and FaceLift guides |
| `head-retextures.html` | Retexturing existing heads – GIMP painting workflow, skin tone variants, indexed BMP conversion, TSC export, Face Photo Wizard |
| `head-creation.html` | FaceLift Gold – creating new head shapes by morphing and blending, full interface reference, export workflow |
| `making-walls-floors.html` | Wall coverings (.WLL), floor tiles (.FLR), and roof textures (.BMP). Sections: How It Works, Getting Tools Working, Designing Your Image (#design-your-image — GIMP walkthrough, free CC0 texture sources: Poly Haven/ambientCG, seamless tiling guide), Making a Wall, Making a Floor, Making a Roof, Common Mistakes |
| `making-objects.html` | Objects overview hub – how objects work in Sims 1 (sprites + IFF), tools you need, two routes (retexture vs create new), single-tile vs multi-tile explanation, common mistakes. Mirrors the clothing/heads overview pattern. |
| `object-retextures.html` | Retexturing existing objects using Transmogrifier – clone, export sprites, paint, import. Magic Cookie guide. Finishing section includes creator handle convention ("Recolour of Maxis X. Made by [handle]") and catalog thumbnail update steps. |
| `object-creation.html` | Creating new objects from scratch – Blender modelling, TS1 Renderer addon for sprite generation, TS1 Compiler for IFF packaging, finishing workflow, further reading. |
| `iff-hacking.html` | IFF Hacking hub: what an IFF is, 12 resource types explained (SPR2, BMP_, BCON, STR#, CTSS, TTAs, TTAB, BHAV, OBJD, OBJf, PALT, DGRP), How BHAV Trees Work primer (nodes, True/False branches, Main/Init/TTAB callers, action/test BHAV pairs), clone vs FAR deployment, two-paths cards into sub-pages, annotated Further Resources |
| `iff-simple-edits.html` | Value-level edits without logic changes. BCON (bookcase skill gain example using Constant Contraption), Text (CTSS catalog name/description, TTAs pie menu labels, STR# dialog — Strings Scavenger workflow), OBJD (price, catalog sort flags, community/residential flag) |
| `iff-advanced.html` | Logic-level edits. Adding new pie menu interactions (TTAB + TTAs + BHAV coordination, Action Tree + Check Tree, reusing vs writing BHAVs), autonomy motive advertising (8-motive TTAB values), Custom Careers using Career Creator 3 (replaces base game career, 10-track limit) |
| `tools.html` | Every modding tool with download links and Legacy Collection compatibility notes. 31 tool cards across 4 sections: Essential Tools, CC Creation (incl. FaceLift Gold, The Sims Creator, GIMP, Paint.NET, IrfanView, Photoshop), 3D & Mesh Tools (incl. Blender, SimShow, Skn2Obj, BMF2SKN, BodyWarp), Community Tools |

### Reference & Help
| Page | Description |
|------|-------------|
| `file-reference.html` | Technical reference with expandable cards: game file types, IFF resource types, skin filename prefixes, Magic Cookie guide |
| `terminology.html` | Plain-English definitions: CC, mod, hacking, IFF, FAR, Maxis Match, buyable skins, and more |
| `credits.html` | Full attribution for every source, tool creator, and community member |
| `cc-troubleshooting.html` | Mods not loading, white skins, CC limits, CMX mismatches, missing meshes, registry fix |
| `game-troubleshooting.html` | Vulkan errors, NVIDIA pixel issue, launch crashes, multi-monitor problems |

### Site
| Page | Description |
|------|-------------|
| `index.html` | Homepage with quick-navigation grid |
| `search.html` | Full-text keyword search across all pages |
| `updates.html` | Site Roadmap – in progress, planned, and being considered |
| `contact.html` | Google Form for corrections, suggestions, and broken link reports |
| `404.html` | Custom error page |

---

## File Structure

Static HTML – no framework, no build step, no dependencies. Deployed via GitHub Pages from the repository root.

```
/
├── style.css                   Shared stylesheet (all pages)
├── index.html                  Homepage
├── about-legacy.html
├── whats-possible.html
├── installing-mods.html
├── download-sites.html
├── mod-list.html
├── cheats.html
├── careers.html
├── making-cc.html              CC creation hub
├── making-clothing.html        Clothing overview hub
├── clothing-retextures.html    Retexturing body skins (GIMP + TSC)
├── clothing-meshes.html        Custom mesh editing and accessories
├── making-heads.html           Hair & Heads overview hub
├── head-retextures.html        Retexturing existing heads (GIMP + TSC)
├── head-creation.html          FaceLift Gold (new head shapes)
├── making-walls-floors.html
├── making-objects.html           Objects overview hub
├── object-retextures.html        Retexturing existing objects (TMog workflow)
├── object-creation.html          Creating new objects (Blender + TS1 tools)
├── iff-hacking.html            IFF Hacking hub (concepts, BHAV trees, clone vs FAR)
├── iff-simple-edits.html       BCON, text, OBJD value edits
├── iff-advanced.html           Interactions, motive advertising, custom careers
├── tools.html
├── file-reference.html         Technical reference (expandable cards)
├── credits.html                Sources and attribution
├── terminology.html
├── cc-troubleshooting.html
├── game-troubleshooting.html
├── search.html
├── updates.html
├── contact.html
├── 404.html
├── robots.txt
├── sitemap.xml
├── README.md
├── icons/                      Career icons, expansion pack badges
└── _dev/                       Development reference (not served to site)
    └── style_guide_v6.html     Component reference and formatting rules
```

---

## Navigation

Horizontal scrolling nav bar on desktop, slide-in drawer on mobile. Organised into dropdowns:

| Dropdown | Pages |
|----------|-------|
| **ℹ️ Site Info** | 📅 About Legacy, 📖 Terminology, 🗂️ File Reference, 📝 Sources & Credits, *(divider)*, 📋 Site Roadmap, ✉️ Contact |
| **⚙️ Mods / CC** | 🔬 What's Possible, 📁 Installing Mods, 🌐 Mod Download Sites, ⚙️ Must-Have Mods |
| **🎮 Gameplay** | 🎮 Cheats, 💼 Career Guide |
| **🎨 Create CC** | 🎨 Overview, 👗 Clothing Overview (→ 🎨 Retexturing Clothing, 🧵 Custom Meshes), 💇 Hair & Heads Overview (→ 🎨 Retexturing Heads, 🧬 FaceLift Gold), 🏠 Walls & Floors, 🪑 Objects, *(divider)*, 🔧 IFF Hacking, 🧰 Tools |
| **🛠️ Troubleshooting** | 🛠️ CC Issues, 🖥️ Game Issues |

Top-level links: 🏠 Home, 🔍 Search, ☰ Menu (opens drawer)

---

## Key Design Patterns

### Callouts
```html
<div class="callout teal">ℹ️ Info note</div>      <!-- blue-green -->
<div class="callout gold">⚠️ Warning</div>         <!-- yellow -->
<div class="callout red">🚨 Critical warning</div> <!-- red -->
<div class="callout green">✅ Tip</div>             <!-- green -->
```

### Step-by-step lists
```html
<div class="steps">
  <div class="step">
    <div class="step-num"></div>
    <div class="step-body"><h4>Title</h4><p>Content</p></div>
  </div>
</div>
```

### Expandable accordion cards
Used on file-reference, credits, careers (transfer loop), cheats (tips). Click header to expand – body text is selectable without triggering close.
```html
<div class="ref-card">
  <div class="ref-head" onclick="this.parentElement.classList.toggle('open')">
    <span class="ref-arrow">&#9656;</span>
    <span class="ref-name">Title</span>
  </div>
  <div class="ref-body"><p>Content</p></div>
</div>
```

### Expand/collapse toggle
Single button per section, scoped so it only affects cards in its own section:
```html
<button class="expand-all" onclick="toggleAll(this)">Expand all</button>
```

### Tables
Always wrapped in `.table-wrap` for responsive overflow:
```html
<div class="table-wrap"><table>...</table></div>
```

---

## Key Sources

| Source | What it provided |
|--------|-----------------|
| **Maxis Design Documents** (98 PDFs) | IFF file format, object system, sprite generation, suit conventions |
| **Transmogrifier Documentation** (Don Hopkins) | Retexture workflow, Export Whizzer, Magic Cookie system |
| **IFF Pencil 2** (Tom van Dijk / trolando) | BHAV editing, TTAB interactions, BCON constants |
| **Simania Sims Support Page** | Skinning tutorials, object hacking, character editing |
| **Crash Creations (Skin Shop)** | Head meshing workflow, body meshing, texture mapping, CMX writing |
| **Jerome (SimFreaks)** | Mesh creation guide, CMX/SKN file structure documentation, filename naming tables |
| **The Sims Creator Readme** | Face Photo Wizard workflow, TSC paint tool, accepted file formats |
| **FaceLift Gold** | Head shape creation via morphing and blending (Roger E. Critchlow Jr and Steve DiPaola) |
| **Raeven / Woobsha** | Expert corrections on tool workflows, TTAB accuracy, object hacking |
| **Community testing** | Tool compatibility, folder structures, game behaviour on Legacy Collection |

Full attribution on the [Sources & Credits](https://cyndersanity.github.io/sims-legacy-mod-guide/credits.html) page.

---

## Development Reference

The `_dev/` folder contains `style_guide_v6.html` – a comprehensive component reference with live demos of every UI pattern, colour swatches, CSS variables, and formatting rules. This folder is excluded from the live site by Jekyll (underscore prefix).

Open it locally in a browser to see:
- All CSS colour variables with visual swatches
- Typography scale
- Callout, card, tag, step, table, and accordion card patterns
- Credits role tag colours (gold, teal, red, green, lilac, pink, orange)
- Navigation structure and emoji assignments

---

## Contributing

Flag issues via the **contact form on the live site** or use GitHub Issues / Pull Requests.

### Content rules
- **Accuracy first** – every claim should be verifiable against a known source
- **Beginner-friendly** – explain what and why, not just list actions
- **Consistent formatting** – follow the callout, step, and table patterns above
- **Accessibility** – use bullet lists for 3+ inline items, keep paragraphs readable
- **Bold "Example:" prefixes** – always `<strong>Example:</strong>`
- **Code tags on file paths** – always `<code>\\Downloads\\</code>`

### What not to change without discussion
- Career list and transfer loop data (verified against multiple sources)
- Skin prefix table (cross-referenced against Maxis SuitConventions.pdf and community sources)
- Tool descriptions (TMog handles sprites, IFF Pencil does not – this is verified)

---

## Notes

- Not affiliated with EA, Maxis, or any mod creator
- All external links verified as of April 2026
- Google Analytics (G-8ZDF0Q80RR) tracks visitor numbers only
- Covers the Windows version of the Legacy Collection only
- Built with VSCodium, hosted on GitHub Pages
