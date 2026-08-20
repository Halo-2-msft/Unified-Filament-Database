"""
generate_voxelpla.py — VoxelPLA filament workbook
Sources:
  - voxelpla.com product listings (confirmed SKUs + colors)
  - voxelpla.com/pages/preset-and-profiles (print settings)
  - filamentcheatsheet.com/brands/voxel_pla/ (tier/quality assessment)
  - filamentcolors.xyz (hex approximations for unconfirmed colors)
Run: python generate_voxelpla.py
"""

import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from template_v3 import build_workbook

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ── Print settings (from voxelpla.com/pages/preset-and-profiles) ─────────────
# PLA+ HS / Bambu: Use Bambu PLA Basic profile — no changes needed
# PETG+ HS / Bambu: Use Bambu PETG HF preset, raise nozzle temp to 265°C

_VX_PLA_PRINT  = "200–210°C"   # Manufacturer TDS (Bowden & Direct extruder both spec this range) — corrected 2026-08-18, was assumed from "Bambu PLA Basic, no changes needed"
_VX_PLA_BED    = "45–60°C"     # Manufacturer TDS — corrected 2026-08-18, prior 35–45°C was an unverified assumption, ran ~10–15°C low
_VX_PLA_DRY    = "55°C / 6h"

_VX_PETG_PRINT = "235–265°C"   # PETG HF preset + raise nozzle to 265°C per VoxelPLA; confirmed within mfr TDS range (230–260°C)
_VX_PETG_BED   = "65–75°C"     # Confirmed within mfr TDS range (60–80°C)
_VX_PETG_DRY   = "65°C / 6h"

# Manufacturer TDS mechanical data (VOXELPLA+ (PRO) TDS, VOXELPETG+ (PRO) TDS — both
# sourced directly 2026-08-18, GB/T test methodology). Not currently exposed as
# catalog columns (no mechanical-properties field in template_v3 schema), but
# recorded here for tier_rationale citation and available for a future schema
# addition if wanted.
_VX_PLA_HDT_C  = 53   # Heat Distortion Temperature, GB/T 1634
_VX_PETG_HDT_C = 72   # Heat Distortion Temperature, GB/T 1634
# SDS on file for both (VOXELPLA+ (PRO), VOXELPETG+ (PRO)): no classified hazards,
# no PEL/TLV limits, standard PLA/PETG combustion-product profile. Nothing
# print-workflow-relevant beyond what's already in the expert guide's general
# material sections.

_VX_PLA_R  = ("USA-made; 250-machine farm-tested; HS rated to 400mm/s; "
               "print/bed temps per manufacturer TDS (200–210°C / 45–60°C), sourced "
               "2026-08-18 — corrects prior assumption that stock Bambu PLA Basic "
               "profile needed no changes; HDT 53°C (GB/T 1634)")
_VX_PETG_R = ("USA-made; 250-machine farm-tested; PETG+ formulation with "
               "special additives; use Bambu PETG HF profile + raise nozzle to 265°C; "
               "print/bed temps confirmed within manufacturer TDS range (230–260°C / "
               "60–80°C), sourced 2026-08-18; HDT 72°C (GB/T 1634)")
_VX_GAL_R  = ("Galaxy glitter PETG+; sparkle-particle variant of PETG+ HS; "
               "USA-made; same print settings as PETG+ HS")
_VX_GALPLA_R = ("Galaxy glitter PLA+; sparkle-particle variant of PLA+ HS; "
               "USA-made; same print settings as PLA+ HS")

_NOTES_TIER = ("Tier B: good chemistry and HS-rated but TrustPilot reports "
                "shipping delays, occasional broken spools, and color-batch "
                "mismatch — verify spool condition on arrival")

