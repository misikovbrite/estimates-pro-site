#!/usr/bin/env python3
"""Batch 6 — 9 new project types × all ~730 cities."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import generate_new_projects2 as proj2
import generate_batch3 as b3
import generate_batch5 as b5

# All ~730 cities
ALL_CITIES = {}
ALL_CITIES.update(proj2.ALL_CITIES)
ALL_CITIES.update(b3.NEW_CITIES)
ALL_CITIES.update(b5.NEW_CITIES)

PROJECTS = {
    "driveway-installation": {
        "name": "Driveway Installation",
        "slug": "driveway-installation",
        "national_kw": "driveway installation cost calculator",
        "national_vol": 25000,
        "title_tmpl":   "Driveway Installation Cost Calculator {city_suffix}(2026)",
        "desc_tmpl":    "Free driveway installation cost calculator{city_prep}. Estimate asphalt, concrete, and paver driveway costs by size — updated 2026 material & labor prices{city_in}.",
        "h1_tmpl":      "Driveway Installation Cost Calculator{city_h1}",
        "intro_tmpl":   "Driveway installation{city_intro} costs {cost_vs_avg} the national average. Material choice (asphalt vs. concrete vs. pavers), driveway size, and site prep are the biggest cost drivers.",
        "base_low":  2500,
        "base_mid":  8000,
        "base_high": 25000,
        "sqft_min": 200, "sqft_max": 2000, "sqft_default": 600,
        "sqft_label": "Driveway square footage",
        "items": [
            {"label": "Asphalt driveway (per sqft)", "base": 5.00, "unit": "per sqft", "checked": True},
            {"label": "Concrete driveway (per sqft)", "base": 9.00, "unit": "per sqft", "checked": False},
            {"label": "Paver driveway (per sqft)", "base": 18.00, "unit": "per sqft", "checked": False},
            {"label": "Gravel / crush & run base (per sqft)", "base": 2.00, "unit": "per sqft", "checked": True},
            {"label": "Excavation & grading", "base": 1.50, "unit": "per sqft", "checked": True},
            {"label": "Old driveway removal", "base": 2.50, "unit": "per sqft", "checked": False},
            {"label": "Edging / curbing (per linear ft)", "base": 12.00, "unit": "per sqft", "checked": False},
            {"label": "Drainage / French drain", "base": 1800, "unit": "flat", "checked": False},
            {"label": "Sealing (asphalt, first coat)", "base": 0.40, "unit": "per sqft", "checked": True},
            {"label": "Permit & inspection", "base": 300, "unit": "flat", "checked": False},
        ],
        "faq": [
            ("How much does driveway installation cost{city_faq}",
             "Driveway installation{city_in} costs ${low}–${high}. A basic asphalt driveway (600 sqft) runs ${low}–${mid_low}. A concrete driveway the same size costs ${mid_low}–${mid}. Paver driveways can reach ${high} for a 2-car driveway with decorative borders."),
            ("Asphalt vs. concrete vs. pavers — which is best{city_faq}",
             "Asphalt is cheapest ($4–$8/sqft) and easy to repair, but needs sealing every 3–5 years and lasts 20–30 years. Concrete ($8–$14/sqft) lasts 30–50 years with less maintenance. Pavers ($15–$30/sqft) look premium, last 50+ years, and individual units can be replaced — but cost the most upfront."),
            ("How long does driveway installation take{city_faq}",
             "Asphalt installation takes 1–2 days (plus 2–3 days curing before driving on it). Concrete takes 1–2 days for the pour plus 7 days curing. Paver driveways take 3–5 days. Excavation and grading add 1–2 days to any project{city_in}."),
            ("Do I need a permit for a new driveway{city_faq}",
             "Many jurisdictions{city_in} require a permit for new driveway construction or major resurfacing, especially if it affects drainage or curb cuts. Your contractor should handle permit applications. Budget $150–$500 for permit fees."),
        ],
        "cost_table_rows": [
            ("1-car asphalt driveway (300 sqft)", "${low_sm}", "${mid_sm}"),
            ("2-car asphalt driveway (600 sqft)", "${low}", "${mid_low}"),
            ("2-car concrete driveway (600 sqft)", "${mid_low}", "${mid}"),
            ("2-car paver driveway (600 sqft)", "${mid}", "${high}"),
        ],
    },

    "well-drilling": {
        "name": "Well Drilling",
        "slug": "well-drilling",
        "national_kw": "well drilling cost calculator",
        "national_vol": 14800,
        "title_tmpl":   "Well Drilling Cost Calculator {city_suffix}(2026)",
        "desc_tmpl":    "Free well drilling cost calculator{city_prep}. Estimate residential well drilling costs by depth and pump type — updated 2026 drilling & equipment prices{city_in}.",
        "h1_tmpl":      "Well Drilling Cost Calculator{city_h1}",
        "intro_tmpl":   "Well drilling{city_intro} costs {cost_vs_avg} the national average. Drilling depth, rock conditions, and pump type are the biggest cost variables. Get your estimate below.",
        "base_low":  3500,
        "base_mid":  9500,
        "base_high": 30000,
        "sqft_min": 50, "sqft_max": 500, "sqft_default": 200,
        "sqft_label": "Target depth (feet)",
        "items": [
            {"label": "Drilling (per foot, soft soil)", "base": 30, "unit": "each", "checked": True},
            {"label": "Drilling (per foot, hard rock)", "base": 55, "unit": "each", "checked": False},
            {"label": "Submersible pump (1–2 HP)", "base": 1800, "unit": "flat", "checked": True},
            {"label": "Pump installation & wiring", "base": 900, "unit": "flat", "checked": True},
            {"label": "Pressure tank & controls", "base": 850, "unit": "flat", "checked": True},
            {"label": "Casing (per foot)", "base": 18, "unit": "each", "checked": True},
            {"label": "Well cap & sanitary seal", "base": 350, "unit": "flat", "checked": True},
            {"label": "Water testing & analysis", "base": 300, "unit": "flat", "checked": True},
            {"label": "Water treatment system (if needed)", "base": 2200, "unit": "flat", "checked": False},
            {"label": "Permit & well log filing", "base": 400, "unit": "flat", "checked": True},
        ],
        "faq": [
            ("How much does well drilling cost{city_faq}",
             "Well drilling{city_in} costs ${low}–${high}. Drilling alone runs $25–$60/foot depending on soil and rock conditions. A 200-foot well with pump, casing, and installation typically totals ${mid_low}–${mid}. Rock formations or very deep aquifers can push costs to ${high}."),
            ("How deep does a residential well need to be{city_faq}",
             "Most residential wells{city_in} are drilled 100–400 feet deep to reach a reliable aquifer. Average depth is around 150–300 feet. Your well driller will review local geological surveys and neighbor well records to estimate the depth needed for your property."),
            ("How long does well water last{city_faq}",
             "A properly drilled well can last 20–40+ years. The pump typically needs replacement every 10–25 years ($1,200–$2,500). In {city_or_us}, drought conditions can affect water table levels — your driller will advise on appropriate depth to ensure year-round supply."),
            ("Do I need a permit to drill a well{city_faq}",
             "Yes — virtually all states{city_in} require a permit before drilling a water well, and the well must be logged with the state geological survey. Your licensed well driller handles the permit process. Budget $300–$600 for permit fees and required water testing."),
        ],
        "cost_table_rows": [
            ("Shallow well (50–100 ft, soft soil)", "${low_sm}", "${mid_sm}"),
            ("Average well (150–200 ft) with pump", "${low}", "${mid_low}"),
            ("Deep well (300–400 ft) with pump & tank", "${mid_low}", "${mid}"),
            ("Deep rock well with water treatment", "${mid}", "${high}"),
        ],
    },

    "bathroom-addition": {
        "name": "Bathroom Addition",
        "slug": "bathroom-addition",
        "national_kw": "bathroom addition cost calculator",
        "national_vol": 9900,
        "title_tmpl":   "Bathroom Addition Cost Calculator {city_suffix}(2026)",
        "desc_tmpl":    "Free bathroom addition cost calculator{city_prep}. Estimate half bath, full bath, and master bath addition costs by size — updated 2026 labor & material prices{city_in}.",
        "h1_tmpl":      "Bathroom Addition Cost Calculator{city_h1}",
        "intro_tmpl":   "Adding a bathroom{city_intro} costs {cost_vs_avg} the national average. Type (half vs. full vs. master), proximity to existing plumbing, and finish level are the biggest cost factors.",
        "base_low":  5000,
        "base_mid":  18000,
        "base_high": 55000,
        "sqft_min": 20, "sqft_max": 200, "sqft_default": 60,
        "sqft_label": "Bathroom square footage",
        "items": [
            {"label": "Framing & structural work", "base": 14, "unit": "per sqft", "checked": True},
            {"label": "Plumbing rough-in (new bathroom)", "base": 4500, "unit": "flat", "checked": True},
            {"label": "Plumbing fixtures (toilet, sink, shower)", "base": 2200, "unit": "flat", "checked": True},
            {"label": "Electrical (GFCI, fan, lighting)", "base": 1200, "unit": "flat", "checked": True},
            {"label": "Tile flooring (per sqft)", "base": 12, "unit": "per sqft", "checked": True},
            {"label": "Tile shower walls (per sqft)", "base": 18, "unit": "per sqft", "checked": False},
            {"label": "Drywall & moisture-resistant backer", "base": 4.50, "unit": "per sqft", "checked": True},
            {"label": "Vanity & countertop", "base": 900, "unit": "flat", "checked": True},
            {"label": "Walk-in shower (vs. tub)", "base": 4500, "unit": "flat", "checked": False},
            {"label": "Permit & inspection fees", "base": 800, "unit": "flat", "checked": True},
        ],
        "faq": [
            ("How much does a bathroom addition cost{city_faq}",
             "Adding a bathroom{city_in} costs ${low}–${high}. A half bath (toilet + sink, ~35 sqft) runs ${low}–${mid_sm}. A full bath (60–80 sqft) costs ${mid_sm}–${mid}. A master bath with walk-in shower, double vanity, and premium tile can reach ${high}."),
            ("Is adding a bathroom worth it{city_faq}",
             "Adding a bathroom typically returns 50–60% of the cost at resale{city_in}. Homes with only 1 bathroom gain the most value from a second bath. Half bath additions near living areas have the best ROI — typically $10,000–$25,000 added to home value."),
            ("How long does bathroom addition take{city_faq}",
             "A half bath addition takes 2–4 weeks. A full bath addition takes 3–6 weeks. A master bath with custom tile work can take 6–10 weeks. In {city_or_us}, allow 2–4 weeks extra for permit approval. Plan for the space to be unusable during construction."),
            ("Can I add a bathroom without breaking through walls{city_faq}",
             "If you're converting existing space (large closet, unused room corner) and plumbing lines are accessible, you may minimize wall opening. However, new bathrooms need supply lines, drain lines, and venting — which almost always requires some wall or floor access. A licensed plumber{city_in} can advise on the least invasive approach."),
        ],
        "cost_table_rows": [
            ("Half bath (35 sqft, basic fixtures)", "${low_sm}", "${mid_sm}"),
            ("Full bath (60 sqft, mid-grade)", "${low}", "${mid_low}"),
            ("Full bath (80 sqft, tile shower)", "${mid_low}", "${mid}"),
            ("Master bath (100+ sqft, premium)", "${mid}", "${high}"),
        ],
    },

    "crawl-space-encapsulation": {
        "name": "Crawl Space Encapsulation",
        "slug": "crawl-space-encapsulation",
        "national_kw": "crawl space encapsulation cost calculator",
        "national_vol": 9900,
        "title_tmpl":   "Crawl Space Encapsulation Cost Calculator {city_suffix}(2026)",
        "desc_tmpl":    "Free crawl space encapsulation cost calculator{city_prep}. Estimate vapor barrier, insulation, and dehumidifier costs by square footage — updated 2026 labor prices{city_in}.",
        "h1_tmpl":      "Crawl Space Encapsulation Cost Calculator{city_h1}",
        "intro_tmpl":   "Crawl space encapsulation{city_intro} costs {cost_vs_avg} the national average. Square footage, moisture level, and whether you add a dehumidifier or drainage system are the main cost factors.",
        "base_low":  3000,
        "base_mid":  8000,
        "base_high": 20000,
        "sqft_min": 500, "sqft_max": 3000, "sqft_default": 1200,
        "sqft_label": "Crawl space square footage",
        "items": [
            {"label": "Vapor barrier (20-mil liner)", "base": 1.80, "unit": "per sqft", "checked": True},
            {"label": "Wall insulation (rigid foam)", "base": 1.50, "unit": "per sqft", "checked": True},
            {"label": "Floor insulation (spray foam)", "base": 2.50, "unit": "per sqft", "checked": False},
            {"label": "Installation labor", "base": 1.20, "unit": "per sqft", "checked": True},
            {"label": "Drainage matting", "base": 0.80, "unit": "per sqft", "checked": False},
            {"label": "Sump pump installation", "base": 1600, "unit": "flat", "checked": False},
            {"label": "Dehumidifier (whole-crawl unit)", "base": 1800, "unit": "flat", "checked": True},
            {"label": "Vent sealing", "base": 600, "unit": "flat", "checked": True},
            {"label": "Mold treatment / remediation", "base": 1500, "unit": "flat", "checked": False},
            {"label": "Old insulation removal", "base": 1.00, "unit": "per sqft", "checked": False},
        ],
        "faq": [
            ("How much does crawl space encapsulation cost{city_faq}",
             "Crawl space encapsulation{city_in} costs ${low}–${high}. Basic vapor barrier and wall insulation for a 1,200 sqft crawl space runs ${low}–${mid}. Adding a dehumidifier, sump pump, and drainage system pushes costs toward ${high}. Severe moisture or mold issues add $1,500–$5,000."),
            ("Is crawl space encapsulation worth it{city_faq}",
             "Yes — encapsulation reduces moisture, prevents mold, lowers heating/cooling costs by 10–20%, and extends the life of floor joists and structural wood. In {city_or_us}, most homeowners see the investment pay back within 5–10 years in energy savings and avoided repairs."),
            ("How long does crawl space encapsulation last{city_faq}",
             "A properly installed 20-mil vapor barrier lasts 25+ years. The dehumidifier runs continuously and typically needs service every 2–3 years and replacement after 10–15 years. Annual inspection ensures the system is working and drains are clear{city_in}."),
            ("Do I need encapsulation or just a vapor barrier{city_faq}",
             "A basic vapor barrier (thin plastic sheeting, $0.50–$0.80/sqft) covers the floor only and is a minimal fix. Full encapsulation seals all surfaces — floor, walls, and vents — and actively controls humidity. In {city_or_us}, full encapsulation is recommended for homes with visible moisture, musty odors, or high humidity readings above 60%."),
        ],
        "cost_table_rows": [
            ("Small crawl space (600 sqft), basic", "${low_sm}", "${mid_sm}"),
            ("Average crawl space (1,200 sqft)", "${low}", "${mid_low}"),
            ("Large crawl space (1,800 sqft) + dehumidifier", "${mid_low}", "${mid}"),
            ("Full system with sump pump & drainage", "${mid}", "${high}"),
        ],
    },

    "attic-insulation": {
        "name": "Attic Insulation",
        "slug": "attic-insulation",
        "national_kw": "attic insulation cost calculator",
        "national_vol": 8100,
        "title_tmpl":   "Attic Insulation Cost Calculator {city_suffix}(2026)",
        "desc_tmpl":    "Free attic insulation cost calculator{city_prep}. Estimate blown-in, batt, and spray foam insulation costs by attic size and R-value — updated 2026 material & labor prices{city_in}.",
        "h1_tmpl":      "Attic Insulation Cost Calculator{city_h1}",
        "intro_tmpl":   "Attic insulation{city_intro} costs {cost_vs_avg} the national average. Insulation type, attic square footage, and current R-value determine the scope and cost of the project.",
        "base_low":  1200,
        "base_mid":  3500,
        "base_high": 10000,
        "sqft_min": 500, "sqft_max": 3000, "sqft_default": 1200,
        "sqft_label": "Attic square footage",
        "items": [
            {"label": "Blown-in fiberglass (per sqft)", "base": 1.50, "unit": "per sqft", "checked": True},
            {"label": "Blown-in cellulose (per sqft)", "base": 1.40, "unit": "per sqft", "checked": False},
            {"label": "Fiberglass batts (per sqft)", "base": 1.20, "unit": "per sqft", "checked": False},
            {"label": "Open-cell spray foam (per sqft)", "base": 3.50, "unit": "per sqft", "checked": False},
            {"label": "Closed-cell spray foam (per sqft)", "base": 6.00, "unit": "per sqft", "checked": False},
            {"label": "Installation labor", "base": 0.80, "unit": "per sqft", "checked": True},
            {"label": "Old insulation removal", "base": 1.80, "unit": "per sqft", "checked": False},
            {"label": "Air sealing (penetrations, gaps)", "base": 700, "unit": "flat", "checked": True},
            {"label": "Attic ventilation check & baffles", "base": 400, "unit": "flat", "checked": False},
            {"label": "Radiant barrier (per sqft)", "base": 0.80, "unit": "per sqft", "checked": False},
        ],
        "faq": [
            ("How much does attic insulation cost{city_faq}",
             "Attic insulation{city_in} costs ${low}–${high}. Blown-in fiberglass or cellulose for a 1,200 sqft attic (R-38 to R-49) typically runs ${low}–${mid}. Spray foam insulation costs 3–5x more but provides superior air sealing and is ideal for cathedral ceilings or unvented attics."),
            ("What R-value do I need for my attic{city_faq}",
             "The DOE recommends R-38 to R-60 for attics in most of {state}. {city_or_us} falls in climate zone {region} — hotter climates need less, colder climates need more. If you currently have R-11 or less, upgrading to R-49 typically cuts heating/cooling costs by 15–20%."),
            ("How much can I save with attic insulation{city_faq}",
             "Proper attic insulation{city_in} can reduce heating and cooling bills by 10–20%. For a home spending $200/month on energy, that's $240–$480/year in savings. Most attic insulation projects pay back in 3–6 years and come with significant utility rebates from {state} utilities."),
            ("Should I remove old insulation before adding new{city_faq}",
             "If old insulation is damaged, contaminated (pest droppings, mold, vermiculite asbestos), or wet, remove it before adding new. For old fiberglass batts in good condition, blown-in insulation can usually be added on top. Removal adds $1.50–$2.50/sqft to the project cost{city_in}."),
        ],
        "cost_table_rows": [
            ("Small attic (600 sqft, blown-in)", "${low_sm}", "${mid_sm}"),
            ("Average attic (1,200 sqft, blown-in R-38)", "${low}", "${mid_low}"),
            ("Large attic (2,000 sqft, blown-in R-49)", "${mid_low}", "${mid}"),
            ("Spray foam (1,200 sqft, unvented attic)", "${mid}", "${high}"),
        ],
    },

    "septic-system": {
        "name": "Septic System Installation",
        "slug": "septic-system",
        "national_kw": "septic system cost calculator",
        "national_vol": 6600,
        "title_tmpl":   "Septic System Cost Calculator {city_suffix}(2026)",
        "desc_tmpl":    "Free septic system cost calculator{city_prep}. Estimate conventional, mound, and aerobic septic system costs by home size — updated 2026 installation prices{city_in}.",
        "h1_tmpl":      "Septic System Cost Calculator{city_h1}",
        "intro_tmpl":   "Septic system installation{city_intro} costs {cost_vs_avg} the national average. System type, tank size, and soil conditions (perc test results) determine the total cost.",
        "base_low":  4000,
        "base_mid":  12000,
        "base_high": 35000,
        "sqft_min": 1000, "sqft_max": 5000, "sqft_default": 2000,
        "sqft_label": "Home square footage",
        "items": [
            {"label": "Conventional septic tank (1,000 gal)", "base": 1200, "unit": "flat", "checked": True},
            {"label": "Concrete tank (1,500 gal)", "base": 1800, "unit": "flat", "checked": False},
            {"label": "Drain field / leach field", "base": 5500, "unit": "flat", "checked": True},
            {"label": "Mound system (poor drainage)", "base": 15000, "unit": "flat", "checked": False},
            {"label": "Aerobic system (ATU)", "base": 10000, "unit": "flat", "checked": False},
            {"label": "Excavation & site work", "base": 2500, "unit": "flat", "checked": True},
            {"label": "Percolation (perc) test", "base": 500, "unit": "flat", "checked": True},
            {"label": "Distribution box & risers", "base": 600, "unit": "flat", "checked": True},
            {"label": "Pump system (for mound/ATU)", "base": 1500, "unit": "flat", "checked": False},
            {"label": "Permit & engineer design", "base": 1200, "unit": "flat", "checked": True},
        ],
        "faq": [
            ("How much does a septic system cost{city_faq}",
             "Septic system installation{city_in} costs ${low}–${high}. A conventional gravity system with 1,000-gallon tank and drain field typically runs ${low}–${mid}. Mound systems (required for poor drainage) cost ${mid}–${high}. Aerobic treatment units for tight soils can reach ${high}."),
            ("How long does a septic system last{city_faq}",
             "A well-maintained concrete septic system lasts 25–40 years. The drain field can last 25–30 years. In {city_or_us}, pumping the tank every 3–5 years ($300–$600) and avoiding harsh chemicals dramatically extends system life."),
            ("Do I need a perc test before installing a septic system{city_faq}",
             "Yes — almost all jurisdictions{city_in} require a percolation (perc) test to determine soil absorption rates before approving a septic system design. The test costs $300–$800 and is required before a permit is issued. Fast-draining sandy soils and very slow clay soils both affect which system type is approved."),
            ("What's the difference between a conventional and aerobic septic system{city_faq}",
             "Conventional systems use gravity and natural soil bacteria — simpler and cheaper ($4,000–$15,000) but need sufficient land and adequate soil drainage. Aerobic systems (ATUs) add oxygen to accelerate treatment — required for poor soils or smaller lots{city_in}. ATUs cost $10,000–$20,000 but have a smaller footprint."),
        ],
        "cost_table_rows": [
            ("Conventional system (2-bedroom home)", "${low_sm}", "${mid_sm}"),
            ("Conventional system (3–4 bedroom)", "${low}", "${mid_low}"),
            ("Mound system (poor soil / high water table)", "${mid_low}", "${mid}"),
            ("Aerobic / ATU system", "${mid}", "${high}"),
        ],
    },

    "chimney-repair": {
        "name": "Chimney Repair",
        "slug": "chimney-repair",
        "national_kw": "chimney repair cost calculator",
        "national_vol": 4400,
        "title_tmpl":   "Chimney Repair Cost Calculator {city_suffix}(2026)",
        "desc_tmpl":    "Free chimney repair cost calculator{city_prep}. Estimate tuckpointing, liner, and chimney rebuild costs by damage type — updated 2026 masonry & labor prices{city_in}.",
        "h1_tmpl":      "Chimney Repair Cost Calculator{city_h1}",
        "intro_tmpl":   "Chimney repair{city_intro} costs {cost_vs_avg} the national average. Damage type (tuckpointing, liner replacement, or full rebuild), chimney height, and brick type determine the total cost.",
        "base_low":  500,
        "base_mid":  3500,
        "base_high": 15000,
        "sqft_min": 1, "sqft_max": 4, "sqft_default": 2,
        "sqft_label": "Number of chimney stories",
        "items": [
            {"label": "Chimney inspection (Level 2)", "base": 350, "unit": "flat", "checked": True},
            {"label": "Tuckpointing / repointing (per sq ft)", "base": 15, "unit": "each", "checked": True},
            {"label": "Chimney cap replacement", "base": 400, "unit": "flat", "checked": False},
            {"label": "Flashing repair / replacement", "base": 700, "unit": "flat", "checked": False},
            {"label": "Crown repair / rebuild", "base": 900, "unit": "flat", "checked": False},
            {"label": "Stainless steel liner (relining)", "base": 2800, "unit": "flat", "checked": False},
            {"label": "Firebox repair (interior brick)", "base": 1500, "unit": "flat", "checked": False},
            {"label": "Partial chimney rebuild (top 1/3)", "base": 3500, "unit": "flat", "checked": False},
            {"label": "Full chimney rebuild", "base": 9000, "unit": "flat", "checked": False},
            {"label": "Waterproofing treatment", "base": 500, "unit": "flat", "checked": True},
        ],
        "faq": [
            ("How much does chimney repair cost{city_faq}",
             "Chimney repair{city_in} costs ${low}–${high} depending on the work needed. Minor repairs (cap, flashing, tuckpointing) run ${low}–${mid_sm}. Liner replacement costs ${mid_sm}–${mid}. A full chimney rebuild can reach ${high} for a 2-story brick chimney."),
            ("How often should a chimney be inspected{city_faq}",
             "The NFPA recommends annual chimney inspections for fireplaces used regularly. In {city_or_us}, even if you only use the fireplace a few times a year, inspect every 2–3 years. Birds, squirrels, and moisture can damage chimneys between uses."),
            ("What is tuckpointing and do I need it{city_faq}",
             "Tuckpointing removes deteriorated mortar between bricks and fills it with fresh mortar. Signs you need it: crumbling mortar, bricks that shift when pushed, or water stains inside near the fireplace. In {city_or_us}, freeze-thaw cycles accelerate mortar erosion — inspect every 3–5 years and tuckpoint as needed."),
            ("Is a cracked chimney dangerous{city_faq}",
             "Yes — cracks in the firebox or flue liner can allow heat and combustion gases (including carbon monoxide) to enter the home. A damaged liner is the leading cause of chimney fires. If you see cracks wider than 1/8\", have a certified chimney sweep{city_in} do a Level 2 inspection before using the fireplace."),
        ],
        "cost_table_rows": [
            ("Minor repair (cap, flashing, sealant)", "${low_sm}", "${mid_sm}"),
            ("Tuckpointing + crown repair", "${low}", "${mid_low}"),
            ("Liner replacement (stainless)", "${mid_low}", "${mid}"),
            ("Partial or full chimney rebuild", "${mid}", "${high}"),
        ],
    },

    "sunroom-addition": {
        "name": "Sunroom Addition",
        "slug": "sunroom-addition",
        "national_kw": "sunroom addition cost calculator",
        "national_vol": 3600,
        "title_tmpl":   "Sunroom Addition Cost Calculator {city_suffix}(2026)",
        "desc_tmpl":    "Free sunroom addition cost calculator{city_prep}. Estimate three-season, four-season, and solarium addition costs by size — updated 2026 construction prices{city_in}.",
        "h1_tmpl":      "Sunroom Addition Cost Calculator{city_h1}",
        "intro_tmpl":   "Sunroom addition{city_intro} costs {cost_vs_avg} the national average. Sunroom type (3-season vs. 4-season vs. solarium), size, and foundation type drive the biggest cost differences.",
        "base_low":  15000,
        "base_mid":  45000,
        "base_high": 120000,
        "sqft_min": 100, "sqft_max": 600, "sqft_default": 200,
        "sqft_label": "Sunroom square footage",
        "items": [
            {"label": "3-season sunroom (screened/basic glass)", "base": 60, "unit": "per sqft", "checked": True},
            {"label": "4-season sunroom (insulated, HVAC)", "base": 140, "unit": "per sqft", "checked": False},
            {"label": "Solarium (full glass roof & walls)", "base": 200, "unit": "per sqft", "checked": False},
            {"label": "Prefab sunroom kit", "base": 8000, "unit": "flat", "checked": False},
            {"label": "Foundation (slab or piers)", "base": 18, "unit": "per sqft", "checked": True},
            {"label": "HVAC mini-split (4-season)", "base": 4500, "unit": "flat", "checked": False},
            {"label": "Electrical (outlets, lighting)", "base": 1800, "unit": "flat", "checked": True},
            {"label": "Interior finishing (flooring, trim)", "base": 15, "unit": "per sqft", "checked": False},
            {"label": "Permit & engineering", "base": 1500, "unit": "flat", "checked": True},
        ],
        "faq": [
            ("How much does a sunroom addition cost{city_faq}",
             "Sunroom additions{city_in} cost ${low}–${high}. A basic 3-season room (200 sqft) runs ${low}–${mid_sm}. A 4-season heated/cooled sunroom costs ${mid_sm}–${mid}. A full solarium with glass roof can reach ${high}. Prefab kits start around $8,000–$15,000 but require a prepared foundation."),
            ("3-season vs. 4-season sunroom — what's the difference{city_faq}",
             "A 3-season room has screened or thin-glass walls with no HVAC — comfortable spring through fall but unusable in winter{city_in}. A 4-season room has insulated walls, double-pane windows, and a mini-split system — livable year-round and often counts as conditioned square footage, adding more home value."),
            ("Does a sunroom add home value{city_faq}",
             "A 4-season sunroom typically returns 50–70% of its cost at resale{city_in}. A well-built sunroom adds livable square footage, improves natural light, and has strong buyer appeal. 3-season rooms return less (30–50%) since they're seasonal."),
            ("Do I need a permit for a sunroom{city_faq}",
             "Yes — sunrooms are permanent structure additions and require a building permit in virtually all jurisdictions{city_in}. You'll need architectural drawings for a 4-season room. Processing typically takes 2–6 weeks. Your contractor should handle the permit application."),
        ],
        "cost_table_rows": [
            ("Small 3-season room (100–150 sqft)", "${low_sm}", "${mid_sm}"),
            ("Average 3-season (200 sqft)", "${low}", "${mid_low}"),
            ("4-season room (200 sqft, insulated)", "${mid_low}", "${mid}"),
            ("Large 4-season / solarium (300+ sqft)", "${mid}", "${high}"),
        ],
    },

    "mold-remediation": {
        "name": "Mold Remediation",
        "slug": "mold-remediation",
        "national_kw": "mold remediation cost calculator",
        "national_vol": 2900,
        "title_tmpl":   "Mold Remediation Cost Calculator {city_suffix}(2026)",
        "desc_tmpl":    "Free mold remediation cost calculator{city_prep}. Estimate mold testing, removal, and remediation costs by affected area — updated 2026 contractor prices{city_in}.",
        "h1_tmpl":      "Mold Remediation Cost Calculator{city_h1}",
        "intro_tmpl":   "Mold remediation{city_intro} costs {cost_vs_avg} the national average. Affected area size, mold type, and location (crawl space vs. attic vs. walls) are the key cost factors.",
        "base_low":  500,
        "base_mid":  4000,
        "base_high": 20000,
        "sqft_min": 10, "sqft_max": 1000, "sqft_default": 100,
        "sqft_label": "Affected area (square feet)",
        "items": [
            {"label": "Mold inspection & air testing", "base": 600, "unit": "flat", "checked": True},
            {"label": "Surface mold removal (per sqft)", "base": 12, "unit": "per sqft", "checked": True},
            {"label": "Containment & HEPA air scrubbing", "base": 800, "unit": "flat", "checked": True},
            {"label": "Antimicrobial treatment", "base": 4, "unit": "per sqft", "checked": True},
            {"label": "Drywall removal & disposal", "base": 3.50, "unit": "per sqft", "checked": False},
            {"label": "New drywall installation", "base": 5.00, "unit": "per sqft", "checked": False},
            {"label": "Attic mold remediation (blasting)", "base": 3.00, "unit": "per sqft", "checked": False},
            {"label": "Crawl space mold treatment", "base": 2.50, "unit": "per sqft", "checked": False},
            {"label": "HVAC duct cleaning (if affected)", "base": 700, "unit": "flat", "checked": False},
            {"label": "Post-remediation clearance testing", "base": 450, "unit": "flat", "checked": True},
        ],
        "faq": [
            ("How much does mold remediation cost{city_faq}",
             "Mold remediation{city_in} costs ${low}–${high}. Small surface mold patches (under 10 sqft) run ${low}–${mid_sm} including testing. Average bathroom or basement mold costs ${mid_sm}–${mid}. Large-scale attic or crawl space mold affecting structural wood can reach ${high}."),
            ("Can I remove mold myself{city_faq}",
             "For small patches under 10 sqft of non-porous surfaces (tile, glass), DIY removal with commercial mold killer is feasible. For anything larger, behind drywall, in HVAC systems, or involving black mold (Stachybotrys){city_in}, hire a certified remediation contractor. Improper removal spreads spores through the home."),
            ("How long does mold remediation take{city_faq}",
             "Small surface mold remediation takes 1–3 days. Medium projects (bathroom, basement) take 3–5 days. Large attic or whole-basement projects take 1–2 weeks. Post-remediation air testing (clearance) adds 1–2 days wait time{city_in} before re-occupying the space."),
            ("Does homeowner's insurance cover mold remediation{city_faq}",
             "It depends on the cause. If mold results from a covered water event (burst pipe, appliance leak) that was reported promptly, insurance often covers remediation{city_in}. Gradual moisture, flooding, or long-term neglect is typically not covered. Document the source and file a claim immediately when you discover water damage."),
        ],
        "cost_table_rows": [
            ("Small patch (10–20 sqft, surface mold)", "${low_sm}", "${mid_sm}"),
            ("Medium area (50–100 sqft, bathroom)", "${low}", "${mid_low}"),
            ("Large area (200–400 sqft, basement)", "${mid_low}", "${mid}"),
            ("Attic or crawl space (500+ sqft)", "${mid}", "${high}"),
        ],
    },
}

# ─── HELPERS ──────────────────────────────────────────────────────────────────
def save_page(out_dir, html):
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "index.html"), "w") as f:
        f.write(html)

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    cities = ALL_CITIES
    print(f"Cities: {len(cities)}")
    print(f"Project types: {len(PROJECTS)}")
    print(f"Estimated pages: {len(cities) * len(PROJECTS) + len(PROJECTS):,}")
    total = 0

    for proj_key, proj in PROJECTS.items():
        # National page
        national_data = {"cost_mult": 1.0, "state": "US", "slug": "", "region": "national"}
        out_dir = os.path.join(base_dir, f"{proj['slug']}-cost-calculator")
        save_page(out_dir, proj2.generate_page("", national_data, proj_key, proj))
        total += 1

        for city_name, city_data in cities.items():
            city_slug = city_data.get("slug", city_name.lower().replace(" ", "-"))
            out_dir = os.path.join(base_dir, f"{proj['slug']}-cost-{city_slug}")
            save_page(out_dir, proj2.generate_page(city_name, city_data, proj_key, proj))
            total += 1

        print(f"  {proj['name']}... {len(cities)} city pages")

    print(f"\nDone! {total:,} pages generated.")

if __name__ == "__main__":
    main()
