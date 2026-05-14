#!/usr/bin/env python3
"""Generate 5 new project type calculator pages (HVAC, pool, home addition, landscaping, deck) × 237 US cities."""
import os, json

# ─── ALL 237 CITIES ───────────────────────────────────────────────────────────
ALL_CITIES = {
    "New York":{"slug":"new-york","state":"New York","cost_mult":1.35,"region":"Northeast"},
    "Los Angeles":{"slug":"los-angeles","state":"California","cost_mult":1.25,"region":"West"},
    "Chicago":{"slug":"chicago","state":"Illinois","cost_mult":1.10,"region":"Midwest"},
    "Houston":{"slug":"houston","state":"Texas","cost_mult":0.92,"region":"South"},
    "Phoenix":{"slug":"phoenix","state":"Arizona","cost_mult":0.95,"region":"South"},
    "Philadelphia":{"slug":"philadelphia","state":"Pennsylvania","cost_mult":1.12,"region":"Northeast"},
    "San Antonio":{"slug":"san-antonio","state":"Texas","cost_mult":0.88,"region":"South"},
    "San Diego":{"slug":"san-diego","state":"California","cost_mult":1.28,"region":"West"},
    "Dallas":{"slug":"dallas","state":"Texas","cost_mult":0.94,"region":"South"},
    "San Jose":{"slug":"san-jose","state":"California","cost_mult":1.40,"region":"West"},
    "Austin":{"slug":"austin","state":"Texas","cost_mult":0.97,"region":"South"},
    "Jacksonville":{"slug":"jacksonville","state":"Florida","cost_mult":0.90,"region":"South"},
    "Fort Worth":{"slug":"fort-worth","state":"Texas","cost_mult":0.93,"region":"South"},
    "Columbus":{"slug":"columbus","state":"Ohio","cost_mult":0.90,"region":"Midwest"},
    "Charlotte":{"slug":"charlotte","state":"North Carolina","cost_mult":0.93,"region":"South"},
    "Indianapolis":{"slug":"indianapolis","state":"Indiana","cost_mult":0.88,"region":"Midwest"},
    "San Francisco":{"slug":"san-francisco","state":"California","cost_mult":1.55,"region":"West"},
    "Seattle":{"slug":"seattle","state":"Washington","cost_mult":1.30,"region":"West"},
    "Denver":{"slug":"denver","state":"Colorado","cost_mult":1.05,"region":"Mountain"},
    "Nashville":{"slug":"nashville","state":"Tennessee","cost_mult":0.93,"region":"South"},
    "Oklahoma City":{"slug":"oklahoma-city","state":"Oklahoma","cost_mult":0.85,"region":"South"},
    "El Paso":{"slug":"el-paso","state":"Texas","cost_mult":0.82,"region":"South"},
    "Washington DC":{"slug":"washington-dc","state":"District of Columbia","cost_mult":1.30,"region":"Northeast"},
    "Las Vegas":{"slug":"las-vegas","state":"Nevada","cost_mult":1.00,"region":"West"},
    "Boston":{"slug":"boston","state":"Massachusetts","cost_mult":1.35,"region":"Northeast"},
    "Portland":{"slug":"portland","state":"Oregon","cost_mult":1.15,"region":"West"},
    "Memphis":{"slug":"memphis","state":"Tennessee","cost_mult":0.83,"region":"South"},
    "Louisville":{"slug":"louisville","state":"Kentucky","cost_mult":0.87,"region":"South"},
    "Baltimore":{"slug":"baltimore","state":"Maryland","cost_mult":1.12,"region":"Northeast"},
    "Milwaukee":{"slug":"milwaukee","state":"Wisconsin","cost_mult":0.93,"region":"Midwest"},
    "Albuquerque":{"slug":"albuquerque","state":"New Mexico","cost_mult":0.88,"region":"Mountain"},
    "Tucson":{"slug":"tucson","state":"Arizona","cost_mult":0.87,"region":"South"},
    "Fresno":{"slug":"fresno","state":"California","cost_mult":0.97,"region":"West"},
    "Sacramento":{"slug":"sacramento","state":"California","cost_mult":1.10,"region":"West"},
    "Mesa":{"slug":"mesa","state":"Arizona","cost_mult":0.95,"region":"South"},
    "Atlanta":{"slug":"atlanta","state":"Georgia","cost_mult":0.96,"region":"South"},
    "Omaha":{"slug":"omaha","state":"Nebraska","cost_mult":0.87,"region":"Midwest"},
    "Colorado Springs":{"slug":"colorado-springs","state":"Colorado","cost_mult":1.00,"region":"Mountain"},
    "Raleigh":{"slug":"raleigh","state":"North Carolina","cost_mult":0.95,"region":"South"},
    "Miami":{"slug":"miami","state":"Florida","cost_mult":1.08,"region":"South"},
    "Minneapolis":{"slug":"minneapolis","state":"Minnesota","cost_mult":1.05,"region":"Midwest"},
    "Tampa":{"slug":"tampa","state":"Florida","cost_mult":0.98,"region":"South"},
    "New Orleans":{"slug":"new-orleans","state":"Louisiana","cost_mult":0.90,"region":"South"},
    "Cleveland":{"slug":"cleveland","state":"Ohio","cost_mult":0.87,"region":"Midwest"},
    "Bakersfield":{"slug":"bakersfield","state":"California","cost_mult":0.93,"region":"West"},
    "Honolulu":{"slug":"honolulu","state":"Hawaii","cost_mult":1.65,"region":"West"},
    "Anaheim":{"slug":"anaheim","state":"California","cost_mult":1.25,"region":"West"},
    "Riverside":{"slug":"riverside","state":"California","cost_mult":1.10,"region":"West"},
    "Corpus Christi":{"slug":"corpus-christi","state":"Texas","cost_mult":0.87,"region":"South"},
    "Cincinnati":{"slug":"cincinnati","state":"Ohio","cost_mult":0.90,"region":"Midwest"},
    "St. Louis":{"slug":"st-louis","state":"Missouri","cost_mult":0.90,"region":"Midwest"},
    # California
    "Long Beach":{"slug":"long-beach","state":"California","cost_mult":1.22,"region":"West"},
    "Oakland":{"slug":"oakland","state":"California","cost_mult":1.35,"region":"West"},
    "Stockton":{"slug":"stockton","state":"California","cost_mult":0.97,"region":"West"},
    "Irvine":{"slug":"irvine","state":"California","cost_mult":1.30,"region":"West"},
    "San Bernardino":{"slug":"san-bernardino","state":"California","cost_mult":1.00,"region":"West"},
    "Chula Vista":{"slug":"chula-vista","state":"California","cost_mult":1.18,"region":"West"},
    "Modesto":{"slug":"modesto","state":"California","cost_mult":0.95,"region":"West"},
    "Oxnard":{"slug":"oxnard","state":"California","cost_mult":1.12,"region":"West"},
    "Fontana":{"slug":"fontana","state":"California","cost_mult":1.05,"region":"West"},
    "Moreno Valley":{"slug":"moreno-valley","state":"California","cost_mult":1.02,"region":"West"},
    "Santa Ana":{"slug":"santa-ana","state":"California","cost_mult":1.18,"region":"West"},
    "Glendale":{"slug":"glendale","state":"California","cost_mult":1.22,"region":"West"},
    "Huntington Beach":{"slug":"huntington-beach","state":"California","cost_mult":1.25,"region":"West"},
    "Santa Clarita":{"slug":"santa-clarita","state":"California","cost_mult":1.20,"region":"West"},
    "Fremont":{"slug":"fremont","state":"California","cost_mult":1.38,"region":"West"},
    "Torrance":{"slug":"torrance","state":"California","cost_mult":1.22,"region":"West"},
    # Texas
    "Arlington":{"slug":"arlington","state":"Texas","cost_mult":0.93,"region":"South"},
    "Plano":{"slug":"plano","state":"Texas","cost_mult":0.96,"region":"South"},
    "Laredo":{"slug":"laredo","state":"Texas","cost_mult":0.80,"region":"South"},
    "Lubbock":{"slug":"lubbock","state":"Texas","cost_mult":0.82,"region":"South"},
    "Garland":{"slug":"garland","state":"Texas","cost_mult":0.92,"region":"South"},
    "Irving":{"slug":"irving","state":"Texas","cost_mult":0.94,"region":"South"},
    "Amarillo":{"slug":"amarillo","state":"Texas","cost_mult":0.82,"region":"South"},
    "Grand Prairie":{"slug":"grand-prairie","state":"Texas","cost_mult":0.90,"region":"South"},
    "McKinney":{"slug":"mckinney","state":"Texas","cost_mult":0.96,"region":"South"},
    "Frisco":{"slug":"frisco","state":"Texas","cost_mult":1.00,"region":"South"},
    "Killeen":{"slug":"killeen","state":"Texas","cost_mult":0.82,"region":"South"},
    "Brownsville":{"slug":"brownsville","state":"Texas","cost_mult":0.78,"region":"South"},
    "Pasadena":{"slug":"pasadena","state":"Texas","cost_mult":0.90,"region":"South"},
    "Mesquite":{"slug":"mesquite","state":"Texas","cost_mult":0.90,"region":"South"},
    # Florida
    "Orlando":{"slug":"orlando","state":"Florida","cost_mult":1.00,"region":"South"},
    "St. Petersburg":{"slug":"st-petersburg","state":"Florida","cost_mult":0.97,"region":"South"},
    "Hialeah":{"slug":"hialeah","state":"Florida","cost_mult":1.00,"region":"South"},
    "Port St. Lucie":{"slug":"port-st-lucie","state":"Florida","cost_mult":0.95,"region":"South"},
    "Cape Coral":{"slug":"cape-coral","state":"Florida","cost_mult":0.97,"region":"South"},
    "Fort Lauderdale":{"slug":"fort-lauderdale","state":"Florida","cost_mult":1.05,"region":"South"},
    "Pembroke Pines":{"slug":"pembroke-pines","state":"Florida","cost_mult":1.02,"region":"South"},
    "Hollywood FL":{"slug":"hollywood-fl","state":"Florida","cost_mult":1.03,"region":"South"},
    "Gainesville":{"slug":"gainesville","state":"Florida","cost_mult":0.90,"region":"South"},
    "Tallahassee":{"slug":"tallahassee","state":"Florida","cost_mult":0.88,"region":"South"},
    "Miramar":{"slug":"miramar","state":"Florida","cost_mult":1.02,"region":"South"},
    "Clearwater":{"slug":"clearwater","state":"Florida","cost_mult":0.97,"region":"South"},
    # New York
    "Buffalo":{"slug":"buffalo","state":"New York","cost_mult":1.05,"region":"Northeast"},
    "Rochester":{"slug":"rochester","state":"New York","cost_mult":1.00,"region":"Northeast"},
    "Yonkers":{"slug":"yonkers","state":"New York","cost_mult":1.30,"region":"Northeast"},
    "Syracuse":{"slug":"syracuse","state":"New York","cost_mult":0.97,"region":"Northeast"},
    "Albany":{"slug":"albany","state":"New York","cost_mult":1.02,"region":"Northeast"},
    # Illinois
    "Aurora":{"slug":"aurora","state":"Illinois","cost_mult":1.05,"region":"Midwest"},
    "Naperville":{"slug":"naperville","state":"Illinois","cost_mult":1.08,"region":"Midwest"},
    "Joliet":{"slug":"joliet","state":"Illinois","cost_mult":1.02,"region":"Midwest"},
    "Rockford":{"slug":"rockford","state":"Illinois","cost_mult":0.88,"region":"Midwest"},
    "Springfield":{"slug":"springfield","state":"Illinois","cost_mult":0.87,"region":"Midwest"},
    "Peoria":{"slug":"peoria","state":"Illinois","cost_mult":0.85,"region":"Midwest"},
    # Pennsylvania
    "Pittsburgh":{"slug":"pittsburgh","state":"Pennsylvania","cost_mult":1.05,"region":"Northeast"},
    "Allentown":{"slug":"allentown","state":"Pennsylvania","cost_mult":1.00,"region":"Northeast"},
    # Ohio
    "Akron":{"slug":"akron","state":"Ohio","cost_mult":0.87,"region":"Midwest"},
    "Toledo":{"slug":"toledo","state":"Ohio","cost_mult":0.85,"region":"Midwest"},
    "Dayton":{"slug":"dayton","state":"Ohio","cost_mult":0.85,"region":"Midwest"},
    # Michigan
    "Detroit":{"slug":"detroit","state":"Michigan","cost_mult":0.95,"region":"Midwest"},
    "Grand Rapids":{"slug":"grand-rapids","state":"Michigan","cost_mult":0.92,"region":"Midwest"},
    "Warren":{"slug":"warren","state":"Michigan","cost_mult":0.93,"region":"Midwest"},
    "Sterling Heights":{"slug":"sterling-heights","state":"Michigan","cost_mult":0.95,"region":"Midwest"},
    "Ann Arbor":{"slug":"ann-arbor","state":"Michigan","cost_mult":1.05,"region":"Midwest"},
    "Lansing":{"slug":"lansing","state":"Michigan","cost_mult":0.88,"region":"Midwest"},
    # North Carolina
    "Durham":{"slug":"durham","state":"North Carolina","cost_mult":0.97,"region":"South"},
    "Greensboro":{"slug":"greensboro","state":"North Carolina","cost_mult":0.90,"region":"South"},
    "Winston-Salem":{"slug":"winston-salem","state":"North Carolina","cost_mult":0.88,"region":"South"},
    "Fayetteville":{"slug":"fayetteville","state":"North Carolina","cost_mult":0.85,"region":"South"},
    "Cary":{"slug":"cary","state":"North Carolina","cost_mult":1.00,"region":"South"},
    # Georgia
    "Augusta":{"slug":"augusta","state":"Georgia","cost_mult":0.85,"region":"South"},
    "Columbus GA":{"slug":"columbus-ga","state":"Georgia","cost_mult":0.83,"region":"South"},
    "Macon":{"slug":"macon","state":"Georgia","cost_mult":0.82,"region":"South"},
    "Savannah":{"slug":"savannah","state":"Georgia","cost_mult":0.90,"region":"South"},
    # Virginia
    "Virginia Beach":{"slug":"virginia-beach","state":"Virginia","cost_mult":1.05,"region":"South"},
    "Norfolk":{"slug":"norfolk","state":"Virginia","cost_mult":1.02,"region":"South"},
    "Chesapeake":{"slug":"chesapeake","state":"Virginia","cost_mult":1.03,"region":"South"},
    "Richmond":{"slug":"richmond","state":"Virginia","cost_mult":1.00,"region":"South"},
    "Newport News":{"slug":"newport-news","state":"Virginia","cost_mult":0.98,"region":"South"},
    "Alexandria":{"slug":"alexandria","state":"Virginia","cost_mult":1.25,"region":"Northeast"},
    "Arlington VA":{"slug":"arlington-va","state":"Virginia","cost_mult":1.28,"region":"Northeast"},
    # Washington
    "Spokane":{"slug":"spokane","state":"Washington","cost_mult":1.00,"region":"West"},
    "Tacoma":{"slug":"tacoma","state":"Washington","cost_mult":1.15,"region":"West"},
    "Bellevue":{"slug":"bellevue","state":"Washington","cost_mult":1.38,"region":"West"},
    "Kent":{"slug":"kent","state":"Washington","cost_mult":1.12,"region":"West"},
    # Arizona
    "Chandler":{"slug":"chandler","state":"Arizona","cost_mult":0.97,"region":"South"},
    "Scottsdale":{"slug":"scottsdale","state":"Arizona","cost_mult":1.08,"region":"South"},
    "Gilbert":{"slug":"gilbert","state":"Arizona","cost_mult":0.97,"region":"South"},
    "Tempe":{"slug":"tempe","state":"Arizona","cost_mult":0.97,"region":"South"},
    "Peoria AZ":{"slug":"peoria-az","state":"Arizona","cost_mult":0.95,"region":"South"},
    "Surprise":{"slug":"surprise","state":"Arizona","cost_mult":0.93,"region":"South"},
    "Glendale AZ":{"slug":"glendale-az","state":"Arizona","cost_mult":0.93,"region":"South"},
    "Yuma":{"slug":"yuma","state":"Arizona","cost_mult":0.82,"region":"South"},
    "Flagstaff":{"slug":"flagstaff","state":"Arizona","cost_mult":0.97,"region":"Mountain"},
    # Colorado
    "Aurora CO":{"slug":"aurora-co","state":"Colorado","cost_mult":1.03,"region":"Mountain"},
    "Fort Collins":{"slug":"fort-collins","state":"Colorado","cost_mult":1.05,"region":"Mountain"},
    "Lakewood":{"slug":"lakewood","state":"Colorado","cost_mult":1.05,"region":"Mountain"},
    "Thornton":{"slug":"thornton","state":"Colorado","cost_mult":1.02,"region":"Mountain"},
    "Pueblo":{"slug":"pueblo","state":"Colorado","cost_mult":0.88,"region":"Mountain"},
    "Westminster CO":{"slug":"westminster-co","state":"Colorado","cost_mult":1.03,"region":"Mountain"},
    # Tennessee
    "Knoxville":{"slug":"knoxville","state":"Tennessee","cost_mult":0.87,"region":"South"},
    "Chattanooga":{"slug":"chattanooga","state":"Tennessee","cost_mult":0.87,"region":"South"},
    "Clarksville":{"slug":"clarksville","state":"Tennessee","cost_mult":0.85,"region":"South"},
    "Murfreesboro":{"slug":"murfreesboro","state":"Tennessee","cost_mult":0.90,"region":"South"},
    # Indiana
    "Fort Wayne":{"slug":"fort-wayne","state":"Indiana","cost_mult":0.85,"region":"Midwest"},
    "Evansville":{"slug":"evansville","state":"Indiana","cost_mult":0.83,"region":"Midwest"},
    "South Bend":{"slug":"south-bend","state":"Indiana","cost_mult":0.85,"region":"Midwest"},
    # Missouri
    "Kansas City":{"slug":"kansas-city","state":"Missouri","cost_mult":0.92,"region":"Midwest"},
    "Springfield MO":{"slug":"springfield-mo","state":"Missouri","cost_mult":0.83,"region":"Midwest"},
    "Columbia MO":{"slug":"columbia-mo","state":"Missouri","cost_mult":0.87,"region":"Midwest"},
    # Kansas
    "Wichita":{"slug":"wichita","state":"Kansas","cost_mult":0.85,"region":"Midwest"},
    "Overland Park":{"slug":"overland-park","state":"Kansas","cost_mult":0.93,"region":"Midwest"},
    "Topeka":{"slug":"topeka","state":"Kansas","cost_mult":0.82,"region":"Midwest"},
    # Nevada
    "Reno":{"slug":"reno","state":"Nevada","cost_mult":1.03,"region":"West"},
    "Henderson":{"slug":"henderson","state":"Nevada","cost_mult":1.00,"region":"West"},
    "North Las Vegas":{"slug":"north-las-vegas","state":"Nevada","cost_mult":0.97,"region":"West"},
    # Utah
    "Salt Lake City":{"slug":"salt-lake-city","state":"Utah","cost_mult":1.05,"region":"Mountain"},
    "West Valley City":{"slug":"west-valley-city","state":"Utah","cost_mult":1.00,"region":"Mountain"},
    "Provo":{"slug":"provo","state":"Utah","cost_mult":0.98,"region":"Mountain"},
    "Ogden":{"slug":"ogden","state":"Utah","cost_mult":0.97,"region":"Mountain"},
    # New Mexico
    "Las Cruces":{"slug":"las-cruces","state":"New Mexico","cost_mult":0.83,"region":"Mountain"},
    "Rio Rancho":{"slug":"rio-rancho","state":"New Mexico","cost_mult":0.85,"region":"Mountain"},
    # Oregon
    "Eugene":{"slug":"eugene","state":"Oregon","cost_mult":1.05,"region":"West"},
    "Salem":{"slug":"salem","state":"Oregon","cost_mult":1.00,"region":"West"},
    "Gresham":{"slug":"gresham","state":"Oregon","cost_mult":1.10,"region":"West"},
    "Hillsboro":{"slug":"hillsboro","state":"Oregon","cost_mult":1.12,"region":"West"},
    # Minnesota
    "St. Paul":{"slug":"st-paul","state":"Minnesota","cost_mult":1.05,"region":"Midwest"},
    "Rochester MN":{"slug":"rochester-mn","state":"Minnesota","cost_mult":1.00,"region":"Midwest"},
    # Iowa
    "Des Moines":{"slug":"des-moines","state":"Iowa","cost_mult":0.88,"region":"Midwest"},
    "Cedar Rapids":{"slug":"cedar-rapids","state":"Iowa","cost_mult":0.85,"region":"Midwest"},
    # Wisconsin
    "Madison":{"slug":"madison","state":"Wisconsin","cost_mult":1.00,"region":"Midwest"},
    "Green Bay":{"slug":"green-bay","state":"Wisconsin","cost_mult":0.88,"region":"Midwest"},
    "Kenosha":{"slug":"kenosha","state":"Wisconsin","cost_mult":0.90,"region":"Midwest"},
    # Kentucky
    "Lexington":{"slug":"lexington","state":"Kentucky","cost_mult":0.90,"region":"South"},
    "Bowling Green":{"slug":"bowling-green","state":"Kentucky","cost_mult":0.83,"region":"South"},
    # South Carolina
    "Columbia SC":{"slug":"columbia-sc","state":"South Carolina","cost_mult":0.87,"region":"South"},
    "Charleston":{"slug":"charleston","state":"South Carolina","cost_mult":0.97,"region":"South"},
    "North Charleston":{"slug":"north-charleston","state":"South Carolina","cost_mult":0.90,"region":"South"},
    "Greenville SC":{"slug":"greenville-sc","state":"South Carolina","cost_mult":0.90,"region":"South"},
    # Louisiana
    "Baton Rouge":{"slug":"baton-rouge","state":"Louisiana","cost_mult":0.87,"region":"South"},
    "Shreveport":{"slug":"shreveport","state":"Louisiana","cost_mult":0.82,"region":"South"},
    "Lafayette LA":{"slug":"lafayette-la","state":"Louisiana","cost_mult":0.85,"region":"South"},
    "Lake Charles":{"slug":"lake-charles","state":"Louisiana","cost_mult":0.85,"region":"South"},
    # Alabama
    "Birmingham":{"slug":"birmingham","state":"Alabama","cost_mult":0.83,"region":"South"},
    "Montgomery":{"slug":"montgomery","state":"Alabama","cost_mult":0.80,"region":"South"},
    "Huntsville":{"slug":"huntsville","state":"Alabama","cost_mult":0.85,"region":"South"},
    "Mobile":{"slug":"mobile","state":"Alabama","cost_mult":0.82,"region":"South"},
    # Mississippi
    "Jackson MS":{"slug":"jackson-ms","state":"Mississippi","cost_mult":0.78,"region":"South"},
    # Arkansas
    "Little Rock":{"slug":"little-rock","state":"Arkansas","cost_mult":0.80,"region":"South"},
    "Fort Smith":{"slug":"fort-smith","state":"Arkansas","cost_mult":0.78,"region":"South"},
    # Connecticut
    "Bridgeport":{"slug":"bridgeport","state":"Connecticut","cost_mult":1.18,"region":"Northeast"},
    "New Haven":{"slug":"new-haven","state":"Connecticut","cost_mult":1.15,"region":"Northeast"},
    "Hartford":{"slug":"hartford","state":"Connecticut","cost_mult":1.12,"region":"Northeast"},
    "Stamford":{"slug":"stamford","state":"Connecticut","cost_mult":1.28,"region":"Northeast"},
    # Other states
    "Anchorage":{"slug":"anchorage","state":"Alaska","cost_mult":1.35,"region":"West"},
    "Boise":{"slug":"boise","state":"Idaho","cost_mult":0.97,"region":"Mountain"},
    "Sioux Falls":{"slug":"sioux-falls","state":"South Dakota","cost_mult":0.85,"region":"Midwest"},
    "Fargo":{"slug":"fargo","state":"North Dakota","cost_mult":0.90,"region":"Midwest"},
    "Billings":{"slug":"billings","state":"Montana","cost_mult":0.90,"region":"Mountain"},
    "Casper":{"slug":"casper","state":"Wyoming","cost_mult":0.88,"region":"Mountain"},
    "Burlington VT":{"slug":"burlington-vt","state":"Vermont","cost_mult":1.08,"region":"Northeast"},
    "Manchester NH":{"slug":"manchester-nh","state":"New Hampshire","cost_mult":1.10,"region":"Northeast"},
    "Providence":{"slug":"providence","state":"Rhode Island","cost_mult":1.12,"region":"Northeast"},
    "Portland ME":{"slug":"portland-me","state":"Maine","cost_mult":1.05,"region":"Northeast"},
    "Newark":{"slug":"newark","state":"New Jersey","cost_mult":1.28,"region":"Northeast"},
    "Jersey City":{"slug":"jersey-city","state":"New Jersey","cost_mult":1.32,"region":"Northeast"},
    "Wilmington DE":{"slug":"wilmington-de","state":"Delaware","cost_mult":1.08,"region":"Northeast"},
    "Lexington KY":{"slug":"lexington-ky","state":"Kentucky","cost_mult":0.90,"region":"South"},
    "Bismarck":{"slug":"bismarck","state":"North Dakota","cost_mult":0.88,"region":"Midwest"},
    "Lincoln":{"slug":"lincoln","state":"Nebraska","cost_mult":0.88,"region":"Midwest"},
    "Rapid City":{"slug":"rapid-city","state":"South Dakota","cost_mult":0.83,"region":"Midwest"},
}

