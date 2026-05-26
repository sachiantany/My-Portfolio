#!/usr/bin/env python3
"""
Refresh the Certifications section in blue-theme.html from Credly live data.
Fetches all public badges and regenerates the top N cards (pinned certs always shown first).

Usage:
    python3 update-badges.py
    python3 update-badges.py --count 8   # show 8 badges instead of default 6
    python3 update-badges.py --apply     # also run apply-theme.sh after update
"""

import json, re, sys, subprocess
from urllib.request import urlopen, Request
from datetime import datetime
from pathlib import Path

CREDLY_USER   = "sachintha-antany.1f19a389"
THEME_FILE    = Path(__file__).parent / "assets/themes/blue-theme.html"
DEFAULT_COUNT = 6

# Badges that should always appear regardless of date order (by Credly badge ID)
PINNED_IDS = {
    "cb7d2b30-ca64-49c6-aa33-8b89923df6d9",  # Professional Cloud Architect
    "4652af21-f3e8-4c99-bf62-2119e81b9474",  # Associate Cloud Engineer
}

LEVEL_CLASS = {"Advanced": "adv", "Intermediate": "int", "Foundational": "fnd"}

def fetch_badges():
    url = f"https://www.credly.com/users/{CREDLY_USER}/badges.json?page=1&page_size=100"
    req = Request(url, headers={"Accept": "application/json", "User-Agent": "portfolio-badge-updater/1.0"})
    with urlopen(req, timeout=10) as r:
        return json.load(r).get("data", [])

def badge_to_card(b):
    tmpl    = b.get("badge_template", {})
    name    = tmpl.get("name", "")
    level   = tmpl.get("level", "Foundational")
    img     = tmpl.get("image_url", "")
    issued  = b.get("issued_at_date", "")
    issuer  = b["issuer"]["entities"][0]["entity"]["name"]
    badge_url = f"https://www.credly.com/badges/{b['id']}"
    lvl_cls = LEVEL_CLASS.get(level, "fnd")
    date_fmt = datetime.strptime(issued, "%Y-%m-%d").strftime("%b %Y") if issued else ""
    return f"""
      <a class="cert-card" href="{badge_url}" target="_blank">
        <img class="cert-img" src="{img}" alt="{name}" loading="lazy">
        <div class="cert-body">
          <div class="cert-name">{name}</div>
          <div class="cert-meta">
            <span class="cert-level {lvl_cls}">{level}</span>
            <span class="cert-date">{date_fmt}</span>
          </div>
          <div class="cert-issuer">{issuer}</div>
        </div>
      </a>"""

def build_grid(badges, count):
    pinned  = [b for b in badges if b["id"] in PINNED_IDS]
    rest    = [b for b in badges if b["id"] not in PINNED_IDS]
    ordered = pinned + rest  # pinned first, then most-recent
    chosen  = ordered[:count]
    total   = len(badges)
    cards   = "\n".join(badge_to_card(b) for b in chosen)
    footer  = f'      <a href="https://www.credly.com/users/{CREDLY_USER}/badges" target="_blank">View all {total} badges on Credly →</a>'
    return cards, total, footer

def update_theme(cards, total, footer):
    html = THEME_FILE.read_text(encoding="utf-8")

    # Replace grid content between the two sentinel comments
    grid_pattern = re.compile(
        r'(<div class="certs-grid">).*?(</div>\s*\n\s*<div class="certs-footer">)',
        re.DOTALL
    )
    html = grid_pattern.sub(lambda m: m.group(1) + "\n" + cards + "\n\n    " + m.group(2), html)

    # Replace footer link
    footer_pattern = re.compile(r'(<div class="certs-footer">\s*)<a [^>]+>[^<]+</a>')
    html = footer_pattern.sub(lambda m: m.group(1) + footer, html)

    # Update the blurb count
    html = re.sub(r'\d+ badges earned', f'{total} badges earned', html)

    THEME_FILE.write_text(html, encoding="utf-8")

def main():
    count   = DEFAULT_COUNT
    do_apply = False
    args = sys.argv[1:]
    if "--apply" in args:
        do_apply = True
        args.remove("--apply")
    if "--count" in args:
        idx = args.index("--count")
        count = int(args[idx + 1])

    print(f"Fetching badges for {CREDLY_USER}...")
    badges = fetch_badges()
    print(f"  Found {len(badges)} badges")

    cards, total, footer = build_grid(badges, count)
    update_theme(cards, total, footer)
    print(f"  {THEME_FILE.name} updated — showing {count} of {total} badges")

    if do_apply:
        subprocess.run(["./apply-theme.sh"], check=True)
        print("  index.html updated")

if __name__ == "__main__":
    main()
