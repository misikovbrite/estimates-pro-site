#!/usr/bin/env python3
"""Generate city pages for 150+ new cities across all 9 project types."""
import os, json, sys

# ─── ALL 200 CITIES (existing 51 + 150 new) ──────────────────────────────────
ALL_CITIES = {
    # ── EXISTING (already generated, skip) ───────────────────────────────────
    "New York":         {"slug":"new-york",          "state":"New York",             "cost_mult":1.35,"region":"Northeast","existing":True},
    "Los Angeles":      {"slug":"los-angeles",       "state":"California",           "cost_mult":1.25,"region":"West","existing":True},
    "Chicago":          {"slug":"chicago",           "state":"Illinois",             "cost_mult":1.10,"region":"Midwest","existing":True},
    "Houston":          {"slug":"houston",           "state":"Texas",                "cost_mult":0.92,"region":"South","existing":True},
    "Phoenix":          {"slug":"phoenix",           "state":"Arizona",              "cost_mult":0.95,"region":"South","existing":True},
    "Philadelphia":     {"slug":"philadelphia",      "state":"Pennsylvania",         "cost_mult":1.12,"region":"Northeast","existing":True},
    "San Antonio":      {"slug":"san-antonio",       "state":"Texas",                "cost_mult":0.88,"region":"South","existing":True},
    "San Diego":        {"slug":"san-diego",         "state":"California",           "cost_mult":1.28,"region":"West","existing":True},
    "Dallas":           {"slug":"dallas",            "state":"Texas",                "cost_mult":0.94,"region":"South","existing":True},
    "San Jose":         {"slug":"san-jose",          "state":"California",           "cost_mult":1.40,"region":"West","existing":True},
    "Austin":           {"slug":"austin",            "state":"Texas",                "cost_mult":0.97,"region":"South","existing":True},
    "Jacksonville":     {"slug":"jacksonville",      "state":"Florida",              "cost_mult":0.90,"region":"South","existing":True},
    "Fort Worth":       {"slug":"fort-worth",        "state":"Texas",                "cost_mult":0.93,"region":"South","existing":True},
    "Columbus":         {"slug":"columbus",          "state":"Ohio",                 "cost_mult":0.90,"region":"Midwest","existing":True},
    "Charlotte":        {"slug":"charlotte",         "state":"North Carolina",       "cost_mult":0.93,"region":"South","existing":True},
    "Indianapolis":     {"slug":"indianapolis",      "state":"Indiana",              "cost_mult":0.88,"region":"Midwest","existing":True},
    "San Francisco":    {"slug":"san-francisco",     "state":"California",           "cost_mult":1.55,"region":"West","existing":True},
    "Seattle":          {"slug":"seattle",           "state":"Washington",           "cost_mult":1.30,"region":"West","existing":True},
    "Denver":           {"slug":"denver",            "state":"Colorado",             "cost_mult":1.05,"region":"Mountain","existing":True},
    "Nashville":        {"slug":"nashville",         "state":"Tennessee",            "cost_mult":0.93,"region":"South","existing":True},
    "Oklahoma City":    {"slug":"oklahoma-city",     "state":"Oklahoma",             "cost_mult":0.85,"region":"South","existing":True},
    "El Paso":          {"slug":"el-paso",           "state":"Texas",                "cost_mult":0.82,"region":"South","existing":True},
    "Washington DC":    {"slug":"washington-dc",     "state":"District of Columbia", "cost_mult":1.30,"region":"Northeast","existing":True},
    "Las Vegas":        {"slug":"las-vegas",         "state":"Nevada",               "cost_mult":1.00,"region":"West","existing":True},
    "Boston":           {"slug":"boston",            "state":"Massachusetts",        "cost_mult":1.35,"region":"Northeast","existing":True},
    "Portland":         {"slug":"portland",          "state":"Oregon",               "cost_mult":1.15,"region":"West","existing":True},
    "Memphis":          {"slug":"memphis",           "state":"Tennessee",            "cost_mult":0.83,"region":"South","existing":True},
    "Louisville":       {"slug":"louisville",        "state":"Kentucky",             "cost_mult":0.87,"region":"South","existing":True},
    "Baltimore":        {"slug":"baltimore",         "state":"Maryland",             "cost_mult":1.12,"region":"Northeast","existing":True},
    "Milwaukee":        {"slug":"milwaukee",         "state":"Wisconsin",            "cost_mult":0.93,"region":"Midwest","existing":True},
    "Albuquerque":      {"slug":"albuquerque",       "state":"New Mexico",           "cost_mult":0.88,"region":"Mountain","existing":True},
    "Tucson":           {"slug":"tucson",            "state":"Arizona",              "cost_mult":0.87,"region":"South","existing":True},
    "Fresno":           {"slug":"fresno",            "state":"California",           "cost_mult":0.97,"region":"West","existing":True},
    "Sacramento":       {"slug":"sacramento",        "state":"California",           "cost_mult":1.10,"region":"West","existing":True},
    "Mesa":             {"slug":"mesa",              "state":"Arizona",              "cost_mult":0.95,"region":"South","existing":True},
    "Atlanta":          {"slug":"atlanta",           "state":"Georgia",              "cost_mult":0.96,"region":"South","existing":True},
    "Omaha":            {"slug":"omaha",             "state":"Nebraska",             "cost_mult":0.87,"region":"Midwest","existing":True},
    "Colorado Springs": {"slug":"colorado-springs",  "state":"Colorado",             "cost_mult":1.00,"region":"Mountain","existing":True},
    "Raleigh":          {"slug":"raleigh",           "state":"North Carolina",       "cost_mult":0.95,"region":"South","existing":True},
    "Miami":            {"slug":"miami",             "state":"Florida",              "cost_mult":1.08,"region":"South","existing":True},
    "Minneapolis":      {"slug":"minneapolis",       "state":"Minnesota",            "cost_mult":1.05,"region":"Midwest","existing":True},
    "Tampa":            {"slug":"tampa",             "state":"Florida",              "cost_mult":0.98,"region":"South","existing":True},
    "New Orleans":      {"slug":"new-orleans",       "state":"Louisiana",            "cost_mult":0.90,"region":"South","existing":True},
    "Cleveland":        {"slug":"cleveland",         "state":"Ohio",                 "cost_mult":0.87,"region":"Midwest","existing":True},
    "Bakersfield":      {"slug":"bakersfield",       "state":"California",           "cost_mult":0.93,"region":"West","existing":True},
    "Honolulu":         {"slug":"honolulu",          "state":"Hawaii",               "cost_mult":1.65,"region":"West","existing":True},
    "Anaheim":          {"slug":"anaheim",           "state":"California",           "cost_mult":1.25,"region":"West","existing":True},
    "Riverside":        {"slug":"riverside",         "state":"California",           "cost_mult":1.10,"region":"West","existing":True},
    "Corpus Christi":   {"slug":"corpus-christi",    "state":"Texas",                "cost_mult":0.87,"region":"South","existing":True},
    "Cincinnati":       {"slug":"cincinnati",        "state":"Ohio",                 "cost_mult":0.90,"region":"Midwest","existing":True},
    "St. Louis":        {"slug":"st-louis",          "state":"Missouri",             "cost_mult":0.90,"region":"Midwest","existing":True},

    # ── NEW CITIES ─────────────────────────────────────────────────────────────

    # California
    "Long Beach":       {"slug":"long-beach",        "state":"California",           "cost_mult":1.22,"region":"West"},
    "Oakland":          {"slug":"oakland",           "state":"California",           "cost_mult":1.35,"region":"West"},
    "Stockton":         {"slug":"stockton",          "state":"California",           "cost_mult":0.97,"region":"West"},
    "Irvine":           {"slug":"irvine",            "state":"California",           "cost_mult":1.30,"region":"West"},
    "San Bernardino":   {"slug":"san-bernardino",    "state":"California",           "cost_mult":1.00,"region":"West"},
    "Chula Vista":      {"slug":"chula-vista",       "state":"California",           "cost_mult":1.18,"region":"West"},
    "Modesto":          {"slug":"modesto",           "state":"California",           "cost_mult":0.95,"region":"West"},
    "Oxnard":           {"slug":"oxnard",            "state":"California",           "cost_mult":1.12,"region":"West"},
    "Fontana":          {"slug":"fontana",           "state":"California",           "cost_mult":1.05,"region":"West"},
    "Moreno Valley":    {"slug":"moreno-valley",     "state":"California",           "cost_mult":1.02,"region":"West"},
    "Santa Ana":        {"slug":"santa-ana",         "state":"California",           "cost_mult":1.18,"region":"West"},
    "Glendale":         {"slug":"glendale",          "state":"California",           "cost_mult":1.22,"region":"West"},
    "Huntington Beach": {"slug":"huntington-beach",  "state":"California",           "cost_mult":1.25,"region":"West"},
    "Santa Clarita":    {"slug":"santa-clarita",     "state":"California",           "cost_mult":1.20,"region":"West"},
    "Fremont":          {"slug":"fremont",           "state":"California",           "cost_mult":1.38,"region":"West"},
    "San Jose North":   None,  # skip duplicate
    "Torrance":         {"slug":"torrance",          "state":"California",           "cost_mult":1.22,"region":"West"},

    # Texas
    "Arlington":        {"slug":"arlington",         "state":"Texas",                "cost_mult":0.93,"region":"South"},
    "Plano":            {"slug":"plano",             "state":"Texas",                "cost_mult":0.96,"region":"South"},
    "Laredo":           {"slug":"laredo",            "state":"Texas",                "cost_mult":0.80,"region":"South"},
    "Lubbock":          {"slug":"lubbock",           "state":"Texas",                "cost_mult":0.82,"region":"South"},
    "Garland":          {"slug":"garland",           "state":"Texas",                "cost_mult":0.92,"region":"South"},
    "Irving":           {"slug":"irving",            "state":"Texas",                "cost_mult":0.94,"region":"South"},
    "Amarillo":         {"slug":"amarillo",          "state":"Texas",                "cost_mult":0.82,"region":"South"},
    "Grand Prairie":    {"slug":"grand-prairie",     "state":"Texas",                "cost_mult":0.90,"region":"South"},
    "McKinney":         {"slug":"mckinney",          "state":"Texas",                "cost_mult":0.96,"region":"South"},
    "Frisco":           {"slug":"frisco",            "state":"Texas",                "cost_mult":1.00,"region":"South"},
    "Killeen":          {"slug":"killeen",           "state":"Texas",                "cost_mult":0.82,"region":"South"},
    "Brownsville":      {"slug":"brownsville",       "state":"Texas",                "cost_mult":0.78,"region":"South"},
    "Pasadena":         {"slug":"pasadena",          "state":"Texas",                "cost_mult":0.90,"region":"South"},
    "Mesquite":         {"slug":"mesquite",          "state":"Texas",                "cost_mult":0.90,"region":"South"},

    # Florida
    "Orlando":          {"slug":"orlando",           "state":"Florida",              "cost_mult":1.00,"region":"South"},
    "St. Petersburg":   {"slug":"st-petersburg",     "state":"Florida",              "cost_mult":0.97,"region":"South"},
    "Hialeah":          {"slug":"hialeah",           "state":"Florida",              "cost_mult":1.00,"region":"South"},
    "Port St. Lucie":   {"slug":"port-st-lucie",     "state":"Florida",              "cost_mult":0.95,"region":"South"},
    "Cape Coral":       {"slug":"cape-coral",        "state":"Florida",              "cost_mult":0.97,"region":"South"},
    "Fort Lauderdale":  {"slug":"fort-lauderdale",   "state":"Florida",              "cost_mult":1.05,"region":"South"},
    "Pembroke Pines":   {"slug":"pembroke-pines",    "state":"Florida",              "cost_mult":1.02,"region":"South"},
    "Hollywood":        {"slug":"hollywood",         "state":"Florida",              "cost_mult":1.03,"region":"South"},
    "Gainesville":      {"slug":"gainesville",       "state":"Florida",              "cost_mult":0.90,"region":"South"},
    "Tallahassee":      {"slug":"tallahassee",       "state":"Florida",              "cost_mult":0.88,"region":"South"},
    "Miramar":          {"slug":"miramar",           "state":"Florida",              "cost_mult":1.02,"region":"South"},
    "Clearwater":       {"slug":"clearwater",        "state":"Florida",              "cost_mult":0.97,"region":"South"},

    # New York
    "Buffalo":          {"slug":"buffalo",           "state":"New York",             "cost_mult":1.05,"region":"Northeast"},
    "Rochester":        {"slug":"rochester",         "state":"New York",             "cost_mult":1.00,"region":"Northeast"},
    "Yonkers":          {"slug":"yonkers",           "state":"New York",             "cost_mult":1.30,"region":"Northeast"},
    "Syracuse":         {"slug":"syracuse",          "state":"New York",             "cost_mult":0.97,"region":"Northeast"},
    "Albany":           {"slug":"albany",            "state":"New York",             "cost_mult":1.02,"region":"Northeast"},

    # Illinois
    "Aurora":           {"slug":"aurora",            "state":"Illinois",             "cost_mult":1.05,"region":"Midwest"},
    "Naperville":       {"slug":"naperville",        "state":"Illinois",             "cost_mult":1.08,"region":"Midwest"},
    "Joliet":           {"slug":"joliet",            "state":"Illinois",             "cost_mult":1.02,"region":"Midwest"},
    "Rockford":         {"slug":"rockford",          "state":"Illinois",             "cost_mult":0.88,"region":"Midwest"},
    "Springfield":      {"slug":"springfield",       "state":"Illinois",             "cost_mult":0.87,"region":"Midwest"},
    "Peoria":           {"slug":"peoria",            "state":"Illinois",             "cost_mult":0.85,"region":"Midwest"},

    # Pennsylvania
    "Pittsburgh":       {"slug":"pittsburgh",        "state":"Pennsylvania",         "cost_mult":1.05,"region":"Northeast"},
    "Allentown":        {"slug":"allentown",         "state":"Pennsylvania",         "cost_mult":1.00,"region":"Northeast"},

    # Ohio
    "Akron":            {"slug":"akron",             "state":"Ohio",                 "cost_mult":0.87,"region":"Midwest"},
    "Toledo":           {"slug":"toledo",            "state":"Ohio",                 "cost_mult":0.85,"region":"Midwest"},
    "Dayton":           {"slug":"dayton",            "state":"Ohio",                 "cost_mult":0.85,"region":"Midwest"},

    # Michigan
    "Detroit":          {"slug":"detroit",           "state":"Michigan",             "cost_mult":0.95,"region":"Midwest"},
    "Grand Rapids":     {"slug":"grand-rapids",      "state":"Michigan",             "cost_mult":0.92,"region":"Midwest"},
    "Warren":           {"slug":"warren",            "state":"Michigan",             "cost_mult":0.93,"region":"Midwest"},
    "Sterling Heights": {"slug":"sterling-heights",  "state":"Michigan",             "cost_mult":0.95,"region":"Midwest"},
    "Ann Arbor":        {"slug":"ann-arbor",         "state":"Michigan",             "cost_mult":1.05,"region":"Midwest"},
    "Lansing":          {"slug":"lansing",           "state":"Michigan",             "cost_mult":0.88,"region":"Midwest"},

    # North Carolina
    "Durham":           {"slug":"durham",            "state":"North Carolina",       "cost_mult":0.97,"region":"South"},
    "Greensboro":       {"slug":"greensboro",        "state":"North Carolina",       "cost_mult":0.90,"region":"South"},
    "Winston-Salem":    {"slug":"winston-salem",     "state":"North Carolina",       "cost_mult":0.88,"region":"South"},
    "Fayetteville":     {"slug":"fayetteville",      "state":"North Carolina",       "cost_mult":0.85,"region":"South"},
    "Cary":             {"slug":"cary",              "state":"North Carolina",       "cost_mult":1.00,"region":"South"},

    # Georgia
    "Augusta":          {"slug":"augusta",           "state":"Georgia",              "cost_mult":0.85,"region":"South"},
    "Columbus GA":      {"slug":"columbus-ga",       "state":"Georgia",              "cost_mult":0.83,"region":"South"},
    "Macon":            {"slug":"macon",             "state":"Georgia",              "cost_mult":0.82,"region":"South"},
    "Savannah":         {"slug":"savannah",          "state":"Georgia",              "cost_mult":0.90,"region":"South"},

    # Virginia
    "Virginia Beach":   {"slug":"virginia-beach",    "state":"Virginia",             "cost_mult":1.05,"region":"South"},
    "Norfolk":          {"slug":"norfolk",           "state":"Virginia",             "cost_mult":1.02,"region":"South"},
    "Chesapeake":       {"slug":"chesapeake",        "state":"Virginia",             "cost_mult":1.03,"region":"South"},
    "Richmond":         {"slug":"richmond",          "state":"Virginia",             "cost_mult":1.00,"region":"South"},
    "Newport News":     {"slug":"newport-news",      "state":"Virginia",             "cost_mult":0.98,"region":"South"},
    "Alexandria":       {"slug":"alexandria",        "state":"Virginia",             "cost_mult":1.25,"region":"Northeast"},
    "Arlington VA":     {"slug":"arlington-va",      "state":"Virginia",             "cost_mult":1.28,"region":"Northeast"},

    # Washington
    "Spokane":          {"slug":"spokane",           "state":"Washington",           "cost_mult":1.00,"region":"West"},
    "Tacoma":           {"slug":"tacoma",            "state":"Washington",           "cost_mult":1.15,"region":"West"},
    "Bellevue":         {"slug":"bellevue",          "state":"Washington",           "cost_mult":1.38,"region":"West"},
    "Kent":             {"slug":"kent",              "state":"Washington",           "cost_mult":1.12,"region":"West"},

    # Arizona
    "Chandler":         {"slug":"chandler",          "state":"Arizona",              "cost_mult":0.97,"region":"South"},
    "Scottsdale":       {"slug":"scottsdale",        "state":"Arizona",              "cost_mult":1.08,"region":"South"},
    "Gilbert":          {"slug":"gilbert",           "state":"Arizona",              "cost_mult":0.97,"region":"South"},
    "Tempe":            {"slug":"tempe",             "state":"Arizona",              "cost_mult":0.97,"region":"South"},
    "Peoria AZ":        {"slug":"peoria-az",         "state":"Arizona",              "cost_mult":0.95,"region":"South"},
    "Surprise":         {"slug":"surprise",          "state":"Arizona",              "cost_mult":0.93,"region":"South"},
    "Glendale AZ":      {"slug":"glendale-az",       "state":"Arizona",              "cost_mult":0.93,"region":"South"},
    "Yuma":             {"slug":"yuma",              "state":"Arizona",              "cost_mult":0.82,"region":"South"},
    "Flagstaff":        {"slug":"flagstaff",         "state":"Arizona",              "cost_mult":0.97,"region":"Mountain"},

    # Colorado
    "Aurora CO":        {"slug":"aurora-co",         "state":"Colorado",             "cost_mult":1.03,"region":"Mountain"},
    "Fort Collins":     {"slug":"fort-collins",      "state":"Colorado",             "cost_mult":1.05,"region":"Mountain"},
    "Lakewood":         {"slug":"lakewood",          "state":"Colorado",             "cost_mult":1.05,"region":"Mountain"},
    "Thornton":         {"slug":"thornton",          "state":"Colorado",             "cost_mult":1.02,"region":"Mountain"},
    "Pueblo":           {"slug":"pueblo",            "state":"Colorado",             "cost_mult":0.88,"region":"Mountain"},
    "Westminster CO":   {"slug":"westminster-co",    "state":"Colorado",             "cost_mult":1.03,"region":"Mountain"},

    # Tennessee
    "Knoxville":        {"slug":"knoxville",         "state":"Tennessee",            "cost_mult":0.87,"region":"South"},
    "Chattanooga":      {"slug":"chattanooga",       "state":"Tennessee",            "cost_mult":0.87,"region":"South"},
    "Clarksville":      {"slug":"clarksville",       "state":"Tennessee",            "cost_mult":0.85,"region":"South"},
    "Murfreesboro":     {"slug":"murfreesboro",      "state":"Tennessee",            "cost_mult":0.90,"region":"South"},

    # Indiana
    "Fort Wayne":       {"slug":"fort-wayne",        "state":"Indiana",              "cost_mult":0.85,"region":"Midwest"},
    "Evansville":       {"slug":"evansville",        "state":"Indiana",              "cost_mult":0.83,"region":"Midwest"},
    "South Bend":       {"slug":"south-bend",        "state":"Indiana",              "cost_mult":0.85,"region":"Midwest"},

    # Missouri
    "Kansas City":      {"slug":"kansas-city",       "state":"Missouri",             "cost_mult":0.92,"region":"Midwest"},
    "Springfield MO":   {"slug":"springfield-mo",    "state":"Missouri",             "cost_mult":0.83,"region":"Midwest"},
    "Columbia MO":      {"slug":"columbia-mo",       "state":"Missouri",             "cost_mult":0.87,"region":"Midwest"},

    # Kansas
    "Wichita":          {"slug":"wichita",           "state":"Kansas",               "cost_mult":0.85,"region":"Midwest"},
    "Overland Park":    {"slug":"overland-park",     "state":"Kansas",               "cost_mult":0.93,"region":"Midwest"},
    "Topeka":           {"slug":"topeka",            "state":"Kansas",               "cost_mult":0.82,"region":"Midwest"},

    # Nevada
    "Reno":             {"slug":"reno",              "state":"Nevada",               "cost_mult":1.03,"region":"West"},
    "Henderson":        {"slug":"henderson",         "state":"Nevada",               "cost_mult":1.00,"region":"West"},
    "North Las Vegas":  {"slug":"north-las-vegas",   "state":"Nevada",               "cost_mult":0.97,"region":"West"},

    # Utah
    "Salt Lake City":   {"slug":"salt-lake-city",    "state":"Utah",                 "cost_mult":1.05,"region":"Mountain"},
    "West Valley City": {"slug":"west-valley-city",  "state":"Utah",                 "cost_mult":1.00,"region":"Mountain"},
    "Provo":            {"slug":"provo",             "state":"Utah",                 "cost_mult":0.98,"region":"Mountain"},
    "Ogden":            {"slug":"ogden",             "state":"Utah",                 "cost_mult":0.97,"region":"Mountain"},

    # New Mexico
    "Las Cruces":       {"slug":"las-cruces",        "state":"New Mexico",           "cost_mult":0.83,"region":"Mountain"},
    "Rio Rancho":       {"slug":"rio-rancho",        "state":"New Mexico",           "cost_mult":0.85,"region":"Mountain"},

    # Oregon
    "Eugene":           {"slug":"eugene",            "state":"Oregon",               "cost_mult":1.05,"region":"West"},
    "Salem":            {"slug":"salem",             "state":"Oregon",               "cost_mult":1.00,"region":"West"},
    "Gresham":          {"slug":"gresham",           "state":"Oregon",               "cost_mult":1.10,"region":"West"},
    "Hillsboro":        {"slug":"hillsboro",         "state":"Oregon",               "cost_mult":1.12,"region":"West"},

    # Minnesota
    "St. Paul":         {"slug":"st-paul",           "state":"Minnesota",            "cost_mult":1.05,"region":"Midwest"},
    "Rochester MN":     {"slug":"rochester-mn",      "state":"Minnesota",            "cost_mult":1.00,"region":"Midwest"},

    # Iowa
    "Des Moines":       {"slug":"des-moines",        "state":"Iowa",                 "cost_mult":0.88,"region":"Midwest"},
    "Cedar Rapids":     {"slug":"cedar-rapids",      "state":"Iowa",                 "cost_mult":0.85,"region":"Midwest"},

    # Wisconsin
    "Madison":          {"slug":"madison",           "state":"Wisconsin",            "cost_mult":1.00,"region":"Midwest"},
    "Green Bay":        {"slug":"green-bay",         "state":"Wisconsin",            "cost_mult":0.88,"region":"Midwest"},
    "Kenosha":          {"slug":"kenosha",           "state":"Wisconsin",            "cost_mult":0.90,"region":"Midwest"},

    # Kentucky
    "Lexington":        {"slug":"lexington",         "state":"Kentucky",             "cost_mult":0.90,"region":"South"},
    "Bowling Green":    {"slug":"bowling-green",     "state":"Kentucky",             "cost_mult":0.83,"region":"South"},

    # South Carolina
    "Columbia SC":      {"slug":"columbia-sc",       "state":"South Carolina",       "cost_mult":0.87,"region":"South"},
    "Charleston":       {"slug":"charleston",        "state":"South Carolina",       "cost_mult":0.97,"region":"South"},
    "North Charleston": {"slug":"north-charleston",  "state":"South Carolina",       "cost_mult":0.90,"region":"South"},
    "Greenville SC":    {"slug":"greenville-sc",     "state":"South Carolina",       "cost_mult":0.90,"region":"South"},

    # Louisiana
    "Baton Rouge":      {"slug":"baton-rouge",       "state":"Louisiana",            "cost_mult":0.87,"region":"South"},
    "Shreveport":       {"slug":"shreveport",        "state":"Louisiana",            "cost_mult":0.82,"region":"South"},
    "Lafayette LA":     {"slug":"lafayette-la",      "state":"Louisiana",            "cost_mult":0.85,"region":"South"},
    "Lake Charles":     {"slug":"lake-charles",      "state":"Louisiana",            "cost_mult":0.85,"region":"South"},

    # Alabama
    "Birmingham":       {"slug":"birmingham",        "state":"Alabama",              "cost_mult":0.83,"region":"South"},
    "Montgomery":       {"slug":"montgomery",        "state":"Alabama",              "cost_mult":0.80,"region":"South"},
    "Huntsville":       {"slug":"huntsville",        "state":"Alabama",              "cost_mult":0.85,"region":"South"},
    "Mobile":           {"slug":"mobile",            "state":"Alabama",              "cost_mult":0.82,"region":"South"},

    # Mississippi
    "Jackson MS":       {"slug":"jackson-ms",        "state":"Mississippi",          "cost_mult":0.78,"region":"South"},

    # Arkansas
    "Little Rock":      {"slug":"little-rock",       "state":"Arkansas",             "cost_mult":0.80,"region":"South"},
    "Fort Smith":       {"slug":"fort-smith",        "state":"Arkansas",             "cost_mult":0.78,"region":"South"},

    # Connecticut
    "Bridgeport":       {"slug":"bridgeport",        "state":"Connecticut",          "cost_mult":1.18,"region":"Northeast"},
    "New Haven":        {"slug":"new-haven",         "state":"Connecticut",          "cost_mult":1.15,"region":"Northeast"},
    "Hartford":         {"slug":"hartford",          "state":"Connecticut",          "cost_mult":1.12,"region":"Northeast"},
    "Stamford":         {"slug":"stamford",          "state":"Connecticut",          "cost_mult":1.28,"region":"Northeast"},

    # New Jersey
    "Newark":           {"slug":"newark",            "state":"New Jersey",           "cost_mult":1.22,"region":"Northeast"},
    "Jersey City":      {"slug":"jersey-city",       "state":"New Jersey",           "cost_mult":1.25,"region":"Northeast"},
    "Paterson":         {"slug":"paterson",          "state":"New Jersey",           "cost_mult":1.18,"region":"Northeast"},
    "Elizabeth":        {"slug":"elizabeth",         "state":"New Jersey",           "cost_mult":1.18,"region":"Northeast"},
    "Trenton":          {"slug":"trenton",           "state":"New Jersey",           "cost_mult":1.10,"region":"Northeast"},

    # Massachusetts
    "Worcester":        {"slug":"worcester",         "state":"Massachusetts",        "cost_mult":1.18,"region":"Northeast"},
    "Springfield MA":   {"slug":"springfield-ma",    "state":"Massachusetts",        "cost_mult":1.10,"region":"Northeast"},
    "Lowell":           {"slug":"lowell",            "state":"Massachusetts",        "cost_mult":1.15,"region":"Northeast"},
    "Cambridge":        {"slug":"cambridge",         "state":"Massachusetts",        "cost_mult":1.45,"region":"Northeast"},

    # Rhode Island
    "Providence":       {"slug":"providence",        "state":"Rhode Island",         "cost_mult":1.12,"region":"Northeast"},

    # New Hampshire
    "Manchester NH":    {"slug":"manchester-nh",     "state":"New Hampshire",        "cost_mult":1.10,"region":"Northeast"},
    "Nashua":           {"slug":"nashua",            "state":"New Hampshire",        "cost_mult":1.12,"region":"Northeast"},

    # Maine
    "Portland ME":      {"slug":"portland-me",       "state":"Maine",                "cost_mult":1.05,"region":"Northeast"},

    # Idaho
    "Boise":            {"slug":"boise",             "state":"Idaho",                "cost_mult":1.00,"region":"Mountain"},
    "Nampa":            {"slug":"nampa",             "state":"Idaho",                "cost_mult":0.95,"region":"Mountain"},
    "Meridian":         {"slug":"meridian",          "state":"Idaho",                "cost_mult":1.00,"region":"Mountain"},

    # Montana
    "Billings":         {"slug":"billings",          "state":"Montana",              "cost_mult":0.95,"region":"Mountain"},
    "Missoula":         {"slug":"missoula",          "state":"Montana",              "cost_mult":0.97,"region":"Mountain"},

    # Wyoming
    "Cheyenne":         {"slug":"cheyenne",          "state":"Wyoming",              "cost_mult":0.93,"region":"Mountain"},
    "Casper":           {"slug":"casper",            "state":"Wyoming",              "cost_mult":0.90,"region":"Mountain"},

    # South Dakota
    "Sioux Falls":      {"slug":"sioux-falls",       "state":"South Dakota",         "cost_mult":0.88,"region":"Midwest"},
    "Rapid City":       {"slug":"rapid-city",        "state":"South Dakota",         "cost_mult":0.87,"region":"Midwest"},

    # North Dakota
    "Fargo":            {"slug":"fargo",             "state":"North Dakota",         "cost_mult":0.90,"region":"Midwest"},
    "Bismarck":         {"slug":"bismarck",          "state":"North Dakota",         "cost_mult":0.90,"region":"Midwest"},

    # Nebraska
    "Lincoln":          {"slug":"lincoln",           "state":"Nebraska",             "cost_mult":0.87,"region":"Midwest"},

    # West Virginia
    "Charleston WV":    {"slug":"charleston-wv",     "state":"West Virginia",        "cost_mult":0.83,"region":"South"},
    "Huntington WV":    {"slug":"huntington-wv",     "state":"West Virginia",        "cost_mult":0.80,"region":"South"},

    # Maryland
    "Rockville":        {"slug":"rockville",         "state":"Maryland",             "cost_mult":1.22,"region":"Northeast"},
    "Frederick":        {"slug":"frederick",         "state":"Maryland",             "cost_mult":1.15,"region":"Northeast"},

    # Delaware
    "Wilmington":       {"slug":"wilmington",        "state":"Delaware",             "cost_mult":1.05,"region":"Northeast"},

    # Vermont
    "Burlington VT":    {"slug":"burlington-vt",     "state":"Vermont",              "cost_mult":1.07,"region":"Northeast"},

    # Alaska
    "Anchorage":        {"slug":"anchorage",         "state":"Alaska",               "cost_mult":1.45,"region":"West"},
    "Fairbanks":        {"slug":"fairbanks",         "state":"Alaska",               "cost_mult":1.55,"region":"West"},
}

