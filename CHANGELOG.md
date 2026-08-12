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

---

## 2026-08-04 — SUNLU hex code corrections (external verification)

### Fixed
Cross-referenced SUNLU's `#999999` "unconfirmed placeholder" catalog entries against an independent, community-maintained filament-tracking site (3dfilamentprofiles.com). Applied 15 corrections directly in `generate_all.py`'s SUNLU catalog dict (source of truth), then regenerated `SUNLU_filaments_v3.xlsx` and `master_index.xlsx`:

| SKU | Color | Old | New |
|---|---|---|---|
| `SL-PETG-16` | Lavender Purple(Purple) | `#999999` | `#685BC7` |
| `SL-PETG-28` | Cherry Red | `#999999` | `#FC6D5C` |
| `SL-PETG-27` | Chocolate | `#999999` | `#793D00` |
| `SL-PETG-17` | Magenta | `#999999` | `#BA1976` |
| `SL-PETG-30` | Mint Green | `#999999` | `#33F6D8` |
| `SL-PETG-25` | Sakura Pink | `#999999` | `#FFBAC3` |
| `SL-PETG-26` | Sky Blue | `#999999` | `#3AD6EF` |
| `SL-PETG-20` | Transparent Blue | `#999999` | `#001EFF` (mfr RGB; colorimeter-measured `#30477C` differs — noted in Notes) |
| `SL-PETG-21` | Transparent Green | `#999999` | `#0DFD55` (mfr RGB; colorimeter-measured `#A0BC4B` differs — noted in Notes) |
| `SL-PETG-24` | Transparent Orange | `#999999` | `#FDB958` |
| `SL-PETG-22` | Transparent Purple | `#999999` | `#BE38F3` |
| `SL-PETG-23` | Transparent Red | `#999999` | `#FF4747` |
| `SL-PLA-10` | Cherry Red | `#999999` | `#FF615F` |
| `SL-PLA-13` | Lemon Yellow | `#999999` | `#FBE988` |
| `SL-PLA-09` | Mint Green | `#999999` | `#59D9AA` |

Verified all 15 fixes landed correctly in the regenerated workbook (hex value + swatch fill color) before shipping.

### Key learning
Discovered that SUNLU's own third-party-tracked hex values **differ across material lines for the same color name** — e.g. "Lavender Purple" is `#685BC7` for PETG but `#A54DCF` for PLA on the same tracking site. Confirms the project's existing caution against inferring one material line's hex from a sibling line; each `(Material Type, Color Name)` pair needs its own independent lookup.

