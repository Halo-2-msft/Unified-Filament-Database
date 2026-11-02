"""
check_sources.py — flag catalog entries that are missing an exact source address.

Convention (adopted 2026-11-02): whenever an entry is added or changed from
information found on a web page, its `notes` field ends with

    | Source: <full page URL> (consulted YYYY-MM-DD)

Several pages: separate the URLs with "; " inside the same tag. The expert
guide (Part 25) credits outside sources, and this tag is what lets that credit
point at the exact page instead of just the site.

This script is a reminder, not a gate. It looks for entries whose notes or
tier rationale mention a date on or after the cutoff and reports the ones with
no "Source: http..." tag. Older entries (before the convention) are counted but
not flagged.

Usage:  python3 check_sources.py [cutoff YYYY-MM-DD]     (default 2026-11-02)
"""
import re
import sys

import generate_all as g
import generate_azurefilm as az
import generate_elegoo as el
import generate_voxelpla as vx

cutoff = sys.argv[1] if len(sys.argv) > 1 else "2026-11-02"
brands = list(g.BRANDS) + [az.AZUREFILM, el.ELEGOO]
brands += [getattr(vx, k) for k in dir(vx)
           if k.isupper() and isinstance(getattr(vx, k), dict) and "catalog" in getattr(vx, k)]

DATE = re.compile(r"\b(20\d\d-\d\d-\d\d)\b")
SRC = re.compile(r"Source:\s*https?://", re.I)

flagged, with_src, total = [], 0, 0
for b in brands:
    for e in b["catalog"]:
        total += 1
        text = f'{e.get("tier_rationale", "")} | {e.get("notes", "")}'
        if SRC.search(text):
            with_src += 1
            continue
        if any(d >= cutoff for d in DATE.findall(text)):
            flagged.append((b["brand"], e["sku"], e["color_name"]))

print(f"{total} catalog entries; {with_src} carry a Source URL tag.")
if flagged:
    print(f"{len(flagged)} entries dated {cutoff} or later have no Source URL:")
    for brand, sku, color in flagged:
        print(f"  {brand}: {sku} ({color})")
    sys.exit(1)
print(f"No entries dated {cutoff} or later are missing a Source URL.")
