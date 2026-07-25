# Expert Filament Guide for Bambu Lab Printers
### Covering 11 Brands · 26 Material Types · AMS Compatibility · Cross-Brand Comparisons

---

## How to Use This Guide

This guide is structured in three layers:

1. **Material Deep-Dives** — physics, chemistry, strengths, weaknesses, and ideal use cases for each material family
2. **Brand Analysis** — per-brand assessment for every material they sell, including what makes each brand's version distinctive
3. **Cross-Brand Comparisons** — direct head-to-head for each material family across all brands that carry it

**Additional sections** at the end cover topics the standard per-material format doesn't capture well: the Bambu AMS ecosystem, nozzle selection, storage and drying, post-processing, and a printer-model compatibility matrix.

**Notation used throughout:**
- ✓ = compatible / recommended / no caveats
- ⚠ = compatible with conditions or minor caveats
- ✗ = not compatible / not recommended
- 🔧 = requires hardware change (nozzle, etc.)
- 💧 = moisture-sensitive — dry before use
- 📦 = cardboard spool — AMS Adapter Ring required

---

## Part 1 — The PLA Family

PLA (polylactic acid) is a bioplastic derived from corn starch or sugarcane. It is the most widely used desktop FDM filament for good reason: low print temperature, no enclosure required, minimal warping, and the widest color selection of any material. Its main weaknesses are low heat deflection temperature (~55–60°C) and brittleness compared to PETG or ABS.

### 1.1 PLA Basic / Standard PLA

**Chemistry:** Straight polylactic acid, sometimes with minor flow additives.

**Strengths:**
- Widest color selection of any filament type
- Lowest print temperature of any structural filament (190–230°C)
- No enclosure required — prints well on open-frame machines
- Minimal warping even on unheated beds
- Biodegradable under industrial composting conditions
- Works reliably in all AMS variants
- Fastest print speeds of any rigid filament — Bambu printer hardware supports up to 500mm/s; the Bambu PLA Basic optimized profile runs at up to 300mm/s with 258mm/s as the default wall loop speed
- Easiest to tune: very forgiving of temperature variation

**Weaknesses:**
- Heat deflection temperature ~55–60°C — will deform in a hot car, dishwasher, or near electronics under load
- More brittle than PETG or ABS under impact
- Poor UV resistance — yellows and becomes brittle outdoors within weeks
- Not food-safe in printed form (layer lines harbor bacteria)
- Absorbs moisture over time, causing popping/crackling during printing

**Ideal use cases:** Display models, prototypes, miniatures, decorative objects, low-stress mechanical parts, multi-color prints, anything printed for indoor use at room temperature.

**Not suitable for:** Car interiors, outdoor exposure, functional parts near heat sources, parts requiring flexibility.

**Print settings guidance:**
| Parameter | Typical Range | Notes |
|---|---|---|
| Print temp | 190–230°C | Brand-dependent; Prusament runs ~10°C hotter |
| Bed temp | 25–60°C | Textured PEI works best; no bed heat needed at all for small prints |
| Enclosure | Not required | Open enclosure or no enclosure both fine |
| Cooling | Maximum | PLA benefits from aggressive part cooling |
| Speed | Up to 300mm/s | Bambu profiles optimized for high speed |

---

#### Brand Analysis: PLA Basic / Standard PLA

**Bambu Lab — PLA Basic**
Bambu's first-party PLA is the gold standard for AMS printing. The RFID tag in each spool automatically loads an optimized profile in Bambu Studio, eliminating guesswork. 30 colors with official hex codes. The formulation is tuned specifically for Bambu's high-flow hotends and prints reliably at speeds up to 300mm/s in default profile (printer hardware capable of 500mm/s; 258mm/s is the default wall loop speed). Suspected to be manufactured by eSUN under OEM contract.
- Tolerance: ±0.03mm
- AMS: ✓ all variants
- Tier: S — best-in-class for Bambu printers
- Weakness: premium price; limited to Bambu's 30-color palette

**Prusament PLA**
The highest-tolerance PLA available at retail. Czech/US manufactured under direct Prusa quality control with publicly documented batch statistics. NFC tag on spool for profile identification. Runs noticeably hotter than most PLA (~210–230°C vs 190–220°C) — requires a custom Bambu Studio profile.
- Tolerance: ±0.02mm (best-in-class)
- AMS: ✓ all variants
- Tier: A — best third-party PLA for dimensional accuracy
- Weakness: higher price, needs profile adjustment on Bambu, runs hot

**Polymaker PolyLite PLA**
The most complete third-party PLA in terms of verified color data — Polymaker publishes official hex codes for all 29 colors (catalog SKUs PM-PLA-01 through PM-PLA-29). Hardened spool edges improve AMS reliability. Consistent quality across batches.
- Tolerance: ±0.03mm
- AMS: ✓ all variants
- Tier: A — best value premium PLA
- Weakness: slightly higher price than budget brands

**Hatchbox PLA**
One of the most widely used budget PLAs. Long track record, broad color selection (22 colors), easily available on Amazon. The critical caveat for Bambu users: **all Hatchbox spools use cardboard cores** that won't fit standard AMS hubs. The AMS Adapter Ring resolves this but adds a setup step and can occasionally cause feed issues on long prints.
- Tolerance: ±0.03mm
- AMS: ⚠ all variants — cardboard spool requires Adapter Ring 📦
- Tier: B — excellent value but adapter ring friction adds risk
- Weakness: cardboard spool, no optimized Bambu profile

**Overture PLA**
Reliable budget option. 43 colors across several sub-lines (standard, Rock, Easy, Air), plastic spool, no adapter issues. Prints cleanly on standard PLA profiles. Slightly less consistency batch-to-batch than Polymaker but cheaper. The widest color selection of any budget PLA in this catalog.
- Tolerance: ±0.03mm
- AMS: ✓ all variants
- Tier: B — budget pick with no gotchas

**Creality Hyper PLA**
Formulated specifically for high-speed printing (300mm/s+). Performs well on Bambu printers, which already excel at speed. 12 colors, plastic spool. If you're pushing speeds aggressively, Hyper PLA is worth trying for its designed-for-speed flow characteristics. At normal speeds, indistinguishable from other B-tier PLAs.
- Tolerance: ±0.03mm
- AMS: ✓ all variants
- Tier: B — niche advantage at very high speeds

**MatterHackers PRO Series PLA**
Well-regarded quality with tighter QC than most budget brands. 15 colors. The PRO Series is genuinely better than the Build Series — more consistent diameter, better layer adhesion. Slightly pricier but worth it over Build Series for structural parts.
- Tolerance: ±0.03mm
- AMS: ✓ all variants
- Tier: A — premium quality without Prusament's temperature quirks

**MatterHackers Build Series PLA**
Entry-level MatterHackers option. Looser tolerances, fewer colors (6), lower price. Functional for non-critical prints. Not recommended over Overture or Creality Hyper at a similar price.
- Tolerance: ±0.03mm
- AMS: ✓ all variants
- Tier: B

**SUNLU PLA+** / **eSUN ePLA+** / **Overture PLA+**
These PLA+ variants add toughening agents to the base PLA formula — typically rubber or TPU microparticles — to improve impact resistance and reduce brittleness. Print slightly hotter than standard PLA (190–240°C range). SUNLU and eSUN are the most widely available. eSUN is suspected to be the OEM source behind some Bambu first-party filament.
- All: ±0.03mm, AMS ✓ all variants, Tier B

**VoxelPLA — PLA+ HS**
28 colors. USA-made, farm-tested across 250 machines, rated for high-speed printing up to 400mm/s. Uses the stock Bambu PLA Basic profile with no changes needed — one of the easiest third-party PLA+ lines to drop in. TrustPilot reports occasional shipping delays and color-batch mismatches — worth checking spool condition on arrival.
- Tier: B

**AzureFilm — Original PLA / Strongman PLA**
13 colors across two lines: Original PLA (standard) and Strongman PLA (toughened, 3 shared colors — Black, Grey, White). Manufacturer TDS-confirmed on the core line; standard reel, not Bambu-verified, but no unusual print-temp requirements.
- Tolerance: ±0.02mm
- Tier: A

---

#### Cross-Brand PLA Comparison

| Brand | Product | Colors | Tol. | AMS | Price/kg | Tier | Best For |
|---|---|---|---|---|---|---|---|
| Bambu Lab | PLA Basic | 30 | ±0.03 | ✓ all | ~$20 | S | Bambu-first users, multi-color |
| Prusament | PLA | 22 | ±0.02 | ✓ all | ~$30 | A | Dimensional accuracy, engineering |
| Polymaker | PolyLite PLA | 29 | ±0.03 | ✓ all | ~$22 | A | Color variety, reliable quality |
| MatterHackers | PRO Series PLA | 15 | ±0.03 | ✓ all | ~$23 | A | Quality without Prusament quirks |
| Overture | PLA | 43 | ±0.03 | ✓ all | ~$18 | B | Budget, no adapter needed, widest color range |
| Creality Hyper | Hyper PLA | 12 | ±0.03 | ✓ all | ~$20 | B | High-speed printing |
| Hatchbox | PLA | 22 | ±0.03 | ⚠ adapter | ~$22 | B | Wide color range, proven track record |
| SUNLU | PLA+ | 38 | ±0.03 | ✓ all | ~$17 | B | Budget toughened PLA |
| eSUN | ePLA+ | 49 | ±0.03 | ✓ all | ~$19 | A | Suspected Bambu OEM quality |
| MatterHackers | Build Series PLA | 6 | ±0.03 | ✓ all | ~$18 | B | Entry-level only |

**Recommendation by use case:**
- Best all-around (Bambu ecosystem): **Bambu Lab PLA Basic**
- Best for dimensional accuracy: **Prusament** (but needs custom profile)
- Best value with no compromises: **Polymaker PolyLite** or **eSUN ePLA+**
- Best budget pick: **Overture PLA**
- Avoid for AMS: **Hatchbox** (adapter ring friction risk on long prints)

---

### 1.2 PLA Matte

**What makes it different:** Matte PLA contains micro-particles (typically chalk or silica) that scatter light at the surface, eliminating the glossy sheen of standard PLA. The result is a surface that hides layer lines better and has a more premium, "painted" appearance.

**Strengths:**
- Dramatically better visual appearance for display models — hides layer lines far more than glossy PLA
- Same printability as standard PLA — no enclosure, low temps, all AMS variants
- Wider color palettes often include more muted, refined tones not available in gloss
- Forgiving of minor under-extrusion artifacts

**Weaknesses:**
- Slightly more brittle than standard PLA due to filler particles
- Marginally more abrasive to nozzle than standard PLA (minor at normal volumes)
- Colors appear darker/more saturated on screen than in print — harder to color-match
- Slightly higher print temp than standard PLA (195–230°C typical)

**Ideal use cases:** Architectural models, figurines, display prints, cosplay props, anything where appearance matters more than strength.

---

#### Brand Analysis: PLA Matte

**Bambu Lab — PLA Matte**
25 colors with an exceptionally refined palette — terracotta, desert tan, latte brown, nardo gray — designed for aesthetic printing. Official hex codes confirmed. RFID profile. The Bambu Matte has excellent layer-line hiding and prints consistently.
- Tier: S — best matte PLA for Bambu ecosystem

**Polymaker — Panchroma Matte PLA (formerly PolyTerra)**
Rebranded in 2025. 27 colors with a strong earthy/muted palette, spanning numbered core shades plus a named "Army/Savannah/Pastel" extension line. High quality matte finish. The critical caveat: **cardboard spool** requiring AMS Adapter Ring. Also, the cardboard is more sensitive to humidity than plastic spools — store carefully.
- AMS: ⚠ adapter ring required 📦
- Tier: A — excellent quality but adapter friction adds risk

**SUNLU — PLA Matte**
14 colors, budget pricing. Functional matte finish, slightly less refined than Bambu or Polymaker. A good option for large matte prints where cost matters more than surface perfection.
- Tier: B

**eSUN — ePLA-Matte**
5 colors. Consistent eSUN quality control. A reliable budget-to-mid choice. Less color variety than Bambu but reliable performance.
- Tier: B