# ─── 5 NEW PROJECT TYPES ──────────────────────────────────────────────────────
PROJECTS = {
    "hvac-replacement": {
        "name": "HVAC Replacement",
        "slug": "hvac-replacement",
        "national_kw": "hvac replacement cost calculator",
        "national_vol": 6600,
        "title_tmpl":   "HVAC Replacement Cost Calculator {city_suffix}(2026)",
        "desc_tmpl":    "Free HVAC replacement cost calculator{city_prep}. Estimate AC, furnace, and heat pump replacement costs by home size — updated 2026 labor & equipment prices{city_in}.",
        "h1_tmpl":      "HVAC Replacement Cost Calculator{city_h1}",
        "intro_tmpl":   "HVAC replacement{city_intro} costs {cost_vs_avg} the national average. Home size, system type, and ductwork condition are the biggest cost factors. Get your estimate below.",
        "base_low": 4500,
        "base_mid": 8500,
        "base_high": 18000,
        "sqft_min": 500, "sqft_max": 5000, "sqft_default": 1800,
        "sqft_label": "Home square footage",
        "items": [
            {"label": "Central AC unit (3-ton, installed)", "base": 3800, "unit": "flat", "checked": True},
            {"label": "Gas furnace (80K BTU, installed)", "base": 2800, "unit": "flat", "checked": True},
            {"label": "Heat pump (replaces AC + furnace)", "base": 6200, "unit": "flat", "checked": False},
            {"label": "Air handler / indoor unit", "base": 1400, "unit": "flat", "checked": False},
            {"label": "Installation labor", "base": 1.20, "unit": "per sqft", "checked": True},
            {"label": "Ductwork cleaning & sealing", "base": 900, "unit": "flat", "checked": True},
            {"label": "Partial ductwork replacement", "base": 2200, "unit": "flat", "checked": False},
            {"label": "Full ductwork replacement", "base": 4500, "unit": "flat", "checked": False},
            {"label": "Smart thermostat (Nest/Ecobee)", "base": 280, "unit": "flat", "checked": True},
            {"label": "Permit & inspection fees", "base": 380, "unit": "flat", "checked": True},
        ],
        "faq": [
            ("How much does HVAC replacement cost{city_faq}",
             "HVAC replacement{city_in} typically costs ${low}–${high}. Most homeowners pay around ${mid} for a complete AC + furnace system in a standard home. Heat pump systems run ${low}–${high} installed."),
            ("How often does HVAC need to be replaced{city_faq}",
             "HVAC systems typically last 15–25 years. Central AC units last 15–20 years, furnaces 20–30 years, and heat pumps 15–20 years. In {city_or_us}, climate stress (hot summers or cold winters) can shorten lifespan."),
            ("What size HVAC do I need{city_faq}",
             "Most homes need approximately 1 ton of AC capacity per 400–600 sqft. Your 1,800 sqft home likely needs a 3-ton unit. A load calculation (Manual J) from a licensed HVAC contractor{city_in} gives the exact sizing."),
            ("Is it better to repair or replace HVAC{city_faq}",
             "If repair costs exceed 50% of replacement cost, or the unit is over 10 years old, replacement is usually better value. New systems use 30–50% less energy, which can save ${low}–${mid} over 10 years{city_in}."),
        ],
        "cost_table_rows": [
            ("AC only — small home (under 1,200 sqft)", "${low_sm}", "${mid_sm}"),
            ("Full system — average home (1,200–2,000 sqft)", "${low}", "${mid_low}"),
            ("Full system — large home (2,000–3,500 sqft)", "${mid_low}", "${mid}"),
            ("Premium system or full ductwork replacement", "${mid}", "${high}"),
        ],
    },

    "pool-installation": {
        "name": "Pool Installation",
        "slug": "pool-installation",
        "national_kw": "pool installation cost calculator",
        "national_vol": 5400,
        "title_tmpl":   "Pool Installation Cost Calculator {city_suffix}(2026)",
        "desc_tmpl":    "Free pool installation cost calculator{city_prep}. Estimate in-ground pool costs by size and type — concrete, vinyl, and fiberglass. Updated 2026 prices{city_in}.",
        "h1_tmpl":      "Pool Installation Cost Calculator{city_h1}",
        "intro_tmpl":   "In-ground pool installation{city_intro} costs {cost_vs_avg} the national average. Pool type, size, and add-ons like heating and decking are the main cost drivers. Estimate your project below.",
        "base_low": 28000,
        "base_mid": 52000,
        "base_high": 95000,
        "sqft_min": 150, "sqft_max": 800, "sqft_default": 400,
        "sqft_label": "Pool surface area (sq ft)",
        "items": [
            {"label": "Gunite/concrete pool shell", "base": 110, "unit": "per sqft", "checked": True},
            {"label": "Vinyl liner pool (lower cost)", "base": 65, "unit": "per sqft", "checked": False},
            {"label": "Fiberglass shell (installed)", "base": 85, "unit": "per sqft", "checked": False},
            {"label": "Excavation & site prep", "base": 8500, "unit": "flat", "checked": True},
            {"label": "Filtration system & pump", "base": 4200, "unit": "flat", "checked": True},
            {"label": "Pool heater (gas)", "base": 3800, "unit": "flat", "checked": False},
            {"label": "LED pool lighting", "base": 1800, "unit": "flat", "checked": False},
            {"label": "Pool deck (400 sqft concrete)", "base": 7500, "unit": "flat", "checked": True},
            {"label": "Safety fence (code required)", "base": 4800, "unit": "flat", "checked": True},
            {"label": "Permits & inspections", "base": 2000, "unit": "flat", "checked": True},
        ],
        "faq": [
            ("How much does pool installation cost{city_faq}",
             "Pool installation{city_in} costs ${low}–${high} for an in-ground pool. Vinyl liner pools start at ${low}; gunite/concrete pools typically run ${mid}–${high}. Above-ground pools are far cheaper ($2,000–$8,000)."),
            ("What type of pool is cheapest{city_faq}",
             "Vinyl liner pools are the most affordable in-ground option{city_in}, starting around ${low_sm}. Fiberglass shells run ${mid_sm}–${mid_low} installed. Gunite (concrete) is the most expensive at ${mid}–${high} but most customizable."),
            ("How long does pool installation take{city_faq}",
             "Vinyl and fiberglass pool installations take 3–6 weeks. Gunite pools take 8–12 weeks due to the concrete curing process. Permits can add 2–4 weeks depending on {city_or_us} building department."),
            ("Does a pool add home value{city_faq}",
             "A pool adds 5–8% to home value on average. In {city_or_us}'s market, the ROI varies — pools are more valuable in warm climates with longer swimming seasons. Consult a local realtor before investing."),
        ],
        "cost_table_rows": [
            ("Small plunge pool (150–250 sqft)", "${low_sm}", "${mid_sm}"),
            ("Standard vinyl pool (300–400 sqft)", "${low}", "${mid_low}"),
            ("Gunite pool — average size (350–500 sqft)", "${mid_low}", "${mid}"),
            ("Large gunite + heater + deck package", "${mid}", "${high}"),
        ],
    },

    "home-addition": {
        "name": "Home Addition",
        "slug": "home-addition",
        "national_kw": "home addition cost calculator",
        "national_vol": 4400,
        "title_tmpl":   "Home Addition Cost Calculator {city_suffix}(2026)",
        "desc_tmpl":    "Free home addition cost calculator{city_prep}. Estimate room addition costs per square foot — bedroom, bathroom, sunroom, garage. Updated 2026 prices{city_in}.",
        "h1_tmpl":      "Home Addition Cost Calculator{city_h1}",
        "intro_tmpl":   "Home addition costs{city_intro} run {cost_vs_avg} the national average. Square footage, foundation type, and whether you're adding a bathroom or kitchen are the biggest cost drivers in the {region} region.",
        "base_low": 25000,
        "base_mid": 65000,
        "base_high": 150000,
        "sqft_min": 100, "sqft_max": 1000, "sqft_default": 300,
        "sqft_label": "Addition square footage",
        "items": [
            {"label": "Foundation & concrete slab", "base": 14, "unit": "per sqft", "checked": True},
            {"label": "Framing & structural sheathing", "base": 20, "unit": "per sqft", "checked": True},
            {"label": "Roofing (match existing)", "base": 9, "unit": "per sqft", "checked": True},
            {"label": "Exterior siding & trim", "base": 7, "unit": "per sqft", "checked": True},
            {"label": "Insulation (walls + ceiling)", "base": 3.50, "unit": "per sqft", "checked": True},
            {"label": "Drywall, tape & paint", "base": 5.50, "unit": "per sqft", "checked": True},
            {"label": "Flooring (hardwood/LVP)", "base": 7, "unit": "per sqft", "checked": True},
            {"label": "Windows & exterior door(s)", "base": 6500, "unit": "flat", "checked": True},
            {"label": "Electrical rough & finish", "base": 5200, "unit": "flat", "checked": False},
            {"label": "Plumbing (for bathroom/kitchen)", "base": 8500, "unit": "flat", "checked": False},
        ],
        "faq": [
            ("How much does a home addition cost{city_faq}",
             "Home additions{city_in} cost ${low}–${high} depending on size and scope. A simple bedroom addition (200–300 sqft) runs ${low}–${mid_low}. A master suite or in-law addition with a bathroom runs ${mid}–${high}."),
            ("What is the cost per square foot for a home addition{city_faq}",
             "Home additions{city_in} cost $150–$400 per square foot fully finished. The {region} region averages {cost_vs_avg} national rates due to local labor market. Basic additions run ${labor_low}/sqft; luxury finishes hit ${labor_high}/sqft+."),
            ("How long does a home addition take{city_faq}",
             "A standard bedroom addition (200–400 sqft) takes 2–4 months from permit to completion{city_in}. Additions requiring new plumbing or HVAC take 3–6 months. Permitting adds 4–8 weeks upfront."),
            ("Is a home addition worth it vs. moving{city_faq}",
             "In {city_or_us}, home additions often cost less than selling and buying a larger home (especially with closing costs and moving expenses). A ${mid} addition can add ${mid_low}–${mid} in home value while keeping your current location."),
        ],
        "cost_table_rows": [
            ("Simple room bump-out (100–200 sqft)", "${low_sm}", "${mid_sm}"),
            ("Standard bedroom addition (200–350 sqft)", "${low}", "${mid_low}"),
            ("Master suite with bathroom (350–500 sqft)", "${mid_low}", "${mid}"),
            ("Full in-law suite or major addition (600–1,000 sqft)", "${mid}", "${high}"),
        ],
    },

    "landscaping": {
        "name": "Landscaping",
        "slug": "landscaping",
        "national_kw": "landscaping cost calculator",
        "national_vol": 1600,
        "title_tmpl":   "Landscaping Cost Calculator {city_suffix}(2026)",
        "desc_tmpl":    "Free landscaping cost calculator{city_prep}. Estimate lawn, sod, irrigation, plants, and hardscape costs for your yard — updated 2026 prices{city_in}.",
        "h1_tmpl":      "Landscaping Cost Calculator{city_h1}",
        "intro_tmpl":   "Landscaping costs{city_intro} run {cost_vs_avg} the national average. Yard size, plant selection, and hardscape elements like retaining walls and irrigation are the main cost drivers.",
        "base_low": 2500,
        "base_mid": 11000,
        "base_high": 32000,
        "sqft_min": 500, "sqft_max": 5000, "sqft_default": 1500,
        "sqft_label": "Yard area (sq ft)",
        "items": [
            {"label": "Sod installation (lawn)", "base": 1.30, "unit": "per sqft", "checked": True},
            {"label": "Lawn grading & prep work", "base": 0.55, "unit": "per sqft", "checked": True},
            {"label": "Mulch application (3\" depth)", "base": 0.40, "unit": "per sqft", "checked": False},
            {"label": "Decorative shrubs & plants", "base": 3800, "unit": "flat", "checked": False},
            {"label": "Ornamental trees (3-tree pkg)", "base": 2500, "unit": "flat", "checked": False},
            {"label": "Concrete edging / borders", "base": 2.80, "unit": "per sqft", "checked": False},
            {"label": "In-ground sprinkler system", "base": 5200, "unit": "flat", "checked": False},
            {"label": "Retaining wall (50 linear ft)", "base": 6500, "unit": "flat", "checked": False},
            {"label": "French drain / drainage system", "base": 3200, "unit": "flat", "checked": False},
            {"label": "Paver walkway (150 sqft)", "base": 3800, "unit": "flat", "checked": False},
        ],
        "faq": [
            ("How much does landscaping cost{city_faq}",
             "Basic landscaping{city_in} costs ${low}–${mid_low} for lawn, mulch, and basic plantings. Full yard makeovers with irrigation, trees, and hardscape run ${mid}–${high}. Most homeowners spend around ${mid} for a complete front + back yard refresh."),
            ("How much does sod cost per square foot{city_faq}",
             "Sod installation{city_in} costs $1.00–$2.50 per square foot installed, including grading and prep. For a 1,500 sqft lawn, expect $1,500–$3,750. Lawn seeding is cheaper ($0.25–$0.60/sqft) but takes longer to establish."),
            ("How long does landscaping take{city_faq}",
             "Basic lawn and planting work takes 1–3 days. Full yard makeovers with hardscape, irrigation, and grading typically take 1–3 weeks depending on scope. Permit-required retaining walls add 2–4 weeks for approval."),
            ("What landscaping adds the most home value{city_faq}",
             "In {city_or_us}, front yard landscaping returns the highest ROI (up to 100% at resale). A well-landscaped yard can add $15,000–$30,000 to home value. Mature trees, clean lawns, and defined beds are most valued by buyers."),
        ],
        "cost_table_rows": [
            ("Basic lawn care (sod + grading, 1,000 sqft)", "${low}", "${mid_sm}"),
            ("Lawn + mulch + plants (1,500 sqft yard)", "${mid_sm}", "${mid_low}"),
            ("Full yard refresh (lawn, plants, edging, trees)", "${mid_low}", "${mid}"),
            ("Complete landscape (irrigation, hardscape, trees)", "${mid}", "${high}"),
        ],
    },

    "deck-installation": {
        "name": "Deck Installation",
        "slug": "deck-installation",
        "national_kw": "deck installation cost calculator",
        "national_vol": 1900,
        "title_tmpl":   "Deck Installation Cost Calculator {city_suffix}(2026)",
        "desc_tmpl":    "Free deck installation cost calculator{city_prep}. Estimate deck costs by size and material — pressure-treated wood, composite, cedar. Updated 2026 prices{city_in}.",
        "h1_tmpl":      "Deck Installation Cost Calculator{city_h1}",
        "intro_tmpl":   "Deck installation{city_intro} costs {cost_vs_avg} the national average. Deck size, material choice (wood vs. composite), and railing type are the biggest cost variables in the {region} region.",
        "base_low": 6000,
        "base_mid": 16000,
        "base_high": 42000,
        "sqft_min": 100, "sqft_max": 800, "sqft_default": 300,
        "sqft_label": "Deck square footage",
        "items": [
            {"label": "Pressure-treated wood decking", "base": 18, "unit": "per sqft", "checked": True},
            {"label": "Composite decking (Trex/TimberTech)", "base": 34, "unit": "per sqft", "checked": False},
            {"label": "Cedar or redwood decking", "base": 28, "unit": "per sqft", "checked": False},
            {"label": "Deck framing & joists", "base": 9, "unit": "per sqft", "checked": True},
            {"label": "Concrete footings & posts", "base": 5, "unit": "per sqft", "checked": True},
            {"label": "Wood railing (per linear ft)", "base": 55, "unit": "per sqft", "checked": False},
            {"label": "Composite/aluminum railing", "base": 85, "unit": "per sqft", "checked": False},
            {"label": "Stairs (per stair, 4 steps)", "base": 800, "unit": "flat", "checked": True},
            {"label": "Permit & engineering", "base": 900, "unit": "flat", "checked": True},
            {"label": "Deck staining/sealing (1st coat)", "base": 1.80, "unit": "per sqft", "checked": False},
        ],
        "faq": [
            ("How much does deck installation cost{city_faq}",
             "Deck installation{city_in} costs ${low}–${high}. A basic 10x20ft pressure-treated wood deck runs ${low}–${mid_low}. A 16x20ft composite deck with railing and stairs runs ${mid}–${high}. Complex multi-level decks can exceed ${high}."),
            ("Is composite decking worth the extra cost{city_faq}",
             "Composite decking costs 2–3x more upfront than pressure-treated wood but lasts 25–30 years with minimal maintenance vs. 10–15 years for wood that needs regular staining. In {city_or_us}, composite typically pays off in 7–10 years in saved maintenance."),
            ("Do I need a permit for a deck{city_faq}",
             "Most jurisdictions require a permit for decks over 30 inches above grade or over 200 sqft. In {city_or_us}, budget $300–$1,000 for permits and allow 2–6 weeks for approval. Your contractor should handle this."),
            ("How long does deck installation take{city_faq}",
             "A standard 300–400 sqft deck takes 3–7 days to build once materials arrive. Composite decking takes slightly longer to install than wood. Multi-level or custom decks take 1–3 weeks. Permit approval adds 2–6 weeks upfront."),
        ],
        "cost_table_rows": [
            ("Small wood deck (100–200 sqft)", "${low_sm}", "${mid_sm}"),
            ("Standard wood deck (200–350 sqft)", "${low}", "${mid_low}"),
            ("Composite deck (200–350 sqft)", "${mid_low}", "${mid}"),
            ("Large deck with railing & stairs (400–600 sqft)", "${mid}", "${high}"),
        ],
    },
}

