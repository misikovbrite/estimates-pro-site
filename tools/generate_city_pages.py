#!/usr/bin/env python3
"""Generate city × project cost calculator pages for programmatic SEO."""
import os
import json
import re

# ─── CITY DATA ──────────────────────────────────────────────────────────────
# cost_mult: multiplier vs national average
# state: full state name for SEO
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
}

# ─── PROJECT DATA ────────────────────────────────────────────────────────────
PROJECTS = {
    "bathroom-remodel": {
        "name": "Bathroom Remodel",
        "slug": "bathroom-remodel",
        "title_tmpl": "Bathroom Remodel Cost in {city}, {state} (2026)",
        "desc_tmpl": "How much does a bathroom remodel cost in {city}? Use our free calculator to estimate your project — updated 2026 prices for labor and materials in {city}, {state}.",
        "h1_tmpl": "Bathroom Remodel Cost in {city}",
        "intro_tmpl": "Planning a bathroom renovation in {city}, {state}? Costs here are {cost_vs_avg} the national average, driven by local labor rates and material costs in the {region} region. Use the calculator below to estimate your project budget.",
        "base_low": 4500,
        "base_mid": 12000,
        "base_high": 28000,
        "items": [
            {"label": "Toilet replacement", "base": 400, "checked": True},
            {"label": "Bathtub installation", "base": 1800, "checked": False},
            {"label": "Walk-in shower", "base": 2200, "checked": True},
            {"label": "Vanity & sink", "base": 900, "checked": True},
            {"label": "Wall tile & backsplash", "base": 1400, "checked": False},
            {"label": "Flooring (tile/vinyl)", "base": 800, "checked": True},
            {"label": "Lighting & electrical", "base": 600, "checked": False},
            {"label": "Plumbing rough-in", "base": 1200, "checked": False},
            {"label": "Exhaust fan & ventilation", "base": 350, "checked": False},
            {"label": "Paint & finish", "base": 280, "checked": True},
        ],
        "faq": [
            ("How much does a bathroom remodel cost in {city}?",
             "A bathroom remodel in {city} typically costs between ${low} and ${high}, with an average around ${mid}. Small cosmetic updates start around ${low}, while full gut renovations with high-end finishes can exceed ${high}."),
            ("Is a bathroom remodel worth it in {city}?",
             "Yes — bathroom remodels in {city} typically return 60–70% of the investment at resale. A mid-range remodel adds an average of ${return_value} in home value while significantly improving daily comfort."),
            ("How long does a bathroom remodel take in {city}?",
             "Most bathroom remodels in {city} take 1–3 weeks for a standard update, or 3–6 weeks for a full gut renovation requiring new plumbing or tile work."),
            ("What's the biggest cost driver in a {city} bathroom remodel?",
             "Labor is typically 40–60% of the total cost. {city} contractors charge ${labor_low}–${labor_high}/hour depending on trade. Tile work, plumbing, and electrical are the most labor-intensive items."),
        ],
        "cost_table_rows": [
            ("Cosmetic update (paint, fixtures, lighting)", "${low}", "${low_high}"),
            ("Partial remodel (vanity, flooring, toilet)", "${low_high}", "${mid_low}"),
            ("Full remodel (all fixtures, tile, plumbing)", "${mid_low}", "${mid}"),
            ("Luxury / primary suite renovation", "${mid}", "${high}"),
        ],
    },
    "kitchen-remodel": {
        "name": "Kitchen Remodel",
        "slug": "kitchen-remodel",
        "title_tmpl": "Kitchen Remodel Cost in {city}, {state} (2026)",
        "desc_tmpl": "How much does a kitchen remodel cost in {city}? Free calculator with 2026 prices for cabinets, countertops, appliances, and labor in {city}, {state}.",
        "h1_tmpl": "Kitchen Remodel Cost in {city}",
        "intro_tmpl": "Kitchen renovation costs in {city}, {state} run {cost_vs_avg} the national average. The {region} region's labor market and material supply chains directly affect your project budget. Enter your scope below for a personalized estimate.",
        "base_low": 10000,
        "base_mid": 30000,
        "base_high": 75000,
        "items": [
            {"label": "Cabinets (stock/semi-custom)", "base": 6000, "checked": True},
            {"label": "Countertops (quartz/granite)", "base": 4500, "checked": True},
            {"label": "Appliances (fridge/range/DW)", "base": 5000, "checked": False},
            {"label": "Flooring (hardwood/tile)", "base": 3500, "checked": True},
            {"label": "Backsplash tile", "base": 1800, "checked": False},
            {"label": "Lighting & electrical", "base": 2000, "checked": False},
            {"label": "Plumbing (sink/faucet/disposal)", "base": 1500, "checked": True},
            {"label": "Island addition", "base": 4000, "checked": False},
            {"label": "Paint & drywall", "base": 1200, "checked": True},
            {"label": "Permits & inspections", "base": 800, "checked": True},
        ],
        "faq": [
            ("How much does a kitchen remodel cost in {city}?",
             "Kitchen remodels in {city} range from ${low} for minor updates to ${high}+ for full custom renovations. Most homeowners spend ${mid} on a mid-range kitchen remodel in {city}."),
            ("What adds the most value in a {city} kitchen remodel?",
             "Cabinets, countertops, and appliances together drive 60–70% of kitchen remodel value. In {city}'s market, quality countertops and updated appliances typically yield the best ROI."),
            ("How long does a kitchen remodel take in {city}?",
             "A standard kitchen remodel in {city} takes 3–8 weeks. Full gut renovations with custom cabinets can take 10–14 weeks due to lead times for custom orders."),
            ("Do I need permits for a kitchen remodel in {city}?",
             "Most kitchen remodels in {city}, {state} require permits for electrical, plumbing, and structural work. Budget ${permit_cost} for permits. Your contractor should pull all required permits."),
        ],
        "cost_table_rows": [
            ("Cosmetic refresh (paint, hardware, lighting)", "${low}", "${low_high}"),
            ("Mid update (countertops, sink, appliances)", "${low_high}", "${mid_low}"),
            ("Full remodel (cabinets, counters, flooring)", "${mid_low}", "${mid}"),
            ("Luxury / full custom kitchen", "${mid}", "${high}"),
        ],
    },
    "roof-replacement": {
        "name": "Roof Replacement",
        "slug": "roof-replacement",
        "title_tmpl": "Roof Replacement Cost in {city}, {state} (2026)",
        "desc_tmpl": "How much does roof replacement cost in {city}? Free calculator with 2026 prices per square for asphalt, metal, and tile roofing in {city}, {state}.",
        "h1_tmpl": "Roof Replacement Cost in {city}",
        "intro_tmpl": "Roof replacement in {city}, {state} costs {cost_vs_avg} the national average. Local weather patterns, roofing material availability, and contractor demand in the {region} region all affect pricing. Use our calculator for a quick estimate.",
        "base_low": 5500,
        "base_mid": 11000,
        "base_high": 24000,
        "items": [
            {"label": "Asphalt shingle removal (tear-off)", "base": 1500, "checked": True},
            {"label": "Decking repair / plywood replacement", "base": 800, "checked": False},
            {"label": "Underlayment & ice/water shield", "base": 1200, "checked": True},
            {"label": "Asphalt shingles (30-year)", "base": 4500, "checked": True},
            {"label": "Ridge cap & hip shingles", "base": 600, "checked": True},
            {"label": "Flashing (chimney, valleys, vents)", "base": 900, "checked": False},
            {"label": "Gutters & downspouts", "base": 1800, "checked": False},
            {"label": "Skylights (repair/reseal)", "base": 700, "checked": False},
            {"label": "Fascia & soffit repair", "base": 1100, "checked": False},
            {"label": "Attic ventilation upgrade", "base": 600, "checked": False},
        ],
        "faq": [
            ("How much does roof replacement cost in {city}?",
             "Roof replacement in {city} costs ${low}–${high} for a typical 2,000 sq ft home, with an average around ${mid}. Premium materials like metal or tile can exceed ${high}."),
            ("How often do roofs need replacement in {city}?",
             "In {city}'s {region} climate, asphalt shingle roofs typically last 20–30 years. Harsh weather, UV exposure, and storm damage can accelerate wear. Regular inspections after major storms help identify issues early."),
            ("Should I repair or replace my roof in {city}?",
             "If your roof is under 15 years old and damage is limited to a small area, repair (${repair_low}–${repair_high}) often makes sense. If the roof is 20+ years old or damage covers 30%+ of the surface, replacement is more cost-effective long-term."),
            ("What roofing materials are popular in {city}?",
             "Asphalt shingles dominate {city}'s market due to cost and durability. Metal roofing is growing in popularity for its longevity (40–70 years) at a premium of ${metal_premium}% above asphalt."),
        ],
        "cost_table_rows": [
            ("Roof repair (limited area)", "${repair_low}", "${repair_high}"),
            ("Asphalt shingle replacement (1,500 sqft)", "${low}", "${mid_low}"),
            ("Standard asphalt replacement (2,000 sqft)", "${mid_low}", "${mid}"),
            ("Metal or tile roof (2,000 sqft)", "${mid}", "${high}"),
        ],
    },
}