def _vx_pla(color, hex_, sku_sfx, notes=""):
    return dict(
        material_type="PLA+ HS",
        sku=f"VX-PLAP-{sku_sfx}",
        product_name="VOXELPLA+ HS",
        color_name=color,
        color_hex=hex_,
        diameter="1.75mm",
        diameter_tolerance="±0.03mm",
        spool_type="Plastic",
        ams_adapter="No",
        print_temp=_VX_PLA_PRINT,
        bed_temp=_VX_PLA_BED,
        drying=_VX_PLA_DRY,
        ams_xp="✓", ams_lite="✓", ams_2pro="✓", ams_ht="✓",
        tier="B",
        tier_rationale=_VX_PLA_R,
        notes=notes or _NOTES_TIER,
    )

def _vx_petg(color, hex_, sku_sfx, notes=""):
    return dict(
        material_type="PETG+ HS",
        sku=f"VX-PETG-{sku_sfx}",
        product_name="VOXELPETG+ HS",
        color_name=color,
        color_hex=hex_,
        diameter="1.75mm",
        diameter_tolerance="±0.03mm",
        spool_type="Plastic",
        ams_adapter="No",
        print_temp=_VX_PETG_PRINT,
        bed_temp=_VX_PETG_BED,
        drying=_VX_PETG_DRY,
        ams_xp="✓", ams_lite="✓", ams_2pro="✓", ams_ht="✓",
        tier="B",
        tier_rationale=_VX_PETG_R,
        notes=notes or "Bambu PETG HF profile + raise nozzle to 265°C; " + _NOTES_TIER,
    )

def _vx_gal(color, hex_, sku_sfx):
    return dict(
        material_type="Galaxy PETG+ HS",
        sku=f"VX-GALP-{sku_sfx}",
        product_name="VOXEL GALAXY PETG+ HS",
        color_name=color,
        color_hex=hex_,
        diameter="1.75mm",
        diameter_tolerance="±0.03mm",
        spool_type="Plastic",
        ams_adapter="No",
        print_temp=_VX_PETG_PRINT,
        bed_temp=_VX_PETG_BED,
        drying=_VX_PETG_DRY,
        ams_xp="✓", ams_lite="✓", ams_2pro="✓", ams_ht="✓",
        tier="B",
        tier_rationale=_VX_GAL_R,
        notes=("Glitter/sparkle particle variant; same print settings as PETG+ HS; "
               "slightly abrasive — monitor nozzle wear at high volumes"),
    )

def _vx_galpla(color, hex_, sku_sfx):
    return dict(
        material_type="Galaxy PLA+ HS",
        sku=f"VX-GALPLA-{sku_sfx}",
        product_name="VOXEL GALAXY PLA+ HS",
        color_name=color,
        color_hex=hex_,
        diameter="1.75mm",
        diameter_tolerance="±0.03mm",
        spool_type="Plastic",
        ams_adapter="No",
        print_temp=_VX_PLA_PRINT,
        bed_temp=_VX_PLA_BED,
        drying=_VX_PLA_DRY,
        ams_xp="✓", ams_lite="✓", ams_2pro="✓", ams_ht="✓",
        tier="B",
        tier_rationale=_VX_GALPLA_R,
        notes=("Glitter/sparkle particle variant; same print settings as PLA+ HS; "
               "slightly abrasive — monitor nozzle wear at high volumes | "
               "Line confirmed real 2026-08-18 (own voxelpla.com product page, "
               "own SKU, $24.99 — matches Galaxy PETG+ HS pricing tier); currently "
               "shows Sold Out on voxelpla.com. Hex: unconfirmed — no colorimeter "
               "measurement found for this PLA+ line specifically. Do NOT assume "
               "identical to Galaxy PETG+ HS hex despite matching color name — "
               "different material, not independently verified."),
    )


