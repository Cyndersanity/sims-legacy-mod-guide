# Sims 1 Legacy Collection – Modding Guide

A community-maintained guide for modding, customising and creating content for **The Sims Legacy Collection** – the 2025 25th anniversary re-release of The Sims 1 on Steam, EA App and Epic Games Store.

🌐 **Live site: [cyndersanity.github.io/sims-legacy-mod-guide](https://cyndersanity.github.io/sims-legacy-mod-guide/)**

---

## About the guide

This guide was built because the Legacy Collection has a slightly different folder structure, save location and tool compatibility compared to the original Complete Collection or disc versions – and most existing guides were written for one of those. This guide is specifically for Legacy Collection players on Windows, covering everything from installing your first mod through to creating custom content from scratch.

All content is based on community testing, verified tool compatibility checks, official Maxis design documents, and direct research into what works (and doesn't) with the Legacy Collection as of 2026.

---

## What's covered

The guide has 24 pages, grouped into sections:

### Playing & modding
| Page | What it covers |
|------|---------------|
| `about-legacy.html` | What the Legacy Collection is, how it differs from older versions, expansion pack folder reference (EP1–EP7), technical changes (Vulkan renderer, new save location, no registry, encrypted config), and full EA patch history |
| `whats-possible.html` | What can and can't be modded – engine limits, confirmed working features (edit_char, child ageing, resolution), Steam Deck compatibility |
| `installing-mods.html` | Step-by-step installation for every file type, correct folder paths for Steam and EA App, CC file limits, lot and family import/export |
| `download-sites.html` | 52 active CC and mod sites verified working in 2026, archive resources, and community directories |
| `mod-list.html` | Quality-of-life mods, objects, debug tools (FaithBeam), and bug fixes with direct download links |

### Gameplay
| Page | What it covers |
|------|---------------|
| `cheats.html` | Every cheat code, Tips & Tricks section with expandable cards, debug cheats via FaithBeam |
| `careers.html` | Every career track (20 standard + Fame), promotion requirements, salary, work hours, career transfer loop with full transfer table |

### Creating CC
| Page | What it covers |
|------|---------------|
| `making-cc.html` | Overview hub – how skins work in Sims 1, tools summary, links to all CC subpages |
| `making-clothing.html` | Custom body skins: body types (256×256 BMP), skin tones, filename format, xskin chain, mesh editing in Blender and MilkShape |
| `making-heads.html` | Custom hair and face textures: C prefix system (128×128 BMP), Face Photo Wizard, skin tone versions |
| `making-walls-floors.html` | Wall coverings (.WLL), floor tiles (.FLR) via Home Crafter, and roof textures (.BMP) in GIMP |
| `making-objects.html` | Object retextures using Transmogrifier – clone, export sprites, paint, import. Magic Cookie guide |
| `iff-hacking.html` | Gameplay mods: BCON editing, TTAB interactions, FAR override system, custom careers, career transfer loop |
| `tools.html` | Every modding tool with download links – Transmogrifier, IFF Pencil 2, Constant Contraption, Career Creator 3, FARx, FaithBeam, The Sims Creator, Home Crafter, Blender addons |

### Reference & help
| Page | What it covers |
|------|---------------|
| `file-reference.html` | Technical reference: game file types, IFF resource types (expandable cards), skin filename prefixes, Magic Cookie guide |
| `terminology.html` | Plain-English definitions in expandable cards: CC, mod, hacking, IFF, FAR, Maxis Match, buyable skins, and more |
| `credits.html` | Full attribution for every source, tool creator, and community member |
| `cc-troubleshooting.html` | Mods not loading, white skins, CC limits, CMX mismatches, missing meshes, IFF Pencil 2 compatibility, registry fix |
| `game-troubleshooting.html` | Vulkan errors, NVIDIA pixel issue, launch crashes, multi-monitor problems |

### Site
| Page | What it covers |
|------|---------------|
| `search.html` | Full-text keyword search across all 24 pages |
| `updates.html` | Site Roadmap – in progress, planned, and being considered |
| `contact.html` | Google Form for corrections, suggestions, and broken link reports |

---

## Site structure

Static HTML only – no framework, no build step, no dependencies. Deployed via GitHub Pages from the root of the repository. Shared CSS in `style.css`; page-specific rules are inline. All JavaScript is inline and vanilla.

```
/
├── style.css                   Shared stylesheet
├── index.html                  Homepage
├── about-legacy.html
├── whats-possible.html
├── installing-mods.html
├── download-sites.html
├── mod-list.html
├── cheats.html
├── careers.html
├── making-cc.html              CC creation hub
├── making-clothing.html
├── making-heads.html
├── making-walls-floors.html
├── making-objects.html         Object retextures (TMog workflow)
├── iff-hacking.html            Gameplay mods (BCON, TTAB, careers)
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
└── icons/                      Career icons and expansion pack badges
```

---

## Navigation

Horizontal scrolling nav bar on desktop, slide-in drawer on mobile. Organised into dropdowns:

- **Site Info** – About Legacy, Terminology, File Reference, Sources & Credits, [divider], Site Roadmap, Contact
- **Mods / CC** – What's Possible, Installing Mods, Mod Download Sites, Must-Have Mods
- **Gameplay** – Cheats, Career Guide
- **Create CC** – Overview, Making Clothing, Making Hair & Heads, Making Walls & Floors, Object Retextures, IFF Hacking, Tools
- **Troubleshooting** – CC Issues, Game Issues

---

## Key sources

- **Maxis Design Documents** (98 PDFs) – [donhopkins.com](https://donhopkins.com/home/TheSimsDesignDocuments/)
- **Transmogrifier Documentation** – Don Hopkins, [thesimstransmogrifier.com](https://www.thesimstransmogrifier.com/TransmogrifierDocumentation/)
- **IFF Pencil 2** – Tom van Dijk, [github.com/trolando/Sims1Tools](https://github.com/trolando/Sims1Tools)
- **Simania Sims Support Page** – tutorials on skinning, object hacking, and character editing
- **Sims Wiki** – skin filename conventions and general reference
- **Community testing** – tool compatibility, folder structures, and game behaviour

Full attribution on the [Sources & Credits](https://cyndersanity.github.io/sims-legacy-mod-guide/credits.html) page.

---

## Contributing

Flag issues via the **contact form on the live site** or use GitHub Issues / Pull Requests.

---

## Notes

- Not affiliated with EA, Maxis, or any mod creator
- All external links verified as of April 2026
- Google Analytics (G-8ZDF0Q80RR) tracks visitor numbers only
- Covers the Windows version of the Legacy Collection only
