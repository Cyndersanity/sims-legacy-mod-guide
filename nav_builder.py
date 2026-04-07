#!/usr/bin/env python3
"""
nav_builder.py – Maintenance script for the Sims Legacy Collection Modding Guide.

This script regenerates the nav block and footer on any page (or all pages)
from a single source of truth. Run it any time you change the nav order,
add a page, rename a link, or need to sync the footer across all pages.

Usage:
  python nav_builder.py <file.html>        # update a single page
  python nav_builder.py --all              # update all .html files in current directory
  python nav_builder.py --pages a.html b.html   # update specific pages

NOTE: The current nav uses JS-driven dropdown panels. This script rebuilds
the nav-inner block and footer only. Dropdown panel HTML is generated inline.
After running --all, verify dropdown behaviour in browser before deploying.
"""
import os, re, sys

# ── NAV STRUCTURE ───────────────────────────────────────────────────────────
# Reflects the current dropdown nav. Top-level links are listed directly;
# dropdown items are nested under their parent key.

PAGES = {
    # standalone links
    "index.html":               ("🏠", "Home"),
    "about-legacy.html":        ("📖", "About Legacy"),
    "terminology.html":         ("📖", "Terminology"),
    "cheats.html":              ("🎮", "Cheats"),
    "search.html":              ("🔍", "Search"),
    # Mods/CC dropdown
    "whats-possible.html":      ("🔬", "What's Possible"),
    "installing-mods.html":     ("📁", "Installing Mods"),
    "download-sites.html":      ("🌐", "Mod Download Sites"),
    "mod-list.html":            ("⚙️", "Must-Have Mods"),
    # Create CC dropdown
    "making-cc.html":           ("🎨", "Overview & Tools"),
    "making-clothing.html":     ("👗", "Making Clothing"),
    "making-heads.html":        ("💇", "Making Hair & Heads"),
    "making-walls-floors.html": ("🏠", "Making Walls & Floors"),
    "making-objects.html":      ("🪑", "Object Retextures"),
    "iff-hacking.html":         ("🔧", "IFF Hacking"),
    "tools.html":               ("🧰", "Tools"),
    # Troubleshooting dropdown
    "cc-troubleshooting.html":  ("🛠️", "CC Issues"),
    "game-troubleshooting.html":("🖥️", "Game Issues"),
    # Site Info dropdown
    "updates.html":             ("📋", "Site Roadmap"),
    "contact.html":             ("✉️", "Contact"),
}

FOOTER_LINKS = [
    ("https://simblr.cc/ts1/mods/",                      "Simblr.cc"),
    ("http://corylea.com/Sims1ModsByCorylea.html",        "Corylea's Mods"),
    ("https://www.simlogical.com/",                       "Simlogical"),
    ("https://www.reddit.com/r/thesims1/",                "Sims 1 Subreddit"),
    ("https://www.ea.com/games/the-sims/news",            "EA Patch Notes"),
    ("updates.html",                                      "Site Roadmap"),
    ("contact.html",                                      "Contact"),
]

# ── BUILDERS ────────────────────────────────────────────────────────────────

def build_footer():
    links = "\n".join(
        f'      <a href="{h}" target="{"_blank" if h.startswith("http") else "_self"}">{l}</a>'
        for h, l in FOOTER_LINKS
    )
    return (
        '<footer>\n  <div class="footer-inner">\n'
        '    <div class="footer-brand">'
        '<span class="plumbob sm" style="background:#fff;"></span>'
        'The Sims Legacy Collection \u2013 Modding Guide'
        '</div>\n'
        f'    <div class="footer-links">\n{links}\n    </div>\n'
        '    <p>Community guide &middot; Not affiliated with EA or Maxis'
        ' &middot; Last updated April 2026</p>\n'
        '    <p style="margin-top:6px;font-size:11px;color:rgba(255,255,255,0.35);">'
        'This site uses Google Analytics to track visitor numbers and page traffic.'
        '</p>\n  </div>\n</footer>'
    )


def update_page(filepath):
    filename = os.path.basename(filepath)
    with open(filepath, encoding="utf-8") as f:
        c = f.read()

    # Update footer only (nav is managed via inline JS dropdowns)
    c = re.sub(r'<footer>.*?</footer>', build_footer(), c, flags=re.DOTALL)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(c)
    print(f"Updated: {filename}")


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        print("Usage: python nav_builder.py <file.html> | --all | --pages a.html b.html ...")
        sys.exit(0)

    if "--all" in args:
        files = [f for f in os.listdir(".") if f.endswith(".html")]
    elif "--pages" in args:
        idx = args.index("--pages")
        files = args[idx + 1:]
    else:
        files = args

    for f in files:
        if os.path.exists(f):
            update_page(f)
        else:
            print(f"File not found: {f}")
