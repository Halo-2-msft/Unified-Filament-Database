"""
generate_elegoo.py — Elegoo filament workbook (MVP — PLA + PLA Basic lines only)

MVP SCOPE NOTE: Elegoo's full lineup is large (PLA, PLA Basic, PLA Plus, PLA Pro,
PLA Silk, PLA Matte, PLA-CF, a "PLA RFID emoji Brand Edition" line, PETG Pro,
PETG Translucent, PETG-CF, PETG-GF, Rapid PETG, TPU 95A, ASA — realistically
150-250+ colors once fully built out). This first pass covers only the two core
PLA lines as a starting point, matching the same incremental approach used to
originally stand up every other brand in this project. Remaining lines are a
follow-up task, not an oversight.

Sources:
  - us.elegoo.com product pages (confirmed color names + official color counts)
  - 3dfilamentprofiles.com (per-color hex, temps — individually verified per line,
    never inferred across PLA vs PLA Basic vs PLA+/Pro Basic, which are confirmed
    to be genuinely different products with different hex per color even when
    names overlap, e.g. both lines have a "Black"/"Purple"/etc. but were not
    assumed identical)
  - MakerWorld community swatch set ("The Complete Elegoo Colour Swatch ID Set")
    for the plain "PLA" line — community-sourced, not manufacturer-official,
    flagged as such per-entry
Run: python generate_elegoo.py
"""

import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from template_v3 import build_workbook, next_versioned_path

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ── Spool / AMS note ──────────────────────────────────────────────────────────
# Elegoo spools are cardboard, ~199-200mm OD (confirmed via multiple third-party
# AMS adapter-ring products built specifically for Elegoo spools) — requires the
# Bambu AMS Adapter Ring, same as Hatchbox and Polymaker's Panchroma line.
# One community forum post (Bambu Lab forum, 2026) mentions Elegoo may be in the
# process of transitioning some SKUs to plastic spools — not independently
# confirmed this pass, flagged as a watch item, not applied.

def _el_pla(color, hex_, sku_sfx, notes=""):
    return dict(material_type="PLA", sku=f"EL-PLA-{sku_sfx}", product_name="Elegoo PLA",
                color_name=color, color_hex=hex_, diameter="1.75mm",
                diameter_tolerance="±0.03mm", spool_type="Cardboard", ams_adapter="Yes",
                print_temp="190–220°C", bed_temp="45–60°C", drying="45°C / 4h",
                ams_xp="⚠", ams_lite="⚠", ams_2pro="⚠", ams_ht="⚠",
                tier="B" if hex_ != "999999" else "C",
                tier_rationale=("Color confirmed (us.elegoo.com official product page, "
                                 "18-color line); hex via MakerWorld community swatch set "
                                 "\"The Complete Elegoo Colour Swatch ID Set\" — community-"
                                 "sourced, not manufacturer-published, treat as approximate"
                                 if hex_ != "999999" else
                                 "PLACEHOLDER — color confirmed real (us.elegoo.com official "
                                 "product page, 18-color line) but not in the community "
                                 "swatch set checked this pass"),
                notes=(notes + " | " if notes else "") +
                      ("Cardboard spool — AMS Adapter Ring required for all AMS variants | "
                       "Hex: community-sourced (MakerWorld), not manufacturer-confirmed"
                       if hex_ != "999999" else
                       "Cardboard spool — AMS Adapter Ring required for all AMS variants | "
                       "Hex: unconfirmed placeholder"))