**AzureFilm — PLA Matte**
1 color (Black). Line existence confirmed via azurefilm.com navigation, but the full color list has not been verified — this is one of AzureFilm's newer, less-documented lines. Treat as unconfirmed until checked against the actual spool.
- Tier: C — line confirmed but not fully verified

#### Cross-Brand PLA Matte Comparison

| Brand | Colors | Spool | AMS | Price | Tier |
|---|---|---|---|---|---|
| Bambu Lab | 25 | Plastic | ✓ all | ~$20 | S |
| Polymaker Panchroma | 27 | Cardboard | ⚠ adapter | ~$22 | A |
| eSUN ePLA-Matte | 5 | Plastic | ✓ all | ~$19 | B |
| SUNLU PLA Matte | 14 | Plastic | ✓ all | ~$17 | B |
| AzureFilm PLA Matte | 1 | Plastic | ✓ all | ~$19 | C |

---

### 1.3 PLA Silk

**What makes it different:** Silk PLA adds low-viscosity additives (often a polyester blend) that create a high-gloss, metallic-sheen surface resembling polished metal. The visual effect is striking, especially in gold, silver, and copper.

**Strengths:**
- Exceptional visual finish — metallic appearance without metallic weight
- Prints at standard PLA temperatures
- AMS-compatible on all variants

**Weaknesses:**
- **More brittle than standard PLA** — the additive reduces impact resistance significantly. This is the biggest practical limitation.
- Prone to snapping in the AMS bowden tubes during long multi-color runs — monitor closely
- Slight stringing tendency compared to matte PLA
- Metallic appearance doesn't survive sanding — the sheen is entirely surface-level

**Ideal use cases:** Trophies, jewelry, figurines, display objects, anything prioritizing appearance over function.
**Not suitable for:** Functional parts, anything that will be stressed or dropped.

---

#### Brand Analysis: PLA Silk

**Bambu Lab — PLA Silk**
6 colors (Gold, Silver, Copper, Bronze, White, Black). RFID profile. Reliable AMS performance. The Bambu Silk formulation is tuned to minimize brittleness while maintaining sheen — slightly tougher than most silk PLAs.
- Tier: S

**SUNLU — Silk PLA**
8 colors including Rainbow (multi-color transition on a single spool) and Rose Gold. Good value. Rainbow Silk is a popular choice for vase-mode prints. Brittleness is more pronounced than Bambu's formulation.
- Tier: B — Rainbow variant is uniquely useful

**eSUN — ePLA-Silk**
4 colors including Rainbow. Consistent quality. Similar performance to SUNLU Silk.
- Tier: B

**Polymaker — Panchroma Silk**
2 colors (Gold, Copper). Official hex confirmed via shop.polymaker.com. Reliable quality consistent with Polymaker's other lines.
- Tier: A

**AzureFilm — Silk PLA**
2 colors (Copper, Gold). Manufacturer TDS-confirmed. Silk finish prints best slower, same guidance as other silk PLAs.
- Tier: A

---

### 1.4 PLA Specialty Variants (Bambu-exclusive in this catalog)

#### PLA Translucent
9 colors with genuine semi-transparency. Ideal for light diffusers, lampshades, and parts where light transmission matters. Prints identically to standard PLA. Bambu's hex codes represent the lit appearance, not the unlit spool color.
- Tier: S (Bambu only)

#### PLA Marble
White or black base with swirled mineral-particle fill. Creates a convincing stone texture. Slightly abrasive — monitor nozzle wear over very long prints. Excellent for architectural models and decorative objects. No longer Bambu-exclusive — SUNLU offers PLA Marble (including a High Speed variant, 7 colors combined) and eSUN offers a single-color PLA-Marble; both are budget-tier alternatives to Bambu's version.
- Tier: S (Bambu) / B (SUNLU, eSUN)

#### PLA Sparkle
Metallic glitter-particle fill in gold, silver, red. Abrasive at high volumes but manageable. The glitter effect is subtle and sophisticated compared to cheap glitter fills.
- Tier: S (Bambu only)

#### PLA Glow
Phosphorescent (glow-in-the-dark) filament. Charge under UV or daylight. The hex codes in the catalog represent daylight color, not glow color. Most glow filaments emit green-yellow regardless of daylight color. Bambu Lab offers 2 colors; SUNLU offers 4 PLA Glow colors plus 2 PETG Glow colors — SUNLU is currently the wider glow-filament selection in this catalog.
- Tier: S (Bambu) / B (SUNLU)

---

## Part 2 — PETG

PETG (polyethylene terephthalate glycol) sits between PLA and ABS in the material hierarchy. It's stronger and more heat-resistant than PLA (~80°C HDT), more flexible, and significantly tougher under impact. It's also easier to print than ABS — no enclosure required, minimal warping.

**Chemistry note:** The "G" modifier (glycol) makes PETG much more printable than standard PET. Pure PET is difficult to print; PETG is forgiving. The glycol reduces crystallinity and brittleness compared to pure PET — PETG is not flexible (it is a rigid filament), but it is tougher and less brittle than PLA, with better impact resistance and ductility before fracture.

### Strengths
- Heat deflection temperature ~80°C — survives a hot car in summer
- Excellent chemical resistance — handles most household chemicals, gasoline
- Good layer adhesion — stronger interlayer bonds than PLA
- Semi-flexible under load — absorbs impact better than PLA
- Food-safe when printed with food-safe nozzle and correct settings (check filament certification)
- Transparent variants achieve genuine optical clarity

### Weaknesses
- **Very moisture-sensitive** — absorbs humidity quickly. Must be dried before use and stored sealed. Wet PETG produces stringing, bubbling, and weak parts.
- Prone to stringing more than PLA — requires careful retraction tuning
- Sticks aggressively to smooth PEI — use textured PEI or glue stick release agent
- Slightly more expensive than PLA
- Higher print temperature than PLA (220–260°C)
- Soft at elevated temperatures (not suitable for engine bay components)

### Ideal use cases
Functional parts for moderate-heat environments (enclosures, brackets, covers), water containers, parts that see occasional impact, outdoor use in temperate climates (not prolonged UV), food containers (with appropriate certification).

### Not suitable for
High-heat environments (>75°C continuous), parts requiring rigidity under bending stress (more flexible than PLA), applications requiring tight tolerances (slight warping possible).

---

#### Brand Analysis: PETG

**Bambu Lab — PETG Basic**
Bambu reformulated PETG in 2026, replacing PETG HF with PETG Basic — better strength, same AMS reliability. 13 colors. RFID profile. The Bambu formulation is specifically tuned to minimize stringing at Bambu Studio default retraction settings, which is its most practical advantage over third-party PETG.
- Print temp: 220–260°C
- Tier: S

**Bambu Lab — PETG HF (Legacy)**
The original high-flow PETG. Now end-of-life — no restock expected. If you have remaining stock, it still prints fine. The HF formulation allowed higher volumetric flow rates than standard PETG, enabling faster printing. PETG Basic is the replacement.
- Tier: S (legacy — switch to PETG Basic)

**Prusament PETG**
The most demanding PETG in this catalog — runs significantly hotter than typical PETG (240–260°C vs 220–250°C for most brands). Requires a custom Bambu Studio profile. ±0.02mm tolerance. The extra effort pays off in exceptional layer bonding and mechanical properties. Best PETG for functional parts where you need every bit of strength.
- Print temp: 240–260°C (custom profile required)
- Tier: A — best functional PETG, but requires setup work

**Polymaker — PolyLite PETG**
9 colors. Plastic spool, no adapter issues. Consistent quality, prints well on standard PETG profiles. Excellent transparent variant — achieves near-optical clarity in thin walls.
- Tier: A

**eSUN — ePETG**
13 colors. Reliable quality consistent with eSUN's track record. Prints well on standard profiles. Good value. Suspected to be among the more consistent budget-tier PETG options.
- Tier: A

**Hatchbox — PETG**
6 colors. Good quality PETG but all spools are cardboard — same adapter ring caveat as Hatchbox PLA. PETG runs stickier than PLA through the AMS tubes, making the cardboard spool interaction slightly higher-risk for long multi-color prints.
- AMS: ⚠ adapter required 📦
- Tier: B

**Overture — PETG**
24 colors — the widest PETG color range in this catalog. Budget option. Functional on standard PETG profiles. May need minor temperature tuning (+5–10°C vs Bambu default). More batch-to-batch variation than Prusament or Polymaker.
- Tier: B

**SUNLU — PETG**
30 colors including Transparent. Good value. Standard PETG performance. The transparent variant is popular for light-pipe and display applications.
- Tier: B

**Creality Hyper — PETG**
6 colors. High-speed formulation — same advantage as Hyper PLA at very high speeds. Otherwise comparable to other B-tier PETG options.
- Tier: B

**MatterHackers — PRO Series PETG**
6 colors. Consistent with the PRO Series quality level — better than budget brands, slightly below Prusament's ceiling. No temperature quirks, works on standard profiles.
- Tier: A

**AzureFilm — PETG**
3 colors (Black, Clear/Natural, White). Manufacturer TDS-confirmed, runs slightly cooler than most (220–240°C). Standard reel, not Bambu-verified.
- Tier: A

**VoxelPLA — PETG+ HS**
12 colors. USA-made, farm-tested, high-speed rated. Requires the Bambu PETG HF profile with nozzle temp raised to 265°C — the one third-party PETG in this catalog with a specific required profile deviation rather than a drop-in fit.
- Tier: B

**VoxelPLA — Galaxy PETG+ HS**
4 colors (Midnight Blue, Emerald Gold, Gioiello Purple, Aurora Green). A glitter/sparkle-particle variant of PETG+ HS — same print settings, mildly abrasive at volume like other glitter-fill materials. The only glitter-effect PETG in this catalog (Bambu PLA Sparkle is PLA-only).
- Tier: B

---

#### Cross-Brand PETG Comparison

| Brand | Product | Colors | Temp | AMS | Spool | Tier | Notes |
|---|---|---|---|---|---|---|---|
| Bambu Lab | PETG Basic | 13 | 220–260°C | ✓ all | Plastic | S | RFID profile, minimal stringing |
| Prusament | PETG | 8 | 240–260°C | ✓ all | Plastic | A | Needs custom profile; best strength |
| Polymaker | PolyLite PETG | 9 | 220–250°C | ✓ all | Plastic | A | Best transparent variant |
| eSUN | ePETG | 13 | 230–260°C | ✓ all | Plastic | A | Consistent, good value |
| MatterHackers | PRO PETG | 6 | 225–255°C | ✓ all | Plastic | A | Reliable, no quirks |
| SUNLU | PETG | 30 | 220–250°C | ✓ all | Plastic | B | Budget, good transparent |
| Overture | PETG | 24 | 220–250°C | ✓ all | Plastic | B | Budget, minor tuning needed, widest range |
| Creality Hyper | Hyper PETG | 6 | 230–260°C | ✓ all | Plastic | B | High-speed advantage |
| Hatchbox | PETG | 6 | 230–260°C | ⚠ adapter | Cardboard | B | Adapter ring risk 📦 |

**Key decision points:**
- Minimize setup friction: **Bambu PETG Basic**
- Maximum mechanical performance: **Prusament PETG** (custom profile required)
- Best transparency: **Polymaker PolyLite PETG**
- Best value with no compromises: **eSUN ePETG**

---

### 2.1 PETG-CF (Carbon Fiber Reinforced PETG)

**What changes with CF:** Carbon fiber short strands fill the matrix, dramatically increasing stiffness and reducing creep under sustained load. The trade-offs are: the CF strands are abrasive (hardened nozzle required), the material loses PETG's flexibility (more brittle under impact), and color selection is limited to black or very dark shades.

**Strengths:**
- Significantly stiffer than standard PETG
- Retains PETG's chemical and heat resistance
- Lower thermal expansion than pure PETG — better dimensional stability
- Still chemical-resistant

**Weaknesses:**
- 🔧 Hardened nozzle mandatory — brass nozzles wear quickly
- Limited colors (typically black only)
- More brittle than unfilled PETG
- More expensive

**Ideal use cases:** Structural brackets, functional enclosures, lightweight rigid components, anything needing PETG's chemical resistance with added stiffness.