# ─── TEMPLATE ────────────────────────────────────────────────────────────────
HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{page_title}</title>
<meta name="description" content="{page_desc}">
<meta name="keywords" content="{proj_name_lower} cost {city_lower}, {proj_name_lower} cost {city_lower} {state}, how much does {proj_name_lower} cost in {city_lower}, {proj_name_lower} calculator {city_lower}">
<link rel="canonical" href="https://estimates-pro.com/tools/{proj_slug}-cost-{city_slug}/">
<link rel="icon" type="image/x-icon" href="../../favicon.ico">
<link rel="apple-touch-icon" href="../../images/apple-touch-icon.png">
<!-- Open Graph -->
<meta property="og:title" content="{page_title}">
<meta property="og:description" content="{page_desc}">
<meta property="og:url" content="https://estimates-pro.com/tools/{proj_slug}-cost-{city_slug}/">
<meta property="og:type" content="website">
<meta property="og:image" content="https://estimates-pro.com/images/screen1.png">
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "WebApplication",
  "name": "{proj_name} Cost Calculator — {city}",
  "description": "{page_desc}",
  "url": "https://estimates-pro.com/tools/{proj_slug}-cost-{city_slug}/",
  "applicationCategory": "UtilitiesApplication",
  "operatingSystem": "Web",
  "offers": {{ "@type": "Offer", "price": "0", "priceCurrency": "USD" }},
  "geo": {{
    "@type": "GeoCoordinates",
    "addressLocality": "{city}",
    "addressRegion": "{state}"
  }}
}}
</script>
<style>
  *, *::before, *::after {{ margin: 0; padding: 0; box-sizing: border-box; }}
  :root {{
    --blue: #1565C0; --blue-dark: #0D47A1; --blue-light: #E3F2FD;
    --green: #2E7D32; --green-light: #E8F5E9;
    --text: #1C1C1E; --text-sec: #6E6E73;
    --border: #E5E7EB; --bg: #F9FAFB; --white: #fff;
  }}
  body {{ font-family: -apple-system, BlinkMacSystemFont, 'Inter', sans-serif; background: var(--bg); color: var(--text); }}
  nav {{
    background: var(--white); border-bottom: 1px solid var(--border);
    padding: 0 32px; height: 60px;
    display: flex; align-items: center; justify-content: space-between;
    position: sticky; top: 0; z-index: 100;
  }}
  .nav-logo {{ display: flex; align-items: center; gap: 8px; font-weight: 800; font-size: 17px; text-decoration: none; color: var(--text); }}
  .nav-logo img {{ width: 28px; height: 28px; border-radius: 6px; }}
  .nav-logo span {{ color: var(--blue); }}
  .nav-cta {{ background: var(--blue); color: #fff; padding: 8px 18px; border-radius: 7px; font-size: 13px; font-weight: 700; text-decoration: none; }}
  .page-hero {{
    background: linear-gradient(135deg, var(--blue-dark) 0%, var(--blue) 100%);
    padding: 48px 32px 40px; text-align: center; color: #fff;
  }}
  .breadcrumb {{ font-size: 12px; color: rgba(255,255,255,0.6); margin-bottom: 12px; }}
  .breadcrumb a {{ color: rgba(255,255,255,0.7); text-decoration: none; }}
  .page-hero h1 {{ font-size: clamp(24px, 4vw, 42px); font-weight: 900; letter-spacing: -1px; margin-bottom: 10px; }}
  .page-hero p {{ font-size: 16px; color: rgba(255,255,255,0.75); max-width: 580px; margin: 0 auto; }}
  .cost-badges {{ display: flex; gap: 12px; justify-content: center; margin-top: 20px; flex-wrap: wrap; }}
  .cost-badge {{ background: rgba(255,255,255,0.15); border-radius: 8px; padding: 8px 16px; font-size: 14px; font-weight: 700; }}
  .cost-badge span {{ display: block; font-size: 11px; font-weight: 400; opacity: 0.75; margin-bottom: 2px; }}
  .main {{ max-width: 1060px; margin: 0 auto; padding: 32px 20px 80px; display: grid; grid-template-columns: 1fr 340px; gap: 24px; align-items: start; }}
  @media(max-width: 760px) {{ .main {{ grid-template-columns: 1fr; }} .sticky-result {{ position: static !important; }} }}
  .calc-card {{ background: var(--white); border: 1px solid var(--border); border-radius: 16px; overflow: hidden; }}
  .calc-section {{ padding: 24px; border-bottom: 1px solid var(--border); }}
  .calc-section:last-child {{ border-bottom: none; }}
  .calc-section h3 {{ font-size: 14px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.8px; color: var(--text-sec); margin-bottom: 16px; }}
  .slider-row {{ margin-bottom: 20px; }}
  .slider-label {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px; }}
  .slider-label span {{ font-size: 14px; font-weight: 600; }}
  .slider-val {{ font-size: 15px; font-weight: 800; color: var(--blue); }}
  input[type=range] {{
    width: 100%; accent-color: var(--blue); height: 6px;
    -webkit-appearance: none; appearance: none; background: #dbeafe; border-radius: 3px; outline: none;
  }}
  input[type=range]::-webkit-slider-thumb {{ -webkit-appearance: none; width: 18px; height: 18px; border-radius: 50%; background: var(--blue); cursor: pointer; border: 2px solid #fff; box-shadow: 0 1px 4px rgba(0,0,0,0.2); }}
  .quality-row {{ display: grid; grid-template-columns: repeat(3,1fr); gap: 8px; margin-bottom: 4px; }}
  .quality-btn {{
    padding: 10px 6px; border-radius: 8px; border: 1.5px solid var(--border);
    font-size: 13px; font-weight: 600; cursor: pointer;
    background: var(--white); color: var(--text); transition: all 0.15s; text-align: center;
  }}
  .quality-btn.active {{ background: var(--blue-light); border-color: var(--blue); color: var(--blue); }}
  .quality-desc {{ font-size: 12px; color: var(--text-sec); text-align: center; margin-top: 4px; }}
  .item-list {{ display: flex; flex-direction: column; gap: 10px; }}
  .item-row {{ display: flex; align-items: center; gap: 10px; cursor: pointer; }}
  .item-row input[type=checkbox] {{ width: 16px; height: 16px; accent-color: var(--blue); flex-shrink: 0; cursor: pointer; }}
  .item-label {{ flex: 1; font-size: 14px; }}
  .item-cost {{ font-size: 14px; font-weight: 700; color: var(--text-sec); }}
  .sticky-result {{ position: sticky; top: 72px; }}
  .result-card {{ background: var(--white); border: 1px solid var(--border); border-radius: 16px; overflow: hidden; }}
  .result-header {{ background: linear-gradient(135deg, var(--blue-dark), var(--blue)); padding: 20px 24px; }}
  .result-header p {{ color: rgba(255,255,255,0.7); font-size: 12px; margin-bottom: 4px; }}
  .result-total {{ font-size: 36px; font-weight: 900; color: #fff; letter-spacing: -1px; }}
  .result-range {{ font-size: 13px; color: rgba(255,255,255,0.65); margin-top: 4px; }}
  .result-body {{ padding: 20px 24px; }}
  .breakdown-row {{ display: flex; justify-content: space-between; align-items: center; padding: 8px 0; border-bottom: 1px solid var(--border); font-size: 14px; }}
  .breakdown-row:last-child {{ border-bottom: none; }}
  .breakdown-label {{ color: var(--text-sec); }}
  .breakdown-val {{ font-weight: 700; }}
  .app-promo {{ margin-top: 16px; background: var(--blue-light); border-radius: 10px; padding: 16px; }}
  .app-promo p {{ font-size: 13px; font-weight: 700; color: var(--blue-dark); margin-bottom: 10px; }}
  .store-btns {{ display: flex; flex-direction: column; gap: 8px; }}
  .store-btn {{ display: flex; align-items: center; gap: 8px; background: var(--blue-dark); color: #fff; text-decoration: none; border-radius: 8px; padding: 8px 14px; font-size: 12px; }}
  .store-btn svg {{ width: 20px; height: 20px; flex-shrink: 0; }}
  .store-btn-text {{ line-height: 1.2; }}
  .store-btn-text strong {{ font-size: 13px; font-weight: 800; display: block; }}
  .info-section {{ margin-top: 48px; }}
  .info-section h2 {{ font-size: 22px; font-weight: 800; margin-bottom: 20px; }}
  .info-section h3 {{ font-size: 17px; font-weight: 700; margin: 28px 0 10px; }}
  .info-section p {{ font-size: 15px; line-height: 1.65; color: #374151; margin-bottom: 12px; }}
  .cost-table {{ width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 14px; }}
  .cost-table th {{ background: var(--blue-dark); color: #fff; padding: 10px 14px; text-align: left; font-size: 12px; text-transform: uppercase; letter-spacing: 0.5px; }}
  .cost-table td {{ padding: 10px 14px; border-bottom: 1px solid var(--border); }}
  .cost-table tr:nth-child(even) td {{ background: var(--blue-light); }}
  .cost-table tr:last-child td {{ border-bottom: none; }}
  .faq-item {{ border: 1px solid var(--border); border-radius: 10px; margin-bottom: 10px; overflow: hidden; }}
  .faq-q {{ padding: 14px 18px; font-weight: 700; font-size: 15px; cursor: pointer; display: flex; justify-content: space-between; align-items: center; background: var(--white); }}
  .faq-q:hover {{ background: var(--bg); }}
  .faq-a {{ padding: 0 18px 14px; font-size: 14px; line-height: 1.65; color: #374151; display: none; }}
  .faq-item.open .faq-a {{ display: block; }}
  .faq-item.open .faq-chevron {{ transform: rotate(180deg); }}
  .faq-chevron {{ transition: transform 0.2s; color: var(--text-sec); }}
  footer {{ background: var(--blue-dark); color: rgba(255,255,255,0.7); padding: 32px; text-align: center; font-size: 13px; }}
  footer a {{ color: rgba(255,255,255,0.6); text-decoration: none; margin: 0 8px; }}
  footer a:hover {{ color: #fff; }}
  footer .footer-logo {{ font-size: 18px; font-weight: 800; color: #fff; margin-bottom: 8px; }}
  .cta-section {{ background: linear-gradient(135deg, var(--blue-dark), var(--blue)); border-radius: 14px; padding: 32px 28px; text-align: center; margin-top: 40px; color: #fff; }}
  .cta-section h2 {{ font-size: 22px; font-weight: 800; margin-bottom: 8px; }}
  .cta-section p {{ font-size: 15px; opacity: 0.8; margin-bottom: 20px; }}
  .cta-btns {{ display: flex; gap: 12px; justify-content: center; flex-wrap: wrap; }}
  .cta-btn {{ background: rgba(255,255,255,0.15); border: 1.5px solid rgba(255,255,255,0.4); color: #fff; padding: 10px 22px; border-radius: 9px; font-weight: 700; font-size: 14px; text-decoration: none; }}
  .cta-btn.primary {{ background: #fff; color: var(--blue-dark); }}
</style>
</head>
<body>
<nav>
  <a class="nav-logo" href="/">
    <img src="../../images/icon.png" alt="Cost Estimator">
    Cost<span>Estimator</span>
  </a>
  <a class="nav-cta" href="https://apps.apple.com/us/app/cost-estimator-construction/id6758105341">Download Free</a>
</nav>

<div class="page-hero">
  <div class="breadcrumb">
    <a href="/">Home</a> › <a href="/tools/">Tools</a> › {h1}
  </div>
  <h1>{h1}</h1>
  <p>{intro}</p>
  <div class="cost-badges">
    <div class="cost-badge"><span>Low estimate</span>${badge_low}</div>
    <div class="cost-badge"><span>Average</span>${badge_mid}</div>
    <div class="cost-badge"><span>High estimate</span>${badge_high}</div>
  </div>
</div>

<div class="main">
  <div>
    <div class="calc-card">
      <div class="calc-section">
        <h3>Project Size</h3>
        <div class="slider-row">
          <div class="slider-label">
            <span>Square footage</span>
            <span class="slider-val" id="sqftVal">{default_sqft} sq ft</span>
          </div>
          <input type="range" id="sqftSlider" min="{sqft_min}" max="{sqft_max}" value="{default_sqft}" oninput="update()">
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
{item_rows}
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
      <h2>{proj_name} Cost in {city}: 2026 Guide</h2>
      <p>{info_intro}</p>

      <h3>Typical {proj_name} Costs in {city}</h3>
      <table class="cost-table">
        <thead><tr><th>Project Scope</th><th>Low</th><th>High</th></tr></thead>
        <tbody>
{cost_table_rows}
        </tbody>
      </table>

      <h3>What Affects {proj_name} Costs in {city}?</h3>
      <p><strong>Labor rates:</strong> {city} contractors typically charge ${labor_low}–${labor_high}/hour for skilled trades. This is {labor_vs_avg} the national average of $65–$85/hour.</p>
      <p><strong>Material costs:</strong> Material prices in {city} are affected by local supply chain, transportation, and demand. The {region} region generally sees {mat_cost_desc} material prices compared to the national average.</p>
      <p><strong>Permits:</strong> {city}, {state} requires permits for most major {proj_name_lower} work. Budget ${permit_low}–${permit_high} for permit fees depending on project scope.</p>
      <p><strong>Contractor availability:</strong> {city}'s construction market is {market_desc}. Getting multiple quotes (at least 3) is strongly recommended.</p>

      <h3>Frequently Asked Questions</h3>
{faq_rows}

      <div class="cta-section">
        <h2>Create Professional Estimates in 60 Seconds</h2>
        <p>Use Cost Estimator app to generate detailed, accurate estimates for {proj_name_lower} and other projects — share as PDF directly with your clients.</p>
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
        <p>Estimated cost in {city}</p>
        <div class="result-total" id="totalDisplay">$0</div>
        <div class="result-range" id="rangeDisplay">Range: $0 – $0</div>
      </div>
      <div class="result-body">
        <div class="breakdown-row">
          <span class="breakdown-label">Materials</span>
          <span class="breakdown-val" id="matDisplay">$0</span>
        </div>
        <div class="breakdown-row">
          <span class="breakdown-label">Labor</span>
          <span class="breakdown-val" id="laborDisplay">$0</span>
        </div>
        <div class="breakdown-row">
          <span class="breakdown-label">City multiplier</span>
          <span class="breakdown-val">{cost_mult_display}x</span>
        </div>
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
    <a href="/">Home</a>
    <a href="/tools/">More Calculators</a>
    <a href="https://apps.apple.com/us/app/cost-estimator-construction/id6758105341">App Store</a>
    <a href="https://play.google.com/store/apps/details?id=com.britetodo.costestimator">Google Play</a>
  </div>
  <p style="margin-top:12px">© 2026 Brite Technologies LLC · hello@britetodo.com</p>
</footer>

<script>
const ITEMS = {items_json};
const CITY_MULT = {city_mult};
const SQFT_BASE = {sqft_base};
let qualityMult = 1.0;

function setQ(btn) {{
  document.querySelectorAll('.quality-btn').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  qualityMult = parseFloat(btn.dataset.q);
  const descs = ['Budget materials, basic finishes', 'Standard materials, solid craftsmanship', 'Designer materials, premium finishes'];
  const idx = ['0.72','1.0','1.65'].indexOf(btn.dataset.q);
  document.getElementById('qualityDesc').textContent = descs[idx] || descs[1];
  update();
}}

function fmt(n) {{
  return '$' + Math.round(n).toLocaleString('en-US');
}}

function update() {{
  const sqft = parseInt(document.getElementById('sqftSlider').value);
  const laborPct = parseInt(document.getElementById('laborSlider').value) / 100;
  document.getElementById('sqftVal').textContent = sqft + ' sq ft';
  document.getElementById('laborVal').textContent = (laborPct * 100).toFixed(0) + '%';

  const sqftMult = sqft / SQFT_BASE;
  let base = 0;
  ITEMS.forEach(item => {{
    const cb = document.getElementById('cb_' + item.id);
    if (cb && cb.checked) base += item.base;
  }});

  const subtotal = base * sqftMult * qualityMult * CITY_MULT;
  const labor = subtotal * laborPct;
  const materials = subtotal - labor;
  const total = subtotal;
  const low = total * 0.78;
  const high = total * 1.28;

  document.getElementById('totalDisplay').textContent = fmt(total);
  document.getElementById('rangeDisplay').textContent = 'Range: ' + fmt(low) + ' – ' + fmt(high);
  document.getElementById('matDisplay').textContent = fmt(materials);
  document.getElementById('laborDisplay').textContent = fmt(labor);
}}

document.querySelectorAll('.faq-q').forEach(q => {{
  q.addEventListener('click', () => {{
    q.closest('.faq-item').classList.toggle('open');
  }});
}});

update();
</script>
</body>
</html>
'''


# ─── HELPERS ─────────────────────────────────────────────────────────────────
def fmt_cost(n):
    return f"{round(n):,}"

def cost_vs_avg(mult):
    if mult >= 1.20: return "significantly higher than"
    if mult >= 1.08: return "higher than"
    if mult >= 0.97: return "close to"
    if mult >= 0.88: return "slightly below"
    return "notably below"

def labor_vs_avg(mult):
    if mult >= 1.20: return "above"
    if mult >= 1.05: return "slightly above"
    if mult >= 0.95: return "at"
    return "below"

def mat_cost_desc(mult, region):
    if mult >= 1.20: return "higher"
    if mult >= 1.05: return "slightly above average"
    if mult >= 0.95: return "near-average"
    return "competitive"

def market_desc(mult):
    if mult >= 1.25: return "highly competitive — book contractors 4–8 weeks in advance"
    if mult >= 1.05: return "active — get quotes 3–4 weeks ahead for best availability"
    if mult >= 0.90: return "moderately busy — contractors are generally available within 2–3 weeks"
    return "less competitive — multiple contractors typically available within 1–2 weeks"

def generate_page(city_name, city_data, proj_key, proj_data):
    m = city_data["cost_mult"]
    state = city_data["state"]
    region = city_data["region"]
    city_slug = city_data["slug"]
    proj_slug = proj_data["slug"]

    low = round(proj_data["base_low"] * m / 500) * 500
    mid = round(proj_data["base_mid"] * m / 500) * 500
    high = round(proj_data["base_high"] * m / 500) * 500
    low_high = round((low + mid) / 2 / 500) * 500
    mid_low = round((low_high + mid) / 2 / 500) * 500

    labor_low = round(55 * m)
    labor_high = round(95 * m)
    permit_low = round(300 * m / 50) * 50
    permit_high = round(800 * m / 50) * 50
    permit_cost = round((permit_low + permit_high) / 2 / 50) * 50
    repair_low = round(500 * m / 100) * 100
    repair_high = round(2500 * m / 100) * 100
    metal_premium = 40
    return_value = round(mid * 0.65 / 1000) * 1000

    def subst(tmpl, **extra):
        d = {
            "city": city_name, "state": state, "region": region,
            "city_lower": city_name.lower(), "state_lower": state.lower(),
            "proj_name": proj_data["name"],
            "proj_name_lower": proj_data["name"].lower(),
            "proj_slug": proj_slug, "city_slug": city_slug,
            "cost_vs_avg": cost_vs_avg(m),
            "low": fmt_cost(low), "mid": fmt_cost(mid), "high": fmt_cost(high),
            "low_high": fmt_cost(low_high), "mid_low": fmt_cost(mid_low),
            "labor_low": labor_low, "labor_high": labor_high,
            "permit_low": permit_low, "permit_high": permit_high, "permit_cost": permit_cost,
            "repair_low": fmt_cost(repair_low), "repair_high": fmt_cost(repair_high),
            "metal_premium": metal_premium,
            "return_value": fmt_cost(return_value),
            **extra
        }
        return tmpl.format(**d)

    page_title = subst(proj_data["title_tmpl"])
    page_desc = subst(proj_data["desc_tmpl"])
    h1 = subst(proj_data["h1_tmpl"])
    intro = subst(proj_data["intro_tmpl"])

    # Item rows HTML
    import json as _json
    item_rows_html = ""
    items_js = []
    for i, item in enumerate(proj_data["items"]):
        adj_cost = round(item["base"] * m / 50) * 50
        checked = "checked" if item["checked"] else ""
        item_rows_html += f'          <label class="item-row"><input type="checkbox" id="cb_{i}" {checked} onchange="update()"><span class="item-label">{item["label"]}</span><span class="item-cost">${fmt_cost(adj_cost)}</span></label>\n'
        items_js.append({"id": i, "base": adj_cost})

    # Cost table rows
    ct_rows = []
    for row in proj_data["cost_table_rows"]:
        cells = [subst(c) for c in row]
        ct_rows.append(f"          <tr><td>{cells[0]}</td><td>{cells[1]}</td><td>{cells[2]}</td></tr>")

    # FAQ rows
    faq_html = ""
    for q, a in proj_data["faq"]:
        faq_html += f'''      <div class="faq-item">
        <div class="faq-q">{subst(q)} <svg class="faq-chevron" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg></div>
        <div class="faq-a">{subst(a)}</div>
      </div>\n'''

    # sqft defaults
    sqft_defaults = {"bathroom-remodel": (30, 200, 60), "kitchen-remodel": (100, 500, 200), "roof-replacement": (800, 3500, 1800)}
    sqft_min, sqft_max, sqft_default = sqft_defaults.get(proj_key, (100, 1000, 300))
    sqft_base = sqft_default

    info_intro = subst(
        f"{proj_data['name']} costs in {{city}}, {{state}} vary significantly based on the scope of work, materials chosen, and contractor availability. "
        f"The estimates below reflect {{city}}'s local labor market ({{labor_vs_avg}} the national average) and typical material costs in the {{region}} region."
    , labor_vs_avg=labor_vs_avg(m))

    page = HTML_TEMPLATE.format(
        page_title=page_title,
        page_desc=page_desc,
        proj_name=proj_data["name"],
        proj_name_lower=proj_data["name"].lower(),
        proj_slug=proj_slug,
        city=city_name,
        city_lower=city_name.lower(),
        city_slug=city_slug,
        state=state,
        h1=h1,
        intro=intro,
        badge_low=fmt_cost(low),
        badge_mid=fmt_cost(mid),
        badge_high=fmt_cost(high),
        item_rows=item_rows_html,
        items_json=_json.dumps(items_js),
        city_mult=m,
        sqft_min=sqft_min,
        sqft_max=sqft_max,
        default_sqft=sqft_default,
        sqft_base=sqft_base,
        info_intro=info_intro,
        cost_table_rows="\n".join(ct_rows),
        labor_low=labor_low,
        labor_high=labor_high,
        labor_vs_avg=labor_vs_avg(m),
        mat_cost_desc=mat_cost_desc(m, region),
        permit_low=permit_low,
        permit_high=permit_high,
        region=region,
        market_desc=market_desc(m),
        faq_rows=faq_html,
        cost_mult_display=f"{m:.2f}",
    )
    return page


# ─── MAIN ────────────────────────────────────────────────────────────────────
def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    out_dir = base_dir  # output next to this script

    count = 0
    index_links = []
    for city_name, city_data in CITIES.items():
        for proj_key, proj_data in PROJECTS.items():
            folder_name = f"{proj_data['slug']}-cost-{city_data['slug']}"
            folder_path = os.path.join(out_dir, folder_name)
            os.makedirs(folder_path, exist_ok=True)
            html = generate_page(city_name, city_data, proj_key, proj_data)
            out_path = os.path.join(folder_path, "index.html")
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(html)
            count += 1
            index_links.append((folder_name, f"{proj_data['name']} Cost in {city_name}"))
            if count % 30 == 0:
                print(f"  Generated {count} pages...")

    # Generate tools index page
    links_html = "\n".join(
        f'    <li><a href="/tools/{name}/">{title}</a></li>'
        for name, title in sorted(index_links)
    )
    index_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Construction Cost Calculators by City — Free Estimating Tools 2026</title>
<meta name="description" content="Free construction cost calculators for bathroom remodel, kitchen remodel, and roof replacement by city. Updated 2026 prices for all major US cities.">
<link rel="canonical" href="https://estimates-pro.com/tools/">
<link rel="icon" type="image/x-icon" href="../favicon.ico">
<style>
  body {{ font-family: -apple-system,BlinkMacSystemFont,'Inter',sans-serif; background: #F9FAFB; color: #1C1C1E; max-width: 960px; margin: 0 auto; padding: 40px 20px; }}
  h1 {{ font-size: 32px; font-weight: 900; margin-bottom: 8px; }}
  h2 {{ font-size: 20px; font-weight: 700; margin: 32px 0 12px; color: #1565C0; }}
  ul {{ list-style: none; padding: 0; display: grid; grid-template-columns: repeat(auto-fill, minmax(280px,1fr)); gap: 8px; }}
  li a {{ display: block; padding: 10px 14px; background: #fff; border: 1px solid #E5E7EB; border-radius: 8px; text-decoration: none; color: #1565C0; font-size: 14px; font-weight: 600; }}
  li a:hover {{ background: #E3F2FD; border-color: #1565C0; }}
  nav {{ margin-bottom: 32px; font-size: 13px; }}
  nav a {{ color: #1565C0; text-decoration: none; margin-right: 16px; font-weight: 600; }}
</style>
</head>
<body>
<nav><a href="/">← Home</a></nav>
<h1>Construction Cost Calculators</h1>
<p>Free interactive cost calculators for major US cities. Updated 2026 pricing.</p>

<h2>Bathroom Remodel Cost by City</h2>
<ul>
{''.join(f"<li><a href='/tools/{n}/'>Bathroom Remodel Cost in {n.split('-cost-')[1].replace('-',' ').title()}</a></li>" for n,_ in sorted(index_links) if n.startswith('bathroom'))}
</ul>

<h2>Kitchen Remodel Cost by City</h2>
<ul>
{''.join(f"<li><a href='/tools/{n}/'>Kitchen Remodel Cost in {n.split('-cost-')[1].replace('-',' ').title()}</a></li>" for n,_ in sorted(index_links) if n.startswith('kitchen'))}
</ul>

<h2>Roof Replacement Cost by City</h2>
<ul>
{''.join(f"<li><a href='/tools/{n}/'>Roof Replacement Cost in {n.split('-cost-')[1].replace('-',' ').title()}</a></li>" for n,_ in sorted(index_links) if n.startswith('roof'))}
</ul>
</body>
</html>'''

    with open(os.path.join(out_dir, "index.html"), "w") as f:
        f.write(index_html)

    print(f"\nDone! Generated {count} pages + tools/index.html")
    print(f"Output: {out_dir}")


if __name__ == "__main__":
    main()