VOXELPLA = {
    "brand": "VoxelPLA",
    "catalog": [

        # ── VOXELPLA+ HS ──────────────────────────────────────────────────────
        # Core 5 (confirmed 'Main Items' on voxelpla.com):
        _vx_pla("Voxel Black",      "111111", "BK"),
        _vx_pla("Cool White",       "F5F5F5", "CW"),
        _vx_pla("Voxel Grey",       "808080", "GY"),
        _vx_pla("Fire Engine Red",  "CC1010", "FER"),
        _vx_pla("Royal Blue",       "0047AB", "RB"),
        # Extended PLA+ HS lineup (confirmed from voxelpla.com product pages):
        _vx_pla("Fire Orange",      "F56816", "FOR"),
        _vx_pla("Forest Green",     "228B22", "FG"),
        _vx_pla("Ice Clear",        "D8EEF8", "IC",
                notes="Translucent/clear variant; " + _NOTES_TIER),
        _vx_pla("Lavender Purple",  "9B7EC8", "LP"),
        _vx_pla("Yellow",           "F5C518", "YL"),
        _vx_pla("Brown",            "6B3A2A", "BR"),
        _vx_pla("Phantom Blue",     "2A5CAA", "PB"),
        _vx_pla("Silver",           "C0C0C0", "SV"),
        _vx_pla("Army Green",       "4A5240", "AG",
                notes="FLAG 2026-08-18: 3dfilamentprofiles.com colorimeter "
                      "measurement shows #667B65 for this exact product/color, "
                      "differing from catalog's #4A5240 — not re-verified or "
                      "corrected this pass, needs follow-up"),
        _vx_pla("Dark Purple",      "4B0082", "DPU"),
        _vx_pla("Pink",             "FF69B4", "PK"),
        _vx_pla("Wood",             "A0785A", "WD",
                notes=("Wood-composite filler; slightly abrasive — monitor nozzle; "
                       + _NOTES_TIER)),
        _vx_pla("Witch Green",      "2D5A2D", "WG"),
        _vx_pla("Sky Blue",         "87CEEB", "SKB"),
        _vx_pla("Gold",             "D4A017", "GD"),
        _vx_pla("Magenta",          "CC0077", "MA"),
        _vx_pla("Gunmetal Blue",    "3D5A80", "GMB"),
        _vx_pla("Champagne Beige",  "E8D5B0", "CHB"),
        _vx_pla("Turquoise",        "00B4B4", "TQ"),
        _vx_pla("Light Brown",      "C4956A", "LBR"),
        _vx_pla("Dark Brown",       "3D1C02", "DBR"),
        _vx_pla("Eggshell White",   "F0EAD6", "ESW"),
        _vx_pla("Skin",             "FFCC99", "SK"),
        _vx_pla("Mint Green",       "999999", "MG",
                notes="Confirmed real 2026-08-18 (own voxelpla.com product page, "
                      "own SKU); currently shows Sold Out on voxelpla.com. Not "
                      "found in 3dfilamentprofiles.com's High Speed listing (26 "
                      "items) as of this pass — likely not yet indexed there. "
                      "Hex: unconfirmed."),

        # ── VOXELPETG+ HS ─────────────────────────────────────────────────────
        # Confirmed from voxelpla.com PETG+ HS product pages:
        _vx_petg("Black",           "111111", "BK"),
        _vx_petg("White",           "F5F5F5", "WH"),
        _vx_petg("Grey",            "808080", "GY"),
        _vx_petg("Blue",            "0057A8", "BL"),
        _vx_petg("Red",             "CC1010", "RD"),
        _vx_petg("Crystal Clear",   "D8F0F8", "CC",
                 notes=("Transparent variant; use Bambu PETG HF + 265°C nozzle; "
                        + _NOTES_TIER)),
        _vx_petg("Silver",          "C0C0C0", "SV"),
        _vx_petg("Forest Green",    "228B22", "FG"),
        _vx_petg("Yellow",          "F5C518", "YL"),
        _vx_petg("Fire Orange",     "F56816", "FOR"),
        _vx_petg("Dark Purple",     "4B0082", "DPU"),
        _vx_petg("Teal",            "008080", "TEA"),

        # ── VOXEL GALAXY PETG+ HS ─────────────────────────────────────────────
        # Glitter/sparkle specialty PETG line:
        _vx_gal("Midnight Blue",    "1B2A4A", "MB"),
        _vx_gal("Emerald Gold",     "4A7C59", "EG"),
        _vx_gal("Gioiello Purple",  "5B2D8E", "GP"),
        _vx_gal("Aurora Green",     "1A5C3A", "AURG"),

        # ── VOXEL GALAXY PLA+ HS ──────────────────────────────────────────────
        # NEW LINE (added 2026-08-18) — glitter/sparkle specialty PLA+, confirmed
        # to exist via voxelpla.com "New Filaments" product grid; hex placeholders
        # pending research pass (see color-name-matched Galaxy PETG line for
        # reference hex, but NOT assumed identical — separate material, needs
        # independent verification per standing rule).
        _vx_galpla("Aurora Green",    "999999", "AURG"),
        _vx_galpla("Gioiello Purple", "999999", "GP"),
        _vx_galpla("Emerald Gold",    "999999", "EG"),
        _vx_galpla("Midnight Blue",   "999999", "MB"),
    ],

    "inventory": [],   # on-hand inventory now tracked separately in Filament_Inventory.xlsx

    "material_guide": [
        {
            "material":        "PLA+ HS",
            "print_temp":      "200–210°C",
            "bed_temp":        "45–60°C",
            "enclosure":       "No",
            "ams_compat":      "Yes",
            "drying_required": "Recommended",
            "drying":          "55°C / 6h",
            "notes": ("Manufacturer TDS (sourced 2026-08-18): Bowden retraction 60mm/s "
                      "/ 5mm, Direct-drive 50mm/s / 1mm, fan 100%. Rated 400mm/s. "
                      "HDT 53°C. Bed temp corrected from a prior unverified assumption "
                      "(was 35–45°C) — verify spool condition on arrival."),
        },
        {
            "material":        "PETG+ HS",
            "print_temp":      "235–265°C",
            "bed_temp":        "65–75°C",
            "enclosure":       "No",
            "ams_compat":      "Yes",
            "drying_required": "Yes",
            "drying":          "65°C / 6h",
            "notes": ("Bambu: use PETG HF preset + raise nozzle to 265°C per VoxelPLA. "
                      "Manufacturer TDS (sourced 2026-08-18) confirms range: Bowden "
                      "retraction 60mm/s / 6mm, Direct-drive 50mm/s / 1mm, fan 20%. "
                      "HDT 72°C. Must dry before printing. Textured PEI recommended."),
        },
        {
            "material":        "Galaxy PETG+ HS",
            "print_temp":      "235–265°C",
            "bed_temp":        "65–75°C",
            "enclosure":       "No",
            "ams_compat":      "Yes",
            "drying_required": "Yes",
            "drying":          "65°C / 6h",
            "notes": ("Same settings as PETG+ HS. Glitter particles slightly "
                      "abrasive — monitor nozzle wear at high print volumes."),
        },
        {
            "material":        "Galaxy PLA+ HS",
            "print_temp":      "190–220°C",
            "bed_temp":        "35–45°C",
            "enclosure":       "No",
            "ams_compat":      "Yes",
            "drying_required": "Recommended",
            "drying":          "55°C / 6h",
            "notes": ("NEW LINE — added 2026-08-18. Same settings as PLA+ HS. "
                      "Glitter particles slightly abrasive — monitor nozzle wear."),
        },
    ],
}


if __name__ == "__main__":
    wb   = build_workbook(VOXELPLA)
    path = os.path.join(OUTPUT_DIR, "VoxelPLA_filaments_v3.xlsx")
    wb.save(path)
    n_cat = len(VOXELPLA["catalog"])
    print(f"✓  VoxelPLA_filaments_v3.xlsx  ({n_cat} catalog entries)")
    print(f"   Written to: {path}")
