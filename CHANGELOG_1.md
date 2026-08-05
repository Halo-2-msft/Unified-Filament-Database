# Changelog — Filament Reference System

## 2026-08-02 — Inventory schema extension + Reflex Blue resolution

### Added
- **New Inventory columns** in `build_inventory.py` / `Filament_Inventory.xlsx`: `Package Type`, `Net Weight (g)`, `Est. Remaining (g)`, `Est. Remaining %` — inserted between `Last Dried Date` and `Notes`. Schema is now 25 columns (A–Y), matching the structure of the user's `Filament_Inventory_v1b.xlsx` working copy.
- `Est. Remaining %` formula (`=IF(V="","",IF(U="","",V/U))`) on both populated rows and the 50-row headroom pool.
- `Package Type` dropdown data validation (`Spool,Refill`).
- Number formats for the three new numeric columns (`#,##0`, `#,##0`, `0.0%`).
- `__main__` JSON-loading block now passes `Package Type`, `Net Weight (g)`, and `Est. Remaining (g)` through from `real_inventory.json` — previously these keys would have been silently dropped even if present in the JSON.

### Fixed
- **Bambu Lab PETG Basic "Blue" resolved to Reflex Blue** (`SKU: BL-PETG-RFB`, `Hex: #001489`) per user confirmation. The uploaded `v1b` working copy had regressed this back to an unresolved `"Blue"` with blank SKU and a 3-way ambiguity note (Reflex Blue / Navy Blue / Misty Blue) — that note is now cleared since it's resolved.
- **Material Type corrected** for two SUNLU inventory rows that were carrying the raw/ambiguous label `"PLA 2+"`:
  - `SL-PLAP-02` (White) → `PLA+` (correct catalog line for this SKU)
  - `SL-PLAP2-01` (Black) → `PLA+ 2.0` (separate catalog line)
- **Product Name corrected** to catalog-canonical form for SUNLU rows (e.g. `"PETG"` → `"SUNLU PETG"`, `"PLA"` → `"SUNLU PLA"`).

### Regenerated
- `real_inventory.json` rebuilt from `Filament_Inventory_v1b.xlsx` (25 entries) with the Blue fix applied on top.
- `Filament_Inventory.xlsx` regenerated via `build_inventory.py` as a validation artifact.

### Verified
- Ran `build_inventory.py` end-to-end against the new JSON — no errors, header row matches `v1b` exactly, formulas match `v1b` exactly (including on the Reflex Blue row), swatch fill renders `#001489` correctly.
- Confirmed `master_index.py`'s inventory ingestion (SKU-based phantom-row filter, `Reorder Flag`/`Color Swatch`/`Total Value` column drop) is compatible with the new 25-column schema — **no changes needed there**.
- Confirmed Dashboard sheet formulas (Total Spools, Total Inventory Value, Items at Reorder Point, by-Brand breakdown) are unaffected — `Quantity in Stock` / `Reorder Flag` / `Price Paid` stayed at columns N / O / M, so nothing downstream needed to shift.

---

## Prior: 2026-07-23 — Inventory split from per-brand workbooks
- On-hand inventory separated out of the 11 per-brand `Inventory Tracker` sheets into a standalone `build_inventory.py` → `Filament_Inventory.xlsx`, avoiding the "phantom template row" bug class from the old 700-row-per-brand headroom.
- `master_index.py` updated to read the standalone inventory file instead of per-brand sheets.

---

---

## 2026-08-03 — Config version bump + fresh master index

### Fixed
- `Config!$B$4` "File Version" in `build_inventory.py` was still hardcoded `"v1"` despite the 2026-08-02 schema extension. Bumped to `"v2"` with a note documenting what changed (`Package Type` / `Net Weight (g)` / `Est. Remaining (g)` / `Est. Remaining %`).

### Regenerated
- `Filament_Inventory.xlsx` rebuilt with the version bump.
- **`master_index.xlsx` regenerated fresh** — ran the full pipeline (`generate_all.py` + `generate_azurefilm.py` + `generate_voxelpla.py` + `build_inventory.py` + `master_index.py`) end-to-end with zero errors. Supersedes the stale `master_index_11_8.xlsx`, which predated the schema change, the Reflex Blue fix, and the SUNLU Material Type corrections. New totals: 1,172 catalog rows across all 11 brands, 25 inventory rows.

### Found (not fixed — data gap, not a bug)
- **SUNLU "Lavender Purple" PETG** (`SL-PETG-16`) has hex `#999999` — per this project's convention that's an unconfirmed catalog placeholder, not a real color. Flagged in the user's own `v1b` notes. Lives in `SUNLU_filaments_v3_10.xlsx`, not the inventory; needs a real color reference to resolve.

---

## Pending / Open Items

1. **SKU discrepancy unresolved** — SUNLU PLA+ 2.0 White is recorded as `SL-PLAP-02` (user-entered) vs. `SL-PLAP2-02` (catalog's naming convention for that line). Needs a look at the physical spool label.
2. **Two sources of truth risk** — the user hand-edits `Filament_Inventory.xlsx` directly, while `build_inventory.py` generates that same file from `real_inventory.json`. These will drift again unless one is designated canonical, or the xlsx is re-diffed into the JSON after each manual edit.
3. **Deliverables not yet in the project** — `build_inventory.py`, `real_inventory.json`, `Filament_Inventory.xlsx`, and `master_index.xlsx` currently live only in this session's output folder. `/mnt/project/` is read-only from here, so these need to be manually placed into the actual project directory (replacing `master_index_11_8.xlsx`) to take effect for future script runs.
4. **SUNLU "Lavender Purple" PETG hex is an unconfirmed placeholder** (`#999999`) — see above; needs a real color sample to fix at the catalog level.
5. **`Est. Remaining (g)` / `Est. Remaining %` sparsely populated** — currently only set for the one partially-used spool (SUNLU PETG White, ~10.2% remaining). Other "Opened" rows (e.g. Bambu PLA Basic Light Gray) don't yet have a remaining-weight estimate, so those cells render blank until weighed.
