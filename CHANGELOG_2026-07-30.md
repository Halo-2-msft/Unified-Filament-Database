# Changelog — 2026-07-30

Session covering: personal inventory rebuild, master index bug fix, and a two-pass sanity check of catalog claims against manufacturer/retailer sources.

---

## 1. Personal inventory — `Filament_Inventory_v1a.xlsx` → `Filament_Inventory_v1b.xlsx`

- Replaced two ad hoc free-text columns with four structured ones: **Package Type** (Spool/Refill dropdown), **Net Weight (g)**, **Est. Remaining (g)**, **Est. Remaining %** (auto-calculated, amber-highlighted below the Config-sheet threshold).
- Filled in 24 of 25 missing SKUs by matching Brand + Material Type + Color Name against the brand catalog workbooks.
  - **Unresolved:** Bambu Lab PETG Basic "Blue" — no color literally named "Blue" in that line. Candidates left in the row's Notes: Reflex Blue (BL-PETG-RFB), Navy Blue (BL-PETG-NVB), Misty Blue (BL-PETG-MSB).
- Set Quantity in Stock to 1 for two rows that were blank (opened spools still on hand).
- Corrected the two SUNLU "PLA 2+" rows — SL-PLAP-02 is actually the "PLA+" line and SL-PLAP2-01 is the separate "PLA+ 2.0" line, not one shared "PLA 2+" designation.
- Updated SUNLU Product Name values to match brand-catalog convention ("SUNLU PETG" instead of bare "PETG", etc.).
- Added a Moisture Rating conditional format (Damp/Wet → amber highlight).
- **Correction made during the sanity check (see §3):** the Notes cell on the SUNLU "Oliver Green" row originally called this a likely catalog typo for "Olive Green." That was wrong — confirmed via store.sunlu.com that "Oliver Green" is SUNLU's actual official color name. Notes cell corrected.

## 2. Master index — `master_index.xlsx` / `master_index.py`

Bug: column filters were missing on both data sheets.

- **Catalog sheet:** `_build_catalog()` never called `ws.auto_filter.ref` at all.
- **Inventory sheet:** the filter range was set immediately after the header row, before any data rows existed — so it only ever covered `A2:S2` (just the header).

Fixed in both the actual workbook (in-place patch — no formulas exist in this file, so this was low-risk) and in `master_index.py` (moved the Inventory autofilter to after all rows are written; added the missing Catalog autofilter), so the bug won't reappear on the next full regeneration.

## 3. Catalog sanity check — pass 1 (spot-check of flagged/uncertain claims)

Checked a representative sample of entries marked `PLACEHOLDER` or `NEW LINE` against manufacturer and retailer sources.

**Confirmed accurate, no changes needed:**
- VoxelPLA — brand and catalog rationale (USA-made, 250-machine farm, TrustPilot complaints) match independent sources.
- Bambu Lab PAHT-CF — confirmed official successor to discontinued PA-CF, 194°C HDT matches.
- SUNLU PA6-CF (209°C) / PA12-CF (175°C) — both figures confirmed correct. The catalog's internal note had flagged these as "conflicting specs depending on source," which was a false alarm — see fix below.
- AzureFilm PC-ABS, Nylon, Flexible, Carbon Fiber lines — all confirmed to exist.

**Fixed — concrete errors:**

| File | Entry | Change |
|---|---|---|
| `AzureFilm_filaments_v3_6.xlsx` + `generate_azurefilm.py` | PLA Prime (AZ-PRIME-01) | Print temp 200–230°C → **230–265°C**; bed temp 50–60°C → **no heated bed required (0–60°C)** |
| `AzureFilm_filaments_v3_6.xlsx` + `generate_azurefilm.py` | PLA Matte (AZ-MAT-01) | Print temp 200–220°C → **205–255°C**; official name is "PLA Matte HS"; rationale corrected from "newer, less-documented" to established/actively-expanding (~13 colors confirmed, catalog still only carries Black — full color expansion flagged as a follow-up, not done to avoid guessing hex codes) |
| `AzureFilm_filaments_v3_6.xlsx` + `generate_azurefilm.py` | PC-ABS (AZ-PCABS-01) | Reformulated product: 250–270°C/90–110°C → **265–285°C/110°C**; heat resistance now up to 122°C |
| `Hatchbox_filaments_v3_9.xlsx` + `generate_all.py` | PLA MAX (HX-MAX-01) | Renamed **PLA MAX V2**; print temp 190–220°C → **190–210°C**; noted separate "PLA PRO+" line not yet in catalog |
| `filament_expert_guide_complete.md` §6.2 | SUNLU PA-CF note | Reworded — PA6-CF (209°C) and PA12-CF (175°C) aren't conflicting reports about one material, they're two different nylon grades. Both figures are correct; the guide had lumped them together in a way that read as an unresolved discrepancy. |
| `Filament_Inventory_v1b.xlsx` row 25 | "Oliver Green" note | Corrected — confirmed as SUNLU's real official color name, not a typo (see §1) |

## 4. Catalog sanity check — pass 2 (remaining flagged entries)

Went through the rest of the `PLACEHOLDER`/`NEW LINE` list — roughly 30 more entries across SUNLU, Polymaker, eSUN, Hatchbox, and Bambu Lab. **No new concrete errors found** — everything checked out as either already accurate or already appropriately hedged as an estimate.

Confirmed to exist (line-level, not exhaustively re-verified color-by-color):
- **SUNLU:** ASA (already Tier A / accurate), PA (Easy PA), PA-GF, PC, PC-ABS, ABS-GF, ABS-FR, ABS (Easy), PEEK. PEEK's temp class (390–420°C nozzle) matches multiple independent sources; exact bed/chamber/drying figures show genuine variance even across SUNLU's own pages, so left as-is rather than force an unconfirmed number.
- **Polymaker:** ASA, PA (PolyMide), PC (PolyMax) — existing catalog numbers and hedged rationale already reasonably accurate. Minor cosmetic note: Polymaker has since rebranded "PolyLite ASA" to "Polymaker ASA."
- **eSUN:** PETG-Basic, PETG+HS, PLA-HF, PLA-Lite, ABS-ESD, ASA+.
- **Hatchbox:** TPU, PC, PA (line existence only, not deep spec-checked).
- **Bambu Lab:** PLA Lite.

## Still open / not done

- **AzureFilm PLA Matte HS** — full ~13-color expansion (names known, hex codes not manufacturer-confirmed; adding rows would mean guessing swatch colors).
- **Bambu Lab PETG Basic "Blue"** SKU in the personal inventory — needs a manual pick between Reflex/Navy/Misty Blue.
- Individual color-list/hex verification for the ~25–30 lower-risk entries in pass 2 (SUNLU PLA Marble/Twinkling/Meta, eSUN PLA-Marble/PLA-Wood, Prusament/Creality Hyper/MatterHackers per-color hex accuracy, etc.) — line existence confirmed, but not checked color-by-color.
- SUNLU PEEK's exact bed/chamber/drying numbers — directionally right, not pinned to a single authoritative figure.

## Files touched today

- `Filament_Inventory_v1b.xlsx` (new)
- `master_index_11_8.xlsx`, `master_index.py`
- `AzureFilm_filaments_v3_6.xlsx`, `generate_azurefilm.py`
- `Hatchbox_filaments_v3_9.xlsx`
- `generate_all.py`
- `filament_expert_guide_complete.md`
