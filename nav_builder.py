#!/usr/bin/env python3
"""
nav_builder.py - Apply current nav, footer and base CSS to any Sims Legacy Guide page.
Usage:
  python nav_builder.py <file.html>        # update a single page
  python nav_builder.py --all              # update all .html files in current directory
  python nav_builder.py --new page.html    # scaffold a new blank page
"""
import os, re, sys

NAV_GROUPS = [
    ("", [("index.html","Home"),("about-legacy.html","About Legacy")]),
    ("Playing", [("whats-possible.html","Whats Possible"),("installing-mods.html","Install"),
                 ("download-sites.html","Sites"),("mod-list.html","Mods"),("cheats.html","Cheats")]),
    ("Creating", [("making-cc.html","Create CC"),("iff-hacking.html","IFF Hacking"),("tools.html","Tools")]),
    ("Help", [("cc-troubleshooting.html","CC Issues"),("game-troubleshooting.html","Game Issues")]),
    ("Reference", [("terminology.html","Terminology"),("updates.html","Updates"),("contact.html","Contact")]),
]

FOOTER_LINKS = [
    ("https://simblr.cc/ts1/mods/","Simblr.cc"),
    ("http://corylea.com/Sims1ModsByCorylea.html","Corleas Mods"),
    ("https://www.simlogical.com/","Simlogical"),
    ("https://www.reddit.com/r/thesims1/","Sims 1 Subreddit"),
    ("https://www.ea.com/games/the-sims/news","EA Patch Notes"),
    ("updates.html","Updates & Roadmap"),
    ("contact.html","Contact"),
]

def build_nav_links(active):
    out = "\n    <a class=\"nav-brand\" href=\"index.html\"><span class=\"plumbob sm\"></span><span class=\"nav-brand-text\">SIMS LEGACY COLLECTION</span></a>"
    for i,(grp,links) in enumerate(NAV_GROUPS):
        if i > 0: out += "\n    <span class=\"nav-sep\" aria-hidden=\"true\"></span>"
        for href,label in links:
            cls = "nav-link active" if href==active else "nav-link"
            out += f"\n    <a href=\"{href}\" class=\"{cls}\">{label}</a>"
    return out

def build_footer():
    links = "\n".join(f'      <a href="{h}" target="{"_blank" if h.startswith("http") else "_self"}">{l}</a>' for h,l in FOOTER_LINKS)
    return f"""<footer>\n  <div class="footer-inner">\n    <div class="footer-brand"><span class="plumbob sm" style="background:#fff;"></span>The Sims Legacy Collection &mdash; Modding Guide</div>\n    <div class="footer-links">\n{links}\n    </div>\n    <p>Community guide &middot; Not affiliated with EA or Maxis &middot; Last updated March 2026</p>\n    <p style="margin-top:6px;font-size:11px;color:rgba(255,255,255,0.35);">This site uses Google Analytics to track visitor numbers and page traffic.</p>\n  </div>\n</footer>"""

def update_page(filepath):
    filename = os.path.basename(filepath)
    with open(filepath, encoding="utf-8") as f: c = f.read()
    # Update nav-inner links
    c = re.sub(
        r'<div class="nav-inner" id="navInner">.*?</div>',
        f'<div class="nav-inner" id="navInner">{build_nav_links(filename)}\n  </div>',
        c, flags=re.DOTALL
    )
    # Update footer
    c = re.sub(r'<footer>.*?</footer>', build_footer(), c, flags=re.DOTALL)
    with open(filepath, "w", encoding="utf-8") as f: f.write(c)
    print(f"Updated: {filename}")

if __name__ == "__main__":
    args = sys.argv[1:]
    if "--all" in args:
        for f in os.listdir("."):
            if f.endswith(".html"): update_page(f)
    elif args:
        for a in args:
            if os.path.exists(a): update_page(a)
            else: print(f"File not found: {a}")
    else:
        print("Usage: python nav_builder.py <file.html> | --all")