### Still open (not resolved this pass)
- `SL-PETG-08` Orange — source site has two conflicting listings (`#FF6A00` vs `#FF7300`) with no way to tell which matches our SKU.
- `SL-PETG-12` Roasted Chestnut — no PETG Basic-line match found (only "Roasted Chestnut **Black**," a different named color, exists for PLA/PLA+ lines).
- `SL-PETG-07` Clear(Transparent) — ambiguous against "Elite Transparent" vs. a plain "Transparent" listing.
- `SL-PLA-27` Grass Green — two conflicting third-party listings (`#00818A` vs `#11B07B`).
- `SL-PLA-15` Orange, `SL-PLA-18` Sakura Pink, `SL-PLA-20` Sky Blue — not yet checked (didn't fetch page 2 of the PLA Basic listing).
- ~65 other `#999999` entries across niche lines (Marble, Galaxy, TPU Silk, Silk Multi-Color, Matte Dual-Color, Twinkling) — not checked; unlikely to be tracked on these sites given how niche they are.

---

## 2026-08-04 (cont.) — xlsx → JSON sync tooling

### Added
- **`sync_inventory_json.py`** — the mirror image of `build_inventory.py`. Reads `Filament_Inventory.xlsx` and writes `real_inventory.json`, replacing the manual re-parsing that's been done by hand for every prior xlsx update in this project (`v1a`, `v1b`, and the schema-extension pass).
  - Imports `INV_HEADERS` directly from `build_inventory.py` so it automatically tracks future schema changes instead of silently dropping new columns.
  - Filters headroom/phantom rows using `Brand` as the required column, matching this project's own stated convention.
  - Drops derived/formula columns (`Color Swatch`, `Reorder Flag`, `Total Value`, `Est. Remaining %`) — never treats computed output as source data.
  - **Prints a human-readable diff** against the previous `real_inventory.json` before overwriting it (added / removed / changed-field rows) — this automates the exact row-by-row comparison that was done by hand between `v1a` and `v1b`.
  - **Self-validates**: after writing, re-imports `build_inventory.py` and actually builds a workbook from the fresh JSON in a scratch directory, so a schema mistake is caught immediately rather than on the next real run.

### Verified
Ran 4 test scenarios before shipping:
1. Round-trip against the current `Filament_Inventory.xlsx` → correctly reports zero diff.
2. Simulated re-introducing the Reflex Blue → "Blue" regression (color name reverted + SKU blanked) → correctly surfaced as a stark add/remove pair, with the co-occurring quantity change preserved on the new row.
3. A same-key field edit (Price Paid) → correctly reported as a single "changed" line, not add/remove.
4. An unexpected extra column → warns clearly, doesn't crash, still reads the columns it recognizes.

### Impact on pending items
This directly mitigates **Pending Item #2** (two sources of truth) — the risk isn't eliminated (you can still forget to run it), but the manual, error-prone translation step is now a single deterministic command: `python3 sync_inventory_json.py`.

---

---

## 2026-08-04 (cont. 2) — Physical spool verification: SUNLU PLA+ 2.0 White SKU corrected

### Fixed
User photographed the physical spool label and outer box for the SUNLU White filament in question (`IMG_0209.JPG`, `IMG_0210.JPG`). Both clearly read **"PLA+2.0"**, which overturns the 2026-08-02 fix:

| | 2026-08-02 fix (now known wrong) | Corrected 2026-08-04 |
|---|---|---|
| SKU | `SL-PLAP-02` | **`SL-PLAP2-02`** |
| Material Type | `PLA+` | **`PLA+ 2.0`** |
| Product Name | `SUNLU PLA+` | **`SUNLU PLA+ 2.0`** |

The 2026-08-02 fix had reassigned this row to the catalog's separate plain-`PLA+` line based on an ambiguous user-typed SKU (missing the `2`) — reasonable at the time given the available data, but wrong. Physical label evidence takes priority over inferred/typed data. `real_inventory.json` updated, `Filament_Inventory.xlsx` and `master_index.xlsx` regenerated and spot-checked in the rebuilt workbook before shipping.

### Impact on pending items
**Resolves Pending Item #1** (the SKU discrepancy) — fully closed, no longer open.

---

---

## 2026-08-05 — Deployment verified, repo cleanup, first real weight measurements

### Deployed and verified
- `.github/workflows/sync-inventory.yml` is live and confirmed working end-to-end: pushing `Filament_Inventory_v4.xlsx` triggered the Action, which ran `sync_inventory_json.py` and auto-committed the result — visible in the repo as an `actions-user` commit (`chore: auto-sync real_inventory.json from Filament_Inventory_v4.xlsx`). **Pending Item #2 (two sources of truth) is now genuinely closed**, not just mitigated — first real-world proof it works, not just local test scenarios.
- Debugged an initial "No event triggers defined in `on`" workflow failure — traced to the workflow file arriving in the repo empty (0 bytes), not a YAML syntax problem. Root cause: files delivered here don't overwrite on repeat download, so the local Downloads folder had been silently accumulating numbered duplicates (`CHANGELOG.md`, `CHANGELOG (1).md`, `CHANGELOG (2).md`, etc.) — likely the same mechanism that emptied the workflow file. Fixed by pasting the file content directly into GitHub's web editor.

### Repo cleanup
- Confirmed via direct GitHub file-listing screenshots (not assumption) that the repo now holds exactly one current version of every file:
  - Deleted duplicates: `Filament_Inventory_v2.xlsx`, `Filament_Inventory_v3.xlsx`, `SUNLU_filaments_v3_10.xlsx`, `master_index_11_8.xlsx`, `master_index_11_9.xlsx`, three duplicate CHANGELOG files (`CHANGELOG_1.md`, `CHANGELOG_2026-07-30.md`, `CHANGELOG_3.md`), and a leftover `commit_message.txt`.
  - **Version lineage confirmed continuous across sessions** — a `commit_message.txt` recovered from an earlier session (predating this changelog) showed that session had left every brand catalog at `_v3_9` and `master_index` at `_11_7`; this session picked up cleanly at `_v3_10`/`_11_8` with no gaps or overlaps.
- **Pending Item #3 (deliverables in the project) is now verified, not assumed** — confirmed by actually inspecting the live repo file listing rather than trusting that an upload succeeded.

### Fixed — real measured tare weights replace online estimates
User weighed empty spools directly rather than relying on the internet-sourced estimates from 2026-08-04:

| Brand | Online estimate | **Measured (authoritative)** | Difference |
|---|---|---|---|
| Bambu Lab | 256 g (third-party table) | **235 g** (spool + cardboard ring) | 21 g off |
| SUNLU | 133 g (third-party table) / ~197 g (uncertain eBay listing) | **210 g** (spool + cardboard ring) | 77 g / 13 g off |

Applied to the two currently-opened spools:
- **Bambu Lab PLA Basic Light Gray**: raw scale 1189g − 235g tare = **954g remaining (95.4%)**. (This also corrects a near-miss: an earlier edit had set `Net Weight (g)` to `977` — a raw scale reading mistakenly entered into the nominal-fill-weight field instead of `Est. Remaining (g)`. Caught before it reached `real_inventory.json`; `Net Weight (g)` restored to the nominal `1000`.)
- **SUNLU PETG White**: measured **20g remaining (2.0%)** — effectively empty, flagged in Notes as due for replacement.

Both `Est. Remaining (g)` values now reflect real measurements with documented tare weights (reusable for future spools of the same brand, though re-weighing an actual empty spool once one runs out remains the most reliable source over time).

### Impact on pending items
- **Pending Item #5 is resolved for both currently-tracked "Opened" rows.** No `Opened` spools remain with a blank `Est. Remaining (g)`. This isn't a one-time fix, though — it's an ongoing task every time a new spool gets opened, now backed by known-good tare weights instead of guesswork.

---

---

## 2026-08-08 — Inventory growth: 25 → 62 rows, two more SKU catches, conventions established

### Growth
Inventory expanded in two rounds as physical spools got added and weighed:
- Round 1: 25 → 39 rows (7 Bambu Lab PLA Basic colors, 3 SUNLU colors added; several bulk-quantity rows split into individually-trackable single-quantity rows so each physical spool can be weighed separately)
- Round 2: 39 → 62 rows (4 more opened spools, 6 sealed refills across 3 colors added)

### Fixed — same pattern as Reflex Blue/PLA+2.0, caught before it became a problem
Every batch of newly-added purchases has arrived with SKU (and once, Product Name) blank — expected, since the person's typing from the physical label, not looking up the catalog reference code. Caught and cross-referenced against the catalog both times:

- **Round 1:** `Bambu Lab / Indigo Purple` — SKU and Product Name both blank despite `Est. Remaining (g): 940` already being filled in (had been weighed, just not identified). Resolved to `BL-PLAB-IP`, `#482960`, Product Name `PLA Basic`.
- **Round 2:** 6 more colors, 10 rows total (3 of them duplicated across 2 refill bags each) — all resolved via **exact, unambiguous** catalog name matches (unlike the original "Blue" case, none of these had multiple candidates to choose between):

| Color | Material | SKU | Hex |
|---|---|---|---|
| Jade White | Bambu PLA Basic | `BL-PLAB-WH` | `#FFFFFF` |
| Yellow | Bambu PETG Basic | `BL-PETG-YL` | `#FCE300` |
| Cyan | SUNLU PETG | `SL-PETG-15` | `#00A3E0` |
| Red | Bambu PETG Basic | `BL-PETG-RD` | `#D6001C` |
| Blue | Bambu PLA Basic | `BL-PLAB-BL` | `#0A2989` |
| Gray | Bambu PLA Basic | `BL-PLAB-GY` | `#8E9089` |

Zero blank-SKU rows confirmed in both rebuilt workbooks before shipping.

### Conventions established (process decisions, not code changes)
- **`Package Type` graduation:** a `Refill` is tracked as `Refill` until it's physically loaded onto a spool, at which point it becomes `Spool`. Not two different physical objects being tracked — one row's `Package Type` value changes over its lifecycle.
- **Depleted spools: keep the row, zero it out, don't delete.** When a spool runs out with no refill on hand, set `Quantity in Stock` and `Est. Remaining (g)` to `0` and add a dated note (e.g. `"Depleted 2026-08-08, refill pending"`), rather than deleting the row. Preserves purchase history (Lot/Batch, Date Purchased, Price Paid) and avoids re-typing SKU/hex/Material Type from scratch later — the exact mistake that's been caught twice above. First applied to `Bambu Lab / Dark Gray`.

### Verified
- Second real-world proof of `sync-inventory.yml` working correctly: this time the person uploaded a manually-corrected `real_inventory.json` directly (rather than letting the bot generate it), and the workflow correctly recognized it already matched what the xlsx would produce — `"No changes to commit — xlsx and JSON already agree."` Confirms the diff logic itself is sound, not just that the bot can write files.

---

## 2026-08-11 — Version-aware file discovery: master_index.py no longer reads stale/hardcoded filenames

### Problem identified
`master_index.py` looked up each brand's catalog workbook (and the inventory workbook) via a hardcoded filename list — e.g. `Bambu_Lab_filaments_v3.xlsx` — while every actual file in the repo carries a version suffix (`Bambu_Lab_filaments_v3_10.xlsx`). Likewise, `generate_all.py`, `generate_azurefilm.py`, `generate_voxelpla.py`, and `build_inventory.py` all wrote to unversioned output filenames, requiring a manual rename step after every run. Any drift between the hardcoded names and what's actually in the repo would cause `master_index.py` to silently skip a brand (`"⚠ Not found, skipping"`) or aggregate a stale/wrong version — a failure mode that wouldn't surface until someone checked the dashboard totals against expectations.

### Added
- **`find_latest_version(directory, pattern)`** and **`next_versioned_path(directory, pattern, template)`** in `template_v3.py` — shared helpers that scan a directory for filenames matching a regex (one capture group = version number) and return either the current highest version found, or the *next* version to write. Both are pattern-agnostic, so they work across this project's three different versioning schemes (`_v3_N` for brand catalogs, `_vN` for inventory, `_11_N` for the master index).

### Changed
- **`generate_all.py`, `generate_azurefilm.py`, `generate_voxelpla.py`, `build_inventory.py`** — each now calls `next_versioned_path()` to auto-discover the current highest version of its own output and write the next one, instead of overwriting a fixed unversioned filename. Each prints a reminder identifying which old version to delete from the repo after uploading (e.g. `⚠ Delete old version from the repo after uploading: AzureFilm_filaments_v3_6.xlsx`), automating the existing versioning-hygiene habit rather than relying on memory.
- **`master_index.py`** — replaced the hardcoded `BRAND_FILES` list of exact filenames with `_latest_brand_file()` / `_latest_inventory_file()`, which look up the current highest-versioned file for each of the 11 brands and for the inventory workbook at read-time. The script's own output is now versioned too (`master_index_11_{N}.xlsx`), auto-incrementing from whatever's already in the output directory.
- **`build_inventory.py`** — the Config sheet's `File Version` field was hardcoded `"v1"` (stale since the 2026-08-03 bump to `"v2"`, per that changelog entry). Now set dynamically from the actual version number computed by `next_versioned_path()`, so it can't drift again.
- Fixed two leftover **"9 brand files"** references in `master_index.py`'s dashboard note and manual-rows divider — both now read the actual brand count (11) instead of a number left over from before the catalog grew.

### Verified
- Isolated unit tests on `find_latest_version` / `next_versioned_path`: empty directory (starts at version 1), one existing file (increments to 2), a gapped/out-of-order version present (e.g. only `_v3_10` exists — correctly jumps to `_v3_11`, not `_v3_2`), an unrelated brand name (returns none), and a nonexistent directory (returns none, doesn't crash).
- Full end-to-end run of `master_index.py` against copies of the actual current repo files (`Bambu_Lab_filaments_v3_10.xlsx`, `Overture_filaments_v3_12.xlsx`, `AzureFilm_filaments_v3_6.xlsx`, `Filament_Inventory_v2.xlsx`, `master_index_11_8.xlsx`, and all other current versions) — correctly found the exact current version for every one of the 11 brands despite uneven version numbers across brands, aggregated all 1,172 catalog rows + 15 inventory rows, and wrote `master_index_11_9.xlsx`, correctly incrementing past the pre-existing `_8`.
- Re-ran `generate_azurefilm.py` against a directory already containing `AzureFilm_filaments_v3_6.xlsx` — correctly wrote `AzureFilm_filaments_v3_7.xlsx` and flagged `_6` for deletion.
- Diffed the repo's live copies of `generate_azurefilm.py` and `generate_voxelpla.py` against the versions delivered — byte-for-byte identical, confirming no unintended drift before upload.

### Conventions established (process decision, not code)
- **Claude will not run any generator script (`generate_all.py`, `generate_azurefilm.py`, `generate_voxelpla.py`, `build_inventory.py`, `master_index.py`) without first confirming it has the current versioned files available as project uploads.** Version-detection depends on seeing the real current files — running against an empty or assumed working directory would silently reset version numbers or aggregate against stale/missing data. If current files aren't available in-session, Claude asks the user to upload them before running anything.

### Impact on pending items
Closes a latent risk that wasn't previously logged as a pending item: `master_index.py`'s hardcoded `BRAND_FILES` list could have silently gone stale the next time any brand's version number changed without a matching code update. That class of bug is now structurally impossible — the script always reads whatever is actually the highest-versioned file on disk.

---

## Pending / Open Items

1. ~~SKU discrepancy unresolved~~ — **RESOLVED 2026-08-04.** Physical spool/box photos confirmed `SL-PLAP2-02` / `PLA+ 2.0`.
2. ~~Two sources of truth risk~~ — **RESOLVED 2026-08-05.** `sync-inventory.yml` GitHub Action confirmed working in production, not just local tests — auto-commits `real_inventory.json` whenever the xlsx changes.
3. ~~Deliverables not yet in the project~~ — **RESOLVED and VERIFIED 2026-08-05** via direct repo file-listing inspection, including cleanup of accumulated duplicates.
4. **~70 SUNLU `#999999` placeholder hex values remain unresolved** — 15 were fixed 2026-08-04; 6 have known conflicting/ambiguous third-party source data; ~65 more (niche lines: Marble, Galaxy, TPU Silk, Silk Multi-Color, Matte Dual-Color, Twinkling) haven't been checked. Deprioritized — diminishing returns for the effort involved relative to the other items on this list.
5. **Ongoing, not a one-time fix: weighing newly-opened spools.** Progress so far: 3 of 62 rows have a real measured `Est. Remaining (g)` (Bambu PLA Basic Light Gray: 954g/95.4%; Bambu PLA Basic Indigo Purple: 940g/94%; SUNLU PETG White: 20g/2%, flagged for replacement). Process is established — measure raw weight → subtract brand tare → enter as `Est. Remaining (g)` — with real tare weights on file for Bambu Lab (235g) and SUNLU (210g). Every spool opened going forward needs this same treatment; this is routine maintenance, not something to ever fully "close out."