def _el_plab(color, hex_, sku_sfx, print_temp="190–230°C", bed_temp="35–65°C",
             notes="", name_variance=None):
    rationale = ("RESOLVED via 3dfilamentprofiles.com's ELEGOO PLA Basic listing, direct "
                 "name match" if hex_ != "999999" and not name_variance else
                 f"RESOLVED via 3dfilamentprofiles.com's ELEGOO PLA Basic listing, mapped "
                 f"from their listing name \"{name_variance}\" — naming variance from "
                 f"Elegoo's own official color name, treated as the same color"
                 if name_variance else
                 "PLACEHOLDER — color confirmed real (us.elegoo.com official product page, "
                 "19-color US-market line — note some regional Elegoo storefronts show up "
                 "to 24-25 colors for this same line, not reconciled this pass) but hex not "
                 "found on 3dfilamentprofiles.com or any other source checked this pass")
    return dict(material_type="PLA Basic", sku=f"EL-PLAB-{sku_sfx}",
                product_name="Elegoo PLA Basic",
                color_name=color, color_hex=hex_, diameter="1.75mm",
                diameter_tolerance="±0.02mm", spool_type="Cardboard", ams_adapter="Yes",
                print_temp=print_temp, bed_temp=bed_temp, drying="55°C / 6h",
                ams_xp="⚠", ams_lite="⚠", ams_2pro="⚠", ams_ht="⚠",
                tier="A" if hex_ != "999999" else "C",
                tier_rationale=rationale,
                notes=(notes + " | " if notes else "") +
                      "Cardboard spool — AMS Adapter Ring required for all AMS variants | " +
                      ("Hex: manufacturer-listed value (3dfilamentprofiles.com)"
                       if hex_ != "999999" else "Hex: unconfirmed placeholder"))


def _el_plap(color, hex_, sku_sfx, notes=""):
    return dict(material_type="PLA Plus", sku=f"EL-PLAP-{sku_sfx}", product_name="Elegoo PLA Plus",
                color_name=color, color_hex=hex_, diameter="1.75mm",
                diameter_tolerance="±0.03mm", spool_type="Cardboard", ams_adapter="Yes",
                print_temp="190–220°C", bed_temp="45–60°C", drying="45°C / 4h",
                ams_xp="⚠", ams_lite="⚠", ams_2pro="⚠", ams_ht="⚠",
                tier="B",
                tier_rationale=("Color confirmed (us.elegoo.com official product page, "
                                 "17-color line, exact same names as this catalog's PLA "
                                 "line minus Copper Filled); hex via MakerWorld community "
                                 "swatch set, which explicitly states coverage for \"PLA, "
                                 "PLA+, Rapid PETG, TPU 95A\" per color — applied here on "
                                 "that basis, not a cross-line guess"),
                notes=(notes + " | " if notes else "") +
                      "Cardboard spool — AMS Adapter Ring required for all AMS variants | "
                      "Hex: community-sourced (MakerWorld), not manufacturer-confirmed")

def _el_tpu(color, hex_, sku_sfx, notes=""):
    return dict(material_type="TPU 95A", sku=f"EL-TPU-{sku_sfx}", product_name="Elegoo TPU 95A",
                color_name=color, color_hex=hex_, diameter="1.75mm",
                diameter_tolerance="±0.03mm", spool_type="Cardboard", ams_adapter="Yes",
                print_temp="210–240°C", bed_temp="35–60°C", drying="50°C / 8h",
                ams_xp="✗", ams_lite="✗", ams_2pro="✗", ams_ht="✗",
                tier="B" if hex_ != "999999" else "C",
                tier_rationale=("Color and temps manufacturer-confirmed (us.elegoo.com "
                                 "product page, 7-color line; temps cross-checked via "
                                 "3djake.com per-color listings); hex via MakerWorld "
                                 "community swatch set, exact name match"
                                 if hex_ != "999999" else
                                 "PLACEHOLDER — color and temps manufacturer-confirmed "
                                 "(us.elegoo.com product page, 7-color line) but this exact "
                                 "color name is not in the MakerWorld swatch set (which "
                                 "covers \"Dark Blue\"/\"Neon Green\" for other lines, not "
                                 "plain \"Blue\"/\"Green\" as TPU 95A names them) — not "
                                 "assumed identical, per no-cross-inference rule"),
                notes=(notes + " | " if notes else "") +
                      ("Cardboard spool — AMS Adapter Ring required for all AMS variants; "
                       "TPU is external-spool-only on Bambu AMS regardless of adapter ring | "
                       "Hex: community-sourced (MakerWorld), not manufacturer-confirmed"
                       if hex_ != "999999" else
                       "Cardboard spool — AMS Adapter Ring required for all AMS variants; "
                       "TPU is external-spool-only on Bambu AMS regardless of adapter ring | "
                       "Hex: unconfirmed placeholder"))


