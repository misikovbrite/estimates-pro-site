#!/usr/bin/env python3
"""Generate new national calculators + city pages for high-volume keywords."""
import os, json

# ─── CITY DATA (reuse from previous script) ───────────────────────────────
CITIES = {
    "New York":       {"slug": "new-york",       "state": "New York",      "cost_mult": 1.35, "region": "Northeast"},
    "Los Angeles":    {"slug": "los-angeles",     "state": "California",    "cost_mult": 1.25, "region": "West"},
    "Chicago":        {"slug": "chicago",         "state": "Illinois",      "cost_mult": 1.10, "region": "Midwest"},
    "Houston":        {"slug": "houston",         "state": "Texas",         "cost_mult": 0.92, "region": "South"},
    "Phoenix":        {"slug": "phoenix",         "state": "Arizona",       "cost_mult": 0.95, "region": "South"},
    "Philadelphia":   {"slug": "philadelphia",    "state": "Pennsylvania",  "cost_mult": 1.12, "region": "Northeast"},
    "San Antonio":    {"slug": "san-antonio",     "state": "Texas",         "cost_mult": 0.88, "region": "South"},
    "San Diego":      {"slug": "san-diego",       "state": "California",    "cost_mult": 1.28, "region": "West"},
    "Dallas":         {"slug": "dallas",          "state": "Texas",         "cost_mult": 0.94, "region": "South"},
    "San Jose":       {"slug": "san-jose",        "state": "California",    "cost_mult": 1.40, "region": "West"},
    "Austin":         {"slug": "austin",          "state": "Texas",         "cost_mult": 0.97, "region": "South"},
    "Jacksonville":   {"slug": "jacksonville",    "state": "Florida",       "cost_mult": 0.90, "region": "South"},
    "Fort Worth":     {"slug": "fort-worth",      "state": "Texas",         "cost_mult": 0.93, "region": "South"},
    "Columbus":       {"slug": "columbus",        "state": "Ohio",          "cost_mult": 0.90, "region": "Midwest"},
    "Charlotte":      {"slug": "charlotte",       "state": "North Carolina","cost_mult": 0.93, "region": "South"},
    "Indianapolis":   {"slug": "indianapolis",    "state": "Indiana",       "cost_mult": 0.88, "region": "Midwest"},
    "San Francisco":  {"slug": "san-francisco",   "state": "California",    "cost_mult": 1.55, "region": "West"},
    "Seattle":        {"slug": "seattle",         "state": "Washington",    "cost_mult": 1.30, "region": "West"},
    "Denver":         {"slug": "denver",          "state": "Colorado",      "cost_mult": 1.05, "region": "Mountain"},
    "Nashville":      {"slug": "nashville",       "state": "Tennessee",     "cost_mult": 0.93, "region": "South"},
    "Oklahoma City":  {"slug": "oklahoma-city",   "state": "Oklahoma",      "cost_mult": 0.85, "region": "South"},
    "El Paso":        {"slug": "el-paso",         "state": "Texas",         "cost_mult": 0.82, "region": "South"},
    "Washington DC":  {"slug": "washington-dc",   "state": "District of Columbia","cost_mult": 1.30, "region": "Northeast"},
    "Las Vegas":      {"slug": "las-vegas",       "state": "Nevada",        "cost_mult": 1.00, "region": "West"},
    "Boston":         {"slug": "boston",          "state": "Massachusetts", "cost_mult": 1.35, "region": "Northeast"},
    "Portland":       {"slug": "portland",        "state": "Oregon",        "cost_mult": 1.15, "region": "West"},
    "Memphis":        {"slug": "memphis",         "state": "Tennessee",     "cost_mult": 0.83, "region": "South"},
    "Louisville":     {"slug": "louisville",      "state": "Kentucky",      "cost_mult": 0.87, "region": "South"},
    "Baltimore":      {"slug": "baltimore",       "state": "Maryland",      "cost_mult": 1.12, "region": "Northeast"},
    "Milwaukee":      {"slug": "milwaukee",       "state": "Wisconsin",     "cost_mult": 0.93, "region": "Midwest"},
    "Albuquerque":    {"slug": "albuquerque",     "state": "New Mexico",    "cost_mult": 0.88, "region": "Mountain"},
    "Tucson":         {"slug": "tucson",          "state": "Arizona",       "cost_mult": 0.87, "region": "South"},
    "Fresno":         {"slug": "fresno",          "state": "California",    "cost_mult": 0.97, "region": "West"},
    "Sacramento":     {"slug": "sacramento",      "state": "California",    "cost_mult": 1.10, "region": "West"},
    "Mesa":           {"slug": "mesa",            "state": "Arizona",       "cost_mult": 0.95, "region": "South"},
    "Atlanta":        {"slug": "atlanta",         "state": "Georgia",       "cost_mult": 0.96, "region": "South"},
    "Omaha":          {"slug": "omaha",           "state": "Nebraska",      "cost_mult": 0.87, "region": "Midwest"},
    "Colorado Springs":{"slug":"colorado-springs","state": "Colorado",      "cost_mult": 1.00, "region": "Mountain"},
    "Raleigh":        {"slug": "raleigh",         "state": "North Carolina","cost_mult": 0.95, "region": "South"},
    "Miami":          {"slug": "miami",           "state": "Florida",       "cost_mult": 1.08, "region": "South"},
    "Minneapolis":    {"slug": "minneapolis",     "state": "Minnesota",     "cost_mult": 1.05, "region": "Midwest"},
    "Tampa":          {"slug": "tampa",           "state": "Florida",       "cost_mult": 0.98, "region": "South"},
    "New Orleans":    {"slug": "new-orleans",     "state": "Louisiana",     "cost_mult": 0.90, "region": "South"},
    "Cleveland":      {"slug": "cleveland",       "state": "Ohio",          "cost_mult": 0.87, "region": "Midwest"},
    "Bakersfield":    {"slug": "bakersfield",     "state": "California",    "cost_mult": 0.93, "region": "West"},
    "Honolulu":       {"slug": "honolulu",        "state": "Hawaii",        "cost_mult": 1.65, "region": "West"},
    "Anaheim":        {"slug": "anaheim",         "state": "California",    "cost_mult": 1.25, "region": "West"},
    "Riverside":      {"slug": "riverside",       "state": "California",    "cost_mult": 1.10, "region": "West"},
    "Corpus Christi": {"slug": "corpus-christi",  "state": "Texas",         "cost_mult": 0.87, "region": "South"},
    "Cincinnati":     {"slug": "cincinnati",      "state": "Ohio",          "cost_mult": 0.90, "region": "Midwest"},
    "St. Louis":      {"slug": "st-louis",        "state": "Missouri",      "cost_mult": 0.90, "region": "Midwest"},
}

