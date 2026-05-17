#!/usr/bin/env python3
"""Batch 5 — ~280 new US cities (smaller + missing majors) × all 22 project types."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import generate_new_calculators as calc
import generate_new_projects2 as proj2
import generate_batch4 as b4

NEW_CITIES = {
    # ── Florida (many major cities were missing) ──────────────────────────────
    "Orlando":          {"slug":"orlando",           "state":"Florida",          "cost_mult":1.00,"region":"South"},
    "St. Petersburg":   {"slug":"st-petersburg",     "state":"Florida",          "cost_mult":1.00,"region":"South"},
    "Tallahassee":      {"slug":"tallahassee",       "state":"Florida",          "cost_mult":0.88,"region":"South"},
    "Fort Lauderdale":  {"slug":"fort-lauderdale",   "state":"Florida",          "cost_mult":1.10,"region":"South"},
    "Cape Coral":       {"slug":"cape-coral",        "state":"Florida",          "cost_mult":0.92,"region":"South"},
    "Clearwater":       {"slug":"clearwater",        "state":"Florida",          "cost_mult":1.00,"region":"South"},
    "Hialeah":          {"slug":"hialeah",           "state":"Florida",          "cost_mult":1.08,"region":"South"},
    "Hollywood FL":     {"slug":"hollywood-fl",      "state":"Florida",          "cost_mult":1.05,"region":"South"},
    "Fort Myers":       {"slug":"fort-myers",        "state":"Florida",          "cost_mult":0.97,"region":"South"},
    "Pembroke Pines":   {"slug":"pembroke-pines",    "state":"Florida",          "cost_mult":1.05,"region":"South"},
    "Miramar FL":       {"slug":"miramar-fl",        "state":"Florida",          "cost_mult":1.05,"region":"South"},
    "Brandon FL":       {"slug":"brandon-fl",        "state":"Florida",          "cost_mult":0.95,"region":"South"},
    "Spring Hill FL":   {"slug":"spring-hill-fl",    "state":"Florida",          "cost_mult":0.88,"region":"South"},
    "Gainesville FL":   {"slug":"gainesville-fl",    "state":"Florida",          "cost_mult":0.90,"region":"South"},
    "Ocala":            {"slug":"ocala",             "state":"Florida",          "cost_mult":0.85,"region":"South"},
    "Port St. Lucie":   {"slug":"port-st-lucie",     "state":"Florida",          "cost_mult":0.93,"region":"South"},
    "Boynton Beach":    {"slug":"boynton-beach",     "state":"Florida",          "cost_mult":1.03,"region":"South"},
    "Deerfield Beach":  {"slug":"deerfield-beach",   "state":"Florida",          "cost_mult":1.02,"region":"South"},
    "Pensacola":        {"slug":"pensacola",         "state":"Florida",          "cost_mult":0.87,"region":"South"},
    "Pompano Beach":    {"slug":"pompano-beach",     "state":"Florida",          "cost_mult":1.05,"region":"South"},

    # ── Texas (smaller/suburban) ──────────────────────────────────────────────
    "Frisco":           {"slug":"frisco",            "state":"Texas",            "cost_mult":0.97,"region":"South"},
    "McKinney":         {"slug":"mckinney",          "state":"Texas",            "cost_mult":0.95,"region":"South"},
    "Grand Prairie":    {"slug":"grand-prairie",     "state":"Texas",            "cost_mult":0.92,"region":"South"},
    "Irving":           {"slug":"irving",            "state":"Texas",            "cost_mult":0.93,"region":"South"},
    "Mesquite TX":      {"slug":"mesquite-tx",       "state":"Texas",            "cost_mult":0.91,"region":"South"},
    "Killeen":          {"slug":"killeen",           "state":"Texas",            "cost_mult":0.83,"region":"South"},
    "Harlingen":        {"slug":"harlingen",         "state":"Texas",            "cost_mult":0.78,"region":"South"},
    "Edinburg TX":      {"slug":"edinburg-tx",       "state":"Texas",            "cost_mult":0.78,"region":"South"},
    "Pasadena TX":      {"slug":"pasadena-tx",       "state":"Texas",            "cost_mult":0.90,"region":"South"},
    "Flower Mound":     {"slug":"flower-mound",      "state":"Texas",            "cost_mult":0.97,"region":"South"},
    "Mansfield TX":     {"slug":"mansfield-tx",      "state":"Texas",            "cost_mult":0.93,"region":"South"},
    "North Richland Hills":{"slug":"north-richland-hills","state":"Texas",       "cost_mult":0.92,"region":"South"},
    "Baytown":          {"slug":"baytown",           "state":"Texas",            "cost_mult":0.87,"region":"South"},
    "Georgetown TX":    {"slug":"georgetown-tx",     "state":"Texas",            "cost_mult":0.95,"region":"South"},
    "Cedar Park TX":    {"slug":"cedar-park-tx",     "state":"Texas",            "cost_mult":0.97,"region":"South"},
    "Pflugerville":     {"slug":"pflugerville",      "state":"Texas",            "cost_mult":0.95,"region":"South"},
    "San Marcos TX":    {"slug":"san-marcos-tx",     "state":"Texas",            "cost_mult":0.90,"region":"South"},
    "Temple TX":        {"slug":"temple-tx",         "state":"Texas",            "cost_mult":0.82,"region":"South"},
    "Bryan TX":         {"slug":"bryan-tx",          "state":"Texas",            "cost_mult":0.82,"region":"South"},
    "Mission TX":       {"slug":"mission-tx",        "state":"Texas",            "cost_mult":0.78,"region":"South"},

    # ── New York (missing cities) ─────────────────────────────────────────────
    "Buffalo NY":       {"slug":"buffalo-ny",        "state":"New York",         "cost_mult":1.05,"region":"Northeast"},
    "Rochester NY":     {"slug":"rochester-ny",      "state":"New York",         "cost_mult":1.05,"region":"Northeast"},
    "Albany NY":        {"slug":"albany-ny",         "state":"New York",         "cost_mult":1.10,"region":"Northeast"},
    "Syracuse NY":      {"slug":"syracuse-ny",       "state":"New York",         "cost_mult":1.00,"region":"Northeast"},
    "Yonkers":          {"slug":"yonkers",           "state":"New York",         "cost_mult":1.40,"region":"Northeast"},
    "White Plains":     {"slug":"white-plains",      "state":"New York",         "cost_mult":1.48,"region":"Northeast"},
    "Niagara Falls NY": {"slug":"niagara-falls-ny",  "state":"New York",         "cost_mult":0.95,"region":"Northeast"},

    # ── Georgia (missing cities) ──────────────────────────────────────────────
    "Columbus GA":      {"slug":"columbus-ga",       "state":"Georgia",          "cost_mult":0.82,"region":"South"},
    "Macon":            {"slug":"macon",             "state":"Georgia",          "cost_mult":0.80,"region":"South"},
    "Augusta GA":       {"slug":"augusta-ga",        "state":"Georgia",          "cost_mult":0.82,"region":"South"},
    "Savannah":         {"slug":"savannah",          "state":"Georgia",          "cost_mult":0.87,"region":"South"},
    "Marietta GA":      {"slug":"marietta-ga",       "state":"Georgia",          "cost_mult":0.92,"region":"South"},
    "Smyrna GA":        {"slug":"smyrna-ga",         "state":"Georgia",          "cost_mult":0.90,"region":"South"},
    "Alpharetta":       {"slug":"alpharetta",        "state":"Georgia",          "cost_mult":1.00,"region":"South"},
    "Valdosta":         {"slug":"valdosta",          "state":"Georgia",          "cost_mult":0.78,"region":"South"},
    "Kennesaw GA":      {"slug":"kennesaw-ga",       "state":"Georgia",          "cost_mult":0.87,"region":"South"},
    "Stockbridge GA":   {"slug":"stockbridge-ga",    "state":"Georgia",          "cost_mult":0.85,"region":"South"},

    # ── North Carolina (missing) ──────────────────────────────────────────────
    "Greensboro":       {"slug":"greensboro",        "state":"North Carolina",   "cost_mult":0.90,"region":"South"},
    "Durham":           {"slug":"durham",            "state":"North Carolina",   "cost_mult":0.95,"region":"South"},
    "Winston-Salem":    {"slug":"winston-salem",     "state":"North Carolina",   "cost_mult":0.87,"region":"South"},
    "Fayetteville NC":  {"slug":"fayetteville-nc",   "state":"North Carolina",   "cost_mult":0.85,"region":"South"},
    "Cary":             {"slug":"cary",              "state":"North Carolina",   "cost_mult":1.00,"region":"South"},
    "Apex":             {"slug":"apex",              "state":"North Carolina",   "cost_mult":0.97,"region":"South"},
    "Mooresville":      {"slug":"mooresville",       "state":"North Carolina",   "cost_mult":0.92,"region":"South"},
    "Burlington NC":    {"slug":"burlington-nc",     "state":"North Carolina",   "cost_mult":0.85,"region":"South"},

    # ── Virginia (missing) ────────────────────────────────────────────────────
    "Newport News":     {"slug":"newport-news",      "state":"Virginia",         "cost_mult":0.95,"region":"South"},
    "Chesapeake":       {"slug":"chesapeake",        "state":"Virginia",         "cost_mult":0.95,"region":"South"},
    "Suffolk VA":       {"slug":"suffolk-va",        "state":"Virginia",         "cost_mult":0.90,"region":"South"},
    "Lynchburg":        {"slug":"lynchburg",         "state":"Virginia",         "cost_mult":0.88,"region":"South"},
    "Portsmouth VA":    {"slug":"portsmouth-va",     "state":"Virginia",         "cost_mult":0.88,"region":"South"},
    "Blacksburg":       {"slug":"blacksburg",        "state":"Virginia",         "cost_mult":0.90,"region":"South"},

    # ── Ohio (smaller cities) ─────────────────────────────────────────────────
    "Dayton":           {"slug":"dayton",            "state":"Ohio",             "cost_mult":0.87,"region":"Midwest"},
    "Toledo":           {"slug":"toledo",            "state":"Ohio",             "cost_mult":0.87,"region":"Midwest"},
    "Akron":            {"slug":"akron",             "state":"Ohio",             "cost_mult":0.87,"region":"Midwest"},
    "Springfield OH":   {"slug":"springfield-oh",    "state":"Ohio",             "cost_mult":0.83,"region":"Midwest"},
    "Kettering":        {"slug":"kettering",         "state":"Ohio",             "cost_mult":0.87,"region":"Midwest"},
    "Elyria":           {"slug":"elyria",            "state":"Ohio",             "cost_mult":0.85,"region":"Midwest"},
    "Fairfield OH":     {"slug":"fairfield-oh",      "state":"Ohio",             "cost_mult":0.87,"region":"Midwest"},
    "Mansfield OH":     {"slug":"mansfield-oh",      "state":"Ohio",             "cost_mult":0.83,"region":"Midwest"},
    "Lima OH":          {"slug":"lima-oh",           "state":"Ohio",             "cost_mult":0.80,"region":"Midwest"},

    # ── Michigan (suburban) ───────────────────────────────────────────────────
    "Sterling Heights": {"slug":"sterling-heights",  "state":"Michigan",         "cost_mult":0.95,"region":"Midwest"},
    "Warren MI":        {"slug":"warren-mi",         "state":"Michigan",         "cost_mult":0.90,"region":"Midwest"},
    "Ann Arbor":        {"slug":"ann-arbor",         "state":"Michigan",         "cost_mult":1.02,"region":"Midwest"},
    "Lansing":          {"slug":"lansing",           "state":"Michigan",         "cost_mult":0.88,"region":"Midwest"},
    "Clinton Township": {"slug":"clinton-township",  "state":"Michigan",         "cost_mult":0.90,"region":"Midwest"},
    "Pontiac MI":       {"slug":"pontiac-mi",        "state":"Michigan",         "cost_mult":0.87,"region":"Midwest"},
    "Rochester Hills":  {"slug":"rochester-hills",   "state":"Michigan",         "cost_mult":0.97,"region":"Midwest"},
    "Farmington Hills": {"slug":"farmington-hills",  "state":"Michigan",         "cost_mult":1.00,"region":"Midwest"},
    "Battle Creek":     {"slug":"battle-creek",      "state":"Michigan",         "cost_mult":0.83,"region":"Midwest"},
    "Muskegon":         {"slug":"muskegon",          "state":"Michigan",         "cost_mult":0.80,"region":"Midwest"},

    # ── Indiana (smaller) ─────────────────────────────────────────────────────
    "Hammond IN":       {"slug":"hammond-in",        "state":"Indiana",          "cost_mult":0.92,"region":"Midwest"},
    "Gary IN":          {"slug":"gary-in",           "state":"Indiana",          "cost_mult":0.87,"region":"Midwest"},
    "Noblesville":      {"slug":"noblesville",       "state":"Indiana",          "cost_mult":0.93,"region":"Midwest"},
    "Greenwood IN":     {"slug":"greenwood-in",      "state":"Indiana",          "cost_mult":0.90,"region":"Midwest"},
    "Anderson IN":      {"slug":"anderson-in",       "state":"Indiana",          "cost_mult":0.82,"region":"Midwest"},
    "Kokomo":           {"slug":"kokomo",            "state":"Indiana",          "cost_mult":0.80,"region":"Midwest"},

    # ── Missouri (smaller) ────────────────────────────────────────────────────
    "Florissant":       {"slug":"florissant",        "state":"Missouri",         "cost_mult":0.88,"region":"Midwest"},
    "Blue Springs MO":  {"slug":"blue-springs-mo",   "state":"Missouri",         "cost_mult":0.90,"region":"Midwest"},
    "Joplin":           {"slug":"joplin",            "state":"Missouri",         "cost_mult":0.80,"region":"Midwest"},
    "Jefferson City":   {"slug":"jefferson-city",    "state":"Missouri",         "cost_mult":0.85,"region":"Midwest"},
    "Chesterfield MO":  {"slug":"chesterfield-mo",   "state":"Missouri",         "cost_mult":0.97,"region":"Midwest"},

    # ── Tennessee (smaller) ───────────────────────────────────────────────────
    "Brentwood TN":     {"slug":"brentwood-tn",      "state":"Tennessee",        "cost_mult":1.00,"region":"South"},
    "Bartlett TN":      {"slug":"bartlett-tn",       "state":"Tennessee",        "cost_mult":0.87,"region":"South"},
    "Hendersonville TN":{"slug":"hendersonville-tn", "state":"Tennessee",        "cost_mult":0.90,"region":"South"},
    "Spring Hill TN":   {"slug":"spring-hill-tn",    "state":"Tennessee",        "cost_mult":0.90,"region":"South"},
    "Collierville":     {"slug":"collierville",      "state":"Tennessee",        "cost_mult":0.90,"region":"South"},
    "Mount Juliet TN":  {"slug":"mount-juliet-tn",   "state":"Tennessee",        "cost_mult":0.90,"region":"South"},
    "Germantown TN":    {"slug":"germantown-tn",     "state":"Tennessee",        "cost_mult":0.93,"region":"South"},

    # ── South Carolina (smaller) ──────────────────────────────────────────────
    "Mount Pleasant SC":{"slug":"mount-pleasant-sc", "state":"South Carolina",   "cost_mult":1.00,"region":"South"},
    "Hilton Head":      {"slug":"hilton-head",       "state":"South Carolina",   "cost_mult":1.05,"region":"South"},
    "Aiken SC":         {"slug":"aiken-sc",          "state":"South Carolina",   "cost_mult":0.85,"region":"South"},
    "Goose Creek":      {"slug":"goose-creek",       "state":"South Carolina",   "cost_mult":0.90,"region":"South"},
    "Anderson SC":      {"slug":"anderson-sc",       "state":"South Carolina",   "cost_mult":0.83,"region":"South"},
    "Conway SC":        {"slug":"conway-sc",         "state":"South Carolina",   "cost_mult":0.82,"region":"South"},

    # ── Alabama (smaller) ─────────────────────────────────────────────────────
    "Hoover":           {"slug":"hoover",            "state":"Alabama",          "cost_mult":0.87,"region":"South"},
    "Madison AL":       {"slug":"madison-al",        "state":"Alabama",          "cost_mult":0.87,"region":"South"},
    "Vestavia Hills":   {"slug":"vestavia-hills",    "state":"Alabama",          "cost_mult":0.90,"region":"South"},
    "Florence AL":      {"slug":"florence-al",       "state":"Alabama",          "cost_mult":0.80,"region":"South"},
    "Prattville":       {"slug":"prattville",        "state":"Alabama",          "cost_mult":0.80,"region":"South"},

    # ── Louisiana (smaller) ───────────────────────────────────────────────────
    "Alexandria LA":    {"slug":"alexandria-la",     "state":"Louisiana",        "cost_mult":0.82,"region":"South"},
    "Slidell":          {"slug":"slidell",           "state":"Louisiana",        "cost_mult":0.85,"region":"South"},
    "Houma":            {"slug":"houma",             "state":"Louisiana",        "cost_mult":0.83,"region":"South"},
    "Bossier City":     {"slug":"bossier-city",      "state":"Louisiana",        "cost_mult":0.82,"region":"South"},

    # ── Kentucky (smaller) ────────────────────────────────────────────────────
    "Frankfort KY":     {"slug":"frankfort-ky",      "state":"Kentucky",         "cost_mult":0.83,"region":"South"},
    "Henderson KY":     {"slug":"henderson-ky",      "state":"Kentucky",         "cost_mult":0.82,"region":"South"},
    "Hopkinsville":     {"slug":"hopkinsville",      "state":"Kentucky",         "cost_mult":0.78,"region":"South"},
    "Richmond KY":      {"slug":"richmond-ky",       "state":"Kentucky",         "cost_mult":0.80,"region":"South"},
    "Florence KY":      {"slug":"florence-ky",       "state":"Kentucky",         "cost_mult":0.88,"region":"South"},

    # ── Maryland (suburbs) ────────────────────────────────────────────────────
    "Frederick MD":     {"slug":"frederick-md",      "state":"Maryland",         "cost_mult":1.08,"region":"Northeast"},
    "Rockville":        {"slug":"rockville",         "state":"Maryland",         "cost_mult":1.25,"region":"Northeast"},
    "Silver Spring":    {"slug":"silver-spring",     "state":"Maryland",         "cost_mult":1.25,"region":"Northeast"},
    "Germantown MD":    {"slug":"germantown-md",     "state":"Maryland",         "cost_mult":1.15,"region":"Northeast"},
    "Columbia MD":      {"slug":"columbia-md",       "state":"Maryland",         "cost_mult":1.18,"region":"Northeast"},
    "Ellicott City":    {"slug":"ellicott-city",     "state":"Maryland",         "cost_mult":1.20,"region":"Northeast"},
    "Towson":           {"slug":"towson",            "state":"Maryland",         "cost_mult":1.10,"region":"Northeast"},

    # ── New Jersey (more) ─────────────────────────────────────────────────────
    "Paterson":         {"slug":"paterson",          "state":"New Jersey",       "cost_mult":1.25,"region":"Northeast"},
    "Elizabeth NJ":     {"slug":"elizabeth-nj",      "state":"New Jersey",       "cost_mult":1.28,"region":"Northeast"},
    "Lakewood NJ":      {"slug":"lakewood-nj",       "state":"New Jersey",       "cost_mult":1.18,"region":"Northeast"},
    "Cherry Hill":      {"slug":"cherry-hill",       "state":"New Jersey",       "cost_mult":1.15,"region":"Northeast"},
    "Passaic":          {"slug":"passaic",           "state":"New Jersey",       "cost_mult":1.22,"region":"Northeast"},
    "Union City NJ":    {"slug":"union-city-nj",     "state":"New Jersey",       "cost_mult":1.30,"region":"Northeast"},
    "Bayonne":          {"slug":"bayonne",           "state":"New Jersey",       "cost_mult":1.25,"region":"Northeast"},
    "Hamilton NJ":      {"slug":"hamilton-nj",       "state":"New Jersey",       "cost_mult":1.15,"region":"Northeast"},
    "Vineland":         {"slug":"vineland",          "state":"New Jersey",       "cost_mult":1.05,"region":"Northeast"},

    # ── Massachusetts (more) ──────────────────────────────────────────────────
    "Cambridge":        {"slug":"cambridge",         "state":"Massachusetts",    "cost_mult":1.55,"region":"Northeast"},
    "Fall River":       {"slug":"fall-river",        "state":"Massachusetts",    "cost_mult":1.10,"region":"Northeast"},
    "Somerville MA":    {"slug":"somerville-ma",     "state":"Massachusetts",    "cost_mult":1.45,"region":"Northeast"},
    "Newton MA":        {"slug":"newton-ma",         "state":"Massachusetts",    "cost_mult":1.50,"region":"Northeast"},
    "Haverhill":        {"slug":"haverhill",         "state":"Massachusetts",    "cost_mult":1.15,"region":"Northeast"},
    "Waltham":          {"slug":"waltham",           "state":"Massachusetts",    "cost_mult":1.35,"region":"Northeast"},
    "Framingham":       {"slug":"framingham",        "state":"Massachusetts",    "cost_mult":1.30,"region":"Northeast"},

    # ── Connecticut (more) ────────────────────────────────────────────────────
    "New Britain CT":   {"slug":"new-britain-ct",    "state":"Connecticut",      "cost_mult":1.05,"region":"Northeast"},
    "Bristol CT":       {"slug":"bristol-ct",        "state":"Connecticut",      "cost_mult":1.08,"region":"Northeast"},
    "Milford CT":       {"slug":"milford-ct",        "state":"Connecticut",      "cost_mult":1.18,"region":"Northeast"},
    "West Haven":       {"slug":"west-haven",        "state":"Connecticut",      "cost_mult":1.12,"region":"Northeast"},
    "Greenwich CT":     {"slug":"greenwich-ct",      "state":"Connecticut",      "cost_mult":1.55,"region":"Northeast"},

    # ── Washington state (more) ───────────────────────────────────────────────
    "Vancouver WA":     {"slug":"vancouver-wa",      "state":"Washington",       "cost_mult":1.10,"region":"West"},
    "Marysville WA":    {"slug":"marysville-wa",     "state":"Washington",       "cost_mult":1.05,"region":"West"},
    "Yakima":           {"slug":"yakima",            "state":"Washington",       "cost_mult":0.90,"region":"West"},
    "Kennewick":        {"slug":"kennewick",         "state":"Washington",       "cost_mult":0.88,"region":"West"},
    "Richland WA":      {"slug":"richland-wa",       "state":"Washington",       "cost_mult":0.90,"region":"West"},
    "Pasco WA":         {"slug":"pasco-wa",          "state":"Washington",       "cost_mult":0.87,"region":"West"},

    # ── Oregon (more) ────────────────────────────────────────────────────────
    "Beaverton":        {"slug":"beaverton",         "state":"Oregon",           "cost_mult":1.12,"region":"West"},
    "Lake Oswego":      {"slug":"lake-oswego",       "state":"Oregon",           "cost_mult":1.20,"region":"West"},
    "Tigard":           {"slug":"tigard",            "state":"Oregon",           "cost_mult":1.10,"region":"West"},
    "Albany OR":        {"slug":"albany-or",         "state":"Oregon",           "cost_mult":0.95,"region":"West"},
    "Grants Pass":      {"slug":"grants-pass",       "state":"Oregon",           "cost_mult":0.87,"region":"West"},

    # ── Colorado (more suburbs) ───────────────────────────────────────────────
    "Englewood CO":     {"slug":"englewood-co",      "state":"Colorado",         "cost_mult":1.05,"region":"Mountain"},
    "Highlands Ranch":  {"slug":"highlands-ranch",   "state":"Colorado",         "cost_mult":1.08,"region":"Mountain"},
    "Parker CO":        {"slug":"parker-co",         "state":"Colorado",         "cost_mult":1.05,"region":"Mountain"},
    "Broomfield":       {"slug":"broomfield",        "state":"Colorado",         "cost_mult":1.05,"region":"Mountain"},
    "Brighton CO":      {"slug":"brighton-co",       "state":"Colorado",         "cost_mult":0.98,"region":"Mountain"},

    # ── Minnesota (suburbs) ───────────────────────────────────────────────────
    "Eagan":            {"slug":"eagan",             "state":"Minnesota",        "cost_mult":1.05,"region":"Midwest"},
    "Eden Prairie":     {"slug":"eden-prairie",      "state":"Minnesota",        "cost_mult":1.08,"region":"Midwest"},
    "Burnsville MN":    {"slug":"burnsville-mn",     "state":"Minnesota",        "cost_mult":1.00,"region":"Midwest"},
    "Lakeville MN":     {"slug":"lakeville-mn",      "state":"Minnesota",        "cost_mult":1.00,"region":"Midwest"},
    "Woodbury MN":      {"slug":"woodbury-mn",       "state":"Minnesota",        "cost_mult":1.05,"region":"Midwest"},
    "St. Cloud MN":     {"slug":"st-cloud-mn",       "state":"Minnesota",        "cost_mult":0.90,"region":"Midwest"},
    "Apple Valley MN":  {"slug":"apple-valley-mn",   "state":"Minnesota",        "cost_mult":1.00,"region":"Midwest"},
    "Minnetonka":       {"slug":"minnetonka",        "state":"Minnesota",        "cost_mult":1.08,"region":"Midwest"},

    # ── Wisconsin (more) ──────────────────────────────────────────────────────
    "West Allis":       {"slug":"west-allis",        "state":"Wisconsin",        "cost_mult":0.93,"region":"Midwest"},
    "Fond du Lac":      {"slug":"fond-du-lac",       "state":"Wisconsin",        "cost_mult":0.87,"region":"Midwest"},
    "Sheboygan":        {"slug":"sheboygan",         "state":"Wisconsin",        "cost_mult":0.87,"region":"Midwest"},
    "Wauwatosa":        {"slug":"wauwatosa",         "state":"Wisconsin",        "cost_mult":0.95,"region":"Midwest"},
    "La Crosse":        {"slug":"la-crosse",         "state":"Wisconsin",        "cost_mult":0.90,"region":"Midwest"},
    "Beloit WI":        {"slug":"beloit-wi",         "state":"Wisconsin",        "cost_mult":0.85,"region":"Midwest"},

    # ── Arizona (more) ────────────────────────────────────────────────────────
    "Casa Grande":      {"slug":"casa-grande",       "state":"Arizona",          "cost_mult":0.87,"region":"South"},
    "Prescott":         {"slug":"prescott",          "state":"Arizona",          "cost_mult":0.92,"region":"Mountain"},
    "Lake Havasu City": {"slug":"lake-havasu-city",  "state":"Arizona",          "cost_mult":0.90,"region":"South"},
    "Sierra Vista":     {"slug":"sierra-vista",      "state":"Arizona",          "cost_mult":0.85,"region":"South"},
    "Apache Junction":  {"slug":"apache-junction",   "state":"Arizona",          "cost_mult":0.90,"region":"South"},
    "El Mirage":        {"slug":"el-mirage",         "state":"Arizona",          "cost_mult":0.90,"region":"South"},

    # ── Utah (suburbs) ────────────────────────────────────────────────────────
    "Sandy UT":         {"slug":"sandy-ut",          "state":"Utah",             "cost_mult":1.02,"region":"Mountain"},
    "West Jordan":      {"slug":"west-jordan",       "state":"Utah",             "cost_mult":1.00,"region":"Mountain"},
    "Murray UT":        {"slug":"murray-ut",         "state":"Utah",             "cost_mult":1.00,"region":"Mountain"},
    "Orem":             {"slug":"orem",              "state":"Utah",             "cost_mult":0.98,"region":"Mountain"},
    "Taylorsville":     {"slug":"taylorsville",      "state":"Utah",             "cost_mult":0.98,"region":"Mountain"},

    # ── Idaho (more) ──────────────────────────────────────────────────────────
    "Nampa":            {"slug":"nampa",             "state":"Idaho",            "cost_mult":0.92,"region":"Mountain"},
    "Meridian ID":      {"slug":"meridian-id",       "state":"Idaho",            "cost_mult":0.95,"region":"Mountain"},
    "Twin Falls":       {"slug":"twin-falls",        "state":"Idaho",            "cost_mult":0.87,"region":"Mountain"},
    "Caldwell ID":      {"slug":"caldwell-id",       "state":"Idaho",            "cost_mult":0.88,"region":"Mountain"},

    # ── Kansas (more) ────────────────────────────────────────────────────────
    "Olathe":           {"slug":"olathe",            "state":"Kansas",           "cost_mult":0.93,"region":"Midwest"},
    "Lenexa":           {"slug":"lenexa",            "state":"Kansas",           "cost_mult":0.93,"region":"Midwest"},
    "Shawnee KS":       {"slug":"shawnee-ks",        "state":"Kansas",           "cost_mult":0.90,"region":"Midwest"},
    "Salina KS":        {"slug":"salina-ks",         "state":"Kansas",           "cost_mult":0.82,"region":"Midwest"},

    # ── Oklahoma (more) ──────────────────────────────────────────────────────
    "Stillwater OK":    {"slug":"stillwater-ok",     "state":"Oklahoma",         "cost_mult":0.83,"region":"South"},
    "Moore OK":         {"slug":"moore-ok",          "state":"Oklahoma",         "cost_mult":0.87,"region":"South"},
    "Enid":             {"slug":"enid",              "state":"Oklahoma",         "cost_mult":0.80,"region":"South"},

    # ── Nevada (more) ────────────────────────────────────────────────────────
    "Sunrise Manor":    {"slug":"sunrise-manor",     "state":"Nevada",           "cost_mult":0.97,"region":"West"},
    "Paradise NV":      {"slug":"paradise-nv",       "state":"Nevada",           "cost_mult":1.00,"region":"West"},

    # ── Pennsylvania (more) ──────────────────────────────────────────────────
    "Allentown":        {"slug":"allentown",         "state":"Pennsylvania",     "cost_mult":1.00,"region":"Northeast"},
    "Pittsburgh":       {"slug":"pittsburgh",        "state":"Pennsylvania",     "cost_mult":1.05,"region":"Northeast"},
    "Upper Darby":      {"slug":"upper-darby",       "state":"Pennsylvania",     "cost_mult":1.08,"region":"Northeast"},
    "Levittown PA":     {"slug":"levittown-pa",      "state":"Pennsylvania",     "cost_mult":1.05,"region":"Northeast"},

    # ── Illinois (more) ──────────────────────────────────────────────────────
    "Rockford":         {"slug":"rockford",          "state":"Illinois",         "cost_mult":0.88,"region":"Midwest"},
    "Aurora IL":        {"slug":"aurora-il",         "state":"Illinois",         "cost_mult":0.95,"region":"Midwest"},
    "Naperville":       {"slug":"naperville",        "state":"Illinois",         "cost_mult":1.05,"region":"Midwest"},
    "Joliet":           {"slug":"joliet",            "state":"Illinois",         "cost_mult":0.95,"region":"Midwest"},
    "Peoria IL":        {"slug":"peoria-il",         "state":"Illinois",         "cost_mult":0.87,"region":"Midwest"},
    "Springfield IL":   {"slug":"springfield-il",    "state":"Illinois",         "cost_mult":0.90,"region":"Midwest"},
    "Waukegan IL":      {"slug":"waukegan-il",       "state":"Illinois",         "cost_mult":0.97,"region":"Midwest"},
    "Bolingbrook":      {"slug":"bolingbrook",       "state":"Illinois",         "cost_mult":0.97,"region":"Midwest"},

    # ── California (more smaller cities) ────────────────────────────────────
    "Burbank":          {"slug":"burbank",           "state":"California",       "cost_mult":1.25,"region":"West"},
    "Santa Barbara":    {"slug":"santa-barbara",     "state":"California",       "cost_mult":1.40,"region":"West"},
    "Inglewood":        {"slug":"inglewood",         "state":"California",       "cost_mult":1.20,"region":"West"},
    "West Covina":      {"slug":"west-covina",       "state":"California",       "cost_mult":1.18,"region":"West"},
    "Costa Mesa":       {"slug":"costa-mesa",        "state":"California",       "cost_mult":1.28,"region":"West"},
    "Richmond CA":      {"slug":"richmond-ca",       "state":"California",       "cost_mult":1.30,"region":"West"},
    "Downey":           {"slug":"downey",            "state":"California",       "cost_mult":1.18,"region":"West"},
    "El Cajon":         {"slug":"el-cajon",          "state":"California",       "cost_mult":1.10,"region":"West"},
    "Fairfield CA":     {"slug":"fairfield-ca",      "state":"California",       "cost_mult":1.08,"region":"West"},
    "Santa Clara":      {"slug":"santa-clara",       "state":"California",       "cost_mult":1.42,"region":"West"},
    "Berkeley":         {"slug":"berkeley",          "state":"California",       "cost_mult":1.45,"region":"West"},
    "Norwalk CA":       {"slug":"norwalk-ca",        "state":"California",       "cost_mult":1.18,"region":"West"},
    "Daly City":        {"slug":"daly-city",         "state":"California",       "cost_mult":1.38,"region":"West"},
    "San Mateo":        {"slug":"san-mateo",         "state":"California",       "cost_mult":1.48,"region":"West"},
    "Thousand Oaks":    {"slug":"thousand-oaks",     "state":"California",       "cost_mult":1.22,"region":"West"},
    "Simi Valley":      {"slug":"simi-valley",       "state":"California",       "cost_mult":1.18,"region":"West"},

    # ── Mississippi (more) ───────────────────────────────────────────────────
    "Tupelo":           {"slug":"tupelo",            "state":"Mississippi",      "cost_mult":0.78,"region":"South"},
    "Meridian MS":      {"slug":"meridian-ms",       "state":"Mississippi",      "cost_mult":0.78,"region":"South"},
    "Olive Branch":     {"slug":"olive-branch",      "state":"Mississippi",      "cost_mult":0.82,"region":"South"},

    # ── Arkansas (more) ──────────────────────────────────────────────────────
    "Bentonville":      {"slug":"bentonville",       "state":"Arkansas",         "cost_mult":0.85,"region":"South"},
    "Hot Springs AR":   {"slug":"hot-springs-ar",    "state":"Arkansas",         "cost_mult":0.80,"region":"South"},
    "Pine Bluff":       {"slug":"pine-bluff",        "state":"Arkansas",         "cost_mult":0.75,"region":"South"},

    # ── Iowa (more) ──────────────────────────────────────────────────────────
    "Ames IA":          {"slug":"ames-ia",           "state":"Iowa",             "cost_mult":0.88,"region":"Midwest"},
    "Iowa City":        {"slug":"iowa-city",         "state":"Iowa",             "cost_mult":0.90,"region":"Midwest"},
    "Council Bluffs":   {"slug":"council-bluffs",    "state":"Iowa",             "cost_mult":0.85,"region":"Midwest"},

    # ── Nebraska (more) ──────────────────────────────────────────────────────
    "Papillion NE":     {"slug":"papillion-ne",      "state":"Nebraska",         "cost_mult":0.90,"region":"Midwest"},
    "Hastings NE":      {"slug":"hastings-ne",       "state":"Nebraska",         "cost_mult":0.82,"region":"Midwest"},

    # ── West Virginia (more) ─────────────────────────────────────────────────
    "Charleston WV":    {"slug":"charleston-wv",     "state":"West Virginia",    "cost_mult":0.83,"region":"South"},
    "Huntington WV":    {"slug":"huntington-wv",     "state":"West Virginia",    "cost_mult":0.80,"region":"South"},

    # ── New Mexico (more) ────────────────────────────────────────────────────
    "Clovis NM":        {"slug":"clovis-nm",         "state":"New Mexico",       "cost_mult":0.78,"region":"Mountain"},
    "Hobbs NM":         {"slug":"hobbs-nm",          "state":"New Mexico",       "cost_mult":0.78,"region":"Mountain"},

    # ── Montana (more) ───────────────────────────────────────────────────────
    "Missoula":         {"slug":"missoula",          "state":"Montana",          "cost_mult":0.92,"region":"Mountain"},
    "Kalispell":        {"slug":"kalispell",         "state":"Montana",          "cost_mult":0.88,"region":"Mountain"},

    # ── Alaska ────────────────────────────────────────────────────────────────
    "Fairbanks":        {"slug":"fairbanks",         "state":"Alaska",           "cost_mult":1.45,"region":"West"},
    "Juneau":           {"slug":"juneau",            "state":"Alaska",           "cost_mult":1.55,"region":"West"},
}

# ─── HELPERS ──────────────────────────────────────────────────────────────────
def save_page(out_dir, html):
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "index.html"), "w") as f:
        f.write(html)

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    cities = NEW_CITIES
    n_proj1 = len(calc.PROJECTS)
    n_proj2 = len(proj2.PROJECTS)
    n_proj4 = len(b4.PROJECTS)
    total_proj = n_proj1 + n_proj2 + n_proj4
    est = len(cities) * total_proj
    print(f"Cities: {len(cities)}")
    print(f"Project types: {total_proj} ({n_proj1} original + {n_proj2} proj2 + {n_proj4} batch4)")
    print(f"Estimated pages: {est:,}")

    total = 0

    # original 9 types (generate_new_calculators)
    for proj_key, proj in calc.PROJECTS.items():
        for city_name, city_data in cities.items():
            slug = calc.build_slugified(city_name, proj, city_data)
            out_dir = os.path.join(base_dir, slug)
            html = calc.generate_page(city_name, city_data, proj_key, proj)
            save_page(out_dir, html)
            total += 1
        print(f"  {proj['name']} ({n_proj1} types)... {len(cities)} pages")

    # 5 new types (generate_new_projects2)
    for proj_key, proj in proj2.PROJECTS.items():
        for city_name, city_data in cities.items():
            city_slug = city_data.get("slug", city_name.lower().replace(" ", "-"))
            out_dir = os.path.join(base_dir, f"{proj['slug']}-cost-{city_slug}")
            html = proj2.generate_page(city_name, city_data, proj_key, proj)
            save_page(out_dir, html)
            total += 1
        print(f"  {proj['name']} ({n_proj2} types)... {len(cities)} pages")

    # 8 batch4 types
    for proj_key, proj in b4.PROJECTS.items():
        for city_name, city_data in cities.items():
            city_slug = city_data.get("slug", city_name.lower().replace(" ", "-"))
            out_dir = os.path.join(base_dir, f"{proj['slug']}-cost-{city_slug}")
            html = proj2.generate_page(city_name, city_data, proj_key, proj)
            save_page(out_dir, html)
            total += 1
        print(f"  {proj['name']} ({n_proj4} types)... {len(cities)} pages")

    print(f"\nDone! {total:,} pages generated.")

if __name__ == "__main__":
    main()