ELEGOO = {
    "brand": "Elegoo",
    "catalog": [
        # ── PLA Plus (17 colors — us.elegoo.com official) ─────────────────────
        # Same 17 color names as this catalog's PLA line (minus Copper Filled).
        # Hex from the same MakerWorld swatch set, which explicitly covers PLA+.
        _el_plap("Black",       "000000", "BK"),
        _el_plap("White",       "FFFFFF", "WH"),
        _el_plap("Grey",        "8F949B", "GY"),
        _el_plap("Neon Green",  "08E327", "NGN"),
        _el_plap("Dark Blue",   "2240AF", "DBL"),
        _el_plap("Red",         "EA140E", "RD"),
        _el_plap("Yellow",      "F6D701", "YL"),
        _el_plap("Orange",      "FD7C18", "OR"),
        _el_plap("Sky Blue",    "27B2D0", "SKB"),
        _el_plap("Sea Green",   "1ABC83", "SGN"),
        _el_plap("Space Grey",  "5D5D5D", "SPG"),
        _el_plap("Translucent", "E9E9E7", "TR",
                  notes="Mapped from MakerWorld swatch's \"Clear\" — likely the same product under a different name, not confirmed identical"),
        _el_plap("Pink",        "F9B0BD", "PK"),
        _el_plap("Purple",      "603BA0", "PU"),
        _el_plap("Beige",       "FEE7BF", "BEI"),
        _el_plap("Wood Color",  "B19870", "WDC"),
        _el_plap("Brown",       "9E6A4B", "BR"),

        # ── TPU 95A (7 colors — us.elegoo.com official) ────────────────────────
        _el_tpu("Black",       "000000", "BK"),
        _el_tpu("White",       "FFFFFF", "WH"),
        _el_tpu("Grey",        "8F949B", "GY"),
        _el_tpu("Red",         "EA140E", "RD"),
        _el_tpu("Blue",        "999999", "BL"),
        _el_tpu("Green",       "999999", "GN"),
        _el_tpu("Translucent", "999999", "TR"),
        # ── PLA (18 colors — us.elegoo.com official) ──────────────────────────
        # Hex source: MakerWorld community swatch set, covers "PLA, PLA+, Rapid
        # PETG, TPU 95A" per-color — applied here to PLA only, per this
        # catalog's no-cross-line-inference convention.
        _el_pla("Black",        "000000", "BK"),
        _el_pla("White",        "FFFFFF", "WH"),
        _el_pla("Grey",         "8F949B", "GY"),
        _el_pla("Neon Green",   "08E327", "NGN"),
        _el_pla("Dark Blue",    "2240AF", "DBL"),
        _el_pla("Red",          "EA140E", "RD"),
        _el_pla("Yellow",       "F6D701", "YL"),
        _el_pla("Orange",       "FD7C18", "OR"),
        _el_pla("Pink",         "F9B0BD", "PK"),
        _el_pla("Purple",       "603BA0", "PU"),
        _el_pla("Translucent",  "E9E9E7", "TR",
                notes="Mapped from MakerWorld swatch's \"Clear\" — likely the same product under a different name, not confirmed identical"),
        _el_pla("Sky Blue",     "27B2D0", "SKB"),
        _el_pla("Sea Green",    "1ABC83", "SGN"),
        _el_pla("Space Grey",   "5D5D5D", "SPG"),
        _el_pla("Wood Color",   "B19870", "WDC"),
        _el_pla("Brown",        "9E6A4B", "BR"),
        _el_pla("Beige",        "FEE7BF", "BEI"),
        _el_pla("Copper Filled","999999", "CUF",
                notes="MakerWorld swatch set has a \"Bronze Filled\" (#895837) entry but not \"Copper Filled\" specifically — different name, not assumed identical per no-cross-inference rule"),

        # ── PLA Basic (19 colors — us.elegoo.com official, US market) ─────────
        _el_plab("Hot Pink",       "FA7291", "HPK", print_temp="180–210°C", bed_temp="35–65°C"),
        _el_plab("Cocoa Brown",    "9E6A4B", "COB", name_variance="Brown"),
        _el_plab("Beige",          "F4E0B8", "BEI"),
        _el_plab("Translucent",    "BEBBC0", "TR", name_variance="Clear"),
        _el_plab("Black",          "999999", "BK"),
        _el_plab("Red",            "999999", "RD"),
        _el_plab("Yellow",         "999999", "YL"),
        _el_plab("Cyan",           "999999", "CY"),
        _el_plab("Purple",         "999999", "PU"),
        _el_plab("Sunflower Yellow","999999", "SFY"),
        _el_plab("Cobalt Blue",    "999999", "COBL"),
        _el_plab("Apple Green",    "999999", "APG"),
        _el_plab("Turquoise Green","999999", "TQG"),
        _el_plab("White",          "999999", "WH"),
        _el_plab("Grey",           "999999", "GY"),
        _el_plab("Pink",           "999999", "PK"),
        _el_plab("Green",          "999999", "GN"),
        _el_plab("Misty Blue",     "999999", "MSB"),
        _el_plab("Orange",         "999999", "OR"),
    ],

    "inventory": [],

    "material_guide": [
        {
            "material": "PLA", "print_temp": "190–220°C", "bed_temp": "45–60°C",
            "enclosure": "No", "ams_compat": "⚠", "drying_required": "Recommended",
            "drying": "45°C / 4h",
            "notes": "Cardboard spool, ~199-200mm OD — AMS Adapter Ring required for all AMS variants. Hex codes are community-sourced (MakerWorld), not manufacturer-published.",
        },
        {
            "material": "PLA Basic", "print_temp": "190–230°C", "bed_temp": "35–65°C",
            "enclosure": "No", "ams_compat": "⚠", "drying_required": "Recommended",
            "drying": "55°C / 6h",
            "notes": "Cardboard spool — AMS Adapter Ring required. Distinct product line from plain \"PLA\" with different colors and (where checked) different hex for same-named colors — not cross-referenced. Color count varies by region: 19 (US) up to 24-25 (AU/other storefronts) — not reconciled this pass.",
        },
        {
            "material": "PLA Plus", "print_temp": "190–220°C", "bed_temp": "45–60°C",
            "enclosure": "No", "ams_compat": "⚠", "drying_required": "Recommended",
            "drying": "45°C / 4h",
            "notes": "Cardboard spool — AMS Adapter Ring required. Same 17 color names as the plain PLA line; hex from the same community swatch set, which explicitly covers PLA+.",
        },
        {
            "material": "TPU 95A", "print_temp": "210–240°C", "bed_temp": "35–60°C",
            "enclosure": "No", "ams_compat": "No", "drying_required": "Yes",
            "drying": "50°C / 8h",
            "notes": "Cardboard spool. External-spool-only on Bambu AMS regardless of adapter ring, same as every other brand's TPU in this catalog. 7-color line, only 4/7 hex confirmed this pass (Black/White/Grey/Red) — Blue/Green/Translucent use different color names than the source swatch's PLA-line entries, not assumed identical.",
        },
        {
            "material": "ASA", "print_temp": "240–260°C", "bed_temp": "75–95°C",
            "enclosure": "Yes", "ams_compat": "⚠", "drying_required": "Yes",
            "drying": "70°C / 8h",
            "notes": "Cardboard spool — AMS Adapter Ring required; AMS Lite incompatible (open-frame). Real 6-color line (Deep Black, White, Blue, ASA Green, Grey, Red) — this catalog originally assumed 12 colors in error, corrected 2026-09-23. Deep Black uses a colorimeter-measured hex, not the flat nominal value most retailers list.",
        },
        {
            "material": "PETG (Rapid)", "print_temp": "240–270°C", "bed_temp": "65–75°C",
            "enclosure": "No", "ams_compat": "⚠", "drying_required": "Yes",
            "drying": "65°C / 8h",
            "notes": "Cardboard spool — AMS Adapter Ring required. 12-color line, 8/12 hex confirmed. Yellow deliberately left unresolved — two different manufacturer-sourced listings gave conflicting hex for this exact color, not resolved without a physical-spool tiebreaker.",
        },
        {
            "material": "PLA Pro", "print_temp": "190–230°C", "bed_temp": "35–65°C",
            "enclosure": "No", "ams_compat": "⚠", "drying_required": "Recommended",
            "drying": "55°C / 6h",
            "notes": "Cardboard spool — AMS Adapter Ring required. 14-color line, only 1/14 hex confirmed this pass (Burgundy Red) — this line proved unusually hard to source per-color data for; worth a dedicated follow-up pass.",
        },
    ],
}