# ─── NEW PROJECT DATA ─────────────────────────────────────────────────────
PROJECTS = {
    "drywall-installation": {
        "name": "Drywall Installation",
        "slug": "drywall-installation",
        "national_kw": "drywall installation cost calculator",
        "national_vol": 33100,
        "title_tmpl":   "Drywall Installation Cost Calculator {city_suffix}(2026)",
        "desc_tmpl":    "Free drywall installation cost calculator{city_prep}. Estimate drywall costs by room size, thickness, and finish level — updated 2026 prices{city_in}.",
        "h1_tmpl":      "Drywall Installation Cost Calculator{city_h1}",
        "intro_tmpl":   "Drywall installation in{city_intro} typically costs {cost_vs_avg} the national average. Use the calculator below to estimate your project based on room dimensions, drywall type, and finish level.",
        "base_low": 1500,
        "base_mid": 3800,
        "base_high": 9000,
        "sqft_min": 200, "sqft_max": 3000, "sqft_default": 800,
        "items": [
            {"label": "Standard 1/2\" drywall (walls)", "base": 1.85, "unit": "per sqft", "checked": True},
            {"label": "5/8\" Type X fire-rated drywall", "base": 2.40, "unit": "per sqft", "checked": False},
            {"label": "Moisture-resistant (bathrooms)", "base": 2.60, "unit": "per sqft", "checked": False},
            {"label": "Ceiling drywall installation", "base": 2.20, "unit": "per sqft", "checked": True},
            {"label": "Taping & mudding (joints)", "base": 0.90, "unit": "per sqft", "checked": True},
            {"label": "Finishing (Level 4 smooth)", "base": 0.70, "unit": "per sqft", "checked": True},
            {"label": "Corner bead & trim", "base": 320, "unit": "flat", "checked": True},
            {"label": "Texture (knockdown/orange peel)", "base": 0.55, "unit": "per sqft", "checked": False},
            {"label": "Priming & painting prep", "base": 0.45, "unit": "per sqft", "checked": False},
            {"label": "Repair & patch existing drywall", "base": 280, "unit": "flat", "checked": False},
        ],
        "faq": [
            ("How much does drywall installation cost{city_faq}?",
             "Drywall installation{city_in} costs ${low}–${high} for a typical room. Most homeowners pay around ${mid} for a standard bedroom or living room. Full house drywall can range ${house_low}–${house_high}."),
            ("How much does drywall cost per square foot{city_faq}?",
             "Professional drywall installation{city_in} costs $2.50–$5.50 per square foot including materials and labor. Labor alone runs ${labor_low}–${labor_high}/hour for drywall finishers in {city_or_us}."),
            ("How long does drywall installation take{city_faq}?",
             "A standard bedroom takes 1–2 days for hanging and 2–3 days for taping/finishing. A full house drywall project typically takes 1–3 weeks depending on size and finish level."),
            ("What drywall finish level do I need?",
             "Level 4 (smooth finish ready for paint) is standard for most rooms. Level 5 adds a skim coat and is recommended for high-gloss or demanding lighting situations. Level 3 works under heavy texture."),
        ],
        "cost_table_rows": [
            ("Single room (200–400 sqft)", "${low_sm}", "${mid_sm}"),
            ("Master bedroom / living room (400–800 sqft)", "${low}", "${mid_low}"),
            ("Open-plan space (800–1,500 sqft)", "${mid_low}", "${mid}"),
            ("Full house drywall (1,500–3,000 sqft)", "${mid}", "${high}"),
        ],
    },

    "window-replacement": {
        "name": "Window Replacement",
        "slug": "window-replacement",
        "national_kw": "window replacement cost calculator",
        "national_vol": 27100,
        "title_tmpl":   "Window Replacement Cost Calculator {city_suffix}(2026)",
        "desc_tmpl":    "Free window replacement cost calculator{city_prep}. Estimate window replacement costs by window type, count, and frame material — updated 2026 prices{city_in}.",
        "h1_tmpl":      "Window Replacement Cost Calculator{city_h1}",
        "intro_tmpl":   "Window replacement costs{city_intro} run {cost_vs_avg} the national average. Climate, window type, and frame material all affect pricing. Use our calculator to estimate your project.",
        "base_low": 3500,
        "base_mid": 8500,
        "base_high": 20000,
        "sqft_min": 1, "sqft_max": 20, "sqft_default": 8,
        "sqft_label": "Number of windows",
        "items": [
            {"label": "Double-hung vinyl windows", "base": 650, "unit": "each", "checked": True},
            {"label": "Casement windows (crank-out)", "base": 900, "unit": "each", "checked": False},
            {"label": "Bay or bow window", "base": 2800, "unit": "each", "checked": False},
            {"label": "Sliding windows", "base": 700, "unit": "each", "checked": False},
            {"label": "Picture/fixed windows", "base": 550, "unit": "each", "checked": False},
            {"label": "Egress windows (basement)", "base": 2200, "unit": "each", "checked": False},
            {"label": "Low-E glass upgrade", "base": 120, "unit": "each", "checked": True},
            {"label": "Triple-pane glass upgrade", "base": 200, "unit": "each", "checked": False},
            {"label": "Frame removal & disposal", "base": 80, "unit": "each", "checked": True},
            {"label": "Interior trim & casing finish", "base": 150, "unit": "each", "checked": True},
        ],
        "faq": [
            ("How much does window replacement cost{city_faq}?",
             "Window replacement{city_in} costs ${low}–${high} for a typical home (6–15 windows). Per window, expect to pay ${per_low}–${per_high} installed, depending on window type and size."),
            ("Is it worth replacing all windows at once{city_faq}?",
             "Replacing all windows at once{city_in} typically saves 10–15% versus individual replacements. Many contractors in {city_or_us} offer volume discounts for 5+ window projects."),
            ("What type of window replacement lasts the longest?",
             "Fiberglass frames last 30–40+ years and resist warping in extreme temperatures. Vinyl is the most popular choice for value — 20–30 year lifespan at lower cost. Wood requires more maintenance but can last 30+ years with care."),
            ("How much energy savings from new windows{city_faq}?",
             "Energy-efficient windows can reduce heating/cooling costs by 12–24% in {city_or_us}. Low-E coating and double/triple pane glass are the biggest factors. Payback period is typically 8–15 years."),
        ],
        "cost_table_rows": [
            ("Single window (double-hung vinyl)", "${per_low}", "${per_high}"),
            ("Small home (6–8 windows)", "${low}", "${mid_low}"),
            ("Average home (8–12 windows)", "${mid_low}", "${mid}"),
            ("Large home (12–20 windows)", "${mid}", "${high}"),
        ],
    },

    "fence-installation": {
        "name": "Fence Installation",
        "slug": "fence-installation",
        "national_kw": "fence cost calculator",
        "national_vol": 9900,
        "title_tmpl":   "Fence Installation Cost Calculator {city_suffix}(2026)",
        "desc_tmpl":    "Free fence installation cost calculator{city_prep}. Estimate fence costs by linear footage, fence type, and material — 2026 prices{city_in}.",
        "h1_tmpl":      "Fence Installation Cost Calculator{city_h1}",
        "intro_tmpl":   "Fence installation{city_intro} costs {cost_vs_avg} the national average. Material choice, yard size, and terrain are the main cost drivers. Calculate your fence project below.",
        "base_low": 1800,
        "base_mid": 5500,
        "base_high": 14000,
        "sqft_min": 50, "sqft_max": 600, "sqft_default": 200,
        "sqft_label": "Linear feet of fencing",
        "items": [
            {"label": "Wood privacy fence (6ft)", "base": 22, "unit": "per ft", "checked": True},
            {"label": "Vinyl privacy fence (6ft)", "base": 32, "unit": "per ft", "checked": False},
            {"label": "Chain-link fence (4ft)", "base": 14, "unit": "per ft", "checked": False},
            {"label": "Aluminum/ornamental fence", "base": 38, "unit": "per ft", "checked": False},
            {"label": "Split-rail fence (2-rail)", "base": 16, "unit": "per ft", "checked": False},
            {"label": "Post holes & concrete footings", "base": 6.50, "unit": "per ft", "checked": True},
            {"label": "Gate (single 4ft walk gate)", "base": 350, "unit": "each", "checked": True},
            {"label": "Double drive gate (10–12ft)", "base": 800, "unit": "each", "checked": False},
            {"label": "Old fence removal & haul-away", "base": 5.50, "unit": "per ft", "checked": False},
            {"label": "Fence staining/sealing", "base": 3.50, "unit": "per ft", "checked": False},
        ],
        "faq": [
            ("How much does fence installation cost{city_faq}?",
             "Fence installation{city_in} costs ${low}–${high} for a typical residential yard. Most homeowners spend ${mid} for 150–200 linear feet of standard wood privacy fence."),
            ("What's the cheapest fence option{city_faq}?",
             "Chain-link is the most affordable fence type{city_in} at ${chain_low}–${chain_high} per linear foot installed. Split-rail wood is the next cheapest at ${rail_low}–${rail_high}/ft."),
            ("How long does fence installation take{city_faq}?",
             "Most residential fence projects{city_in} take 1–3 days. Larger projects (300+ ft) or installations requiring permits can take 3–5 days plus permit wait time."),
            ("Do I need a permit for a fence in {city_or_us}?",
             "Most cities including {city_or_us} require a permit for fences over 6ft, or near property lines. Budget 1–3 weeks for permit approval. Check with {city_or_us} building department before installation."),
        ],
        "cost_table_rows": [
            ("Chain-link fence (100–200 ft)", "${chain_tot_low}", "${chain_tot_high}"),
            ("Wood privacy fence (100–200 ft)", "${wood_low}", "${wood_high}"),
            ("Vinyl privacy fence (100–200 ft)", "${vinyl_low}", "${vinyl_high}"),
            ("Full yard perimeter (200–400 ft)", "${mid}", "${high}"),
        ],
    },

    "tile-installation": {
        "name": "Tile Installation",
        "slug": "tile-installation",
        "national_kw": "tile installation cost calculator",
        "national_vol": 9900,
        "title_tmpl":   "Tile Installation Cost Calculator {city_suffix}(2026)",
        "desc_tmpl":    "Free tile installation cost calculator{city_prep}. Estimate tile costs for floors, walls, showers, and backsplashes — updated 2026 prices{city_in}.",
        "h1_tmpl":      "Tile Installation Cost Calculator{city_h1}",
        "intro_tmpl":   "Tile installation{city_intro} costs {cost_vs_avg} the national average. Tile type, pattern complexity, and surface prep are the biggest cost drivers. Use the calculator for your estimate.",
        "base_low": 800,
        "base_mid": 3200,
        "base_high": 8500,
        "sqft_min": 20, "sqft_max": 800, "sqft_default": 150,
        "items": [
            {"label": "Ceramic floor tile (standard)", "base": 7.50, "unit": "per sqft", "checked": True},
            {"label": "Porcelain tile (floor)", "base": 10.50, "unit": "per sqft", "checked": False},
            {"label": "Natural stone (marble/travertine)", "base": 18.00, "unit": "per sqft", "checked": False},
            {"label": "Subway tile (wall/backsplash)", "base": 9.00, "unit": "per sqft", "checked": False},
            {"label": "Large format tile (24x24+)", "base": 14.00, "unit": "per sqft", "checked": False},
            {"label": "Mosaic tile / glass tile", "base": 16.00, "unit": "per sqft", "checked": False},
            {"label": "Mortar bed / Schluter system", "base": 3.50, "unit": "per sqft", "checked": True},
            {"label": "Grout & sealing", "base": 1.80, "unit": "per sqft", "checked": True},
            {"label": "Old tile removal & disposal", "base": 3.00, "unit": "per sqft", "checked": False},
            {"label": "Heated floor mat (electric)", "base": 12.00, "unit": "per sqft", "checked": False},
        ],
        "faq": [
            ("How much does tile installation cost{city_faq}?",
             "Tile installation{city_in} costs ${low}–${high} depending on tile type and area size. Basic ceramic tile starts at ${low} for a bathroom floor; natural stone or complex patterns cost ${high}+."),
            ("What's the tile installation cost per square foot{city_faq}?",
             "Tile installation{city_in} runs $7–$25 per square foot installed. Ceramic tile is cheapest ($7–$12/sqft), porcelain runs $9–$16/sqft, and natural stone or large-format tile costs $14–$25/sqft."),
            ("How long does tile installation take{city_faq}?",
             "A standard bathroom floor (50–80 sqft) takes 1–2 days. A full bathroom including walls takes 3–5 days. Large floor areas (200+ sqft) can take a full week."),
            ("Can I tile over existing tile{city_faq}?",
             "Tiling over existing tile is possible if the existing tile is firmly bonded, level, and the added height won't cause issues with transitions. However, most tile contractors{city_in} recommend removing old tile for best results."),
        ],
        "cost_table_rows": [
            ("Backsplash (20–40 sqft)", "${low_sm}", "${mid_sm}"),
            ("Bathroom floor (50–100 sqft)", "${low}", "${mid_low}"),
            ("Full bathroom (100–200 sqft)", "${mid_low}", "${mid}"),
            ("Kitchen + bath combo (200–400 sqft)", "${mid}", "${high}"),
        ],
    },

    "interior-painting": {
        "name": "Interior Painting",
        "slug": "interior-painting",
        "national_kw": "interior painting cost calculator",
        "national_vol": 4400,
        "title_tmpl":   "Interior Painting Cost Calculator {city_suffix}(2026)",
        "desc_tmpl":    "Free interior painting cost calculator{city_prep}. Estimate interior paint costs by room count, ceiling height, and paint quality — 2026 prices{city_in}.",
        "h1_tmpl":      "Interior Painting Cost Calculator{city_h1}",
        "intro_tmpl":   "Interior painting{city_intro} costs {cost_vs_avg} the national average. Room count, ceiling height, and wall condition are the main variables. Get your estimate below.",
        "base_low": 900,
        "base_mid": 3200,
        "base_high": 8000,
        "sqft_min": 200, "sqft_max": 3500, "sqft_default": 1000,
        "items": [
            {"label": "Walls — 1 coat (prep included)", "base": 1.80, "unit": "per sqft", "checked": True},
            {"label": "Walls — 2 coats (full coverage)", "base": 2.80, "unit": "per sqft", "checked": False},
            {"label": "Ceilings (standard height)", "base": 1.50, "unit": "per sqft", "checked": True},
            {"label": "Ceilings (vaulted/9ft+)", "base": 2.20, "unit": "per sqft", "checked": False},
            {"label": "Doors & door frames", "base": 140, "unit": "each", "checked": True},
            {"label": "Window trim & casings", "base": 90, "unit": "each", "checked": False},
            {"label": "Baseboards & crown molding", "base": 1.80, "unit": "per lf", "checked": False},
            {"label": "Accent wall / feature color", "base": 220, "unit": "each", "checked": False},
            {"label": "Drywall repair & patch before paint", "base": 380, "unit": "flat", "checked": False},
            {"label": "Primer coat (new drywall/dark colors)", "base": 0.85, "unit": "per sqft", "checked": False},
        ],
        "faq": [
            ("How much does interior painting cost{city_faq}?",
             "Interior painting{city_in} costs ${low}–${high} for a full home. Per room, expect ${room_low}–${room_high} for a standard bedroom. Larger open-plan spaces cost ${open_low}–${open_high}."),
            ("How much does a painter charge per hour{city_faq}?",
             "Professional painters{city_in} charge ${labor_low}–${labor_high}/hour. Most painting projects are quoted per room or per square foot rather than hourly. Always get a fixed quote for interior work."),
            ("How long does interior painting take{city_faq}?",
             "A single room takes 4–8 hours. A full 3-bedroom home typically takes 2–4 days for walls and ceilings. Add 1–2 extra days if trim, doors, and ceilings are included."),
            ("What paint finish should I use in each room?",
             "Flat/matte works for low-traffic areas (ceilings, master bedrooms). Eggshell is ideal for living rooms and dining rooms. Satin suits hallways and kids' rooms. Semi-gloss or gloss is best for kitchens, bathrooms, and trim."),
        ],
        "cost_table_rows": [
            ("Single room (walls only)", "${room_low}", "${room_high}"),
            ("Bedroom + bathroom (2 rooms)", "${two_low}", "${two_high}"),
            ("3-bedroom home (walls + ceilings)", "${low}", "${mid}"),
            ("Full home with trim & doors", "${mid}", "${high}"),
        ],
    },

    "siding-replacement": {
        "name": "Siding Replacement",
        "slug": "siding-replacement",
        "national_kw": "siding replacement cost calculator",
        "national_vol": 6600,
        "title_tmpl":   "Siding Replacement Cost Calculator {city_suffix}(2026)",
        "desc_tmpl":    "Free siding replacement cost calculator{city_prep}. Estimate siding costs by home size and material — vinyl, fiber cement, wood, and more. Updated 2026 prices{city_in}.",
        "h1_tmpl":      "Siding Replacement Cost Calculator{city_h1}",
        "intro_tmpl":   "Siding replacement{city_intro} costs {cost_vs_avg} the national average. Material choice, home size, and old siding removal are the main cost factors in the {region} region.",
        "base_low": 6500,
        "base_mid": 14000,
        "base_high": 32000,
        "sqft_min": 500, "sqft_max": 4000, "sqft_default": 1500,
        "items": [
            {"label": "Vinyl siding (standard)", "base": 5.50, "unit": "per sqft", "checked": True},
            {"label": "Vinyl siding (insulated)", "base": 7.50, "unit": "per sqft", "checked": False},
            {"label": "Fiber cement (Hardie board)", "base": 9.50, "unit": "per sqft", "checked": False},
            {"label": "Engineered wood siding", "base": 8.00, "unit": "per sqft", "checked": False},
            {"label": "Cedar wood siding", "base": 12.00, "unit": "per sqft", "checked": False},
            {"label": "Metal/steel siding", "base": 10.50, "unit": "per sqft", "checked": False},
            {"label": "Old siding removal & disposal", "base": 1.50, "unit": "per sqft", "checked": True},
            {"label": "House wrap / moisture barrier", "base": 0.90, "unit": "per sqft", "checked": True},
            {"label": "Trim boards & corner posts", "base": 1.20, "unit": "per sqft", "checked": True},
            {"label": "Soffit & fascia replacement", "base": 3200, "unit": "flat", "checked": False},
        ],
        "faq": [
            ("How much does siding replacement cost{city_faq}?",
             "Siding replacement{city_in} costs ${low}–${high} for a typical home. Vinyl siding is the most affordable option at ${vinyl_low}–${vinyl_high}; fiber cement runs ${fc_low}–${fc_high}."),
            ("How long does new siding last{city_faq}?",
             "Vinyl siding lasts 20–40 years with minimal maintenance. Fiber cement (Hardie board) lasts 30–50 years. Cedar wood siding lasts 20–30 years with regular painting/sealing. Metal siding can last 40–60 years."),
            ("Should I repair or replace siding{city_faq}?",
             "If damage covers less than 20% of the surface and the underlying structure is sound, repair (${repair_low}–${repair_high}) is usually cost-effective. Widespread rot, warping, or high energy bills are signs full replacement is better value."),
            ("What siding is best for {region} climate?",
             "In the {region} region, fiber cement is highly recommended for its resistance to moisture and temperature extremes. Insulated vinyl is a cost-effective alternative with good thermal performance. Avoid untreated wood siding in high-humidity areas."),
        ],
        "cost_table_rows": [
            ("Vinyl siding — small home (1,000 sqft)", "${vinyl_low}", "${vinyl_high}"),
            ("Vinyl siding — average home (1,500 sqft)", "${low}", "${mid_low}"),
            ("Fiber cement — average home (1,500 sqft)", "${mid_low}", "${mid}"),
            ("Large home or premium material (2,500 sqft)", "${mid}", "${high}"),
        ],
    },
}