# Remove None entries
ALL_CITIES = {k: v for k, v in ALL_CITIES.items() if v is not None}

NEW_CITIES = {k: v for k, v in ALL_CITIES.items() if not v.get("existing")}
print(f"New cities to generate: {len(NEW_CITIES)}")

# ─── PROJECT SLUGS (all types) ───────────────────────────────────────────────
ALL_PROJECT_SLUGS = [
    "bathroom-remodel",
    "kitchen-remodel",
    "roof-replacement",
    "drywall-installation",
    "window-replacement",
    "fence-installation",
    "tile-installation",
    "interior-painting",
    "siding-replacement",
]

# ─── IMPORT GENERATORS ───────────────────────────────────────────────────────
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_city_pages import PROJECTS as PROJ_OLD, generate_page as gen_old
from generate_new_calculators import PROJECTS as PROJ_NEW, generate_page as gen_new, build_slugified

PROJ_OLD_KEYS  = set(PROJ_OLD.keys())   # bathroom-remodel, kitchen-remodel, roof-replacement
PROJ_NEW_KEYS  = set(PROJ_NEW.keys())   # drywall, window, fence, tile, painting, siding

def make_page(city_name, city_data, proj_key):
    if proj_key in PROJ_OLD_KEYS:
        return gen_old(city_name, city_data, proj_key, PROJ_OLD[proj_key])
    elif proj_key in PROJ_NEW_KEYS:
        return gen_new(city_name, city_data, proj_key, PROJ_NEW[proj_key])
    else:
        raise ValueError(f"Unknown project: {proj_key}")

def get_slug(city_name, city_data, proj_key):
    if proj_key in PROJ_OLD_KEYS:
        proj = PROJ_OLD[proj_key]
    else:
        proj = PROJ_NEW[proj_key]
    return f"{proj['slug']}-cost-{city_data['slug']}"

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    count = 0

    for city_name, city_data in NEW_CITIES.items():
        for proj_key in ALL_PROJECT_SLUGS:
            slug = get_slug(city_name, city_data, proj_key)
            folder = os.path.join(base_dir, slug)
            if os.path.exists(os.path.join(folder, "index.html")):
                continue  # skip if already exists
            os.makedirs(folder, exist_ok=True)
            html = make_page(city_name, city_data, proj_key)
            with open(os.path.join(folder, "index.html"), "w", encoding="utf-8") as f:
                f.write(html)
            count += 1
        if count % 90 == 0 and count:
            print(f"  {count} pages...")

    print(f"\nDone! {count} new pages generated for {len(NEW_CITIES)} cities.")
    return count

if __name__ == "__main__":
    main()