def _el_asa(color, hex_, sku_sfx, measured=None, notes=""):
    hex_note = (f"Hex: colorimeter-MEASURED value used (#{measured}), which differs from "
                f"the nominal/listed #{hex_} — measured value preferred as higher confidence "
                "(3dfilamentprofiles.com)" if measured else
                "Hex: manufacturer-listed value (3dfilamentprofiles.com)" if hex_ != "999999" else
                "Hex: unconfirmed placeholder")
    return dict(material_type="ASA", sku=f"EL-ASA-{sku_sfx}", product_name="Elegoo ASA",
                color_name=color, color_hex=(measured or hex_), diameter="1.75mm",
                diameter_tolerance="±0.03mm", spool_type="Cardboard", ams_adapter="Yes",
                print_temp="240–260°C", bed_temp="75–95°C", drying="70°C / 8h",
                ams_xp="⚠", ams_lite="✗", ams_2pro="⚠", ams_ht="⚠",
                tier="A" if hex_ != "999999" else "C",
                tier_rationale=("Color and official 6-color line count confirmed "
                                 "(us.elegoo.com official product page — this catalog "
                                 "originally assumed a 12-color line; corrected to the real "
                                 "6-color line this pass: Deep Black, White, Blue, ASA Green, "
                                 "Grey, Red); hex via 3dfilamentprofiles.com"
                                 if hex_ != "999999" else
                                 "PLACEHOLDER — color and official 6-color line count "
                                 "confirmed (us.elegoo.com) but hex not found on "
                                 "3dfilamentprofiles.com or any other source checked this pass"),
                notes=(notes + " | " if notes else "") +
                      "Cardboard spool — AMS Adapter Ring required for all AMS variants; "
                      "enclosure recommended (ASA); AMS Lite ✗ (open-frame, no ASA support) | " +
                      hex_note)