# ─── STAR SVG (reusable) ──────────────────────────────────────────────────
STAR_SVG = '<svg viewBox="0 0 24 24" fill="white" width="17" height="17"><path d="M12 2l2.9 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l7.1-1.01L12 2z"/></svg>'
FIVE_STARS = ''.join(f'<div class="t-star">{STAR_SVG}</div>' for _ in range(5))

# ─── HELPERS ─────────────────────────────────────────────────────────────────
def fmt(n): return f"{round(n):,}"

def cost_vs_avg(m):
    if m >= 1.20: return "significantly higher than"
    if m >= 1.08: return "higher than"
    if m >= 0.97: return "close to"
    if m >= 0.88: return "slightly below"
    return "notably below"

def labor_range(m):
    return round(45 * m), round(90 * m)

def build_slugified(city_or_none, proj):
    if city_or_none:
        return f"{proj['slug']}-cost-{CITIES[city_or_none]['slug']}"
    return f"{proj['slug']}-cost-calculator"

def make_tokens(city_name, city_data, proj):
    m = city_data["cost_mult"] if city_data else 1.0
    state = city_data["state"] if city_data else "US"
    region = city_data["region"] if city_data else "national"
    low  = round(proj["base_low"]  * m / 200) * 200
    mid  = round(proj["base_mid"]  * m / 200) * 200
    high = round(proj["base_high"] * m / 200) * 200
    low_sm   = round(low  * 0.35 / 100) * 100
    mid_sm   = round(low  * 0.65 / 100) * 100
    low_high = round((low + mid) / 2 / 200) * 200
    mid_low  = round((low_high + mid) / 2 / 200) * 200
    lab_low, lab_high = labor_range(m)
    per_low = round(proj["base_low"]  * m / (proj.get("sqft_default", 8)) / 50) * 50
    per_high = round(proj["base_mid"] * m / (proj.get("sqft_default", 8)) / 50) * 50
    house_low = round(proj["base_mid"] * m * 2.2 / 500) * 500
    house_high = round(proj["base_high"] * m * 2 / 500) * 500

    # fence-specific
    chain_low = round(14 * m); chain_high = round(20 * m)
    rail_low  = round(16 * m); rail_high  = round(23 * m)
    chain_tot_low = fmt(round(14 * m * 150 / 100) * 100)
    chain_tot_high = fmt(round(20 * m * 200 / 100) * 100)
    wood_low = fmt(round(22 * m * 150 / 100) * 100)
    wood_high = fmt(round(30 * m * 200 / 100) * 100)
    vinyl_low = fmt(round(32 * m * 150 / 100) * 100)
    vinyl_high = fmt(round(42 * m * 200 / 100) * 100)

    # siding-specific
    vinyl_s_low = fmt(round(proj["base_low"] * m * 0.7 / 200) * 200)
    vinyl_s_high = fmt(round(proj["base_mid"] * m * 0.8 / 200) * 200)
    fc_low = fmt(round(proj["base_mid"] * m * 0.9 / 200) * 200)
    fc_high = fmt(round(proj["base_high"] * m * 0.8 / 200) * 200)
    repair_low = fmt(round(400 * m / 100) * 100)
    repair_high = fmt(round(1500 * m / 100) * 100)

    # painting-specific
    room_low = fmt(round(300 * m / 50) * 50)
    room_high = fmt(round(700 * m / 50) * 50)
    two_low  = fmt(round(600 * m / 50) * 50)
    two_high = fmt(round(1400 * m / 50) * 50)
    open_low = fmt(round(600 * m / 50) * 50)
    open_high = fmt(round(1200 * m / 50) * 50)

    city_or_us = city_name if city_name else "your area"
    city_in    = f" in {city_name}" if city_name else ""
    city_prep  = f" for {city_name}" if city_name else ""
    city_h1    = f" — {city_name}" if city_name else ""
    city_faq   = f" in {city_name}?" if city_name else "?"
    city_intro = f" in {city_name}, {state}" if city_name else " across the US"
    city_suffix = f"in {city_name} " if city_name else ""
    city_lc    = city_name.lower() if city_name else ""

    return dict(
        city=city_name or "", city_lower=city_lc, state=state, region=region,
        cost_vs_avg=cost_vs_avg(m),
        low=fmt(low), mid=fmt(mid), high=fmt(high),
        low_sm=fmt(low_sm), mid_sm=fmt(mid_sm),
        low_high=fmt(low_high), mid_low=fmt(mid_low),
        labor_low=lab_low, labor_high=lab_high,
        per_low=fmt(per_low), per_high=fmt(per_high),
        house_low=fmt(house_low), house_high=fmt(house_high),
        chain_low=chain_low, chain_high=chain_high,
        rail_low=rail_low, rail_high=rail_high,
        chain_tot_low=chain_tot_low, chain_tot_high=chain_tot_high,
        wood_low=wood_low, wood_high=wood_high,
        vinyl_low=vinyl_low, vinyl_high=vinyl_high,
        vinyl_s_low=vinyl_s_low, vinyl_s_high=vinyl_s_high,
        fc_low=fc_low, fc_high=fc_high,
        repair_low=repair_low, repair_high=repair_high,
        room_low=room_low, room_high=room_high,
        two_low=two_low, two_high=two_high,
        open_low=open_low, open_high=open_high,
        city_or_us=city_or_us, city_in=city_in, city_prep=city_prep,
        city_h1=city_h1, city_faq=city_faq, city_intro=city_intro,
        city_suffix=city_suffix, city_lc=city_lc,
    )