---

#### Brand Analysis: PETG-CF

**Bambu Lab — PETG-CF**
6 colors — unusually broad for a CF material. The Bambu PETG-CF uses chopped carbon fiber with a proprietary surface treatment for better matrix adhesion. RFID profile. Prints reliably on all AMS variants with hardened nozzle installed.
- Tier: S — only CF PETG with a multi-color selection

**eSUN — ePETG-CF / SUNLU — PETG-CF / Creality Hyper — PETG-CF**
All black only. Functional CF PETG at budget prices. eSUN has a slight edge in consistency. For single-color structural prints where you need CF PETG without Bambu pricing, any of these are viable.
- Tier: B

---

## Part 3 — ABS

ABS (acrylonitrile butadiene styrene) is the original engineering thermoplastic for desktop FDM — it predates PLA in hobbyist printing. It's tough, impact-resistant, machineable, and post-processable with acetone. The trade-offs are significant: it requires high temperatures, an enclosure, and good ventilation.

### Strengths
- Heat deflection temperature ~95–100°C — significantly better than PLA or PETG
- Excellent impact resistance — the "B" component (butadiene) is a rubber toughener
- Post-processable: acetone vapor smoothing produces glass-smooth surfaces; acetone welding joins parts
- Machinable: drills, taps, mills cleanly
- UV-stabilized variants available (ASA is better, but ABS performs adequately)
- Widely available, predictable behavior

### Weaknesses
- **Requires enclosure** — prints above ambient glass transition temperature; open-air printing causes severe warping and layer delamination. This disqualifies ABS from A1/A1 mini printers entirely.
- **Produces styrene fumes** — VOC ventilation is important; not suitable for enclosed living spaces without exhaust
- Warps significantly — large flat prints require careful bed preparation (ABS juice, enclosure temp management)
- Absorbs moisture over time 💧
- Shrinks ~0.5–0.8% during cooling — dimensional compensation needed for precision parts
- Layer adhesion weaker than PETG in Z-axis

### Ideal use cases
Automotive interior components, electronics housings, functional tools, RC car bodies, anything requiring the acetone-smoothing finish or post-machining, parts exposed to heat up to ~95°C.

### Not suitable for
A1/A1 mini printers, open environments, parts with fine details that can't tolerate warping, any food contact application.

---

#### Brand Analysis: ABS

**Bambu Lab — ABS**
12 colors with RFID profile. The Bambu ABS is formulated specifically for the P1S/X1C/H2D enclosure conditions. Strong layer adhesion. Minimal warping in enclosed Bambu printers with the chamber heated. The RFID profile automatically sets the correct chamber pre-heat and bed temperature.
- Enclosure required (P1S/X1C/H2D only)
- AMS Lite: ✗
- Tier: S

**Polymaker — PolyLite ABS**
5 colors. Hardened spool edges. Reliable quality, consistent performance on standard ABS profiles. Good choice if you want a specific color not in Bambu's 12-color ABS palette.
- Tier: A

**eSUN — eABS+**
11 colors. The "+" formulation adds impact modifiers for slightly better toughness than standard ABS. Consistent quality. No optimized Bambu profile — use generic ABS preset with minor tweaks.
- Tier: B

**MatterHackers — PRO Series ABS**
4 colors. PRO Series quality control applies here too — better diameter consistency than SUNLU or Overture. Worth the modest price premium for functional parts.
- Tier: A

**Overture — ABS, SUNLU — ABS, Creality Hyper — ABS, Hatchbox — ABS, AzureFilm — ABS**
These are all functional budget ABS options. They work, but:
- No optimized Bambu profile exists — use generic ABS
- More batch-to-batch variation than Bambu or Polymaker
- Hatchbox ABS is cardboard spool + requires enclosure — double caveat, rated Tier C
- AzureFilm offers 2 colors (Black, White) across its Plus/Prime lines, manufacturer TDS-confirmed, no Bambu-specific profile

---

#### Cross-Brand ABS Comparison

| Brand | Colors | Enclosure | AMS Lite | Spool | Tier | Notable |
|---|---|---|---|---|---|---|
| Bambu Lab | 12 | Required | ✗ | Plastic | S | RFID, chamber preheat profile |
| Polymaker | 5 | Required | ✗ | Plastic | A | Reliable third-party |
| MatterHackers PRO | 4 | Required | ✗ | Plastic | A | Best third-party consistency |
| eSUN eABS+ | 11 | Required | ✗ | Plastic | B | Impact-modified formula |
| Overture | 23 | Required | ✗ | Plastic | B | Budget option, widest color range |
| SUNLU | 5 | Required | ✗ | Plastic | B | Budget option |
| Creality Hyper | 3 | Required | ✗ | Plastic | B | High-speed formulation |
| AzureFilm | 2 | Required | ✗ | Plastic | B | Not Bambu-verified |
| Hatchbox | 3 | Required | ✗ | Cardboard | C | Adapter ring + enclosure required 📦 |

---

## Part 4 — ASA

ASA (acrylonitrile styrene acrylate) is the outdoor-grade version of ABS. The acrylate component replaces ABS's UV-vulnerable butadiene rubber, giving ASA excellent UV resistance while retaining ABS's heat resistance and printability. If ABS is the indoor engineering material, ASA is the outdoor one.

### Strengths
- **Best UV resistance** of any common FDM material — retains color and mechanical properties after extended outdoor exposure
- Heat deflection similar to ABS (~95–100°C)
- Better weather resistance than ABS — handles rain, humidity, temperature cycling
- Similar acetone post-processing capability (slower than ABS but works)
- Better layer adhesion than ABS in some formulations

### Weaknesses
- Same enclosure requirement as ABS
- Same fume concerns as ABS (slightly less severe)
- Same warping tendency as ABS
- Higher print temperature than ABS in some formulations (255–275°C for Prusament)
- Still requires 💧 drying

### Ideal use cases
Outdoor signage, garden hardware, RC car bodies for outdoor use, automotive exterior clips, window and door hardware, anything living outdoors long-term.

---

#### Brand Analysis: ASA

**Bambu Lab — ASA**
6 colors. RFID profile. Enclosure required (same as Bambu ABS). The Bambu ASA formulation prints with less warping than most third-party ASA, thanks to the optimized chamber temperature profile. Solid choice for outdoor Bambu-printer projects.
- Tier: S

**Prusament — ASA**
4 colors. ±0.02mm tolerance. Runs hotter than typical ASA (255–275°C) — needs a custom Bambu Studio profile. The Prusament ASA has excellent UV resistance benchmarks (Prusa publishes test data). Best ASA for long-term outdoor UV exposure.
- Tier: A — but requires custom profile

**eSUN — eASA**
9 colors. Solid budget ASA. Good UV resistance. Enclosure required. No Bambu profile — use generic ASA preset.
- Tier: A — good value

**Creality Hyper — ASA**
2 colors. High-speed ASA formulation. Limited color palette but functional. Budget option for outdoor-use prints.
- Tier: B

**SUNLU — ASA**
8 colors. Budget ASA, functional but more batch variation than Bambu or Prusament. Enclosure required. No Bambu profile — use generic ASA preset with minor tuning.
- Tier: B

**Overture — ASA**
15 colors — the widest ASA color range in this catalog. Budget option, reliable for outdoor/UV-exposed prints where color choice matters more than best-in-class warping control. Enclosure required.
- Tier: B

**AzureFilm — ASA**
2 colors (Original, Prime — Black and Grey). Manufacturer TDS-confirmed. Enclosure required, standard UV/weather-resistant ASA. Not Bambu-verified, but no unusual print-temp requirements.
- Tier: B

#### Cross-Brand ASA Comparison

| Brand | Colors | Temp | AMS Lite | Tier | Notes |
|---|---|---|---|---|---|
| Bambu Lab | 6 | 240–270°C | ✗ | S | RFID, best warping control |
| Prusament | 4 | 255–275°C | ✗ | A | Best UV data, needs custom profile |
| eSUN | 9 | 240–270°C | ✗ | A | Good value |
| Overture | 15 | 240–260°C | ✗ | B | Widest color range |
| SUNLU | 8 | 240–260°C | ✗ | B | Budget |
| Creality Hyper | 2 | 240–270°C | ✗ | B | Budget |
| AzureFilm | 2 | 240–260°C | ✗ | B | Budget, not Bambu-verified |

### 4.1 ASA-CF (Bambu Lab only)
Carbon fiber reinforced ASA. Combines ASA's UV/weather resistance with CF's stiffness increase. Single color (black). Excellent for structural outdoor brackets. Hardened nozzle required. Tier A.

---

## Part 5 — TPU / Flexible Filaments

TPU (thermoplastic polyurethane) is the standard flexible filament for desktop FDM. Shore hardness 95A is the most common — flexible but not rubbery; roughly the feel of a shoe sole.

### Strengths
- Flexible and elastic — absorbs impact without fracturing
- Excellent abrasion resistance — the toughest surface of any FDM material
- Good chemical resistance
- Vibration damping — ideal for feet, gaskets, cable strain reliefs
- Prints at relatively low temperatures (210–240°C)

### Weaknesses
- **Not AMS-compatible in standard form** — flexible filaments buckle in rigid bowden tubes; the AMS feed path is too long for standard TPU
- Low print speed ceiling — flexible materials need slow speeds (20–35mm/s for most brands)
- Strings aggressively — needs zero retraction or near-zero
- Dimensional accuracy lower than rigid filaments
- Difficult to post-process

### Critical Bambu AMS note:
**Only Bambu Lab TPU 95A for AMS** is rated for any AMS use — and only through the **AMS HT dedicated TPU path**. All other TPU brands (SUNLU, Polymaker, eSUN, Overture, Creality) must be run from an external spool on all Bambu printers. This is a fundamental design constraint, not a compatibility quirk.

---

#### Brand Analysis: TPU

**Bambu Lab — TPU 95A for AMS**
Specifically engineered for the AMS HT's dedicated flexible-filament path. 3 colors. The only TPU in this catalog that can be run through any AMS. On AMS X/P (standard), it requires a special AMS mode and is not fully reliable — AMS HT is the correct solution.
- AMS: ✓ HT (dedicated path) / ⚠ X/P special mode / ✗ Lite / ✗ 2 Pro
- Tier: A

**Polymaker — PolyFlex TPU95**
3 colors. High-quality TPU, good elasticity and surface quality. External spool only. One of the more print-friendly standard TPUs for speed and stringing control.
- Tier: A — best non-AMS TPU for quality

**eSUN — eTPU-95A**
12 colors. Reliable quality, consistent shore hardness. External spool only. Good value.
- Tier: B

**SUNLU — TPU 95A**
14 colors. Budget option. External spool only. Works but more prone to stringing than eSUN or Polymaker.
- Tier: B

**Overture and Creality Hyper TPU**
Overture has expanded to 37 colors across standard and high-speed TPU formulations — by far the widest TPU color range in this catalog. Creality Hyper remains a narrow 2-color budget option. Both are functional at low speeds on external spools.
- Tier: B

**AzureFilm — Flexible 85A TPU**
2 colors (Black, White). Manufacturer product-page confirmed, 85A shore hardness. External spool only on all Bambu AMS variants, same as every third-party TPU in this catalog except Bambu's own AMS-specific line.
- Tier: B

---

#### Cross-Brand TPU Comparison

| Brand | Colors | AMS Compatible | Speed | Tier | Notes |
|---|---|---|---|---|---|
| Bambu TPU 95A | 3 | ✓ HT only | Standard | A | Only AMS-capable TPU |
| Polymaker PolyFlex | 3 | ✗ ext. spool | Moderate | A | Best quality non-AMS |
| Overture TPU | 37 | ✗ ext. spool | Slow/HS | B | Widest TPU color range by far |
| SUNLU TPU 95A | 14 | ✗ ext. spool | Slow | B | Budget |
| eSUN eTPU-95A | 12 | ✗ ext. spool | Slow | B | Reliable, consistent |
| Creality Hyper TPU | 2 | ✗ ext. spool | Slow | B | Budget |
| AzureFilm Flexible 85A | 2 | ✗ ext. spool | Slow | B | Budget, not Bambu-verified |

