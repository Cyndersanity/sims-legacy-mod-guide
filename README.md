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
| `mod-list.html` | Maxis Get Cool Stuff archive, quality-of-life mods, objects, debug tools (FaithBeam), bug fixes |

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
| `clothing-retextures.html` | Retexturing clothing – GIMP painting workflow, UV layout, backwards-text quirk, skin tone variants, indexed BMP conversion, TSC Wardrobe, getting into game, editing CMX files (duplicating, moving between categories, adding accessories, silent mesh failure causes) |
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
| `terminology.html` | Plain-English definitions: CC, mod, hacking, IFF, FAR, Maxis Match, buyable skins, and technical file formats and IFF resource types (CMX, SKN, BCF, BMF, BMP, xskin-, identifier, GUID, Magic Cookie, BCON, STR#, PALT, SPR2, OBJD, TTAB/TTAs, SimAntics, accessory, bodystring, dress style, NPC) |
| `credits.html` | Full attribution for every source, tool creator, and community member |
| `cc-troubleshooting.html` | Mods not loading, crashes after mods, invisible meshes (headless/bodyless Sims), white skins, CC limits, CMX mismatches, FAR files, old .exe installers, registry fix |
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
| **🎨 Create CC** | 🎨 Overview, *(divider)*, 👗 Clothing Overview &rarr; Retexturing Clothing, Custom Meshes, *(divider)*, 💇 Hair & Heads Overview &rarr; Retexturing Heads, FaceLift Gold, *(divider)*, 🏠 Walls & Floors, *(divider)*, 🪑 Objects Overview &rarr; Retexturing Objects, Creating New Objects, *(divider)*, 🔧 IFF Hacking &rarr; Simple Edits, Advanced Edits, *(divider)*, 🧰 Tools |
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
Reserved for genuine imperative tutorial steps. Parallel "checks" or phase groupings should use descriptive H3 subheadings plus card grids instead &ndash; don't label non-step content as "Step 1".

### Prose box
White panel for multi-paragraph prose blocks on prose-heavy sections. Targeted use only &ndash; blanket application to every section is explicitly rejected. See `_dev/prose_box_preview.html` for candidate sections across the site.
```html
<div class="prose-box">
  <p>First paragraph.</p>
  <p>Second paragraph.</p>
  <ul style="padding-left:18px;"><li>...</li></ul>
</div>
```
Currently applied on: `making-cc.html` (4x), `making-clothing.html` (filename-format, 1x), `clothing-retextures.html` (gimp-basics + painting, 2x), `making-objects.html` (1x), `object-retextures.html` (going-further, 1x).

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

The site draws on Maxis design documents (98 PDFs published by Don Hopkins), tool README files, community tutorials from the 2000s era that still apply to Legacy, and direct testing against the Legacy Collection. Specific creators, guides, tools, and references are listed on the [Sources &amp; Credits](https://cyndersanity.github.io/sims-legacy-mod-guide/credits.html) page &ndash; inline attribution is not used on the guide pages themselves.

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
- **Every claim needs a source** &ndash; all written information on the site should be factual and come from a known source (an attached document, a linked wiki, an official repo, or verified community knowledge). Reasoning from adjacent facts does not count as a source.
- **Paraphrase, do not copy** &ndash; community guides (Simania, Jerome, Crash Creations, and others) can inform content but must not be copied or closely paraphrased. Rewrite in your own voice with your own sentence structure, use different representative examples, and avoid reusing creators&rsquo; coined terms as structured concepts. The technical process must remain accurate, but the text must be genuinely original.
- **Credits go on `credits.html` only** &ndash; no inline attribution to creators or guides in the guide pages themselves. No &ldquo;Simania notes&rdquo;, &ldquo;Jerome recommends&rdquo;, &ldquo;per Crash Creations&rdquo;. Every creator, guide, or source the site has drawn on belongs in a ref-card on `credits.html`. Exceptions: resource link cards in &ldquo;Further Resources&rdquo; sections that point users to a specific external URL (they need to name their destination), plus `download-sites.html` and `tools.html` where naming resources is the page&rsquo;s job.
- **Accuracy first** &ndash; every claim should be verifiable against a known source. If a detail is not sourced, leave it out or rewrite the sentence to say only what is actually known.
- **Sims Legacy + original Sims 1 framing** &ndash; where a technique carries over to the original Sims 1, frame it as &ldquo;should work&rdquo; (the site has not tested on the original game). Work the note into a natural place on the page, not as a dumped callout at the top. Do not attribute the claim to &ldquo;others have said&rdquo; or similar weak framing.
- **Beginner-friendly but not dumbed down** &ndash; explain what and why, not just list actions. Technical depth is important; the target tone is knowledgeable friend explaining something to a beginner.
- **Consistent formatting** &ndash; follow the callout, step, and table patterns in `_dev/style_guide_v6.html`.
- **Accessibility** &ndash; use bullet lists for 3+ inline items, keep paragraphs readable, en dashes not em dashes.
- **No nested callouts** &ndash; a callout inside another callout is never acceptable. Adjacent callouts sit in a `.callout-grid`.
- **Unclassed `<ul>` needs inline padding** &ndash; add `style="padding-left:18px;"` because the CSS reset removes default indent.
- **Bold &ldquo;Example:&rdquo; prefixes** &ndash; always `<strong>Example:</strong>`
- **Code tags on file paths** &ndash; always `<code>\Downloads\</code>` (single backslashes, no double)
- **Plain human writing** &ndash; keep the tone conversational and specific. Avoid stacked negatives for rhetorical effect, capitalised warning words (&ldquo;do NOT&rdquo;), filler intensifiers like &ldquo;ensures that / leverages / seamless / robust&rdquo;, arrow notation outside of actual menu paths, and obvious fillers like &ldquo;as you can see&rdquo; or &ldquo;it is worth noting&rdquo;.

### Files to update together
When a structural or rule change lands, three files are kept in sync:

- **`_dev/style_guide_v6.html`** &ndash; new rules and patterns
- **`README.md`** &ndash; structural changes to pages, sections, file layout
- **`credits.html`** &ndash; any new creator or source the site has drawn on

`_dev/` holds only the style guide. Work-in-progress files and local drafts stay out of the repository.

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