def build_items_html(proj, city_data):
    m = city_data["cost_mult"] if city_data else 1.0
    rows = []
    items_js = []
    for i, item in enumerate(proj["items"]):
        checked = "checked" if item["checked"] else ""
        unit = item.get("unit", "")
        base = item["base"]
        if unit == "per sqft" or unit == "per ft" or unit == "per lf":
            adj = round(base * m * 100) / 100
            display = f"${adj:.2f}/{unit.split(' ')[-1]}"
        elif unit == "each":
            adj = round(base * m / 50) * 50
            display = f"${fmt(adj)}/ea"
        else:
            adj = round(base * m / 50) * 50
            display = f"${fmt(adj)}"
        rows.append(f'          <label class="item-row"><input type="checkbox" id="cb_{i}" {checked} onchange="update()"><span class="item-label">{item["label"]}</span><span class="item-cost">{display}</span></label>')
        items_js.append({"id": i, "base": round(adj * 100) / 100, "is_rate": unit not in ("each", "flat", "")})
    return "\n".join(rows), items_js

def build_faq_html(proj, tok):
    html = ""
    for q_tmpl, a_tmpl in proj["faq"]:
        q = q_tmpl.format(**tok).rstrip("?") + "?"
        a = a_tmpl.format(**tok)
        html += f'''      <div class="faq-item">
        <div class="faq-q">{q} <svg class="faq-chevron" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg></div>
        <div class="faq-a">{a}</div>
      </div>\n'''
    return html