---

## Part 6 — Engineering Materials

### 6.1 PA (Nylon)

Nylon (polyamide) is one of the toughest FDM materials available — excellent impact resistance, fatigue resistance, and low coefficient of friction. It is also the most hygroscopic common filament, which is its greatest weakness.

**Strengths:**
- Outstanding toughness and fatigue resistance — springs back from repeated flexing
- Low coefficient of friction — natural bearing/bushing material
- Good heat resistance (HDT ~100–130°C depending on grade)
- Chemical resistance to fuels, oils, many solvents
- Self-lubricating

**Weaknesses:**
- **Extremely moisture-sensitive** 💧💧 — absorbs moisture from air within hours. Must be dried immediately before printing (80°C, 8–12 hours) and kept sealed while printing. Wet nylon produces weak, stringy, bubbling prints.
- Warps significantly — enclosure strongly recommended
- Difficult bed adhesion — requires specialized surfaces (Garolite, PVA glue)
- Higher print temperature (260–270°C for Bambu PA)
- AMS HT required for multi-color printing (AMS X/P ⚠ only)

**Ideal use cases:** Gears, living hinges, snap-fit mechanisms, cable guides, any part requiring fatigue resistance, low-friction bushings.

---

#### Brand Analysis: PA

**Bambu Lab — PA** ⚠ Discontinued
2 colors (Natural, Black) — both discontinued in the current catalog and no longer available to order new. RFID profile. Requires AMS HT for reliable multi-color — AMS X/P can attempt it in special mode but is unreliable. The Bambu PA profile manages drying requirements well if you print immediately after drying. For current PA needs on a Bambu printer, look to third-party PA below.
- Tier: A (historical — line discontinued)

**eSUN — ePA-12**
1 color (Natural). PA-12 grade (more flexible, more moisture-resistant than PA-6). Good value. External spool preferred.
- Tier: B

**AzureFilm — Nylon**
1 color (Natural). Line existence confirmed via azurefilm.com; full spec not yet manufacturer-verified. Very moisture-sensitive like all PA — dry immediately before printing. External spool preferred.
- Tier: C — line confirmed but specs not fully verified

### 6.2 PA-CF

Carbon fiber reinforced nylon. The stiffest, strongest readily-printable FDM material short of continuous fiber systems. Combines nylon's toughness with CF's stiffness and heat resistance. Requires hardened nozzle, immediate pre-print drying, and (on Bambu) AMS HT. All brands in this catalog offer PA-CF in black only.

