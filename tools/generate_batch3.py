#!/usr/bin/env python3
"""Generate all 14 project types for ~250 new US cities (batch 3)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import generate_new_calculators as calc
import generate_new_projects2 as proj2

TOOLS_DIR = os.path.dirname(os.path.abspath(__file__))

NEW_CITIES = {
    # ── TEXAS (major missing metros) ──────────────────────────────────────────
    "Tulsa":            {"slug":"tulsa",            "state":"Oklahoma",          "cost_mult":0.87,"region":"South"},
    "Waco":             {"slug":"waco",             "state":"Texas",             "cost_mult":0.85,"region":"South"},
    "Denton":           {"slug":"denton",           "state":"Texas",             "cost_mult":0.95,"region":"South"},
    "Carrollton":       {"slug":"carrollton",       "state":"Texas",             "cost_mult":0.95,"region":"South"},
    "Lewisville":       {"slug":"lewisville",       "state":"Texas",             "cost_mult":0.93,"region":"South"},
    "Sugar Land":       {"slug":"sugar-land",       "state":"Texas",             "cost_mult":0.97,"region":"South"},
    "Round Rock":       {"slug":"round-rock",       "state":"Texas",             "cost_mult":0.97,"region":"South"},
    "Pearland":         {"slug":"pearland",         "state":"Texas",             "cost_mult":0.93,"region":"South"},
    "Allen TX":         {"slug":"allen-tx",         "state":"Texas",             "cost_mult":0.97,"region":"South"},
    "Richardson":       {"slug":"richardson",       "state":"Texas",             "cost_mult":0.96,"region":"South"},
    "Midland":          {"slug":"midland",          "state":"Texas",             "cost_mult":0.87,"region":"South"},
    "Odessa":           {"slug":"odessa",           "state":"Texas",             "cost_mult":0.85,"region":"South"},
    "Beaumont":         {"slug":"beaumont",         "state":"Texas",             "cost_mult":0.85,"region":"South"},
    "Wichita Falls":    {"slug":"wichita-falls",    "state":"Texas",             "cost_mult":0.82,"region":"South"},
    "Abilene":          {"slug":"abilene",          "state":"Texas",             "cost_mult":0.82,"region":"South"},
    "College Station":  {"slug":"college-station",  "state":"Texas",             "cost_mult":0.87,"region":"South"},
    "McAllen":          {"slug":"mcallen",          "state":"Texas",             "cost_mult":0.80,"region":"South"},
    "New Braunfels":    {"slug":"new-braunfels",    "state":"Texas",             "cost_mult":0.92,"region":"South"},
    "Tyler":            {"slug":"tyler",            "state":"Texas",             "cost_mult":0.83,"region":"South"},
    "Conroe":           {"slug":"conroe",           "state":"Texas",             "cost_mult":0.90,"region":"South"},
    "League City":      {"slug":"league-city",      "state":"Texas",             "cost_mult":0.93,"region":"South"},
    # ── FLORIDA ───────────────────────────────────────────────────────────────
    "West Palm Beach":  {"slug":"west-palm-beach",  "state":"Florida",           "cost_mult":1.10,"region":"South"},
    "Boca Raton":       {"slug":"boca-raton",       "state":"Florida",           "cost_mult":1.15,"region":"South"},
    "Lakeland":         {"slug":"lakeland",         "state":"Florida",           "cost_mult":0.95,"region":"South"},
    "Palm Bay":         {"slug":"palm-bay",         "state":"Florida",           "cost_mult":0.93,"region":"South"},
    "Pompano Beach":    {"slug":"pompano-beach",    "state":"Florida",           "cost_mult":1.05,"region":"South"},
    "Davie":            {"slug":"davie",            "state":"Florida",           "cost_mult":1.05,"region":"South"},
    "Deltona":          {"slug":"deltona",          "state":"Florida",           "cost_mult":0.92,"region":"South"},
    "Daytona Beach":    {"slug":"daytona-beach",    "state":"Florida",           "cost_mult":0.90,"region":"South"},
    "Melbourne FL":     {"slug":"melbourne-fl",     "state":"Florida",           "cost_mult":0.93,"region":"South"},
    "Palm Coast":       {"slug":"palm-coast",       "state":"Florida",           "cost_mult":0.92,"region":"South"},
    "Sunrise FL":       {"slug":"sunrise-fl",       "state":"Florida",           "cost_mult":1.03,"region":"South"},
    "Coral Springs":    {"slug":"coral-springs",    "state":"Florida",           "cost_mult":1.05,"region":"South"},
    "Kissimmee":        {"slug":"kissimmee",        "state":"Florida",           "cost_mult":0.97,"region":"South"},
    # ── CALIFORNIA ────────────────────────────────────────────────────────────
    "Palmdale":         {"slug":"palmdale",         "state":"California",        "cost_mult":1.10,"region":"West"},
    "Lancaster CA":     {"slug":"lancaster-ca",     "state":"California",        "cost_mult":1.05,"region":"West"},
    "Sunnyvale":        {"slug":"sunnyvale",        "state":"California",        "cost_mult":1.45,"region":"West"},
    "Santa Rosa":       {"slug":"santa-rosa",       "state":"California",        "cost_mult":1.25,"region":"West"},
    "Hayward":          {"slug":"hayward",          "state":"California",        "cost_mult":1.35,"region":"West"},
    "Pasadena CA":      {"slug":"pasadena-ca",      "state":"California",        "cost_mult":1.28,"region":"West"},
    "Thousand Oaks":    {"slug":"thousand-oaks",    "state":"California",        "cost_mult":1.25,"region":"West"},
    "Simi Valley":      {"slug":"simi-valley",      "state":"California",        "cost_mult":1.20,"region":"West"},
    "Corona":           {"slug":"corona",           "state":"California",        "cost_mult":1.15,"region":"West"},
    "Murrieta":         {"slug":"murrieta",         "state":"California",        "cost_mult":1.10,"region":"West"},
    "Temecula":         {"slug":"temecula",         "state":"California",        "cost_mult":1.10,"region":"West"},
    "Pomona":           {"slug":"pomona",           "state":"California",        "cost_mult":1.15,"region":"West"},
    "Escondido":        {"slug":"escondido",        "state":"California",        "cost_mult":1.20,"region":"West"},
    "Visalia":          {"slug":"visalia",          "state":"California",        "cost_mult":0.95,"region":"West"},
    "Roseville CA":     {"slug":"roseville-ca",     "state":"California",        "cost_mult":1.12,"region":"West"},
    "Concord CA":       {"slug":"concord-ca",       "state":"California",        "cost_mult":1.32,"region":"West"},
    "Salinas":          {"slug":"salinas",          "state":"California",        "cost_mult":1.15,"region":"West"},
    "Elk Grove":        {"slug":"elk-grove",        "state":"California",        "cost_mult":1.10,"region":"West"},
    "Rancho Cucamonga": {"slug":"rancho-cucamonga", "state":"California",        "cost_mult":1.15,"region":"West"},
    "Ontario CA":       {"slug":"ontario-ca",       "state":"California",        "cost_mult":1.12,"region":"West"},
    "El Monte":         {"slug":"el-monte",         "state":"California",        "cost_mult":1.18,"region":"West"},
    "Fullerton":        {"slug":"fullerton",        "state":"California",        "cost_mult":1.22,"region":"West"},
    "Garden Grove":     {"slug":"garden-grove",     "state":"California",        "cost_mult":1.20,"region":"West"},
    "Oceanside":        {"slug":"oceanside",        "state":"California",        "cost_mult":1.22,"region":"West"},
    "Salinas CA":       None,  # duplicate slug, skip
    "Vallejo":          {"slug":"vallejo",          "state":"California",        "cost_mult":1.20,"region":"West"},
    "Victorville":      {"slug":"victorville",      "state":"California",        "cost_mult":1.05,"region":"West"},
    # ── WASHINGTON ────────────────────────────────────────────────────────────
    "Renton":           {"slug":"renton",           "state":"Washington",        "cost_mult":1.28,"region":"West"},
    "Federal Way":      {"slug":"federal-way",      "state":"Washington",        "cost_mult":1.18,"region":"West"},
    "Kirkland":         {"slug":"kirkland",         "state":"Washington",        "cost_mult":1.38,"region":"West"},
    "Everett":          {"slug":"everett",          "state":"Washington",        "cost_mult":1.20,"region":"West"},
    "Bellingham":       {"slug":"bellingham",       "state":"Washington",        "cost_mult":1.15,"region":"West"},
    "Redmond WA":       {"slug":"redmond-wa",       "state":"Washington",        "cost_mult":1.42,"region":"West"},
    # ── COLORADO ──────────────────────────────────────────────────────────────
    "Greeley":          {"slug":"greeley",          "state":"Colorado",          "cost_mult":0.97,"region":"Mountain"},
    "Arvada":           {"slug":"arvada",           "state":"Colorado",          "cost_mult":1.05,"region":"Mountain"},
    "Centennial":       {"slug":"centennial",       "state":"Colorado",          "cost_mult":1.05,"region":"Mountain"},
    "Longmont":         {"slug":"longmont",         "state":"Colorado",          "cost_mult":1.00,"region":"Mountain"},
    "Loveland CO":      {"slug":"loveland-co",      "state":"Colorado",          "cost_mult":1.02,"region":"Mountain"},
    "Castle Rock":      {"slug":"castle-rock",      "state":"Colorado",          "cost_mult":1.08,"region":"Mountain"},
    # ── GEORGIA ───────────────────────────────────────────────────────────────
    "Athens GA":        {"slug":"athens-ga",        "state":"Georgia",           "cost_mult":0.90,"region":"South"},
    "Sandy Springs":    {"slug":"sandy-springs",    "state":"Georgia",           "cost_mult":1.02,"region":"South"},
    "Roswell GA":       {"slug":"roswell-ga",       "state":"Georgia",           "cost_mult":1.00,"region":"South"},
    "Warner Robins":    {"slug":"warner-robins",    "state":"Georgia",           "cost_mult":0.83,"region":"South"},
    "Gainesville GA":   {"slug":"gainesville-ga",   "state":"Georgia",           "cost_mult":0.88,"region":"South"},
    "Peachtree City":   {"slug":"peachtree-city",   "state":"Georgia",           "cost_mult":0.95,"region":"South"},
    "Albany GA":        {"slug":"albany-ga",        "state":"Georgia",           "cost_mult":0.80,"region":"South"},
    "Johns Creek":      {"slug":"johns-creek",      "state":"Georgia",           "cost_mult":1.05,"region":"South"},
    # ── NORTH CAROLINA ────────────────────────────────────────────────────────
    "Wilmington NC":    {"slug":"wilmington-nc",    "state":"North Carolina",    "cost_mult":0.97,"region":"South"},
    "High Point":       {"slug":"high-point",       "state":"North Carolina",    "cost_mult":0.87,"region":"South"},
    "Concord NC":       {"slug":"concord-nc",       "state":"North Carolina",    "cost_mult":0.95,"region":"South"},
    "Gastonia":         {"slug":"gastonia",         "state":"North Carolina",    "cost_mult":0.87,"region":"South"},
    "Chapel Hill":      {"slug":"chapel-hill",      "state":"North Carolina",    "cost_mult":1.05,"region":"South"},
    "Asheville":        {"slug":"asheville",        "state":"North Carolina",    "cost_mult":0.97,"region":"South"},
    "Huntersville":     {"slug":"huntersville",     "state":"North Carolina",    "cost_mult":0.97,"region":"South"},
    # ── VIRGINIA ──────────────────────────────────────────────────────────────
    "Hampton":          {"slug":"hampton",          "state":"Virginia",          "cost_mult":1.00,"region":"South"},
    "Roanoke":          {"slug":"roanoke",          "state":"Virginia",          "cost_mult":0.92,"region":"South"},
    "Fredericksburg":   {"slug":"fredericksburg",   "state":"Virginia",          "cost_mult":1.10,"region":"South"},
    "Charlottesville":  {"slug":"charlottesville",  "state":"Virginia",          "cost_mult":1.05,"region":"South"},
    "Manassas":         {"slug":"manassas",         "state":"Virginia",          "cost_mult":1.15,"region":"Northeast"},
    "Harrisonburg":     {"slug":"harrisonburg",     "state":"Virginia",          "cost_mult":0.90,"region":"South"},
    # ── OHIO ──────────────────────────────────────────────────────────────────
    "Canton":           {"slug":"canton",           "state":"Ohio",              "cost_mult":0.83,"region":"Midwest"},
    "Lorain":           {"slug":"lorain",           "state":"Ohio",              "cost_mult":0.83,"region":"Midwest"},
    "Parma":            {"slug":"parma",            "state":"Ohio",              "cost_mult":0.87,"region":"Midwest"},
    "Youngstown":       {"slug":"youngstown",       "state":"Ohio",              "cost_mult":0.80,"region":"Midwest"},
    "Hamilton OH":      {"slug":"hamilton-oh",      "state":"Ohio",              "cost_mult":0.85,"region":"Midwest"},
    "Cuyahoga Falls":   {"slug":"cuyahoga-falls",   "state":"Ohio",              "cost_mult":0.85,"region":"Midwest"},
    # ── MICHIGAN ──────────────────────────────────────────────────────────────
    "Dearborn":         {"slug":"dearborn",         "state":"Michigan",          "cost_mult":0.95,"region":"Midwest"},
    "Flint":            {"slug":"flint",            "state":"Michigan",          "cost_mult":0.82,"region":"Midwest"},
    "Kalamazoo":        {"slug":"kalamazoo",        "state":"Michigan",          "cost_mult":0.90,"region":"Midwest"},
    "Livonia":          {"slug":"livonia",          "state":"Michigan",          "cost_mult":0.97,"region":"Midwest"},
    "Saginaw":          {"slug":"saginaw",          "state":"Michigan",          "cost_mult":0.80,"region":"Midwest"},
    "Westland":         {"slug":"westland",         "state":"Michigan",          "cost_mult":0.92,"region":"Midwest"},
    "Troy MI":          {"slug":"troy-mi",          "state":"Michigan",          "cost_mult":1.00,"region":"Midwest"},
    # ── PENNSYLVANIA ──────────────────────────────────────────────────────────
    "Erie":             {"slug":"erie",             "state":"Pennsylvania",      "cost_mult":0.90,"region":"Northeast"},
    "Reading PA":       {"slug":"reading-pa",       "state":"Pennsylvania",      "cost_mult":0.95,"region":"Northeast"},
    "Scranton":         {"slug":"scranton",         "state":"Pennsylvania",      "cost_mult":0.92,"region":"Northeast"},
    "Lancaster PA":     {"slug":"lancaster-pa",     "state":"Pennsylvania",      "cost_mult":0.97,"region":"Northeast"},
    "York PA":          {"slug":"york-pa",          "state":"Pennsylvania",      "cost_mult":0.92,"region":"Northeast"},
    "Bethlehem PA":     {"slug":"bethlehem-pa",     "state":"Pennsylvania",      "cost_mult":1.00,"region":"Northeast"},
    # ── ILLINOIS ──────────────────────────────────────────────────────────────
    "Elgin":            {"slug":"elgin",            "state":"Illinois",          "cost_mult":1.05,"region":"Midwest"},
    "Waukegan":         {"slug":"waukegan",         "state":"Illinois",          "cost_mult":1.00,"region":"Midwest"},
    "Champaign":        {"slug":"champaign",        "state":"Illinois",          "cost_mult":0.90,"region":"Midwest"},
    "Cicero IL":        {"slug":"cicero-il",        "state":"Illinois",          "cost_mult":1.05,"region":"Midwest"},
    "Decatur IL":       {"slug":"decatur-il",       "state":"Illinois",          "cost_mult":0.83,"region":"Midwest"},
    "Evanston":         {"slug":"evanston",         "state":"Illinois",          "cost_mult":1.15,"region":"Midwest"},
    # ── MISSOURI ──────────────────────────────────────────────────────────────
    "Independence MO":  {"slug":"independence-mo",  "state":"Missouri",          "cost_mult":0.88,"region":"Midwest"},
    "Lee's Summit":     {"slug":"lees-summit",      "state":"Missouri",          "cost_mult":0.93,"region":"Midwest"},
    "St. Joseph MO":    {"slug":"st-joseph-mo",     "state":"Missouri",          "cost_mult":0.83,"region":"Midwest"},
    "St. Charles MO":   {"slug":"st-charles-mo",    "state":"Missouri",          "cost_mult":0.92,"region":"Midwest"},
    "O'Fallon MO":      {"slug":"ofallon-mo",       "state":"Missouri",          "cost_mult":0.93,"region":"Midwest"},
    # ── INDIANA ───────────────────────────────────────────────────────────────
    "Bloomington IN":   {"slug":"bloomington-in",   "state":"Indiana",           "cost_mult":0.88,"region":"Midwest"},
    "Carmel IN":        {"slug":"carmel-in",        "state":"Indiana",           "cost_mult":1.00,"region":"Midwest"},
    "Terre Haute":      {"slug":"terre-haute",      "state":"Indiana",           "cost_mult":0.83,"region":"Midwest"},
    "Muncie":           {"slug":"muncie",           "state":"Indiana",           "cost_mult":0.82,"region":"Midwest"},
    "Fishers":          {"slug":"fishers",          "state":"Indiana",           "cost_mult":0.97,"region":"Midwest"},
    # ── TENNESSEE ─────────────────────────────────────────────────────────────
    "Jackson TN":       {"slug":"jackson-tn",       "state":"Tennessee",         "cost_mult":0.83,"region":"South"},
    "Johnson City":     {"slug":"johnson-city",     "state":"Tennessee",         "cost_mult":0.83,"region":"South"},
    "Kingsport":        {"slug":"kingsport",        "state":"Tennessee",         "cost_mult":0.82,"region":"South"},
    "Smyrna TN":        {"slug":"smyrna-tn",        "state":"Tennessee",         "cost_mult":0.88,"region":"South"},
    "Franklin TN":      {"slug":"franklin-tn",      "state":"Tennessee",         "cost_mult":1.02,"region":"South"},
    # ── KENTUCKY ──────────────────────────────────────────────────────────────
    "Owensboro":        {"slug":"owensboro",        "state":"Kentucky",          "cost_mult":0.83,"region":"South"},
    "Covington KY":     {"slug":"covington-ky",     "state":"Kentucky",          "cost_mult":0.88,"region":"South"},
    "Elizabethtown":    {"slug":"elizabethtown",    "state":"Kentucky",          "cost_mult":0.82,"region":"South"},
    # ── SOUTH CAROLINA ────────────────────────────────────────────────────────
    "Rock Hill":        {"slug":"rock-hill",        "state":"South Carolina",    "cost_mult":0.90,"region":"South"},
    "Myrtle Beach":     {"slug":"myrtle-beach",     "state":"South Carolina",    "cost_mult":0.92,"region":"South"},
    "Summerville SC":   {"slug":"summerville-sc",   "state":"South Carolina",    "cost_mult":0.93,"region":"South"},
    "Florence SC":      {"slug":"florence-sc",      "state":"South Carolina",    "cost_mult":0.83,"region":"South"},
    "Spartanburg":      {"slug":"spartanburg",      "state":"South Carolina",    "cost_mult":0.87,"region":"South"},
    # ── ALABAMA ───────────────────────────────────────────────────────────────
    "Tuscaloosa":       {"slug":"tuscaloosa",       "state":"Alabama",           "cost_mult":0.83,"region":"South"},
    "Dothan":           {"slug":"dothan",           "state":"Alabama",           "cost_mult":0.80,"region":"South"},
    "Auburn AL":        {"slug":"auburn-al",        "state":"Alabama",           "cost_mult":0.85,"region":"South"},
    "Decatur AL":       {"slug":"decatur-al",       "state":"Alabama",           "cost_mult":0.80,"region":"South"},
    # ── MISSISSIPPI ───────────────────────────────────────────────────────────
    "Gulfport":         {"slug":"gulfport",         "state":"Mississippi",       "cost_mult":0.80,"region":"South"},
    "Hattiesburg":      {"slug":"hattiesburg",      "state":"Mississippi",       "cost_mult":0.78,"region":"South"},
    "Biloxi":           {"slug":"biloxi",           "state":"Mississippi",       "cost_mult":0.80,"region":"South"},
    "Southaven":        {"slug":"southaven",        "state":"Mississippi",       "cost_mult":0.82,"region":"South"},
    # ── ARKANSAS ──────────────────────────────────────────────────────────────
    "Fayetteville AR":  {"slug":"fayetteville-ar",  "state":"Arkansas",          "cost_mult":0.85,"region":"South"},
    "Springdale":       {"slug":"springdale",       "state":"Arkansas",          "cost_mult":0.83,"region":"South"},
    "Jonesboro":        {"slug":"jonesboro",        "state":"Arkansas",          "cost_mult":0.80,"region":"South"},
    "Conway AR":        {"slug":"conway-ar",        "state":"Arkansas",          "cost_mult":0.82,"region":"South"},
    # ── MARYLAND ──────────────────────────────────────────────────────────────
    "Annapolis":        {"slug":"annapolis",        "state":"Maryland",          "cost_mult":1.18,"region":"Northeast"},
    "Hagerstown":       {"slug":"hagerstown",       "state":"Maryland",          "cost_mult":1.00,"region":"Northeast"},
    "Bowie MD":         {"slug":"bowie-md",         "state":"Maryland",          "cost_mult":1.15,"region":"Northeast"},
    "Gaithersburg":     {"slug":"gaithersburg",     "state":"Maryland",          "cost_mult":1.20,"region":"Northeast"},
    "College Park MD":  {"slug":"college-park-md",  "state":"Maryland",          "cost_mult":1.15,"region":"Northeast"},
    # ── NEW JERSEY ────────────────────────────────────────────────────────────
    "Trenton":          {"slug":"trenton",          "state":"New Jersey",        "cost_mult":1.15,"region":"Northeast"},
    "Edison NJ":        {"slug":"edison-nj",        "state":"New Jersey",        "cost_mult":1.25,"region":"Northeast"},
    "Woodbridge NJ":    {"slug":"woodbridge-nj",    "state":"New Jersey",        "cost_mult":1.22,"region":"Northeast"},
    "Toms River":       {"slug":"toms-river",       "state":"New Jersey",        "cost_mult":1.18,"region":"Northeast"},
    "Clifton":          {"slug":"clifton",          "state":"New Jersey",        "cost_mult":1.22,"region":"Northeast"},
    # ── MASSACHUSETTS ─────────────────────────────────────────────────────────
    "Worcester":        {"slug":"worcester",        "state":"Massachusetts",     "cost_mult":1.20,"region":"Northeast"},
    "Springfield MA":   {"slug":"springfield-ma",   "state":"Massachusetts",     "cost_mult":1.10,"region":"Northeast"},
    "Lowell":           {"slug":"lowell",           "state":"Massachusetts",     "cost_mult":1.20,"region":"Northeast"},
    "Brockton":         {"slug":"brockton",         "state":"Massachusetts",     "cost_mult":1.18,"region":"Northeast"},
    "New Bedford":      {"slug":"new-bedford",      "state":"Massachusetts",     "cost_mult":1.12,"region":"Northeast"},
    "Quincy MA":        {"slug":"quincy-ma",        "state":"Massachusetts",     "cost_mult":1.28,"region":"Northeast"},
    "Lynn":             {"slug":"lynn",             "state":"Massachusetts",     "cost_mult":1.22,"region":"Northeast"},
    # ── CONNECTICUT ───────────────────────────────────────────────────────────
    "Waterbury":        {"slug":"waterbury",        "state":"Connecticut",       "cost_mult":1.10,"region":"Northeast"},
    "Norwalk CT":       {"slug":"norwalk-ct",       "state":"Connecticut",       "cost_mult":1.35,"region":"Northeast"},
    "Danbury":          {"slug":"danbury",          "state":"Connecticut",       "cost_mult":1.20,"region":"Northeast"},
    "Meriden":          {"slug":"meriden",          "state":"Connecticut",       "cost_mult":1.08,"region":"Northeast"},
    # ── NEW YORK ──────────────────────────────────────────────────────────────
    "Binghamton":       {"slug":"binghamton",       "state":"New York",          "cost_mult":0.93,"region":"Northeast"},
    "Utica":            {"slug":"utica",            "state":"New York",          "cost_mult":0.92,"region":"Northeast"},
    "Schenectady":      {"slug":"schenectady",      "state":"New York",          "cost_mult":1.00,"region":"Northeast"},
    "New Rochelle":     {"slug":"new-rochelle",     "state":"New York",          "cost_mult":1.32,"region":"Northeast"},
    "Mount Vernon NY":  {"slug":"mount-vernon-ny",  "state":"New York",          "cost_mult":1.30,"region":"Northeast"},
    # ── MINNESOTA ─────────────────────────────────────────────────────────────
    "Duluth":           {"slug":"duluth",           "state":"Minnesota",         "cost_mult":0.93,"region":"Midwest"},
    "Bloomington MN":   {"slug":"bloomington-mn",   "state":"Minnesota",         "cost_mult":1.05,"region":"Midwest"},
    "Brooklyn Park MN": {"slug":"brooklyn-park-mn", "state":"Minnesota",         "cost_mult":1.02,"region":"Midwest"},
    "Plymouth MN":      {"slug":"plymouth-mn",      "state":"Minnesota",         "cost_mult":1.08,"region":"Midwest"},
    "Coon Rapids":      {"slug":"coon-rapids",      "state":"Minnesota",         "cost_mult":1.00,"region":"Midwest"},
    "Maple Grove":      {"slug":"maple-grove",      "state":"Minnesota",         "cost_mult":1.05,"region":"Midwest"},
    # ── WISCONSIN ─────────────────────────────────────────────────────────────
    "Racine":           {"slug":"racine",           "state":"Wisconsin",         "cost_mult":0.92,"region":"Midwest"},
    "Appleton":         {"slug":"appleton",         "state":"Wisconsin",         "cost_mult":0.90,"region":"Midwest"},
    "Eau Claire":       {"slug":"eau-claire",       "state":"Wisconsin",         "cost_mult":0.88,"region":"Midwest"},
    "Oshkosh":          {"slug":"oshkosh",          "state":"Wisconsin",         "cost_mult":0.87,"region":"Midwest"},
    "Janesville":       {"slug":"janesville",       "state":"Wisconsin",         "cost_mult":0.88,"region":"Midwest"},
    "Waukesha":         {"slug":"waukesha",         "state":"Wisconsin",         "cost_mult":0.95,"region":"Midwest"},
    # ── IOWA ──────────────────────────────────────────────────────────────────
    "Davenport":        {"slug":"davenport",        "state":"Iowa",              "cost_mult":0.87,"region":"Midwest"},
    "Sioux City":       {"slug":"sioux-city",       "state":"Iowa",              "cost_mult":0.85,"region":"Midwest"},
    "Waterloo IA":      {"slug":"waterloo-ia",      "state":"Iowa",              "cost_mult":0.83,"region":"Midwest"},
    "Dubuque":          {"slug":"dubuque",          "state":"Iowa",              "cost_mult":0.87,"region":"Midwest"},
    # ── NEBRASKA ──────────────────────────────────────────────────────────────
    "Bellevue NE":      {"slug":"bellevue-ne",      "state":"Nebraska",          "cost_mult":0.87,"region":"Midwest"},
    "Grand Island NE":  {"slug":"grand-island-ne",  "state":"Nebraska",          "cost_mult":0.82,"region":"Midwest"},
    "Kearney NE":       {"slug":"kearney-ne",       "state":"Nebraska",          "cost_mult":0.80,"region":"Midwest"},
    # ── OKLAHOMA ──────────────────────────────────────────────────────────────
    "Norman":           {"slug":"norman",           "state":"Oklahoma",          "cost_mult":0.85,"region":"South"},
    "Broken Arrow":     {"slug":"broken-arrow",     "state":"Oklahoma",          "cost_mult":0.87,"region":"South"},
    "Edmond":           {"slug":"edmond",           "state":"Oklahoma",          "cost_mult":0.88,"region":"South"},
    "Lawton":           {"slug":"lawton",           "state":"Oklahoma",          "cost_mult":0.80,"region":"South"},
    "Midwest City":     {"slug":"midwest-city",     "state":"Oklahoma",          "cost_mult":0.83,"region":"South"},
    # ── NEVADA ────────────────────────────────────────────────────────────────
    "Sparks":           {"slug":"sparks",           "state":"Nevada",            "cost_mult":1.03,"region":"West"},
    "Carson City":      {"slug":"carson-city",      "state":"Nevada",            "cost_mult":1.00,"region":"West"},
    # ── UTAH ──────────────────────────────────────────────────────────────────
    "St. George UT":    {"slug":"st-george-ut",     "state":"Utah",              "cost_mult":0.95,"region":"Mountain"},
    "Layton":           {"slug":"layton",           "state":"Utah",              "cost_mult":1.00,"region":"Mountain"},
    "South Jordan":     {"slug":"south-jordan",     "state":"Utah",              "cost_mult":1.02,"region":"Mountain"},
    "Millcreek":        {"slug":"millcreek",        "state":"Utah",              "cost_mult":1.03,"region":"Mountain"},
    # ── IDAHO ─────────────────────────────────────────────────────────────────
    "Idaho Falls":      {"slug":"idaho-falls",      "state":"Idaho",             "cost_mult":0.92,"region":"Mountain"},
    "Pocatello":        {"slug":"pocatello",        "state":"Idaho",             "cost_mult":0.88,"region":"Mountain"},
    "Coeur d'Alene":    {"slug":"coeur-dalene",     "state":"Idaho",             "cost_mult":1.00,"region":"Mountain"},
    # ── MONTANA ───────────────────────────────────────────────────────────────
    "Great Falls MT":   {"slug":"great-falls-mt",   "state":"Montana",           "cost_mult":0.87,"region":"Mountain"},
    "Bozeman":          {"slug":"bozeman",          "state":"Montana",           "cost_mult":1.05,"region":"Mountain"},
    "Helena MT":        {"slug":"helena-mt",        "state":"Montana",           "cost_mult":0.90,"region":"Mountain"},
    # ── WYOMING ───────────────────────────────────────────────────────────────
    "Laramie":          {"slug":"laramie",          "state":"Wyoming",           "cost_mult":0.88,"region":"Mountain"},
    "Gillette":         {"slug":"gillette",         "state":"Wyoming",           "cost_mult":0.87,"region":"Mountain"},
    # ── NORTH DAKOTA ──────────────────────────────────────────────────────────
    "Grand Forks":      {"slug":"grand-forks",      "state":"North Dakota",      "cost_mult":0.88,"region":"Midwest"},
    "Minot":            {"slug":"minot",            "state":"North Dakota",      "cost_mult":0.87,"region":"Midwest"},
    # ── SOUTH DAKOTA ──────────────────────────────────────────────────────────
    "Aberdeen SD":      {"slug":"aberdeen-sd",      "state":"South Dakota",      "cost_mult":0.83,"region":"Midwest"},
    # ── HAWAII ────────────────────────────────────────────────────────────────
    "Hilo":             {"slug":"hilo",             "state":"Hawaii",            "cost_mult":1.45,"region":"West"},
    "Pearl City":       {"slug":"pearl-city",       "state":"Hawaii",            "cost_mult":1.55,"region":"West"},
    "Kailua HI":        {"slug":"kailua-hi",        "state":"Hawaii",            "cost_mult":1.58,"region":"West"},
    # ── NEW MEXICO ────────────────────────────────────────────────────────────
    "Santa Fe":         {"slug":"santa-fe",         "state":"New Mexico",        "cost_mult":0.97,"region":"Mountain"},
    "Roswell NM":       {"slug":"roswell-nm",       "state":"New Mexico",        "cost_mult":0.80,"region":"Mountain"},
    # ── RHODE ISLAND ──────────────────────────────────────────────────────────
    "Warwick":          {"slug":"warwick",          "state":"Rhode Island",      "cost_mult":1.12,"region":"Northeast"},
    "Cranston":         {"slug":"cranston",         "state":"Rhode Island",      "cost_mult":1.10,"region":"Northeast"},
    "Pawtucket":        {"slug":"pawtucket",        "state":"Rhode Island",      "cost_mult":1.08,"region":"Northeast"},
    # ── MAINE ─────────────────────────────────────────────────────────────────
    "Lewiston":         {"slug":"lewiston",         "state":"Maine",             "cost_mult":1.00,"region":"Northeast"},
    "Bangor":           {"slug":"bangor",           "state":"Maine",             "cost_mult":1.02,"region":"Northeast"},
    # ── NEW HAMPSHIRE ─────────────────────────────────────────────────────────
    "Nashua":           {"slug":"nashua",           "state":"New Hampshire",     "cost_mult":1.15,"region":"Northeast"},
    "Concord NH":       {"slug":"concord-nh",       "state":"New Hampshire",     "cost_mult":1.10,"region":"Northeast"},
    # ── VERMONT ───────────────────────────────────────────────────────────────
    "Rutland":          {"slug":"rutland",          "state":"Vermont",           "cost_mult":1.05,"region":"Northeast"},
    # ── DELAWARE ──────────────────────────────────────────────────────────────
    "Dover DE":         {"slug":"dover-de",         "state":"Delaware",          "cost_mult":1.05,"region":"Northeast"},
    "Newark DE":        {"slug":"newark-de",        "state":"Delaware",          "cost_mult":1.08,"region":"Northeast"},
    # ── WEST VIRGINIA ─────────────────────────────────────────────────────────
    "Morgantown WV":    {"slug":"morgantown-wv",    "state":"West Virginia",     "cost_mult":0.83,"region":"South"},
    "Parkersburg WV":   {"slug":"parkersburg-wv",   "state":"West Virginia",     "cost_mult":0.80,"region":"South"},
    # ── ARIZONA (more suburbs) ────────────────────────────────────────────────
    "Goodyear":         {"slug":"goodyear",         "state":"Arizona",           "cost_mult":0.95,"region":"South"},
    "Avondale":         {"slug":"avondale",         "state":"Arizona",           "cost_mult":0.93,"region":"South"},
    "Queen Creek":      {"slug":"queen-creek",      "state":"Arizona",           "cost_mult":0.95,"region":"South"},
    "Buckeye":          {"slug":"buckeye",          "state":"Arizona",           "cost_mult":0.92,"region":"South"},
    "Maricopa AZ":      {"slug":"maricopa-az",      "state":"Arizona",           "cost_mult":0.90,"region":"South"},
    # ── OREGON (more) ─────────────────────────────────────────────────────────
    "Bend":             {"slug":"bend",             "state":"Oregon",            "cost_mult":1.10,"region":"West"},
    "Medford":          {"slug":"medford",          "state":"Oregon",            "cost_mult":1.00,"region":"West"},
    "Corvallis":        {"slug":"corvallis",        "state":"Oregon",            "cost_mult":1.05,"region":"West"},
    "Springfield OR":   {"slug":"springfield-or",   "state":"Oregon",            "cost_mult":1.05,"region":"West"},
    # ── LOUISIANA (more) ──────────────────────────────────────────────────────
    "Metairie":         {"slug":"metairie",         "state":"Louisiana",         "cost_mult":0.92,"region":"South"},
    "Kenner":           {"slug":"kenner",           "state":"Louisiana",         "cost_mult":0.88,"region":"South"},
    "Monroe LA":        {"slug":"monroe-la",        "state":"Louisiana",         "cost_mult":0.80,"region":"South"},
    # ── KANSAS (more) ─────────────────────────────────────────────────────────
    "Lawrence KS":      {"slug":"lawrence-ks",      "state":"Kansas",            "cost_mult":0.87,"region":"Midwest"},
    "Manhattan KS":     {"slug":"manhattan-ks",     "state":"Kansas",            "cost_mult":0.83,"region":"Midwest"},
    # ── NEW MEXICO (more) ─────────────────────────────────────────────────────
    "Farmington NM":    {"slug":"farmington-nm",    "state":"New Mexico",        "cost_mult":0.82,"region":"Mountain"},
}

# Remove None entries
NEW_CITIES = {k: v for k, v in NEW_CITIES.items() if v is not None}

def main():
    total = 0
    city_count = len(NEW_CITIES)
    proj_count = len(calc.PROJECTS) + len(proj2.PROJECTS)

    print(f"Cities: {city_count}")
    print(f"Project types: {proj_count} (9 original + 5 new)")
    print(f"Estimated pages: {city_count * proj_count:,}")
    print()

    # ── 9 original project types (from generate_new_calculators.py) ──────────
    for proj_key, proj in calc.PROJECTS.items():
        print(f"  {proj['name']}...", end=" ", flush=True)
        for city_name, city_data in NEW_CITIES.items():
            slug = calc.build_slugified(city_name, proj, city_data)
            folder = os.path.join(TOOLS_DIR, slug)
            os.makedirs(folder, exist_ok=True)
            html = calc.generate_page(city_name, city_data, proj_key, proj)
            with open(os.path.join(folder, "index.html"), "w", encoding="utf-8") as f:
                f.write(html)
            total += 1
        print(f"{city_count} pages")

    # ── 5 new project types (from generate_new_projects2.py) ─────────────────
    for proj_key, proj in proj2.PROJECTS.items():
        print(f"  {proj['name']}...", end=" ", flush=True)
        for city_name, city_data in NEW_CITIES.items():
            slug = f"{proj['slug']}-cost-{city_data['slug']}"
            folder = os.path.join(TOOLS_DIR, slug)
            os.makedirs(folder, exist_ok=True)
            html = proj2.generate_page(city_name, city_data, proj_key, proj)
            with open(os.path.join(folder, "index.html"), "w", encoding="utf-8") as f:
                f.write(html)
            total += 1
        print(f"{city_count} pages")

    print(f"\nDone! {total:,} pages generated.")
    return total

if __name__ == "__main__":
    main()