def generate_page(city_name, city_data, proj_key, proj):
    tok = make_tokens(city_name, city_data, proj)
    m = city_data["cost_mult"] if city_data else 1.0
    is_city = bool(city_name)
    canon_slug = build_slugified(city_name, proj)
    canon_url = f"https://estimates-pro.com/tools/{canon_slug}/"

    page_title = proj["title_tmpl"].format(**tok)
    page_desc  = proj["desc_tmpl"].format(**tok)
    h1 = proj["h1_tmpl"].format(**tok)
    intro = proj["intro_tmpl"].format(**tok)
    items_html, items_js = build_items_html(proj, city_data)
    faq_html = build_faq_html(proj, tok)
    cost_table = "\n".join(
        f'          <tr><td>{row[0].format(**tok)}</td><td>{row[1].format(**tok)}</td><td>{row[2].format(**tok)}</td></tr>'
        for row in proj["cost_table_rows"]
    )
    sqft_label = proj.get("sqft_label", "Square footage")

    page = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{page_title}</title>
<meta name="description" content="{page_desc}">
<meta name="keywords" content="{proj['national_kw']}{', ' + tok['city_lower'] if is_city else ''}, {proj['name'].lower()} cost{tok['city_in']}, how much does {proj['name'].lower()} cost{tok['city_in']}">
<link rel="canonical" href="{canon_url}">
<link rel="icon" type="image/x-icon" href="../../favicon.ico">
<link rel="apple-touch-icon" href="../../images/apple-touch-icon.png">
<meta property="og:title" content="{page_title}">
<meta property="og:description" content="{page_desc}">
<meta property="og:url" content="{canon_url}">
<meta property="og:type" content="website">
<meta property="og:image" content="https://estimates-pro.com/images/screen1.png">
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "WebApplication",
  "name": "{h1}",
  "description": "{page_desc}",
  "url": "{canon_url}",
  "applicationCategory": "UtilitiesApplication",
  "operatingSystem": "Web",
  "offers": {{ "@type": "Offer", "price": "0", "priceCurrency": "USD" }}
}}
</script>
<style>
  *,*::before,*::after{{margin:0;padding:0;box-sizing:border-box}}
  :root{{--blue:#1565C0;--blue-dark:#0D47A1;--blue-light:#E3F2FD;--text:#1C1C1E;--text-sec:#6E6E73;--border:#E5E7EB;--bg:#F9FAFB;--white:#fff}}
  body{{font-family:-apple-system,BlinkMacSystemFont,'Inter',sans-serif;background:var(--bg);color:var(--text)}}
  nav{{background:var(--white);border-bottom:1px solid var(--border);padding:0 32px;height:60px;display:flex;align-items:center;justify-content:space-between;position:sticky;top:0;z-index:100}}
  .nav-logo{{display:flex;align-items:center;gap:8px;font-weight:800;font-size:17px;text-decoration:none;color:var(--text)}}
  .nav-logo img{{width:28px;height:28px;border-radius:6px}}
  .nav-logo span{{color:var(--blue)}}
  .nav-cta{{background:var(--blue);color:#fff;padding:8px 18px;border-radius:7px;font-size:13px;font-weight:700;text-decoration:none}}
  .page-hero{{background:linear-gradient(135deg,var(--blue-dark) 0%,var(--blue) 100%);padding:48px 32px 40px;text-align:center;color:#fff}}
  .breadcrumb{{font-size:12px;color:rgba(255,255,255,0.6);margin-bottom:12px}}
  .breadcrumb a{{color:rgba(255,255,255,0.7);text-decoration:none}}
  .page-hero h1{{font-size:clamp(22px,4vw,40px);font-weight:900;letter-spacing:-1px;margin-bottom:10px}}
  .page-hero p{{font-size:16px;color:rgba(255,255,255,0.75);max-width:580px;margin:0 auto}}
  .cost-badges{{display:flex;gap:12px;justify-content:center;margin-top:20px;flex-wrap:wrap}}
  .cost-badge{{background:rgba(255,255,255,0.15);border-radius:8px;padding:8px 16px;font-size:14px;font-weight:700}}
  .cost-badge span{{display:block;font-size:11px;font-weight:400;opacity:.75;margin-bottom:2px}}
  .main{{max-width:1060px;margin:0 auto;padding:32px 20px 80px;display:grid;grid-template-columns:1fr 340px;gap:24px;align-items:start}}
  @media(max-width:760px){{.main{{grid-template-columns:1fr}}.sticky-result{{position:static!important}}}}
  .calc-card{{background:var(--white);border:1px solid var(--border);border-radius:16px;overflow:hidden}}
  .calc-section{{padding:24px;border-bottom:1px solid var(--border)}}
  .calc-section:last-child{{border-bottom:none}}
  .calc-section h3{{font-size:14px;font-weight:700;text-transform:uppercase;letter-spacing:.8px;color:var(--text-sec);margin-bottom:16px}}
  .slider-row{{margin-bottom:20px}}
  .slider-label{{display:flex;justify-content:space-between;align-items:center;margin-bottom:8px}}
  .slider-label span{{font-size:14px;font-weight:600}}
  .slider-val{{font-size:15px;font-weight:800;color:var(--blue)}}
  input[type=range]{{width:100%;accent-color:var(--blue);height:6px;-webkit-appearance:none;appearance:none;background:#dbeafe;border-radius:3px;outline:none}}
  input[type=range]::-webkit-slider-thumb{{-webkit-appearance:none;width:18px;height:18px;border-radius:50%;background:var(--blue);cursor:pointer;border:2px solid #fff;box-shadow:0 1px 4px rgba(0,0,0,.2)}}
  .quality-row{{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-bottom:4px}}
  .quality-btn{{padding:10px 6px;border-radius:8px;border:1.5px solid var(--border);font-size:13px;font-weight:600;cursor:pointer;background:var(--white);color:var(--text);transition:all .15s;text-align:center}}
  .quality-btn.active{{background:var(--blue-light);border-color:var(--blue);color:var(--blue)}}
  .quality-desc{{font-size:12px;color:var(--text-sec);text-align:center;margin-top:4px}}
  .item-list{{display:flex;flex-direction:column;gap:10px}}
  .item-row{{display:flex;align-items:center;gap:10px;cursor:pointer}}
  .item-row input[type=checkbox]{{width:16px;height:16px;accent-color:var(--blue);flex-shrink:0;cursor:pointer}}
  .item-label{{flex:1;font-size:14px}}
  .item-cost{{font-size:14px;font-weight:700;color:var(--text-sec)}}
  .sticky-result{{position:sticky;top:72px}}
  .result-card{{background:var(--white);border:1px solid var(--border);border-radius:16px;overflow:hidden}}
  .result-header{{background:linear-gradient(135deg,var(--blue-dark),var(--blue));padding:20px 24px}}
  .result-header p{{color:rgba(255,255,255,.7);font-size:12px;margin-bottom:4px}}
  .result-total{{font-size:36px;font-weight:900;color:#fff;letter-spacing:-1px}}
  .result-range{{font-size:13px;color:rgba(255,255,255,.65);margin-top:4px}}
  .result-body{{padding:20px 24px}}
  .breakdown-row{{display:flex;justify-content:space-between;align-items:center;padding:8px 0;border-bottom:1px solid var(--border);font-size:14px}}
  .breakdown-row:last-child{{border-bottom:none}}
  .breakdown-label{{color:var(--text-sec)}}
  .breakdown-val{{font-weight:700}}
  .app-promo{{margin-top:16px;background:var(--blue-light);border-radius:10px;padding:16px}}
  .app-promo p{{font-size:13px;font-weight:700;color:var(--blue-dark);margin-bottom:10px}}
  .store-btns{{display:flex;flex-direction:column;gap:8px}}
  .store-btn{{display:flex;align-items:center;gap:8px;background:var(--blue-dark);color:#fff;text-decoration:none;border-radius:8px;padding:8px 14px;font-size:12px}}
  .store-btn svg{{width:20px;height:20px;flex-shrink:0}}
  .store-btn-text{{line-height:1.2}}
  .store-btn-text strong{{font-size:13px;font-weight:800;display:block}}
  .info-section{{margin-top:48px}}
  .info-section h2{{font-size:22px;font-weight:800;margin-bottom:20px}}
  .info-section h3{{font-size:17px;font-weight:700;margin:28px 0 10px}}
  .info-section p{{font-size:15px;line-height:1.65;color:#374151;margin-bottom:12px}}
  .cost-table{{width:100%;border-collapse:collapse;margin:16px 0;font-size:14px}}
  .cost-table th{{background:var(--blue-dark);color:#fff;padding:10px 14px;text-align:left;font-size:12px;text-transform:uppercase;letter-spacing:.5px}}
  .cost-table td{{padding:10px 14px;border-bottom:1px solid var(--border)}}
  .cost-table tr:nth-child(even) td{{background:var(--blue-light)}}
  .cost-table tr:last-child td{{border-bottom:none}}
  .faq-item{{border:1px solid var(--border);border-radius:10px;margin-bottom:10px;overflow:hidden}}
  .faq-q{{padding:14px 18px;font-weight:700;font-size:15px;cursor:pointer;display:flex;justify-content:space-between;align-items:center;background:var(--white)}}
  .faq-q:hover{{background:var(--bg)}}
  .faq-a{{padding:0 18px 14px;font-size:14px;line-height:1.65;color:#374151;display:none}}
  .faq-item.open .faq-a{{display:block}}
  .faq-item.open .faq-chevron{{transform:rotate(180deg)}}
  .faq-chevron{{transition:transform .2s;color:var(--text-sec)}}
  footer{{background:var(--blue-dark);color:rgba(255,255,255,.7);padding:32px;text-align:center;font-size:13px}}
  footer a{{color:rgba(255,255,255,.6);text-decoration:none;margin:0 8px}}
  footer a:hover{{color:#fff}}
  .footer-logo{{font-size:18px;font-weight:800;color:#fff;margin-bottom:8px}}
  .cta-section{{background:linear-gradient(135deg,var(--blue-dark),var(--blue));border-radius:14px;padding:32px 28px;text-align:center;margin-top:40px;color:#fff}}
  .cta-section h2{{font-size:22px;font-weight:800;margin-bottom:8px}}
  .cta-section p{{font-size:15px;opacity:.8;margin-bottom:20px}}
  .cta-btns{{display:flex;gap:12px;justify-content:center;flex-wrap:wrap}}
  .cta-btn{{background:rgba(255,255,255,.15);border:1.5px solid rgba(255,255,255,.4);color:#fff;padding:10px 22px;border-radius:9px;font-weight:700;font-size:14px;text-decoration:none}}
  .cta-btn.primary{{background:#fff;color:var(--blue-dark)}}
</style>
</head>
<body>
<nav>
  <a class="nav-logo" href="/"><img src="../../images/icon.png" alt="Cost Estimator">Cost<span>Estimator</span></a>
  <a class="nav-cta" href="https://apps.apple.com/us/app/cost-estimator-construction/id6758105341">Download Free</a>
</nav>

<div class="page-hero">
  <div class="breadcrumb"><a href="/">Home</a> › <a href="/tools/">Tools</a> › {h1}</div>
  <h1>{h1}</h1>
  <p>{intro}</p>
  <div class="cost-badges">
    <div class="cost-badge"><span>Low estimate</span>${tok['low']}</div>
    <div class="cost-badge"><span>Average</span>${tok['mid']}</div>
    <div class="cost-badge"><span>High estimate</span>${tok['high']}</div>
  </div>
</div>

<div class="main">
  <div>
    <div class="calc-card">
      <div class="calc-section">
        <h3>{sqft_label}</h3>
        <div class="slider-row">
          <div class="slider-label">
            <span>{sqft_label}</span>
            <span class="slider-val" id="sqftVal">{proj['sqft_default']}</span>
          </div>
          <input type="range" id="sqftSlider" min="{proj['sqft_min']}" max="{proj['sqft_max']}" value="{proj['sqft_default']}" oninput="update()">
        </div>
      </div>
      <div class="calc-section">
        <h3>Quality Tier</h3>
        <div class="quality-row">
          <button class="quality-btn" data-q="0.72" onclick="setQ(this)">Budget</button>
          <button class="quality-btn active" data-q="1.0" onclick="setQ(this)">Mid-Range</button>
          <button class="quality-btn" data-q="1.65" onclick="setQ(this)">Premium</button>
        </div>
        <p class="quality-desc" id="qualityDesc">Standard materials, solid craftsmanship</p>
      </div>
      <div class="calc-section">
        <h3>Scope of Work</h3>
        <div class="item-list">
{items_html}
        </div>
      </div>
      <div class="calc-section">
        <h3>Labor</h3>
        <div class="slider-row">
          <div class="slider-label">
            <span>Labor portion of total cost</span>
            <span class="slider-val" id="laborVal">40%</span>
          </div>
          <input type="range" id="laborSlider" min="25" max="60" value="40" oninput="update()">
        </div>
      </div>
    </div>

    <div class="info-section">
      <h2>{proj['name']} Cost{tok['city_in']}: 2026 Guide</h2>
      <p>Use the calculator above to get a quick estimate. The guide below explains what drives {proj['name'].lower()} costs{tok['city_in']} and what to expect from contractors in {tok['city_or_us']}.</p>

      <h3>Typical {proj['name']} Costs{tok['city_in']}</h3>
      <table class="cost-table">
        <thead><tr><th>Project Scope</th><th>Low</th><th>High</th></tr></thead>
        <tbody>
{cost_table}
        </tbody>
      </table>

      <h3>What Affects {proj['name']} Costs in {tok['city_or_us']}?</h3>
      <p><strong>Labor rates:</strong> Contractors in {tok['city_or_us']} charge ${tok['labor_low']}–${tok['labor_high']}/hour for {proj['name'].lower()} work — {cost_vs_avg(m)} the national average.</p>
      <p><strong>Material costs:</strong> Material prices in the {tok['region']} region are {cost_vs_avg(m)} national average due to local supply, transportation, and demand.</p>
      <p><strong>Project complexity:</strong> Non-standard layouts, difficult access, old material removal, and permitting all add to the total cost.</p>

      <h3>Frequently Asked Questions</h3>
{faq_html}
      <div class="cta-section">
        <h2>Create Pro Estimates in 60 Seconds</h2>
        <p>Use Cost Estimator app to generate detailed {proj['name'].lower()} estimates — share as PDF directly with clients.</p>
        <div class="cta-btns">
          <a class="cta-btn primary" href="https://apps.apple.com/us/app/cost-estimator-construction/id6758105341">App Store — Free</a>
          <a class="cta-btn" href="https://play.google.com/store/apps/details?id=com.britetodo.costestimator">Google Play — Free</a>
        </div>
      </div>
    </div>
  </div>

  <div class="sticky-result">
    <div class="result-card">
      <div class="result-header">
        <p>Estimated cost{tok['city_in']}</p>
        <div class="result-total" id="totalDisplay">$0</div>
        <div class="result-range" id="rangeDisplay">Range: $0 – $0</div>
      </div>
      <div class="result-body">
        <div class="breakdown-row"><span class="breakdown-label">Materials</span><span class="breakdown-val" id="matDisplay">$0</span></div>
        <div class="breakdown-row"><span class="breakdown-label">Labor</span><span class="breakdown-val" id="laborDisplay">$0</span></div>
        {'<div class="breakdown-row"><span class="breakdown-label">City multiplier</span><span class="breakdown-val">' + f'{m:.2f}x</span></div>' if is_city else ''}
        <div class="app-promo">
          <p>Want a full itemized estimate? Use the free app:</p>
          <div class="store-btns">
            <a href="https://apps.apple.com/us/app/cost-estimator-construction/id6758105341" class="store-btn">
              <svg viewBox="0 0 24 24" fill="currentColor"><path d="M18.71 19.5c-.83 1.24-1.71 2.45-3.05 2.47-1.34.03-1.77-.79-3.29-.79-1.53 0-2 .77-3.27.82-1.31.05-2.3-1.32-3.14-2.53C4.25 17 2.94 12.45 4.7 9.39c.87-1.52 2.43-2.48 4.12-2.51 1.28-.02 2.5.87 3.29.87.78 0 2.26-1.07 3.8-.91.65.03 2.47.26 3.64 1.98-.09.06-2.17 1.28-2.15 3.81.03 3.02 2.65 4.03 2.68 4.04-.03.07-.42 1.44-1.38 2.83M13 3.5c.73-.83 1.94-1.46 2.94-1.5.13 1.17-.34 2.35-1.04 3.19-.69.85-1.83 1.51-2.95 1.42-.15-1.15.41-2.35 1.05-3.11z"/></svg>
              <span class="store-btn-text"><strong>App Store</strong>iOS — Free</span>
            </a>
            <a href="https://play.google.com/store/apps/details?id=com.britetodo.costestimator" class="store-btn">
              <svg viewBox="0 0 24 24" fill="currentColor"><path d="M3.18 23.76c.37.21.83.19 1.25-.05l13.14-7.56L14.12 12l-10.94 11.76zM.69 1.56C.26 1.87 0 2.38 0 3.02v17.96c0 .64.26 1.15.69 1.46L.82 22.5 12.69 12 .82 1.5.69 1.56zM20.81 9.59L17.96 8l-4.16 4 4.16 4 2.88-1.62c.82-.46.82-1.87-.03-2.79zM4.43.29L17.57 7.85 14.12 11 3.18.24c.42-.24.88-.22 1.25.05z"/></svg>
              <span class="store-btn-text"><strong>Google Play</strong>Android — Free</span>
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

<footer>
  <div class="footer-logo">CostEstimator</div>
  <p style="margin-bottom:12px">Professional construction estimating app for contractors</p>
  <div>
    <a href="/">Home</a><a href="/tools/">More Calculators</a>
    <a href="https://apps.apple.com/us/app/cost-estimator-construction/id6758105341">App Store</a>
    <a href="https://play.google.com/store/apps/details?id=com.britetodo.costestimator">Google Play</a>
  </div>
  <p style="margin-top:12px">© 2026 Brite Technologies LLC · hello@britetodo.com</p>
</footer>

<script>
const ITEMS = {json.dumps(items_js)};
const CITY_MULT = {m};
const SQFT_BASE = {proj['sqft_default']};
let qualityMult = 1.0;

function setQ(btn) {{
  document.querySelectorAll('.quality-btn').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  qualityMult = parseFloat(btn.dataset.q);
  const descs = ['Budget materials, basic finishes','Standard materials, solid craftsmanship','Designer materials, premium finishes'];
  document.getElementById('qualityDesc').textContent = descs[['0.72','1.0','1.65'].indexOf(btn.dataset.q)] || descs[1];
  update();
}}
function fmt(n) {{ return '$' + Math.round(n).toLocaleString('en-US'); }}
function update() {{
  const sqft = parseInt(document.getElementById('sqftSlider').value);
  const laborPct = parseInt(document.getElementById('laborSlider').value) / 100;
  document.getElementById('sqftVal').textContent = sqft;
  document.getElementById('laborVal').textContent = (laborPct*100).toFixed(0) + '%';
  const sqftMult = sqft / SQFT_BASE;
  let base = 0;
  ITEMS.forEach(item => {{
    const cb = document.getElementById('cb_' + item.id);
    if (cb && cb.checked) {{
      base += item.is_rate ? item.base * sqft : item.base;
    }}
  }});
  const subtotal = base * qualityMult * CITY_MULT;
  const labor = subtotal * laborPct;
  const materials = subtotal - labor;
  document.getElementById('totalDisplay').textContent = fmt(subtotal);
  document.getElementById('rangeDisplay').textContent = 'Range: ' + fmt(subtotal*0.78) + ' – ' + fmt(subtotal*1.28);
  document.getElementById('matDisplay').textContent = fmt(materials);
  document.getElementById('laborDisplay').textContent = fmt(labor);
}}
document.querySelectorAll('.faq-q').forEach(q => {{
  q.addEventListener('click', () => q.closest('.faq-item').classList.toggle('open'));
}});
update();
</script>
</body>
</html>'''
    return page


# ─── MAIN ────────────────────────────────────────────────────────────────────
def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    count = 0
    new_dirs = []

    for proj_key, proj in PROJECTS.items():
        # 1. National calculator page (no city)
        folder = os.path.join(base_dir, f"{proj['slug']}-cost-calculator")
        os.makedirs(folder, exist_ok=True)
        html = generate_page(None, {"cost_mult": 1.0, "state": "US", "region": "national", "slug": ""}, proj_key, proj)
        with open(os.path.join(folder, "index.html"), "w", encoding="utf-8") as f:
            f.write(html)
        count += 1
        new_dirs.append(f"{proj['slug']}-cost-calculator")

        # 2. City pages
        for city_name, city_data in CITIES.items():
            slug = build_slugified(city_name, proj)
            folder = os.path.join(base_dir, slug)
            os.makedirs(folder, exist_ok=True)
            html = generate_page(city_name, city_data, proj_key, proj)
            with open(os.path.join(folder, "index.html"), "w", encoding="utf-8") as f:
                f.write(html)
            count += 1
            new_dirs.append(slug)

        if count % 50 == 0:
            print(f"  {count} pages...")

    print(f"\nDone! {count} pages generated.")
    print(f"New dirs: {len(new_dirs)}")
    return new_dirs

if __name__ == "__main__":
    main()
