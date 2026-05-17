#!/usr/bin/env python3
"""Generate 8 new project type pages × all cities (batch 1+2+3) — batch 4."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import generate_new_projects2 as proj2
import generate_batch3 as b3

# ─── ALL CITIES: merge original 237 + batch3 252 ──────────────────────────────
ALL_CITIES = {}
ALL_CITIES.update(proj2.ALL_CITIES)
ALL_CITIES.update(b3.NEW_CITIES)

# ─── 8 NEW PROJECT TYPES ──────────────────────────────────────────────────────
PROJECTS = {
    "solar-panel-installation": {
        "name": "Solar Panel Installation",
        "slug": "solar-panel-installation",
        "national_kw": "solar panel installation cost calculator",
        "national_vol": 90500,
        "title_tmpl":   "Solar Panel Installation Cost Calculator {city_suffix}(2026)",
        "desc_tmpl":    "Free solar panel installation cost calculator{city_prep}. Estimate total system cost, payback period, and savings by home size — updated 2026 equipment & labor prices{city_in}.",
        "h1_tmpl":      "Solar Panel Installation Cost Calculator{city_h1}",
        "intro_tmpl":   "Solar panel installation{city_intro} costs {cost_vs_avg} the national average. System size (kW), panel brand, and roof type are the biggest cost drivers. Use the calculator to estimate your system.",
        "base_low":  12000,
        "base_mid":  24000,
        "base_high": 45000,
        "sqft_min": 1000, "sqft_max": 5000, "sqft_default": 2000,
        "sqft_label": "Home square footage",
        "items": [
            {"label": "Solar panels (per kW, 8 kW avg)", "base": 2800, "unit": "flat", "checked": True},
            {"label": "String inverter", "base": 1400, "unit": "flat", "checked": True},
            {"label": "Microinverters (per panel)", "base": 200, "unit": "each", "checked": False},
            {"label": "Installation labor", "base": 0.85, "unit": "per sqft", "checked": True},
            {"label": "Roof mounting hardware & racking", "base": 1100, "unit": "flat", "checked": True},
            {"label": "Main panel upgrade (if needed)", "base": 2200, "unit": "flat", "checked": False},
            {"label": "Battery storage (Tesla Powerwall)", "base": 12000, "unit": "flat", "checked": False},
            {"label": "Permit & utility interconnection", "base": 800, "unit": "flat", "checked": True},
            {"label": "System monitoring (annual)", "base": 150, "unit": "flat", "checked": True},
        ],
        "faq": [
            ("How much does solar panel installation cost{city_faq}",
             "Solar panel installation{city_in} typically costs ${low}–${high} before incentives. After the 30% federal tax credit, most homeowners pay ${low}–${mid}. Average payback period is 6–10 years, then 15+ years of free electricity."),
            ("How many solar panels do I need{city_faq}",
             "A typical 2,000 sqft home{city_in} uses about 10,000 kWh/year and needs an 8–10 kW system (24–30 panels). Your actual usage and local sun hours determine the right size. A solar installer will provide a free site assessment."),
            ("What incentives are available for solar{city_faq}",
             "The federal Investment Tax Credit (ITC) gives you 30% back on your total cost. {state} may offer additional rebates or net metering programs. Many utilities also offer buyback rates for excess energy you generate."),
            ("How long do solar panels last{city_faq}",
             "Most solar panels carry a 25-year performance warranty and last 30–40 years. Inverters typically need replacement after 10–15 years ($1,500–$3,000). Maintenance is minimal — annual cleaning and inspection is usually sufficient{city_in}."),
        ],
        "cost_table_rows": [
            ("Small system (4–6 kW, starter home)", "${low_sm}", "${mid_sm}"),
            ("Average system (6–8 kW, 2,000 sqft)", "${low}", "${mid_low}"),
            ("Large system (8–10 kW, 2,500+ sqft)", "${mid_low}", "${mid}"),
            ("System with battery storage", "${mid}", "${high}"),
        ],
    },

    "carpet-installation": {
        "name": "Carpet Installation",
        "slug": "carpet-installation",
        "national_kw": "carpet installation cost calculator",
        "national_vol": 49500,
        "title_tmpl":   "Carpet Installation Cost Calculator {city_suffix}(2026)",
        "desc_tmpl":    "Free carpet installation cost calculator{city_prep}. Estimate carpet & pad costs by room size, carpet grade, and removal — updated 2026 labor & material prices{city_in}.",
        "h1_tmpl":      "Carpet Installation Cost Calculator{city_h1}",
        "intro_tmpl":   "Carpet installation{city_intro} costs {cost_vs_avg} the national average. Room size, carpet grade, and whether old carpet needs removal are the biggest factors. Calculate your project below.",
        "base_low":  800,
        "base_mid":  2800,
        "base_high": 8500,
        "sqft_min": 100, "sqft_max": 2000, "sqft_default": 500,
        "sqft_label": "Area to carpet (square feet)",
        "items": [
            {"label": "Economy carpet (Berber/loop)", "base": 2.50, "unit": "per sqft", "checked": False},
            {"label": "Mid-grade carpet (cut pile)", "base": 4.50, "unit": "per sqft", "checked": True},
            {"label": "Premium carpet (wool/frieze)", "base": 8.00, "unit": "per sqft", "checked": False},
            {"label": "Standard foam pad (8lb)", "base": 0.60, "unit": "per sqft", "checked": True},
            {"label": "Premium memory foam pad", "base": 1.20, "unit": "per sqft", "checked": False},
            {"label": "Installation labor", "base": 1.20, "unit": "per sqft", "checked": True},
            {"label": "Old carpet removal & haul-away", "base": 0.55, "unit": "per sqft", "checked": True},
            {"label": "Subfloor repair (if needed)", "base": 1.80, "unit": "per sqft", "checked": False},
            {"label": "Tack strip replacement", "base": 0.30, "unit": "per sqft", "checked": False},
            {"label": "Stair carpet (per step)", "base": 40, "unit": "each", "checked": False},
        ],
        "faq": [
            ("How much does carpet installation cost{city_faq}",
             "Carpet installation{city_in} costs ${low}–${high} for a typical room, depending on carpet grade and square footage. Budget $3–$7/sqft installed for mid-grade carpet, or $6–$12/sqft for premium. Whole-home installs (1,500 sqft) typically run ${mid}–${high}."),
            ("How long does carpet installation take{city_faq}",
             "A standard bedroom (200 sqft) takes 2–4 hours. Whole-home installation (1,500 sqft) typically takes 1–2 days. Old carpet removal adds a few hours. Most installers{city_in} complete average projects in a single day."),
            ("How often should carpet be replaced{city_faq}",
             "Quality carpet lasts 10–15 years with regular care. High-traffic areas may need replacement after 7–8 years. Signs it's time: matting that won't recover, visible stains that won't clean, or persistent odors from the pad{city_in}."),
            ("What carpet grade is best for my home{city_faq}",
             "For bedrooms and low traffic: economy to mid-grade ($2.50–$5/sqft) is fine. For living rooms and stairs, choose mid-grade or better. For rentals{city_in}, economy carpet installed professionally gives the best ROI. Families with pets should choose stain-resistant fiber (nylon or SmartStrand)."),
        ],
        "cost_table_rows": [
            ("Small bedroom (100–150 sqft)", "${low_sm}", "${mid_sm}"),
            ("Master bedroom (200–250 sqft)", "${low}", "${mid_low}"),
            ("Living room (300–400 sqft)", "${mid_low}", "${mid}"),
            ("Whole floor / whole home (1,000–1,500 sqft)", "${mid}", "${high}"),
        ],
    },

    "water-heater-replacement": {
        "name": "Water Heater Replacement",
        "slug": "water-heater-replacement",
        "national_kw": "water heater replacement cost calculator",
        "national_vol": 40500,
        "title_tmpl":   "Water Heater Replacement Cost Calculator {city_suffix}(2026)",
        "desc_tmpl":    "Free water heater replacement cost calculator{city_prep}. Estimate tank vs. tankless water heater costs by fuel type and home size — updated 2026 equipment & installation prices{city_in}.",
        "h1_tmpl":      "Water Heater Replacement Cost Calculator{city_h1}",
        "intro_tmpl":   "Water heater replacement{city_intro} costs {cost_vs_avg} the national average. Fuel type (gas vs. electric), tank vs. tankless, and capacity are the main cost factors.",
        "base_low":  900,
        "base_mid":  2200,
        "base_high": 6000,
        "sqft_min": 500, "sqft_max": 5000, "sqft_default": 1800,
        "sqft_label": "Home square footage",
        "items": [
            {"label": "Gas tank water heater (40–50 gal)", "base": 950, "unit": "flat", "checked": True},
            {"label": "Electric tank water heater (50 gal)", "base": 700, "unit": "flat", "checked": False},
            {"label": "Gas tankless water heater", "base": 2200, "unit": "flat", "checked": False},
            {"label": "Electric tankless water heater", "base": 1400, "unit": "flat", "checked": False},
            {"label": "Heat pump water heater", "base": 2800, "unit": "flat", "checked": False},
            {"label": "Installation labor", "base": 600, "unit": "flat", "checked": True},
            {"label": "Old unit removal & disposal", "base": 150, "unit": "flat", "checked": True},
            {"label": "Permit & inspection", "base": 250, "unit": "flat", "checked": True},
            {"label": "Gas line upgrade (if needed)", "base": 450, "unit": "flat", "checked": False},
            {"label": "Expansion tank (code required in some areas)", "base": 180, "unit": "flat", "checked": False},
        ],
        "faq": [
            ("How much does water heater replacement cost{city_faq}",
             "Water heater replacement{city_in} costs ${low}–${high}. A standard 50-gallon gas tank unit runs ${low}–${mid_low} installed. A tankless gas unit costs ${mid}–${high} installed. Electric units are generally $200–$400 less than gas."),
            ("How long does a water heater last{city_faq}",
             "Tank water heaters last 10–15 years. Tankless units last 20+ years with proper maintenance. In {city_or_us}, hard water can shorten tank life by 2–5 years. Annual flushing extends life significantly."),
            ("Tank vs. tankless water heater — which is better{city_faq}",
             "Tankless heaters cost 2–3x more upfront but use 25–35% less energy and last longer. In {city_or_us}, a tankless unit typically pays back in 7–12 years. For homes with high hot water demand (3+ people), tankless is often the better long-term choice."),
            ("Can I install a water heater myself{city_faq}",
             "While possible for a licensed plumber, DIY water heater installation{city_in} typically voids the warranty and may not pass inspection. Most municipalities require a permit and licensed plumber. Hiring a pro costs $400–$800 but ensures proper venting, seismic strapping (where required), and code compliance."),
        ],
        "cost_table_rows": [
            ("Electric tank (50 gal), basic install", "${low_sm}", "${mid_sm}"),
            ("Gas tank (50 gal), standard install", "${low}", "${mid_low}"),
            ("Electric tankless, standard install", "${mid_low}", "${mid}"),
            ("Gas tankless, full install with permits", "${mid}", "${high}"),
        ],
    },

    "hardwood-floor-installation": {
        "name": "Hardwood Floor Installation",
        "slug": "hardwood-floor-installation",
        "national_kw": "hardwood floor installation cost calculator",
        "national_vol": 33100,
        "title_tmpl":   "Hardwood Floor Installation Cost Calculator {city_suffix}(2026)",
        "desc_tmpl":    "Free hardwood floor installation cost calculator{city_prep}. Estimate solid vs. engineered hardwood costs by room size and species — updated 2026 material & labor prices{city_in}.",
        "h1_tmpl":      "Hardwood Floor Installation Cost Calculator{city_h1}",
        "intro_tmpl":   "Hardwood floor installation{city_intro} costs {cost_vs_avg} the national average. Wood species, solid vs. engineered, and subfloor condition are the main cost drivers.",
        "base_low":  3000,
        "base_mid":  8500,
        "base_high": 22000,
        "sqft_min": 100, "sqft_max": 2500, "sqft_default": 500,
        "sqft_label": "Floor area (square feet)",
        "items": [
            {"label": "Engineered hardwood (mid-grade)", "base": 7.50, "unit": "per sqft", "checked": True},
            {"label": "Solid hardwood — oak (3¼\")", "base": 9.50, "unit": "per sqft", "checked": False},
            {"label": "Solid hardwood — maple or hickory", "base": 11.00, "unit": "per sqft", "checked": False},
            {"label": "Premium exotic hardwood (walnut, teak)", "base": 18.00, "unit": "per sqft", "checked": False},
            {"label": "Nail-down installation labor", "base": 3.50, "unit": "per sqft", "checked": True},
            {"label": "Glue-down installation (over concrete)", "base": 4.50, "unit": "per sqft", "checked": False},
            {"label": "Subfloor prep & leveling", "base": 1.50, "unit": "per sqft", "checked": False},
            {"label": "Old floor removal", "base": 1.20, "unit": "per sqft", "checked": True},
            {"label": "Sanding & finishing (unfinished wood)", "base": 3.00, "unit": "per sqft", "checked": False},
            {"label": "Baseboards & trim (per linear ft)", "base": 4.50, "unit": "per sqft", "checked": False},
        ],
        "faq": [
            ("How much does hardwood floor installation cost{city_faq}",
             "Hardwood floor installation{city_in} costs ${low}–${high} for a typical room. Engineered hardwood runs $8–$15/sqft installed; solid hardwood runs $12–$22/sqft. A 500 sqft living room typically costs ${mid_low}–${mid} for mid-grade engineered hardwood."),
            ("Solid vs. engineered hardwood — what's the difference{city_faq}",
             "Solid hardwood is one piece of real wood (¾\" thick) — can be refinished many times but sensitive to humidity. Engineered hardwood has a real wood veneer over a plywood core — more stable, can go over concrete or radiant heat, and costs less. Both look identical after installation."),
            ("How long do hardwood floors last{city_faq}",
             "Solid hardwood floors can last 100+ years with refinishing every 10–15 years. Engineered hardwood lasts 20–40 years (fewer refinishes possible). In {city_or_us}, with proper care and humidity control (35–55% RH), hardwood is one of the most durable flooring options."),
            ("Can hardwood floors be installed over concrete{city_faq}",
             "Solid hardwood should not be installed directly on concrete due to moisture. Engineered hardwood can be glued or floated over concrete with a moisture barrier. If you have a concrete slab{city_in}, engineered hardwood is the practical choice."),
        ],
        "cost_table_rows": [
            ("Small room (100–150 sqft, engineered)", "${low_sm}", "${mid_sm}"),
            ("Bedroom (200–300 sqft, engineered oak)", "${low}", "${mid_low}"),
            ("Living room (400–600 sqft, solid oak)", "${mid_low}", "${mid}"),
            ("Open floor plan (1,000+ sqft, premium)", "${mid}", "${high}"),
        ],
    },

    "garage-door-replacement": {
        "name": "Garage Door Replacement",
        "slug": "garage-door-replacement",
        "national_kw": "garage door replacement cost calculator",
        "national_vol": 14800,
        "title_tmpl":   "Garage Door Replacement Cost Calculator {city_suffix}(2026)",
        "desc_tmpl":    "Free garage door replacement cost calculator{city_prep}. Estimate single vs. double garage door costs by material and style — updated 2026 equipment & installation prices{city_in}.",
        "h1_tmpl":      "Garage Door Replacement Cost Calculator{city_h1}",
        "intro_tmpl":   "Garage door replacement{city_intro} costs {cost_vs_avg} the national average. Door size, material (steel vs. wood vs. aluminum), and opener type are the main cost factors.",
        "base_low":  700,
        "base_mid":  1800,
        "base_high": 6000,
        "sqft_min": 1, "sqft_max": 4, "sqft_default": 2,
        "sqft_label": "Number of garage bays",
        "items": [
            {"label": "Steel insulated door (single, 9×8)", "base": 850, "unit": "flat", "checked": True},
            {"label": "Steel insulated door (double, 16×8)", "base": 1400, "unit": "flat", "checked": False},
            {"label": "Carriage house style steel door", "base": 1900, "unit": "flat", "checked": False},
            {"label": "Wood garage door (single)", "base": 2200, "unit": "flat", "checked": False},
            {"label": "Aluminum & glass modern door", "base": 3500, "unit": "flat", "checked": False},
            {"label": "Professional installation labor", "base": 350, "unit": "flat", "checked": True},
            {"label": "Old door removal & disposal", "base": 120, "unit": "flat", "checked": True},
            {"label": "Belt-drive opener (quiet)", "base": 380, "unit": "flat", "checked": False},
            {"label": "Smart opener with camera & app", "base": 480, "unit": "flat", "checked": False},
            {"label": "Springs, cables & hardware", "base": 180, "unit": "flat", "checked": True},
        ],
        "faq": [
            ("How much does garage door replacement cost{city_faq}",
             "Garage door replacement{city_in} costs ${low}–${high}. A standard 9×8 single steel insulated door installed runs ${low}–${mid_low}. A 16×8 double door runs ${mid_low}–${mid}. Premium carriage-house or wood doors with opener can reach ${high}."),
            ("How long do garage doors last{city_faq}",
             "Steel garage doors last 20–30 years with proper maintenance. Wood doors last 15–20 years but require regular painting or staining. Openers typically last 10–15 years. In {city_or_us}, coastal or humid areas may shorten steel door life by 5–10 years without coating maintenance."),
            ("Do I need a permit to replace a garage door{city_faq}",
             "In most jurisdictions{city_in}, a like-for-like garage door replacement doesn't require a permit. However, changing the door opening size or adding a new opening typically does require one. Your installer should advise on local requirements."),
            ("Should I replace or repair my garage door{city_faq}",
             "If repair costs exceed 50% of replacement cost — or the door is over 20 years old, heavily dented, or poorly insulated — replacement usually makes more sense. A new insulated door can reduce garage temperature by 10–15°F{city_in} and meaningfully cut heating/cooling costs."),
        ],
        "cost_table_rows": [
            ("Single steel door (9×8), basic install", "${low_sm}", "${mid_sm}"),
            ("Single steel insulated door + install", "${low}", "${mid_low}"),
            ("Double steel door (16×8) + opener", "${mid_low}", "${mid}"),
            ("Premium wood or glass door, full install", "${mid}", "${high}"),
        ],
    },

    "foundation-repair": {
        "name": "Foundation Repair",
        "slug": "foundation-repair",
        "national_kw": "foundation repair cost calculator",
        "national_vol": 9900,
        "title_tmpl":   "Foundation Repair Cost Calculator {city_suffix}(2026)",
        "desc_tmpl":    "Free foundation repair cost calculator{city_prep}. Estimate crack sealing, pier installation, and waterproofing costs by damage level — updated 2026 labor & material prices{city_in}.",
        "h1_tmpl":      "Foundation Repair Cost Calculator{city_h1}",
        "intro_tmpl":   "Foundation repair{city_intro} costs {cost_vs_avg} the national average. Damage severity, foundation type (slab vs. basement vs. crawl space), and soil conditions are the biggest factors.",
        "base_low":  2500,
        "base_mid":  9000,
        "base_high": 35000,
        "sqft_min": 500, "sqft_max": 5000, "sqft_default": 1800,
        "sqft_label": "Home square footage",
        "items": [
            {"label": "Crack injection (epoxy/polyurethane, per crack)", "base": 500, "unit": "each", "checked": True},
            {"label": "Slab crack repair (per linear ft)", "base": 250, "unit": "each", "checked": False},
            {"label": "Slab jacking / mudjacking", "base": 1800, "unit": "flat", "checked": False},
            {"label": "Steel push pier (per pier)", "base": 1600, "unit": "each", "checked": False},
            {"label": "Helical pier (per pier)", "base": 2000, "unit": "each", "checked": False},
            {"label": "Crawl space encapsulation", "base": 1.50, "unit": "per sqft", "checked": False},
            {"label": "Interior drainage system", "base": 6500, "unit": "flat", "checked": False},
            {"label": "Sump pump installation", "base": 1400, "unit": "flat", "checked": False},
            {"label": "Basement waterproofing (exterior)", "base": 2.80, "unit": "per sqft", "checked": False},
            {"label": "Structural engineer inspection", "base": 500, "unit": "flat", "checked": True},
        ],
        "faq": [
            ("How much does foundation repair cost{city_faq}",
             "Foundation repair{city_in} costs ${low}–${high} depending on damage type. Minor crack sealing runs ${low}–${mid_sm}. Pier installation for settling foundations costs ${mid}–${high} (8–12 piers at $1,600–$2,500 each). Severe damage with extensive waterproofing can exceed ${high}."),
            ("What causes foundation problems{city_faq}",
             "In {city_or_us}, the most common causes are expansive clay soils (shrink/swell with moisture), poor drainage around the foundation, tree root intrusion, and plumbing leaks. Horizontal cracks and bowing walls are more serious than vertical hairline cracks."),
            ("Is foundation repair covered by homeowner's insurance{city_faq}",
             "Standard homeowner's insurance typically does NOT cover foundation settling or soil movement — these are considered maintenance issues. Sudden damage from a covered peril (burst pipe, earthquake with earthquake coverage) may be covered. Always check your specific policy{city_in}."),
            ("How do I know if my foundation is failing{city_faq}",
             "Warning signs include: cracks wider than ¼\" that are growing, doors or windows that stick or won't close, sloping floors (use a marble test), gaps between walls and ceilings, and water intrusion. In {city_or_us}, get a free inspection from a licensed foundation contractor if you notice any of these."),
        ],
        "cost_table_rows": [
            ("Minor crack repair (1–3 cracks)", "${low_sm}", "${mid_sm}"),
            ("Slab settling / mudjacking", "${low}", "${mid_low}"),
            ("Pier installation (4–6 piers)", "${mid_low}", "${mid}"),
            ("Major repair with waterproofing", "${mid}", "${high}"),
        ],
    },

    "gutter-replacement": {
        "name": "Gutter Replacement",
        "slug": "gutter-replacement",
        "national_kw": "gutter replacement cost calculator",
        "national_vol": 6600,
        "title_tmpl":   "Gutter Replacement Cost Calculator {city_suffix}(2026)",
        "desc_tmpl":    "Free gutter replacement cost calculator{city_prep}. Estimate aluminum, steel, and copper gutter costs by linear footage — updated 2026 material & installation prices{city_in}.",
        "h1_tmpl":      "Gutter Replacement Cost Calculator{city_h1}",
        "intro_tmpl":   "Gutter replacement{city_intro} costs {cost_vs_avg} the national average. Material (aluminum vs. steel vs. copper), home perimeter, and whether you add gutter guards are the main factors.",
        "base_low":  600,
        "base_mid":  2200,
        "base_high": 8000,
        "sqft_min": 500, "sqft_max": 5000, "sqft_default": 1800,
        "sqft_label": "Home square footage",
        "items": [
            {"label": "Aluminum gutters (per linear ft)", "base": 8.50, "unit": "per sqft", "checked": True},
            {"label": "Galvanized steel gutters (per ft)", "base": 11.00, "unit": "per sqft", "checked": False},
            {"label": "Copper gutters (per linear ft)", "base": 28.00, "unit": "per sqft", "checked": False},
            {"label": "Vinyl gutters (per linear ft, budget)", "base": 5.50, "unit": "per sqft", "checked": False},
            {"label": "Seamless gutter fabrication & install", "base": 2.00, "unit": "per sqft", "checked": True},
            {"label": "Downspout installation (per spout)", "base": 90, "unit": "each", "checked": True},
            {"label": "Old gutter removal", "base": 1.20, "unit": "per sqft", "checked": True},
            {"label": "Gutter guards / leaf protection", "base": 9.00, "unit": "per sqft", "checked": False},
            {"label": "Fascia board repair (per ft)", "base": 7.50, "unit": "per sqft", "checked": False},
            {"label": "Underground downspout extension", "base": 350, "unit": "flat", "checked": False},
        ],
        "faq": [
            ("How much does gutter replacement cost{city_faq}",
             "Gutter replacement{city_in} costs ${low}–${high}. Aluminum seamless gutters (the most common) run $8–$14/ft installed. A typical 150-ft perimeter home costs ${low}–${mid}. Copper gutters run $28–$40/ft and can push costs to ${high}."),
            ("How long do gutters last{city_faq}",
             "Aluminum gutters last 20–30 years, steel 20–30 years, and copper 50+ years. Vinyl gutters may need replacement in 10–15 years, especially in areas with temperature extremes. In {city_or_us}, annual cleaning and inspection significantly extends gutter life."),
            ("Should I get gutter guards{city_faq}",
             "Gutter guards cost $6–$15/ft and can reduce cleaning from 2x/year to once every few years. In {city_or_us}, if you have trees overhanging your roof, guards typically pay for themselves in 3–5 years of avoided cleaning costs. Micro-mesh guards are the most effective type."),
            ("When should gutters be replaced vs. repaired{city_faq}",
             "Repair (re-slope, re-seal, patch) is fine for gutters under 15 years old with isolated issues. Replace when: gutters sag, pull away from fascia, have multiple leaks, show rust/corrosion{city_in}, or were installed as sectional (seamed) gutters — seamless replacements eliminate 90% of leak points."),
        ],
        "cost_table_rows": [
            ("Small home (≤100 linear ft, aluminum)", "${low_sm}", "${mid_sm}"),
            ("Average home (150–200 ft, aluminum seamless)", "${low}", "${mid_low}"),
            ("Large home (200–250 ft) with gutter guards", "${mid_low}", "${mid}"),
            ("Premium copper gutters (150 ft)", "${mid}", "${high}"),
        ],
    },

    "concrete-patio": {
        "name": "Concrete Patio",
        "slug": "concrete-patio",
        "national_kw": "concrete patio cost calculator",
        "national_vol": 5400,
        "title_tmpl":   "Concrete Patio Cost Calculator {city_suffix}(2026)",
        "desc_tmpl":    "Free concrete patio cost calculator{city_prep}. Estimate plain, stamped, and exposed aggregate patio costs by size — updated 2026 labor & material prices{city_in}.",
        "h1_tmpl":      "Concrete Patio Cost Calculator{city_h1}",
        "intro_tmpl":   "Concrete patio installation{city_intro} costs {cost_vs_avg} the national average. Patio size, concrete finish (plain vs. stamped vs. exposed aggregate), and ground prep are the main cost drivers.",
        "base_low":  2500,
        "base_mid":  7500,
        "base_high": 22000,
        "sqft_min": 100, "sqft_max": 1200, "sqft_default": 300,
        "sqft_label": "Patio square footage",
        "items": [
            {"label": "Plain broom-finish concrete", "base": 8.00, "unit": "per sqft", "checked": True},
            {"label": "Stamped concrete (basic pattern)", "base": 14.00, "unit": "per sqft", "checked": False},
            {"label": "Stamped concrete (premium pattern)", "base": 22.00, "unit": "per sqft", "checked": False},
            {"label": "Exposed aggregate finish", "base": 12.00, "unit": "per sqft", "checked": False},
            {"label": "Excavation & grading", "base": 2.50, "unit": "per sqft", "checked": True},
            {"label": "Gravel base & compaction", "base": 1.80, "unit": "per sqft", "checked": True},
            {"label": "Rebar / wire mesh reinforcement", "base": 1.20, "unit": "per sqft", "checked": True},
            {"label": "Concrete sealer (1st application)", "base": 1.00, "unit": "per sqft", "checked": True},
            {"label": "Control joints & edging", "base": 0.80, "unit": "per sqft", "checked": True},
            {"label": "Permit & inspection", "base": 350, "unit": "flat", "checked": False},
        ],
        "faq": [
            ("How much does a concrete patio cost{city_faq}",
             "A concrete patio{city_in} costs ${low}–${high}. Plain broom-finish concrete runs ${low}–${mid_low} for a 300 sqft patio. Stamped concrete with a stone or brick pattern runs ${mid}–${high} for the same size. The finish choice is the single biggest cost variable."),
            ("How thick should a concrete patio be{city_faq}",
             "Residential concrete patios should be at least 4\" thick, poured over a compacted gravel base. In {city_or_us}, if you expect heavy vehicle traffic or have expansive soils, 6\" with rebar is recommended. Thicker slabs cost 20–30% more but last significantly longer."),
            ("How long does concrete last{city_faq}",
             "A properly poured and sealed concrete patio lasts 30–50+ years. In {city_or_us}, freeze-thaw cycles (if applicable) are the biggest threat — use air-entrained concrete and reseal every 2–3 years. Stamped concrete requires more frequent sealing to maintain color."),
            ("Stamped concrete vs. pavers — which is better{city_faq}",
             "Stamped concrete is cheaper upfront (${low}–${mid_low} vs. $15–$30/sqft for pavers) and seamless, but cracks are harder to repair. Pavers cost more but individual units can be replaced. In {city_or_us}, pavers are better in freeze-thaw climates; stamped concrete excels in mild climates."),
        ],
        "cost_table_rows": [
            ("Small patio (100–150 sqft, plain)", "${low_sm}", "${mid_sm}"),
            ("Average patio (250–350 sqft, plain/broom)", "${low}", "${mid_low}"),
            ("Stamped patio (300 sqft, basic pattern)", "${mid_low}", "${mid}"),
            ("Large stamped patio (600+ sqft, premium)", "${mid}", "${high}"),
        ],
    },
}

# ─── REUSE HELPERS FROM proj2 ────────────────────────────────────────────────
generate_page  = proj2.generate_page
make_tokens    = proj2.make_tokens
build_items_html = proj2.build_items_html
build_faq_html = proj2.build_faq_html
fmt            = proj2.fmt

# ─── MAIN ─────────────────────────────────────────────────────────────────────
def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    cities = ALL_CITIES
    print(f"Cities: {len(cities)}")
    print(f"Project types: {len(PROJECTS)}")
    print(f"Estimated pages: {len(cities) * len(PROJECTS) + len(PROJECTS):,}")
    total = 0

    for proj_key, proj in PROJECTS.items():
        # National page
        out_dir = os.path.join(base_dir, f"{proj['slug']}-cost-calculator")
        os.makedirs(out_dir, exist_ok=True)
        national_data = {"cost_mult": 1.0, "state": "US", "slug": "", "region": "national"}
        html = generate_page("", national_data, proj_key, proj)
        with open(os.path.join(out_dir, "index.html"), "w") as f:
            f.write(html)
        total += 1

        # City pages
        for city_name, city_data in cities.items():
            city_slug = city_data.get("slug", city_name.lower().replace(" ", "-"))
            out_dir = os.path.join(base_dir, f"{proj['slug']}-cost-{city_slug}")
            os.makedirs(out_dir, exist_ok=True)
            html = generate_page(city_name, city_data, proj_key, proj)
            with open(os.path.join(out_dir, "index.html"), "w") as f:
                f.write(html)
            total += 1

        print(f"  {proj['name']}... {len(cities)} city pages + 1 national")

    print(f"\nDone! {total:,} pages generated.")

if __name__ == "__main__":
    main()