- **Bambu Lab** — 1 color (Black). AMS HT required. Tier A.
- **SUNLU** — 1 color (Black), 2 catalog entries at different confirmed heat-resistance specs depending on source (209°C per 3DJake vs 175°C per SUNLU's own store page — worth double-checking against the actual spool label). Tier B.
- **Polymaker** — 1 color (Black). Line existence confirmed; individual specs estimated from sibling materials, not TDS-confirmed. Tier C — verify before high-heat use.
- **eSUN** — 2 lines: ePA-CF and ePA12-CF, both Black, both specs estimated from sibling materials rather than individually confirmed. Tier C.

### 6.3 PC (Polycarbonate)

PC is the clearest, most impact-resistant engineering thermoplastic available for FDM. It has the highest heat deflection temperature of any material in this catalog (~115–120°C) and legendary impact resistance (polycarbonate is used in bulletproof glass and riot shields).

**Strengths:**
- Highest HDT in this catalog (~115–120°C)
- Excellent impact resistance
- Optical clarity in transparent variants
- Flame retardant (depending on grade)

**Weaknesses:**
- Requires enclosure and very high temperatures (260–295°C)
- Very moisture-sensitive 💧💧 — dry at 80°C minimum before printing
- Significant warping — large flat prints are extremely challenging
- Requires AMS HT (AMS X/P ⚠ only)
- Softer than expected from its reputation — surface scratches relatively easily

**Ideal use cases:** High-temperature functional parts (near motors, engines), transparent structural components, parts requiring bulletproof-level impact resistance.

---

#### Brand Analysis: PC

**Bambu Lab — PC**
2 colors (White, Black). RFID profile for H2D/X1C. AMS HT required.
- Tier: A

**Prusament — PC Blend**
3 colors (Natural, Jet Black, Pewter Grey). The PC Blend formulation is easier to print than pure PC — better layer adhesion, less warping, lower minimum temperature. ±0.02mm tolerance. The best-rounded PC option in this catalog for printability.
- Print temp: 275–295°C
- Tier: A — best PC printability

**Overture — PC**
6 colors (Black, Gray, White, Red, Blue, Transparent) — the widest color selection of any PC in this catalog, and rated Tier A despite the budget positioning. Runs cooler than most third-party PC (250–270°C).
- Tier: A

**SUNLU — PC, Polymaker — PC, eSUN — PC, Creality Hyper — PC**
All single-color (Natural/White or Black), all running hot (255–280°C) with no Bambu-optimized profile. Functional but noticeably behind Bambu, Prusament, and Overture on this material.
- Tier: C — usable, but not a first choice for PC if better options are available

**AzureFilm — PC-ABS**
1 color (Black). A PC/ABS blend rather than pure PC — trades some of PC's heat resistance for easier printing, similar in spirit to Prusament's PC Blend. Line existence confirmed via azurefilm.com; full spec not yet manufacturer-verified. Requires enclosure.
- Tier: C — line confirmed but specs not fully verified

---

### 6.4 Support Materials (Bambu Lab)

**Support W (Water-Soluble Support)**
PVA-based support material that dissolves in warm water. Enables complex geometry that would otherwise require difficult manual support removal. Must be stored completely sealed — absorbs moisture within hours. Primarily for use with PLA prints.
- All AMS: ✓
- Tier: S (Bambu only in this catalog)

**Support G (Glassy Breakaway Support)** ⚠ Discontinued
Rigid support that fractures cleanly at the interface with the model. Does not require water or solvents — just snap it off. Leaves a cleaner surface than standard support interface materials. Best paired with PETG Basic and ABS. No longer available to order new — check Bambu's current lineup for its replacement.
- All AMS: ✓
- Tier: S (historical — line discontinued)

**Polymaker — Support**
1 color (Natural). Line existence confirmed via Polymaker wiki/shop, but the color list hasn't been individually verified — treat as unconfirmed.
- Tier: C — line confirmed but not fully verified

---

## Part 7 — CF Composite PLA (PLA-CF)

### Strengths
- Significantly stiffer than standard PLA (increased modulus)
- Lower thermal expansion — better dimensional stability over temperature
- Matte surface finish — similar appearance to high-end composite parts

### Weaknesses
- 🔧 Abrasive — hardened nozzle required (≥0.4mm; 0.6mm recommended)
- More brittle than standard PLA — CF adds stiffness at the cost of toughness
- Black or very dark colors only
- More expensive

### Brand Analysis: PLA-CF

| Brand | Colors | Tier | Notes |
|---|---|---|---|
| Bambu Lab | 1 (Black) | S | RFID profile |
| eSUN ePLA-CF | 1 (Black) | B | Budget option |
| Creality Hyper | 1 (Black) | B | High-speed formulation |
| Polymaker | 1 (Black) | C | Line confirmed; specs estimated, not individually TDS-confirmed |
| SUNLU | 1 (Black) | C | Budget option |
| AzureFilm | 1 (Black) | C | Line confirmed via azurefilm.com; specs not manufacturer-verified |

For PLA-CF, Bambu's RFID-profiled version is the most convenient. Budget options work but require manual profile creation.

---

## Part 7.1 — Wood-Fill PLA

Wood-fill PLA blends genuine wood particles (typically 20–40% by weight) into the PLA base, producing a matte, slightly porous surface that can be sanded and stained similarly to real wood. No brand in this catalog offers RFID or AMS-optimized profiles for wood-fill — all four options below run the same way.

| Brand | Product | Colors | Tier | Notes |
|---|---|---|---|---|
| SUNLU | PLA Wood | 1 | B | Budget option |
| eSUN | ePLA-Wood | 1 | B | Consistent with eSUN's other lines |
| Prusament | Woodfill | 1 | A | PRO Series-level QC applies |
| AzureFilm | LumberLay Wood PLA | 1 (Bamboo) | C | Line confirmed via azurefilm.com; specs not manufacturer-verified |

**Print notes:** Larger nozzle (≥0.4mm) recommended, mildly abrasive — expect faster nozzle wear than standard PLA. Lower print temps (195–215°C) give a more pronounced wood-grain effect; higher temps produce smoother, less textured surfaces.

---

### AzureFilm — Additional Newer Lines

A few AzureFilm lines exist in the catalog as confirmed-but-not-fully-verified additions from a 2026-07-19 deep-dive pass — line existence is confirmed via azurefilm.com navigation, but full specs (temps, complete color lists) haven't been individually TDS-confirmed:

- **PLA Glitter** — 2 colors (Blue, Red). Glitter-fill, similar concept to Bambu PLA Sparkle. 0.4mm+ nozzle recommended. Tier C.
- **PLA Pastel** — 2 colors (Baby Blue, Mint). Standard pastel PLA. Tier B.
- **PLA Prime** — 1 color (Black). A premium tier distinct from AzureFilm's Original/Strongman PLA lines; positioning not yet independently verified. Tier C.

None of these have close analogues elsewhere in this catalog except PLA Glitter (≈ Bambu PLA Sparkle) and PLA Pastel (≈ general pastel-toned PLA from other brands' core lines). Treat all three as lower-confidence entries until cross-checked against the actual spool.

---

## Part 8 — Brand Tiers: Overall Assessment

Across all material types, here is how each brand ranks holistically for Bambu printer users:

### Tier S — Best in class
**Bambu Lab** — The only brand with RFID profiles that automatically configure Bambu Studio. First-party materials are formulated specifically for Bambu hotends and enclosure conditions. No other brand can match the zero-setup experience. Still the only source for PLA Sparkle, PLA Translucent, and RFID-profiled support materials — though PLA Marble and PLA Glow are no longer Bambu-exclusive (SUNLU and eSUN now offer both). Best choice as the default.

### Tier A — Excellent, with minor caveats
**Prusament** — Best dimensional tolerance (±0.02mm). Best choice for precision engineering parts where you're willing to create custom profiles. Runs hot — need to set up correct profiles once per material type, then it's excellent. Best UV data published for ASA.

**Polymaker** — Most complete confirmed color data for PolyLite PLA (29 colors with official hex). Excellent overall quality, plastic spools (except Panchroma Matte). No unusual print temp requirements. The best "drop-in, no surprises" third-party brand.

**eSUN** — Suspected OEM source for some Bambu first-party PLA. Exceptional quality-to-price ratio. Broad third-party material range (PLA+, PLA Matte, PLA Silk, PLA-CF, PETG, PETG-CF, ABS, ASA, PA, TPU). The most versatile *quality-focused* third-party brand — Overture now has more raw material lines and colors overall, but with more variation in verification depth across them.

**MatterHackers PRO Series** — Tighter QC than most budget brands. Reliable, no quirks. Good choice when you need a specific material/color not available from Bambu.

**AzureFilm** — Manufacturer TDS-confirmed on its core PLA, PLA Silk, ASA, and PETG lines, with reasonable color counts (13, 2, 2, and 3 respectively). Its newer lines (PLA Matte, PLA Prime, PLA Glitter, PLA Pastel, PLA-CF, PC-ABS, Nylon) are confirmed to exist but not yet independently spec-verified — treat those with more caution than the core lines. Not Bambu-verified for any material. A reasonable brand to consider once you're past the more established options above, particularly for its core PLA range.

**VoxelPLA** — USA-made, farm-tested across 250 machines, high-speed rated (400mm/s) on its PLA+ line. Drops straight into the stock Bambu PLA Basic profile with no changes — genuinely easy to use. Its PETG+ HS needs one specific profile tweak (PETG HF + 265°C nozzle) rather than being a pure drop-in. Decent chemistry and HS rating, but real-world shipping/color-consistency reports (TrustPilot) are a notch below the top-tier brands — check spools on arrival.

### Tier B — Good, use with awareness
**Overture** — Solid budget PLA and PETG, and by a wide margin the deepest catalog in this guide — 344 catalog entries spanning 15 material families including the widest color selection for PLA, PETG, ABS, ASA, TPU, and PC of any brand covered here. No adapter ring issues. Slightly more batch variation than Tier A.

**SUNLU** — Wide product range at budget prices. Silk PLA Rainbow is a unique item. All spools are plastic — no adapter issues. The go-to for budget silk and specialty PLAs.

**Creality Hyper** — Niche advantage at very high print speeds. Good range of materials. No exotic issues. Budget tier for most use cases.

### Tier B (use with caution)
**Hatchbox** — Proven quality but **every spool is cardboard** — the AMS Adapter Ring is mandatory for all materials. The adapter adds setup friction and low-level feed risk on long multi-color prints. Fine for single-color external spool use. For AMS printing, the cardboard spool is a meaningful operational disadvantage.

**MatterHackers Build Series** — Looser tolerances than PRO Series, fewer colors, lower price. Choose only when price is the sole constraint.

---

## Part 9 — Bambu Printer Compatibility Matrix

| Material | X1C / X1E | P1S | P1P | A1 | A1 mini | H2D |
|---|---|---|---|---|---|---|
| PLA (all variants) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| PETG | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| ABS | ✓ | ✓ | ✗ | ✗ | ✗ | ✓ |
| ASA | ✓ | ✓ | ✗ | ✗ | ✗ | ✓ |
| TPU (Bambu AMS) | ⚠ | ⚠ | ⚠ | ✗ | ✗ | ✓ AMS HT |
| PA / PA-CF | ✓ | ✓ | ✗ | ✗ | ✗ | ✓ |
| PC | ✓ | ✓ | ✗ | ✗ | ✗ | ✓ |
| PLA-CF / PETG-CF | ✓🔧 | ✓🔧 | ✓🔧 | ✓🔧 | ✓🔧 | ✓🔧 |
| Support W/G | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

🔧 = hardened nozzle required
Note: P1P has no enclosure — ABS, ASA, PC, PA are technically printable but warping risk is high. Not recommended.

---

## Part 10 — AMS Variant Compatibility Summary

| Material | AMS X/P | AMS Lite | AMS 2 Pro | AMS HT |
|---|---|---|---|---|
| PLA (all variants) | ✓ | ✓ | ✓ | ✓ |
| PETG | ✓ | ✓ | ✓ | ✓ |
| ABS | ✓ | ✗ | ✓ | ✓ |
| ASA / ASA-CF | ✓ | ✗ | ✓ | ✓ |
| TPU (Bambu for AMS) | ⚠ | ✗ | ✗ | ✓ |
| PA / PA-CF | ⚠ | ✗ | ⚠ | ✓ |
| PC | ⚠ | ✗ | ⚠ | ✓ |
| PLA-CF / PETG-CF | ✓🔧 | ✓🔧 | ✓🔧 | ✓🔧 |
| Cardboard spool (any) | ⚠📦 | ⚠📦 | ⚠📦 | ⚠📦 |

AMS HT is the most capable unit — required for TPU, PA, PA-CF, and PC multi-color printing.
AMS Lite (A1/A1 mini) cannot run ABS, ASA, or any material requiring enclosure.

---

## Part 11 — Nozzle Selection Guide

| Material | 0.4mm Brass | 0.4mm Hardened | 0.6mm Hardened | Notes |
|---|---|---|---|---|
| PLA, PETG, ABS, ASA, TPU | ✓ | ✓ | ✓ | Standard brass is fine |
| PLA Marble, PLA Sparkle | ⚠ | ✓ | ✓ | Monitor brass wear at volume |
| PLA-CF, PETG-CF, ASA-CF | ✗ | ✓ | ✓ recommended | 0.6mm reduces clogging risk |
| PA, PA-CF | ✗ | ✓ | ✓ recommended | PA-CF especially abrasive |
| PC | ⚠ | ✓ | ✓ | High temp — brass OK short-term |
| Support W / G | ✓ | ✓ | ✓ | Standard |

The Bambu hardened steel nozzle (0.4mm or 0.6mm) is the correct tool for any CF or abrasive material. The E3D ObXidian nozzle is a drop-in premium alternative with lower friction and longer life.

---

## Part 12 — Drying and Storage Reference

| Material Family | Drying Temp | Min Time | Priority | Storage |
|---|---|---|---|---|
| PLA, PLA+ | 45–55°C | 4–8h | Recommended | Sealed bag with desiccant |
| PETG, PETG-CF | 65°C | 6–8h | **Required** | Sealed, especially in humid climates |
| ABS, ASA | 65–80°C | 8h | Required | Sealed bag |
| TPU | 45–55°C | 6–8h | Required | Sealed bag |
| PA, PA-CF | **80°C** | **8–12h** | **Critical** | Sealed + desiccant + immediate print |
| PC, PC Blend | **80°C** | 6–8h | **Critical** | Sealed + desiccant |
| Support W | 55°C | 6h | Critical | Sealed — absorbs moisture in hours |
| Silk PLA | 45–55°C | 4h | Recommended | Sealed |

**Drying tips:**
- A food dehydrator is the most cost-effective drying solution for most filaments (set to appropriate temp)
- Print-dry simultaneously if your dryer supports the temperature and you're printing at speed
- Wet filament signs: popping/crackling sounds, excessive stringing, rough surface texture, reduced part strength
- PA is the most unforgiving — it will feel dry to touch but still have enough moisture to ruin a print. 12 hours at 80°C is the safe standard.

---

## Part 13 — Post-Processing by Material

| Material | Sanding | Acetone | Priming | Painting |
|---|---|---|---|---|
| PLA | ✓ (tedious) | ✗ | ✓ filler primer | ✓ acrylic/enamel |
| PETG | ✓ (gummy) | ✗ | ✓ adhesion primer | ✓ acrylic |
| ABS | ✓ | ✓✓ vapor smooth | ✓ | ✓ all types |
| ASA | ✓ | ⚠ (slower) | ✓ | ✓ |
| TPU | ✗ impractical | ✗ | ✗ | ⚠ flexible paint |
| PA | ✓ | ✗ | ✓ | ✓ acrylic |
| PC | ✓ | ⚠ | ✓ | ✓ |

**Acetone vapor smoothing for ABS/ASA** is the most powerful post-processing technique in FDM — a 30-minute vapor bath can produce injection-mold-like surface quality. Use with proper ventilation and no open flames. ASA smooths more slowly than ABS.

---

## Part 14 — What to Print in What Material: Decision Guide

```
Is the part structural / load-bearing?
├── No → PLA (fastest, easiest, cheapest)
└── Yes
    ├── Will it see heat > 60°C?
    │   ├── No → PETG (toughest easy material)
    │   └── Yes
    │       ├── Is it outdoors / UV-exposed?
    │       │   ├── Yes → ASA
    │       │   └── No
    │       │       ├── Up to 100°C → ABS
    │       │       └── Over 100°C → PC or PA-CF
    ├── Does it need to flex / absorb impact repeatedly?
    │   └── Yes → TPU (external spool) or PA (if rigidity also needed)
    ├── Does it need maximum stiffness / lightness?
    │   └── Yes → PLA-CF, PETG-CF, or PA-CF (+ hardened nozzle)
    └── Does it need precision tolerances?
        └── Yes → Prusament PLA (±0.02mm) or Prusament PETG
```

---

## Part 15 — Suggested Improvements Over the Original Request

Several additions in this guide go beyond what was explicitly requested. These are worth highlighting:

**1. Printer-model compatibility matrix (Part 9)**
A filament guide without printer context is incomplete for Bambu users. Whether you own an A1, P1S, or H2D determines which materials are even physically possible. The matrix makes this immediately clear.

**2. AMS variant compatibility summary (Part 10)**
The four AMS variants (X/P, Lite, 2 Pro, HT) have meaningfully different material limits. This is frequently misunderstood — many users assume "AMS-compatible" means compatible with all AMS variants. The summary table shows the real picture at a glance.

**3. Decision tree (Part 14)**
A guide that only describes materials without helping you choose between them leaves the key question unanswered. The decision tree takes you from application requirements to material recommendation in 4–5 steps.

**4. Nozzle selection (Part 11)**
Material selection and nozzle selection are inseparable for abrasive materials. The guide covers which nozzle to use for each material — this is a practical gap that causes real print failures for users who don't know CF materials eat brass nozzles.

**5. Drying reference table (Part 12)**
Drying is the single most common cause of print quality failures, especially for PETG, PA, and PC. A quick reference with temperatures and times is more useful than burying this information in each material section.

**6. Post-processing by material (Part 13)**
The finishing capabilities of a material are part of its practical profile. Knowing that ABS is acetone-smoothable and PA is paintable informs material choice for aesthetic applications.

**7. Overall brand tier summary (Part 8)**
Rather than leaving brand comparison implicit across 25 material sections, the consolidated tier table gives a single reference point for "which brand should be my default" across the whole catalog.

**8. OEM relationship notes**
eSUN's likely OEM relationship with Bambu Lab is actionable information — it suggests eSUN quality is closer to Bambu first-party than its price implies. Similarly, knowing Polymaker publishes confirmed hex codes and Prusament publishes tolerance batch statistics helps users calibrate how much to trust the data in the spreadsheets.

---

*Guide based on catalog data as of the filament reference system v3 generation date. Prices approximate. Brand formulations and product lines change — verify current availability at manufacturer sites.*
---

## Part 16 — Troubleshooting by Material

Understanding why a print is failing is just as important as knowing the right settings. This section organizes failure modes by material and gives concrete corrective actions specific to Bambu printers.

---

### 16.1 PLA Troubleshooting

#### Stringing / Oozing
**Symptoms:** Fine hairs between features, especially on small models.
**Causes:** Temperature too high, retraction too low, print speed too slow for the temperature.
**Fix on Bambu:**
- Reduce nozzle temperature by 5°C increments
- Enable "Avoid crossing perimeters" in Bambu Studio
- Increase travel speed
- If using third-party PLA: enable "wipe on retract" in filament settings

#### Under-extrusion / Gaps
**Symptoms:** Missing layers, rough surface, weak layer bonding.
**Causes:** Nozzle partially clogged, filament diameter inconsistency (more common in budget brands), feed gear slipping.
**Fix:**
- Cold pull: heat to 200°C, manually push filament, cool to 90°C, pull sharply to extract debris plug
- Increase temperature by 5°C
- Check filament diameter in 5 spots with calipers — if varies >0.05mm, switch brands
- With Bambu: run the built-in Flow Calibration tool

#### Layer Adhesion Failure / Delamination
**Symptoms:** Layers separate easily, print snaps along layer lines with minimal force.
**Causes:** Print temperature too low, cooling too aggressive, print speed too high for the temperature.
**Fix:**
- Increase print temperature 5°C
- Reduce part cooling fan speed by 10–15%
- Reduce print speed for wall loops specifically

#### First Layer Not Sticking
**Symptoms:** Print lifts, curls at corners, or detaches mid-print.
**Fix:**
- Run Bambu's automatic bed leveling before print
- Clean PEI plate with isopropyl alcohol
- For smooth PEI: PLA often needs 50–60°C bed temp despite being "optional"
- For textured PEI: 35°C is usually sufficient — PLA bonds strongly to texture

#### Brittle Prints / Snapping Filament
**Symptoms:** Prints snap under light force, filament breaks in the AMS buffer.
**Causes:** Filament has absorbed moisture (even PLA becomes brittle when wet), or material is inherently brittle (silk variants, cold storage).
**Fix:**
- Dry at 55°C for 6–8 hours
- For silk PLA: this is partly inherent — avoid AMS on long multi-color prints with silk
- Store sealed with desiccant

---

### 16.2 PETG Troubleshooting

PETG is more demanding than PLA in two specific areas: moisture and bed adhesion. Most PETG problems trace to one of these two root causes.

#### Excessive Stringing
**Symptoms:** Thick strings between features, oozing blobs at travel endpoints.
**Causes:** Moisture is the #1 cause of PETG stringing. Wet PETG strings massively more than dry PETG. Temperature too high is the #2 cause.
**Fix:**
- **Dry the filament first** — 65°C, 6–8 hours. Retry before adjusting any other settings.
- If still stringing after drying: reduce temperature 5°C
- Increase retraction slightly (Bambu default retraction for PETG is conservative)
- Enable "Avoid crossing perimeters"

#### Sticking to Build Plate (Can't Remove Print)
**Symptoms:** Print won't flex off PEI, or tears the surface.
**Causes:** PETG bonds aggressively to smooth PEI. A serious and common problem.
**Fix:**
- **Use textured PEI** for PETG — this is the strongest recommendation. PETG releases cleanly from textured PEI after cooling.
- If using smooth PEI: apply thin layer of glue stick as release agent, or use the Bambu Cool Plate
- Never try to remove PETG from smooth PEI while warm — let it cool to room temperature first; thermal contraction helps release

#### Bubbling / Popping During Print
**Symptoms:** Audible popping sounds, surface pitting, rough texture, weak parts.
**Cause:** Moisture in filament. This is the clearest and most unambiguous moisture signal.
**Fix:** Dry immediately at 65°C for 8h minimum. There is no other fix — this is definitively moisture.

#### Poor Transparency (Transparent Variants)
**Symptoms:** Translucent variant looks milky/opaque rather than clear.
**Causes:** Fast printing, high cooling, too many walls.
**Fix:**
- Slow down significantly (40–60mm/s)
- Reduce cooling fan speed
- Print fewer perimeters (1–2 walls max for transparency)
- Increase layer height (0.2–0.3mm for better light transmission)
- Polymaker PolyLite PETG in transparent produces the best optical results of brands in this catalog

#### Warping / Lifting Corners
**Symptoms:** Corners lift off bed during print.
**Fix:**
- Ensure bed temp is 70–85°C for PETG
- Add brim (3–5mm) in Bambu Studio slicer settings
- Ensure enclosure is closed or at least draft-free

---

### 16.3 ABS/ASA Troubleshooting

ABS and ASA problems are almost always environment-related. If your Bambu enclosure isn't holding heat, every ABS/ASA problem becomes harder to solve.

#### Warping / Delamination / Cracking
**Symptoms:** Print warps up from bed, layers crack during printing (sometimes audibly), corners lift.
**Causes:** Enclosure temperature too low, draft air entering enclosure, insufficient bed temperature, insufficient first-layer adhesion.
**Fix:**
- Pre-heat enclosure: run ABS preheat for 10+ minutes before print starts. Target chamber temp >40°C.
- Close all doors and top cover on X1C/P1S
- Use Bambu's first-party ABS profile — it includes the correct chamber management sequence
- Increase bed temperature to 90–100°C
- Apply ABS juice (ABS dissolved in acetone) to PEI if severe warping persists
- Add brim, especially on tall or thin prints

#### Fumes / Odor
**Symptoms:** Strong styrene smell during printing.
**Fix (not optional):**
- Run HEPA + activated carbon filter module (built into X1C/H2D, optional on P1S)
- Ensure print room has ventilation to outside
- Do not print ABS/ASA in unventilated small rooms
- Do not remain in the room during extended ABS prints without exhaust ventilation

#### Surface Crazing / Micro-cracks
**Symptoms:** Fine cracks appear on print surface after removal, especially with dimensional stress.
**Cause:** Residual internal stress from rapid cooling, or low-quality filament with poor rubber content.
**Fix:**
- Slow down print speed
- Increase enclosure temperature
- Switch to Bambu Lab ABS for most consistent results — third-party ABS has more variation

#### Weak Layer Bonds
**Symptoms:** ABS print snaps along layers with less force than expected.
**Cause:** Print temperature too low, enclosure temperature too low, or cooling fan running.
**Fix:**
- Disable part cooling fan for ABS (the Bambu ABS profile does this)
- Increase nozzle temp to 250–270°C
- Ensure enclosure is sealed and pre-heated

---

### 16.4 TPU Troubleshooting

TPU printing is distinct enough from rigid materials that it almost requires a separate mindset. The flexibility that makes TPU useful also makes it mechanically awkward in any feed system.

#### Grinding / Slipping at Extruder
**Symptoms:** Clicking from extruder, under-extrusion, or filament ground to powder.
**Cause:** Print speed too fast for TPU's flexibility — the soft filament buckles between the extruder gear and the melt zone.
**Fix:**
- Reduce print speed to 20–35mm/s for wall loops and infill
- Do not exceed 40mm/s for any TPU feature
- Bambu's TPU profile handles this correctly — do not override the speed settings

#### Excessive Stringing
**Cause:** TPU is inherently stringy. Retraction is the enemy — too much retraction causes jams.
**Fix:**
- Use zero or near-zero retraction for TPU
- The Bambu TPU profile sets this correctly
- Enable "Avoid crossing perimeters" to reduce travel moves

#### AMS Feeding Issues (Bambu TPU only)
**Symptoms:** TPU not feeding properly through AMS X/P, buckling in buffer.
**Fix:**
- Use AMS HT with dedicated TPU outlet — this is the correct solution
- AMS X/P special mode for TPU is unreliable for long prints
- For non-Bambu TPU on any AMS: use external spool (bypass AMS entirely)

---

### 16.5 PA (Nylon) Troubleshooting

Nylon is unforgiving of moisture. Before diagnosing any other issue, dry the filament.

#### Stringing / Oozing
**Cause:** Almost certainly moisture.
**Fix:** Dry at 80°C for 12 hours minimum. If printing immediately from the dryer, most nylon stringing problems disappear.

#### Layer Delamination
**Cause:** Nylon has poor layer adhesion when moisture content is high, or when print temperature is too low.
**Fix:**
- Dry thoroughly first
- Increase temperature 5°C at a time up to max spec
- Reduce part cooling to minimum

#### Warping and Bed Adhesion
**Cause:** Nylon shrinks significantly on cooling.
**Fix:**
- Use Garolite (G10 sheet) bed surface — nylon bonds to it better than any PEI surface
- Or: apply generous PVA glue (Elmer's) to PEI and let dry before printing
- Keep enclosure sealed, chamber temperature elevated
- Add generous brim (5–8mm)
- Print first layer slow and hot

#### Absorbing Moisture After Print
Nylon parts absorb moisture from ambient air over days/weeks, becoming slightly flexible and dimensionally unstable. For critical-tolerance PA parts in humid environments, apply a clear coat sealant.

---

### 16.6 PC (Polycarbonate) Troubleshooting

PC is the most demanding material in this catalog. It combines high temperatures, high shrinkage, and high moisture sensitivity.

#### Warping
**Cause:** PC has one of the highest thermal expansion coefficients of any FDM material. Shrinkage on cooling creates severe internal stress.
**Fix:**
- Pre-heat enclosure to maximum (50°C+)
- High bed temperature (100–120°C)
- ABS juice or PC-specific adhesive on bed
- Keep prints small or add warp-compensation geometry
- Prusament PC Blend warps significantly less than pure PC — consider it instead

#### Layer Delamination
**Cause:** Temperature too low, or moisture.
**Fix:**
- Dry at 80°C, 8+ hours immediately before print
- Increase temperature to upper end of spec (290–295°C for Prusament PC Blend)
- Maximum enclosure temperature

---

## Part 17 — Multi-Color Printing and AMS-Specific Guidance

Multi-color printing on Bambu printers is one of the most powerful and distinctive features of the platform. The AMS system enables color changes within a single print without manual intervention. This section covers how material choices affect multi-color print success.

### 17.1 How the AMS Works (Mechanically)

The AMS stores up to 4 spools (8 with dual AMS units). When a color change is needed, the current filament is retracted back to the AMS, a purge sequence deposits the color-contaminated melt into the waste chute, and the new filament is fed forward. The purge volume determines how cleanly the transition appears.

Key mechanical constraints:
- **Bowden tube length:** filaments travel up to 700mm+ from AMS to nozzle. Brittle filaments (silk PLA, some CF variants) are at risk of snapping during long retractions.
- **Feed path diameter:** designed for 1.75mm rigid filaments. Flexible materials (TPU) buckle — only AMS HT with dedicated flexible path handles this.
- **Spool hub dimensions:** designed for plastic spools. Cardboard spools don't fit without the Adapter Ring.

### 17.2 Purge Volume Optimization

Every color change wastes filament in the purge tower or chute. The purge volume required depends on:
- **Color direction:** dark-to-light requires far more purge volume than light-to-dark
- **Material:** PETG requires more purge than PLA due to higher melt viscosity
- **Nozzle size:** larger nozzles need proportionally more purge

**Bambu Studio purge optimization:**
- Use the color flush multiplier settings — don't accept defaults for dark/light transitions
- Enable "Flush into infill" — this hides purge material inside the print rather than wasting it in a tower
- Enable "Flush into support" — same principle for support-heavy prints
- Order your AMS slots so light colors are loaded first, dark colors last — reduces average purge volume

### 17.3 Best Materials for Multi-Color Printing

**Excellent for multi-color (high reliability, low waste):**
- PLA Basic — best AMS reliability, lowest purge volume, widest color range
- PLA Matte — excellent; the matte texture hides any minor color bleed at boundaries
- PETG Basic — reliable; slightly higher purge volume than PLA
- Support W/G — excellent for dissolve/break support in multi-material prints

**Good for multi-color (minor caveats):**
- PLA Silk — functional but brittleness increases snapping risk on long jobs. Monitor buffer. Use shorter AMS-to-extruder distance if possible.
- PLA Translucent — reliable, but mixing with opaque colors in a single layer creates interesting bleed effects — design for it or plan transitions carefully
- PLA Marble/Sparkle/Glow — all print reliably in AMS; particle content is not problematic

**Use with caution:**
- ABS / ASA — work in AMS X/P and 2 Pro but require full enclosure temperature management for each material in the AMS. Multi-material ABS requires all slots to use materials compatible with enclosure temperatures (~90°C chamber). Mixing ABS with PLA in AMS is not recommended — the temperature gap is too large.
- PETG-CF / PLA-CF — require hardened nozzle. The abrasive CF content doesn't affect AMS operation, only nozzle wear. Use hardened nozzle and plan for slightly higher purge volume.

**Not suitable for multi-color AMS:**
- Standard TPU (all brands except Bambu AMS TPU) — external spool only
- PA, PA-CF, PC — require AMS HT with appropriate high-temp path management

### 17.4 Material Compatibility in Multi-Material Prints

When printing two materials in the same print (e.g. rigid body + flexible interface, or model + support), compatibility between materials is critical. The support/interface material must not bond too strongly to the model material.

| Model Material | Compatible Support | Notes |
|---|---|---|
| PLA | Support W (dissolve) | Ideal — clean removal, smooth surface |
| PLA | Support G (breakaway) | Good — snaps clean, no solvent needed |
| PLA | PLA (same material) | Works; removal more difficult |
| PETG | Support G | Best option for PETG — designed for this |
| PETG | PLA interface | PETG doesn't bond strongly to PLA — functional |
| ABS | Support G | Good; ABS-on-PLA interface also works |
| ABS | ABS support | Works but bonds strongly — harder removal |

**Avoid:** Printing PETG directly against PLA support — PETG bonds too strongly to PLA for easy separation in most geometries.

### 17.5 Cardboard Spool Warning for Multi-Color Prints

Hatchbox and Polymaker Panchroma Matte use cardboard spools that require the AMS Adapter Ring. For single-color prints, the adapter ring adds minimal risk. For multi-color prints with 4+ hour runtimes, the friction dynamics between the cardboard core and adapter ring can cause intermittent feed issues — the cardboard can deform slightly under the mechanical cycling of repeated AMS retractions.

**Recommendation:** Use plastic-spool filaments in AMS for multi-color prints. Reserve cardboard-spool brands for single-color external-spool use or accept the risk with monitoring.

---

## Part 18 — Bambu Studio Settings Deep-Dive by Material

This section covers the non-obvious Bambu Studio settings that matter most for each material family. Default profiles are excellent starting points, but knowing why the settings are what they are enables better troubleshooting and optimization.

### 18.1 PLA Settings

| Setting | Default | Notes |
|---|---|---|
| Nozzle temp | 220°C | First layer 225°C; Prusament needs 230°C |
| Bed temp | 55°C (smooth PEI) | 35°C textured PEI; 0°C engineering plate |
| Part cooling | 100% | Maximum for PLA — critical for bridging and overhang quality |
| Retraction length | 0.8–1.0mm | Direct drive; AMS adds effective retraction through bowden |
| Print speed | Up to 300mm/s | Bambu PLA supports this; third-party may need 200mm/s max |
| First layer speed | 50mm/s | Don't reduce further — slows print significantly |
| Volumetric flow | Up to 24mm³/s | Bambu PLA; third-party 14–18mm³/s |

**Key optimization:** Volumetric flow rate is the real speed limit. The `mm/s` speed setting is only meaningful when combined with layer height and line width. At 0.2mm layer height and 0.4mm line width, 24mm³/s ≈ 300mm/s. At 0.08mm layer height (fine quality mode), 24mm³/s ≈ 750mm/s nominal but wall acceleration limits apply.

### 18.2 PETG Settings

| Setting | Default | Notes |
|---|---|---|
| Nozzle temp | 240°C | Prusament: 250°C; SUNLU/Overture: 235°C |
| Bed temp | 70°C (textured PEI) | Strongly recommend textured PEI for PETG |
| Part cooling | 30–50% | Less than PLA — cooling too fast weakens layer bonds |
| Retraction | 0.8mm | PETG needs slightly less retraction than PLA |
| Avoid crossing perimeters | Enable | Critical for PETG stringing reduction |
| Print speed | Up to 200mm/s | PETG flows more slowly than PLA |
| Volumetric flow | 14–16mm³/s | PETG max flow is lower than PLA |

**Critical PETG setting:** In Bambu Studio, under Filament → Advanced, there is a "pressure advance" (PA) calibration setting. PETG benefits significantly from running the PA calibration test before long prints — it reduces corner bulging and stringing simultaneously.

### 18.3 ABS Settings

| Setting | Default (Bambu) | Notes |
|---|---|---|
| Nozzle temp | 260°C | 270°C for better layer bonding on tall prints |
| Bed temp | 100°C | Never below 90°C |
| Part cooling | 0% | Disable completely for ABS |
| Chamber preheat | Enable | Bambu profile runs 10-min preheat sequence |
| Print speed | Up to 200mm/s | Speed less critical than temperature management |
| First layer speed | 40mm/s | Slower than PLA first layer |
| Brim width | 5–10mm | Almost always use brim for ABS |

**Critical ABS setting:** In Bambu Studio, enable "Enable AUX fan" and set it to 0% for ABS. The auxiliary fan on X1C can cool the print chamber if misconfigured — it should be off for ABS. The Bambu ABS profile handles this, but verify when using third-party ABS profiles.

### 18.4 TPU Settings

| Setting | Default | Notes |
|---|---|---|
| Nozzle temp | 235°C | Range 220–240°C |
| Bed temp | 35°C | Low bed temp prevents over-adhesion |
| Part cooling | 30–50% | Moderate — TPU needs some cooling |
| Retraction | 0–0.5mm | Minimal retraction only — over-retraction causes jams |
| Print speed | 30–40mm/s | Wall loops; max overall 50mm/s |
| Infill speed | 30mm/s | Don't push infill speed for TPU |
| Avoid crossing perimeters | Enable | Reduces stringing |
| Infill overlap | 20–25% | Reduced vs PLA — prevents over-extrusion bulging |

**TPU-specific Bambu note:** In the filament settings, set "Filament type" to TPU-95A for correct flow compensation. The Bambu TPU profile automatically reduces the extruder's maximum movement acceleration — this is important and should not be overridden.

### 18.5 PA Settings

| Setting | Default | Notes |
|---|---|---|
| Nozzle temp | 270°C | Max for standard hotend |
| Bed temp | 55°C with PVA glue | Or Garolite sheet at 55°C |
| Part cooling | 0–10% | Minimal — PA needs heat to bond layers |
| Retraction | 1.0–1.5mm | More than PLA to prevent ooze |
| Enclosure | Required | Chamber temperature matters significantly |
| Brim | 5–8mm | Always for PA |
| Dry immediately before print | Critical | Pre-warm in dryer at 80°C; print directly from dryer if possible |

### 18.6 PC Settings

| Setting | Default | Notes |
|---|---|---|
| Nozzle temp | 280–295°C | Prusament PC Blend range |
| Bed temp | 110–120°C | Very high — ensure bed can reach this |
| Part cooling | 0% | Disable entirely |
| Enclosure | Required + preheated | 50°C chamber target |
| Print speed | Slow — 60–80mm/s | PC doesn't tolerate fast printing well |
| Layer height | 0.2mm | Thicker layers improve bonding |
| Brim | 8–10mm | Large brim always |
| Dry before printing | 80°C / 8h | Non-negotiable |

---

## Part 19 — Cost-Per-Kilogram Analysis and Value Assessment

Understanding the true cost of filament involves more than the price tag. Failed prints, wasted purge material, and nozzle wear all factor in.

### 19.1 Price Reference (USD, 1kg spool, approximate)

| Brand | PLA | PETG | ABS | ASA | TPU | Specialty |
|---|---|---|---|---|---|---|
| Bambu Lab | ~$20 | ~$20 | ~$22 | ~$22 | ~$25 | ~$25–35 |
| Prusament | ~$30 | ~$32 | N/A | ~$35 | N/A | ~$38 (PC) |
| Polymaker | ~$22 | ~$22 | ~$22 | N/A | ~$24 | ~$22 (Panchroma) |
| eSUN | ~$19 | ~$19 | ~$19 | ~$22 | ~$20 | ~$20 |
| MatterHackers PRO | ~$23 | ~$23 | ~$25 | N/A | N/A | N/A |
| Overture | ~$18 | ~$18 | ~$18 | N/A | ~$18 | N/A |
| SUNLU | ~$17 | ~$17 | ~$17 | N/A | ~$18 | ~$18 (silk) |
| Creality Hyper | ~$20 | ~$20 | ~$20 | ~$22 | ~$18 | ~$22 (CF) |
| Hatchbox | ~$22 | ~$22 | ~$22 | N/A | N/A | N/A |

### 19.2 True Cost Factors

**Print failure rate:**
A failed 100g print at $22/kg costs $2.20 in material plus time. Budget brands with more batch variation have higher effective failure rates. For critical functional parts, Prusament's ±0.02mm tolerance and Bambu's RFID profiles justify their price premium through reduced failure rate.

**Purge waste for multi-color:**
In a 4-color AMS print with 20 color changes, purge waste can easily reach 20–40g per print. At $22/kg, that's $0.44–$0.88 of waste per print. Across hundreds of prints this accumulates. Materials with lower purge requirements (PLA vs PETG) and optimized purge settings (flush into infill) reduce this.

**Nozzle wear:**
Brass nozzles last indefinitely with PLA but wear quickly with CF materials. A brass nozzle costs ~$3–5. A hardened steel nozzle costs ~$15–25 but lasts effectively indefinitely with any material. If you print CF materials regularly, a hardened nozzle pays for itself quickly and removes any per-print cost anxiety.

**Drying time/energy:**
Budget brands often need more drying time or more frequent drying due to lesser moisture barrier packaging. Most Bambu first-party filaments come individually vacuum-sealed with desiccant — better factory moisture protection means less pre-print drying for casual users.

### 19.3 Price vs. Quality Matrix

For different user types, the optimal brand mix differs:

**Hobbyist / casual user:**
- PLA: Bambu Basic (RFID convenience) or Overture (budget)
- PETG: eSUN or SUNLU
- Specialty: Bambu only (no third-party alternatives for marble, glow, etc.)
- Total recommendation: Bambu for first-party, Overture/SUNLU as fillers

**Multi-color printing enthusiast:**
- All AMS slots: Bambu Basic PLA (most reliable AMS performance)
- Accent colors: Bambu Matte or Translucent
- Don't compromise AMS reliability with cardboard-spool or exotic brands

**Functional parts / engineering:**
- PLA: Prusament (tolerance matters)
- PETG: Prusament or eSUN
- ABS: Bambu (enclosure integration)
- ASA: Prusament (published UV data)
- CF: Bambu (widest CF selection, RFID profiles)
- Total recommendation: Prusament + Bambu for engineering

**High-volume / cost-conscious:**
- PLA: eSUN ePLA+ (Bambu OEM quality at lower cost)
- PETG: eSUN ePETG
- ABS: eSUN eABS+ or Overture
- TPU: Overture (external spool — brand matters less)
- Total recommendation: eSUN across the board

---

## Part 20 — Color Selection Across Brands

One of the most practical reference questions in this catalog is: "I want a specific shade — which brand has it and can I trust the hex?"

### 20.1 Hex Code Reliability by Brand

| Brand | Hex Source | Reliability |
|---|---|---|
| Bambu Lab (PLA Basic, Matte, PETG, ABS, PLA Trans.) | Official Bambu hex PDF | ✓ Confirmed |
| Polymaker PolyLite PLA | Official shop.polymaker.com | ✓ Confirmed |
| Prusament | Prusa website product pages | ✓ Confirmed |
| All other brands in catalog | Approximate from product images | ⚠ Visual estimate |

For confirmed hex codes, the color chips in the spreadsheets accurately represent the filament color. For approximate brands, treat the hex as a visual reference — the actual swatch color may vary by 5–20% in any channel.

### 20.2 Finding Specific Shades

**Need true black:** All brands offer black PLA. Hex varies from #000000 (true black, Bambu) to #111111 (slightly warm black, others). For photorealistic black in a print, Bambu Black at #000000 is the deepest.

**Need true white:** Bambu PLA Basic "Jade White" is actually #FFFFFF but warm-tinted in practice. Bambu PLA Matte "Ivory White" is also #FFFFFF. Polymaker's "Cold White" (#EAECF5) has a slight blue tint — better for scientific/industrial aesthetics.

**Need skin tones:** SUNLU PLA+ has a "Skin" color (#FFCC99) and Polymaker PolyLite PLA has "Beige" (#C2AB72). Neither is ideal for human skin representation — mixing multi-color is more effective.

**Need specific corporate colors:** With Bambu PLA Basic's 30-color palette and confirmed hex codes, it's possible to find reasonable approximations of brand colors. Bambu's "Cobalt Blue" (#0056B8) is close to many institutional blues; "Red" (#C12E1F) approximates many corporate reds.

**Need pastels or muted tones:** Bambu PLA Matte has the strongest muted/earthy palette with 25 colors. Sakura Pink, Latte Brown, Desert Tan, and Ice Blue have no close equivalents in other brands' catalogs.

**Need metallics:** Bambu Silk PLA (6 colors) or eSUN/SUNLU/Polymaker/AzureFilm Silk PLA. For true-metallic-feel filament (weighted, brushed metal), no FDM material matches — but Bambu Sparkle and CF materials give the closest visual approximation.

### 20.3 Color Availability Gap Analysis

Some categories are underserved across all brands in the catalog:

- **Pastels:** Bambu Matte has the best pastel range. Most brands have few or no true pastels.
- **Neons/Fluorescents:** SUNLU PLA+ "Glow Green" (#39FF14) is the brightest available. True neons are rare.
- **Browns/Earth tones:** Bambu Matte excels (terracotta, latte, caramel, dark chocolate). Other brands have 1–2 browns at most.
- **Multi-transition colors:** No longer a two-option niche — color-transition/rainbow filaments now span several brands: Overture (5 variants across PLA, PLA Matte, PLA Rock, and PLA Professional lines), SUNLU (4, including a PETG Rainbow and a dedicated Silk Multi-Color Rainbow), eSUN (PLA-Silk Rainbow and TPU Rainbow), and Creality Hyper (1, gradient PLA). Overture currently has the widest transition-color selection.
- **True translucents beyond PLA:** Only Bambu offers PETG in non-opaque form (though all PETG becomes slightly translucent in thin walls). True transparent PETG is available from Polymaker.

---

## Part 21 — Environmental Considerations

### 21.1 PLA Biodegradability — the Real Story

PLA is frequently marketed as "biodegradable" and "eco-friendly." The reality is more nuanced:

- PLA **is** compostable — under industrial composting conditions (>60°C, high humidity, specific microorganisms)
- PLA does **not** degrade in home compost, backyard conditions, or in the ocean in any practical timeframe
- Printed PLA has lower surface area than PLA sheet/film, meaning even industrial composting is slower
- The environmental advantage of PLA over petroleum-based plastics is real but modest — it primarily reduces the carbon intensity of feedstock production

**Practical implication:** Don't print PLA with the expectation that scrapped prints will biodegrade safely. Dispose via plastic recycling programs where available, or dedicated filament recycling services.

### 21.2 Filament Recycling

Several services accept failed prints and spool cores for recycling:
- Filament-specific recycling programs exist in some regions
- Bambu's spool return program (check current availability)
- Polymaker's cardboard spools (Panchroma/PolyTerra) are more readily recyclable than plastic spools, which is the design rationale for the cardboard choice despite the AMS adapter inconvenience

### 21.3 Fumes and Particle Emissions

All heated thermoplastics emit particles and volatile organic compounds (VOCs):

| Material | Emission Level | Key Compounds | Precautions |
|---|---|---|---|
| PLA | Low | Lactide, trace | Room ventilation adequate |
| PETG | Low-moderate | Acetaldehyde | Ventilation recommended |
| ABS | High | Styrene, butadiene | Exhaust ventilation required |
| ASA | High | Styrene, acrylate | Exhaust ventilation required |
| Nylon/PA | Moderate | Caprolactam | Ventilation recommended |
| PC | Moderate-high | Styrene (trace) | Ventilation recommended; BPA emission from FDM PC is disputed in literature |
| CF composites | Moderate | Base material + micro-fibers | Fine particle concern — HEPA filter |

The Bambu HEPA + activated carbon filter module significantly reduces particle and VOC exposure. For ABS/ASA printing, an additional exhaust duct to outside is recommended even with the filter running.

---

## Part 22 — Specialty Filament Notes (Expanded)

### 22.1 Glow-in-the-Dark Filaments

Both Bambu PLA Glow and Hatchbox Glow variants work on the same principle: strontium aluminate phosphorescent particles embedded in PLA. Key practical notes:

- **Glow intensity increases with UV charging** — a UV flashlight for 30 seconds produces a stronger and longer-lasting glow than room light exposure
- **The glow color is always blue-green regardless of daylight spool color** — there is no red glow or purple glow in any current affordable FDM material
- **Particle abrasiveness is minimal** — strontium aluminate is softer than carbon fiber; brass nozzle wear is negligible at normal volumes
- **Print temperature** can be slightly lower than standard PLA — the particles absorb heat slightly; starting at 215°C and adjusting is recommended
- **Layer height** affects glow intensity — thicker layers (0.2mm+) transmit more light through the part

### 22.2 Marble and Composite PLA

The marble effect in Bambu PLA Marble comes from swirled layers of different density material within the spool — the "veining" is not printed, it's already in the filament and rotates as the spool unwinds. This means:

- The marble pattern is **random and unrepeatable** — two identical print files will have different vein patterns
- The effect is most prominent on **larger, flatter surfaces** — small features don't show it
- The mineral fill makes marble PLA slightly more abrasive than standard PLA — monitor nozzle wear on very long single-color prints
- **Blending marble with non-marble PLA in multi-color** can produce interesting effects — marble for main body, solid for accents

### 22.3 Silk PLA Behavior in Multi-Color Prints

When combining Silk PLA with matte or standard PLA in a multi-color print, the interface between gloss and matte surfaces becomes visible as a distinct line. This can be:

- **Intentional design element** — the gloss/matte boundary creates a natural visual separation that works well for logos, text, accents
- **Unintended artifact** — if you want a seamless multi-color print, use materials from the same finish family (all matte or all standard)

Silk PLA also has a higher melt viscosity than standard PLA, which means color purging between silk and non-silk materials requires 10–15% more purge volume than same-type transitions.

### 22.4 Support W vs Support G — Choosing the Right Support Material

| Factor | Support W (Water-Soluble) | Support G (Breakaway) |
|---|---|---|
| Removal method | Dissolve in warm water | Snap/break off manually |
| Surface quality | Excellent — smoothest possible | Very good — minor marks |
| Suitable model materials | PLA primarily | PETG, ABS, PLA |
| Suitable geometry | Complex internal supports, deep channels | External supports, accessible surfaces |
| Cost | Higher (material cost) | Lower |
| Time | Dissolution time + water contact | Manual removal time |
| Moisture sensitivity | Extreme — store sealed | Low |
| AMS slot usage | 1 slot for support | 1 slot for support |

**Practical guidance:**
- For models with **internal cavities** or supports that can't be physically reached: Support W (water-dissolve) is the only practical choice
- For models with **external supports** on accessible surfaces: Support G is faster and cheaper
- For **PETG** models: Support G is almost always the right choice — Support W was designed for PLA temperatures and doesn't interface as cleanly with PETG
- For **ABS** models: Support G; Support W is too temperature-sensitive for the ABS chamber temps

---

## Part 23 — Buying Guide and Practical Recommendations

### 23.1 Starter Inventory for a New Bambu Owner

If you're just starting out or building your first filament inventory:

**Essential (buy these first):**
1. **Bambu Lab PLA Basic — White** — the universal starting color; calibrate everything against white
2. **Bambu Lab PLA Basic — Black** — the universal accent/contrast color
3. **Bambu Lab PETG Basic — Black or White** — one functional material for actual parts

**Expand to:**
4. **Bambu Lab PLA Basic — 2–3 more colors** of your choice for multi-color printing
5. **Bambu Lab PLA Matte** — 1–2 colors in the matte/earthy range for improved aesthetics
6. **eSUN ePETG — Transparent** — for diffuser/display applications

**When ready for engineering materials:**
7. **Bambu Lab ABS — Black** — for heat-resistant functional parts (P1S/X1C/H2D only)
8. **Prusament PETG — Prusa Orange or Black** — for precision functional parts
9. **Bambu Lab PETG-CF — Black** — for maximum stiffness applications

**For advanced multi-color:**
10. **Bambu Lab Support W** — for complex internal support geometries
11. **Bambu Lab PLA Translucent** — 1–2 colors for light-diffusion features

### 23.2 Storage System Recommendations

Based on the moisture sensitivity profiles in this catalog:

**Immediate-use storage (1–4 weeks):**
- Sealed zip-lock bag with one 30g silica desiccant pack per spool
- Store in cool, dry location away from sunlight
- Fine for PLA, PETG, ABS, ASA

**Long-term storage (>1 month):**
- Vacuum-sealed bags with desiccant
- Or airtight filament storage boxes with desiccant indicator
- Check desiccant monthly — regenerate in oven at 120°C for 1 hour when indicator changes

**Critical materials — dedicated containers:**
- PA, PA-CF: Store in sealed containers with fresh desiccant. Use within 24 hours of opening.
- Support W: Never leave open. Remove from container, print, reseal immediately.
- PC, PC Blend: Same as PA

**Filament dryers worth owning:**
A dedicated filament dryer is more consistent than an oven (ovens have large temperature swings). The Bambu AMS HT has a built-in drying function for most common materials. For other AMS variants, a standalone filament dryer set to the appropriate temperature for each material is the most reliable solution.

### 23.3 When to Retire Filament

Even with good storage, filament has a practical shelf life:

| Material | Well-stored (sealed/desiccant) | Poorly stored (open air) |
|---|---|---|
| PLA, ABS, ASA | 2–4 years | 6–12 months |
| PETG | 2–3 years | 3–6 months |
| TPU | 2–3 years | 6–12 months |
| PA, PC | 1–2 years (sealed) | Weeks to months |
| Support W | 1 year (sealed) | Days |

Signs that filament is past its useful life even after drying attempts:
- Snaps when bent in a small radius (especially severe in PLA)
- Bubbles or pitting persist after extended drying at correct temperature
- Inconsistent extrusion that can't be resolved with temperature or speed changes
- Visible surface degradation on the spool (whitening, color change)

---

## Part 24 — Quick Reference Summary Tables

### Material Properties at a Glance

| Material | HDT (°C) | Strength | Flexibility | UV Resist | Enclosure | AMS | Diff. |
|---|---|---|---|---|---|---|---|
| PLA | 55–60 | Medium | Low | Poor | No | ✓ all | ★☆☆☆☆ |
| PLA+ | 55–65 | Med-High | Low-Med | Poor | No | ✓ all | ★☆☆☆☆ |
| PLA Silk | 55–60 | Low-Med | Very Low | Poor | No | ✓ all | ★☆☆☆☆ |
| PLA-CF | 55–65 | High (rigid) | Very Low | Poor | No | ✓ all🔧 | ★★☆☆☆ |
| PETG | 75–85 | Med-High | Med | Fair | No | ✓ all | ★★☆☆☆ |
| PETG-CF | 80–90 | High (rigid) | Low | Fair | No | ✓ all🔧 | ★★☆☆☆ |
| ABS | 95–100 | High | Med | Fair | Required | ✓ (no Lite) | ★★★☆☆ |
| ASA | 95–100 | High | Med | Excellent | Required | ✓ (no Lite) | ★★★☆☆ |
| ASA-CF | 100–110 | Very High | Low | Excellent | Required | ✓ (no Lite)🔧 | ★★★★☆ |
| TPU | 70–80 | Med | Very High | Good | No | ✓ HT only | ★★★☆☆ |
| PA | 100–130 | Very High | Med-High | Good | Recommended | ⚠ HT best | ★★★★☆ |
| PA-CF | 130–150 | Exceptional | Low | Good | Required | ⚠ HT best🔧 | ★★★★★ |
| PC | 115–120 | Exceptional | Low | Good | Required | ⚠ HT best | ★★★★★ |

*HDT = Heat Deflection Temperature. Difficulty ★☆☆☆☆ = beginner friendly, ★★★★★ = expert only.*

---

### Print Temperature Quick Reference

| Material | Print Temp Range | Bed Temp | Enclosure |
|---|---|---|---|
| PLA / PLA+ | 190–230°C | 25–60°C | Not required |
| PLA Matte | 195–230°C | 35–55°C | Not required |
| PLA Silk | 190–225°C | 35–55°C | Not required |
| PLA-CF | 200–250°C | 50–70°C | Not required |
| PETG | 220–260°C | 70–90°C | Not required |
| PETG-CF | 230–260°C | 70–85°C | Not required |
| ABS | 240–270°C | 90–110°C | Required |
| ASA | 240–275°C | 90–110°C | Required |
| TPU 95A | 210–240°C | 25–45°C | Not required |
| PA | 255–275°C | 45–65°C | Strongly recommended |
| PA-CF | 260–280°C | 45–65°C | Strongly recommended |
| PC | 260–295°C | 100–120°C | Required |
| Support W | 200–230°C | 35–50°C | Not required |
| Support G | 220–240°C | 35–50°C | Not required |

---

### Brand Quick Reference

| Brand | Best Material(s) | Avoid For | AMS Caveat | Price Range |
|---|---|---|---|---|
| Bambu Lab | Everything — esp. specialty | N/A | None | Mid–High |
| Prusament | PLA (precision), PETG, ASA | — | Custom profiles needed | High |
| Polymaker | PLA variety, PETG transparent | Panchroma in AMS (cardboard) | Panchroma needs adapter ring | Mid |
| eSUN | PLA+, PETG, full range value | — | None | Budget–Mid |
| Overture | PLA budget, PETG budget | — | None | Budget |
| SUNLU | Silk PLA, PLA budget | — | None | Budget |
| Hatchbox | Colors variety | AMS multi-color (cardboard risk) | Adapter ring on all spools | Mid |
| Creality Hyper | High-speed printing | — | None | Mid |
| MatterHackers PRO | PLA/PETG quality third-party | — | None | Mid–High |
| MatterHackers Build | Budget starter only | Precision parts | None | Budget–Mid |

---

*This guide covers the full catalog as of the filament reference system v3 generation date. Brand formulations, product lines, and pricing change — verify current specifications at manufacturer sites before purchasing. The cross-brand comparisons are based on documented catalog data and known technical properties; individual batch variation means real-world performance may differ from stated tiers.*