# ─── HELPERS (same as generate_new_calculators.py) ───────────────────────────
STAR_SVG = '<svg viewBox="0 0 24 24" fill="white" width="17" height="17"><path d="M12 2l2.9 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l7.1-1.01L12 2z"/></svg>'

def fmt(n): return f"{round(n):,}"

def cost_vs_avg(m):
    if m >= 1.20: return "significantly higher than"
    if m >= 1.08: return "higher than"
    if m >= 0.97: return "close to"
    if m >= 0.88: return "slightly below"
    return "notably below"

def labor_range(m):
    return round(45 * m), round(90 * m)

def make_tokens(city_name, city_data, proj):
    m = city_data["cost_mult"] if city_data else 1.0
    state = city_data.get("state", "US")
    region = city_data.get("region", "national")
    low  = round(proj["base_low"]  * m / 200) * 200
    mid  = round(proj["base_mid"]  * m / 200) * 200
    high = round(proj["base_high"] * m / 200) * 200
    low_sm   = round(low  * 0.35 / 100) * 100
    mid_sm   = round(low  * 0.65 / 100) * 100
    low_high = round((low + mid) / 2 / 200) * 200
    mid_low  = round((low_high + mid) / 2 / 200) * 200
    lab_low, lab_high = labor_range(m)

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
        if unit in ("per sqft", "per ft", "per lf"):
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
    city_slug = city_data.get("slug", "")
    canon_slug = f"{proj['slug']}-cost-{city_slug}" if is_city else f"{proj['slug']}-cost-calculator"
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
      <p><strong>Material costs:</strong> Material prices in the {tok['region']} region are {cost_vs_avg(m)} national average due to local supply, transportation costs, and market demand.</p>
      <p><strong>Project complexity:</strong> Site conditions, permitting requirements, and non-standard layouts can add 15–30% to total project cost.</p>

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


# ─── MAIN ─────────────────────────────────────────────────────────────────────
def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    count = 0

    for proj_key, proj in PROJECTS.items():
        print(f"\n→ {proj['name']} ({len(ALL_CITIES)} cities + national)...")

        # National calculator
        folder = os.path.join(base_dir, f"{proj['slug']}-cost-calculator")
        os.makedirs(folder, exist_ok=True)
        html = generate_page(None, {"cost_mult": 1.0, "state": "US", "region": "national", "slug": ""}, proj_key, proj)
        with open(os.path.join(folder, "index.html"), "w", encoding="utf-8") as f:
            f.write(html)
        count += 1

        # City pages
        for city_name, city_data in ALL_CITIES.items():
            slug = f"{proj['slug']}-cost-{city_data['slug']}"
            folder = os.path.join(base_dir, slug)
            os.makedirs(folder, exist_ok=True)
            html = generate_page(city_name, city_data, proj_key, proj)
            with open(os.path.join(folder, "index.html"), "w", encoding="utf-8") as f:
                f.write(html)
            count += 1

        print(f"  ✓ {len(ALL_CITIES)+1} pages")

    print(f"\nTotal: {count} pages generated in tools/")
    return count

if __name__ == "__main__":
    main()