def _el_rapetg(color, hex_, sku_sfx, notes=""):
    return dict(material_type="PETG (Rapid)", sku=f"EL-RPETG-{sku_sfx}",
                product_name="Elegoo Rapid PETG",
                color_name=color, color_hex=hex_, diameter="1.75mm",
                diameter_tolerance="±0.02mm", spool_type="Cardboard", ams_adapter="Yes",
                print_temp="240–270°C", bed_temp="65–75°C", drying="65°C / 8h",
                ams_xp="⚠", ams_lite="⚠", ams_2pro="⚠", ams_ht="⚠",
                tier="A" if hex_ != "999999" else "C",
                tier_rationale=("Color and official 12-color line count confirmed "
                                 "(us.elegoo.com official product page); hex and temps via "
                                 "3dfilamentprofiles.com per-color detail pages"
                                 if hex_ != "999999" else
                                 "PLACEHOLDER — color and official 12-color line count "
                                 "confirmed (us.elegoo.com) but hex not found on "
                                 "3dfilamentprofiles.com or any other source checked this pass"),
                notes=(notes + " | " if notes else "") +
                      "Cardboard spool — AMS Adapter Ring required for all AMS variants | " +
                      ("Hex: manufacturer-listed value (3dfilamentprofiles.com)"
                       if hex_ != "999999" else "Hex: unconfirmed placeholder"))


ELEGOO["catalog"].extend([
    # ── ASA (6 colors — us.elegoo.com official; CORRECTED 2026-09-23, this
    # catalog originally assumed a 12-color line based on a misread bundle
    # listing — the real official line is 6 colors) ─────────────────────────
    _el_asa("Deep Black", "000000", "BK", measured="101A25",
            notes="Manufacturer lists this as \"Deep Black\"; colorimeter-measured RGB (#101A25, a dark navy-black) differs meaningfully from the nominal listed #000000"),
    _el_asa("White",      "FFFFFF", "WH"),
    _el_asa("Blue",       "0C2388", "BL"),
    _el_asa("ASA Green",  "00CC33", "GN"),
    _el_asa("Grey",       "999999", "GY"),
    _el_asa("Red",        "D61212", "RD"),

    # ── Rapid PETG (12 colors — us.elegoo.com official) ────────────────────
    _el_rapetg("Black",       "000000", "BK"),
    _el_rapetg("White",       "FFFFFF", "WH"),
    _el_rapetg("Blue",        "0000FF", "BL"),
    _el_rapetg("Green",       "00CC33", "GN"),
    _el_rapetg("Red",         "EA140E", "RD"),
    _el_rapetg("Orange",      "FFA500", "OR"),
    _el_rapetg("Yellow",      "999999", "YL",
               notes="AMBIGUOUS — two different 3dfilamentprofiles.com detail pages give conflicting confirmed hex for this exact color (#FFEF47 vs #FFFF00); not resolved without a tiebreaker (e.g. checking a physical spool), left as placeholder rather than guessing between them"),
    _el_rapetg("Space Grey",  "616161", "SPG"),
    _el_rapetg("Transparent", "F7F7F8", "TR"),
    _el_rapetg("Grey",        "999999", "GY"),
    _el_rapetg("Brown",       "999999", "BR"),
    _el_rapetg("Beige",       "999999", "BEI"),
])


def _el_plapro(color, hex_, sku_sfx, notes=""):
    return dict(material_type="PLA Pro", sku=f"EL-PLAPRO-{sku_sfx}",
                product_name="Elegoo PLA Pro",
                color_name=color, color_hex=hex_, diameter="1.75mm",
                diameter_tolerance="±0.02mm", spool_type="Cardboard", ams_adapter="Yes",
                print_temp="190–230°C", bed_temp="35–65°C", drying="55°C / 6h",
                ams_xp="⚠", ams_lite="⚠", ams_2pro="⚠", ams_ht="⚠",
                tier="A" if hex_ != "999999" else "C",
                tier_rationale=("Color and official 14-color line count confirmed "
                                 "(us.elegoo.com official product page); print/bed temps "
                                 "confirmed via SpoolScout TDS (190-230°C / 35-65°C); hex "
                                 "via 3dfilamentprofiles.com's \"PLA+/Pro Pro\" sub-tier "
                                 "listing, which is their categorization specifically for "
                                 "this Elegoo product line (distinct from their \"Basic\", "
                                 "\"HF\", and \"High Speed\" sub-tiers, which are different "
                                 "products not used here)"
                                 if hex_ != "999999" else
                                 "PLACEHOLDER — color and official 14-color line count "
                                 "confirmed (us.elegoo.com) but hex not found this pass; this "
                                 "line proved genuinely hard to find per-color data for, "
                                 "unlike most other Elegoo lines this session — multiple "
                                 "searches mostly surfaced other 3dfilamentprofiles.com "
                                 "sub-tiers (Basic/HF/High Speed) for this same material "
                                 "family, not the \"Pro\" sub-tier that matches this product"),
                notes=(notes + " | " if notes else "") +
                      "Cardboard spool — AMS Adapter Ring required for all AMS variants | " +
                      ("Hex: manufacturer-listed value (3dfilamentprofiles.com)"
                       if hex_ != "999999" else "Hex: unconfirmed placeholder"))


ELEGOO["catalog"].extend([
    # ── PLA Pro (14 colors — us.elegoo.com official) ────────────────────────
    # Hard bucket: only 1/14 hex resolved this pass despite multiple search
    # attempts — 3dfilamentprofiles.com's search results kept surfacing their
    # Basic/HF/High Speed sub-tiers instead of the "Pro" sub-tier that actually
    # matches this Elegoo product.
    _el_plapro("Black",       "999999", "BK"),
    _el_plapro("White",       "999999", "WH"),
    _el_plapro("Burgundy Red","990000", "BGR"),
    _el_plapro("Blue",        "999999", "BL"),
    _el_plapro("Light Blue",  "999999", "LBL"),
    _el_plapro("Green",       "999999", "GN"),
    _el_plapro("Yellow",      "999999", "YL"),
    _el_plapro("Grey",        "999999", "GY"),
    _el_plapro("Purple",      "999999", "PU"),
    _el_plapro("Silver",      "999999", "SV"),
    _el_plapro("True Red",    "999999", "TRD"),
    _el_plapro("Neon Green",  "999999", "NGN"),
    _el_plapro("Beige",       "999999", "BEI"),
    _el_plapro("Hot Pink",    "999999", "HPK"),
])


if __name__ == "__main__":
    pattern  = r'^Elegoo_filaments_v3_(\d+)\.xlsx$'
    template = 'Elegoo_filaments_v3_{n}.xlsx'
    path, version, prev = next_versioned_path(OUTPUT_DIR, pattern, template)

    wb = build_workbook(ELEGOO)
    wb.save(path)
    n_cat = len(ELEGOO["catalog"])
    print(f"✓  {os.path.basename(path)}  ({n_cat} catalog entries)")
    print(f"   Written to: {path}")
    if prev:
        print(f"   ⚠  Delete old version from the repo after uploading: {prev}")
