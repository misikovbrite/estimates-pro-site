#!/usr/bin/env python3
"""
Generate:
  1. /guides/how-much-does-X-cost/ — 10 national guide pages (53K/mo)
  2. /tools/X-cost-calculator/ + cities — 4 new calc types (13K/mo)
  3. /templates/X-estimate-template/ — 5 template pages (8K/mo)
"""
import os, json

BASE = os.path.dirname(os.path.abspath(__file__))

# ─── SHARED HELPERS ───────────────────────────────────────────────────────────
def fmt(n): return f"{round(n):,}"

NAV = '''<nav>
  <a class="nav-logo" href="/"><img src="{icon}" alt="Cost Estimator">Cost<span>Estimator</span></a>
  <a class="nav-cta" href="https://apps.apple.com/us/app/cost-estimator-construction/id6758105341">Download Free</a>
</nav>'''

FOOTER = '''<footer>
  <div class="footer-logo">CostEstimator</div>
  <p style="margin-bottom:12px">Free construction estimating app for contractors</p>
  <div><a href="/">Home</a><a href="/tools/">Calculators</a><a href="/guides/">Cost Guides</a><a href="/templates/">Templates</a>
  <a href="https://apps.apple.com/us/app/cost-estimator-construction/id6758105341">App Store</a>
  <a href="https://play.google.com/store/apps/details?id=com.britetodo.costestimator">Google Play</a></div>
  <p style="margin-top:12px">© 2026 Brite Technologies LLC · hello@britetodo.com</p>
</footer>'''

BASE_CSS = '''<style>
*,*::before,*::after{margin:0;padding:0;box-sizing:border-box}
:root{--blue:#1565C0;--blue-dark:#0D47A1;--blue-light:#E3F2FD;--text:#1C1C1E;--text-sec:#6E6E73;--border:#E5E7EB;--bg:#F9FAFB;--white:#fff}
body{font-family:-apple-system,BlinkMacSystemFont,'Inter',sans-serif;background:var(--bg);color:var(--text)}
nav{background:var(--white);border-bottom:1px solid var(--border);padding:0 32px;height:60px;display:flex;align-items:center;justify-content:space-between;position:sticky;top:0;z-index:100}
.nav-logo{display:flex;align-items:center;gap:8px;font-weight:800;font-size:17px;text-decoration:none;color:var(--text)}
.nav-logo img{width:28px;height:28px;border-radius:6px}
.nav-logo span{color:var(--blue)}
.nav-cta{background:var(--blue);color:#fff;padding:8px 18px;border-radius:7px;font-size:13px;font-weight:700;text-decoration:none}
footer{background:var(--blue-dark);color:rgba(255,255,255,.7);padding:32px;text-align:center;font-size:13px}
footer a{color:rgba(255,255,255,.6);text-decoration:none;margin:0 8px}
footer a:hover{color:#fff}
.footer-logo{font-size:18px;font-weight:800;color:#fff;margin-bottom:8px}
h1{font-size:clamp(26px,4vw,44px);font-weight:900;letter-spacing:-1px;line-height:1.1;margin-bottom:14px}
h2{font-size:22px;font-weight:800;margin:36px 0 14px}
h3{font-size:17px;font-weight:700;margin:24px 0 8px}
p{font-size:15px;line-height:1.7;color:#374151;margin-bottom:12px}
a{color:var(--blue)}
.hero{background:linear-gradient(135deg,var(--blue-dark),var(--blue));padding:52px 32px 44px;text-align:center;color:#fff}
.hero h1{color:#fff;margin-bottom:10px}
.hero p{color:rgba(255,255,255,.8);max-width:600px;margin:0 auto 20px}
.breadcrumb{font-size:12px;color:rgba(255,255,255,.6);margin-bottom:14px}
.breadcrumb a{color:rgba(255,255,255,.7);text-decoration:none}
.cost-pills{display:flex;gap:10px;justify-content:center;flex-wrap:wrap;margin-top:16px}
.cost-pill{background:rgba(255,255,255,.15);border-radius:8px;padding:8px 16px;font-size:14px;font-weight:700}
.cost-pill span{display:block;font-size:11px;opacity:.75;margin-bottom:2px}
.content{max-width:860px;margin:0 auto;padding:40px 24px 80px}
.cost-table{width:100%;border-collapse:collapse;margin:16px 0 24px;font-size:14px}
.cost-table th{background:var(--blue-dark);color:#fff;padding:10px 14px;text-align:left;font-size:12px;text-transform:uppercase;letter-spacing:.5px}
.cost-table td{padding:10px 14px;border-bottom:1px solid var(--border)}
.cost-table tr:nth-child(even) td{background:var(--blue-light)}
.cost-table tr:last-child td{border-bottom:none}
.faq-item{border:1px solid var(--border);border-radius:10px;margin-bottom:10px;overflow:hidden}
.faq-q{padding:14px 18px;font-weight:700;font-size:15px;cursor:pointer;display:flex;justify-content:space-between;align-items:center;background:var(--white)}
.faq-q:hover{background:var(--bg)}
.faq-a{padding:0 18px 14px;font-size:14px;line-height:1.7;color:#374151;display:none}
.faq-item.open .faq-a{display:block}
.faq-item.open .faq-chevron{transform:rotate(180deg)}
.faq-chevron{transition:transform .2s;color:var(--text-sec)}
.city-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:8px;margin:16px 0}
.city-link{display:block;padding:8px 12px;background:var(--white);border:1px solid var(--border);border-radius:8px;font-size:13px;font-weight:600;text-decoration:none;color:var(--blue)}
.city-link:hover{background:var(--blue-light);border-color:var(--blue)}
.app-cta{background:linear-gradient(135deg,var(--blue-dark),var(--blue));border-radius:14px;padding:32px 28px;text-align:center;margin:40px 0;color:#fff}
.app-cta h2{color:#fff;margin:0 0 8px}
.app-cta p{color:rgba(255,255,255,.8);margin-bottom:20px}
.cta-btns{display:flex;gap:12px;justify-content:center;flex-wrap:wrap}
.cta-btn{background:rgba(255,255,255,.15);border:1.5px solid rgba(255,255,255,.4);color:#fff;padding:10px 22px;border-radius:9px;font-weight:700;font-size:14px;text-decoration:none}
.cta-btn.primary{background:#fff;color:var(--blue-dark)}
.info-box{background:var(--blue-light);border-left:4px solid var(--blue);border-radius:0 8px 8px 0;padding:14px 18px;margin:16px 0;font-size:14px;color:var(--blue-dark)}
.region-table td:first-child{font-weight:600}
</style>'''

FAQ_JS = '''<script>
document.querySelectorAll('.faq-q').forEach(q=>{
  q.addEventListener('click',()=>q.closest('.faq-item').classList.toggle('open'));
});
</script>'''

CHEVRON = '<svg class="faq-chevron" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>'

def faq(q, a):
    return f'''<div class="faq-item">
  <div class="faq-q">{q} {CHEVRON}</div>
  <div class="faq-a">{a}</div>
</div>'''

def app_cta(proj_name):
    return f'''<div class="app-cta">
  <h2>Get a Precise {proj_name} Estimate in 60 Seconds</h2>
  <p>Use Cost Estimator app — snap a photo of the job site and get an accurate, itemized cost breakdown instantly.</p>
  <div class="cta-btns">
    <a class="cta-btn primary" href="https://apps.apple.com/us/app/cost-estimator-construction/id6758105341">App Store — Free</a>
    <a class="cta-btn" href="https://play.google.com/store/apps/details?id=com.britetodo.costestimator">Google Play — Free</a>
  </div>
</div>'''

# ─────────────────────────────────────────────────────────────────────────────
# PART 1 — "HOW MUCH DOES X COST" GUIDES
# ─────────────────────────────────────────────────────────────────────────────

GUIDES = [
    {
        "slug": "how-much-does-bathroom-remodel-cost",
        "title": "How Much Does a Bathroom Remodel Cost? (2026)",
        "desc": "The average bathroom remodel costs $6,000–$16,000. See full cost breakdowns by scope, materials, and location — updated 2026 data.",
        "h1": "How Much Does a Bathroom Remodel Cost?",
        "keywords": "how much does it cost to remodel a bathroom, average cost to remodel a bathroom, bathroom remodel cost 2026, bathroom renovation cost",
        "vol": 19800,
        "low": 4500, "mid": 12000, "high": 30000,
        "calc_slug": "bathroom-remodel",
        "intro": "The average bathroom remodel in the US costs <strong>$6,000–$16,000</strong>, with most homeowners spending around <strong>$12,000</strong> for a mid-range renovation. A simple cosmetic update starts around $4,500, while a full gut renovation with premium finishes can exceed $30,000.",
        "scope_rows": [
            ("Cosmetic refresh (paint, fixtures, lighting)", "$1,500", "$4,500"),
            ("Partial remodel (vanity, flooring, toilet)", "$4,500", "$9,000"),
            ("Full remodel (all fixtures, tile, plumbing)", "$9,000", "$18,000"),
            ("Luxury / primary suite renovation", "$18,000", "$40,000+"),
        ],
        "component_rows": [
            ("Labor (40–60% of total)", "$3,000", "$9,000"),
            ("Vanity & sink", "$400", "$2,500"),
            ("Toilet", "$150", "$900"),
            ("Bathtub or walk-in shower", "$1,500", "$7,000"),
            ("Tile (walls + floor)", "$800", "$4,000"),
            ("Lighting & electrical", "$400", "$1,500"),
            ("Plumbing rough-in", "$800", "$2,500"),
            ("Paint & drywall", "$300", "$800"),
            ("Permits", "$200", "$700"),
        ],
        "region_rows": [
            ("South (TX, FL, GA)", "$4,000", "$12,000", "0.88–0.95×"),
            ("Midwest (OH, IL, MI)", "$5,000", "$13,000", "0.90–1.10×"),
            ("Mountain (CO, AZ, UT)", "$5,500", "$14,000", "0.95–1.05×"),
            ("Northeast (NY, MA, CT)", "$8,000", "$22,000", "1.15–1.35×"),
            ("West (CA, WA, OR)", "$9,000", "$25,000", "1.15–1.55×"),
        ],
        "faqs": [
            ("How long does a bathroom remodel take?", "Most bathroom remodels take 1–3 weeks. A simple cosmetic update (paint, fixtures) can be done in 2–3 days. Full gut renovations requiring new plumbing or tile work typically take 3–6 weeks."),
            ("What adds the most value in a bathroom remodel?", "Walk-in showers, double vanities, and heated floors offer the best return on investment. Bathroom remodels typically return 60–70% of cost at resale, making them one of the best home improvement investments."),
            ("Can I do a bathroom remodel myself?", "Cosmetic work (painting, fixture replacement, accessories) is DIY-friendly and can save 30–40%. Plumbing, electrical, and tile work should be done by licensed professionals — permits are required in most jurisdictions."),
            ("How much does a bathroom remodel add to home value?", "A mid-range bathroom remodel adds an average of $8,000–$12,000 in home value. A full primary suite renovation can add $15,000–$25,000 in high-demand markets."),
            ("Do I need permits for a bathroom remodel?", "Permits are required for most work involving plumbing, electrical, or structural changes. Cosmetic-only projects (replacing fixtures without moving pipes) typically don't require permits. Check with your local building department."),
        ],
        "city_proj": "bathroom-remodel",
    },
    {
        "slug": "how-much-does-kitchen-remodel-cost",
        "title": "How Much Does a Kitchen Remodel Cost? (2026)",
        "desc": "The average kitchen remodel costs $15,000–$45,000. See full cost breakdowns by scope, materials, and US region — updated 2026 data.",
        "h1": "How Much Does a Kitchen Remodel Cost?",
        "keywords": "how much does a kitchen remodel cost, average kitchen remodel cost, kitchen renovation cost 2026, kitchen remodel cost breakdown",
        "vol": 13200,
        "low": 10000, "mid": 30000, "high": 75000,
        "calc_slug": "kitchen-remodel",
        "intro": "The average kitchen remodel costs <strong>$15,000–$45,000</strong>, with most homeowners spending around <strong>$30,000</strong> for a full mid-range renovation. A minor update (new appliances, paint, hardware) starts around $10,000, while a full custom kitchen can exceed $75,000.",
        "scope_rows": [
            ("Minor update (paint, hardware, lighting)", "$5,000", "$15,000"),
            ("Mid update (countertops, sink, appliances)", "$15,000", "$30,000"),
            ("Full remodel (cabinets, counters, flooring)", "$30,000", "$55,000"),
            ("Luxury / full custom kitchen", "$55,000", "$100,000+"),
        ],
        "component_rows": [
            ("Cabinets (largest cost driver)", "$5,000", "$25,000"),
            ("Labor (35–50% of total)", "$6,000", "$18,000"),
            ("Countertops (quartz/granite)", "$2,000", "$8,000"),
            ("Appliances", "$3,000", "$12,000"),
            ("Flooring", "$1,500", "$6,000"),
            ("Backsplash", "$800", "$3,500"),
            ("Lighting & electrical", "$1,000", "$4,000"),
            ("Plumbing (sink/disposal)", "$500", "$2,500"),
            ("Permits", "$400", "$1,500"),
        ],
        "region_rows": [
            ("South (TX, FL, GA)", "$10,000", "$32,000", "0.88–0.95×"),
            ("Midwest (OH, IL, MI)", "$12,000", "$36,000", "0.90–1.10×"),
            ("Mountain (CO, AZ, UT)", "$14,000", "$40,000", "0.95–1.05×"),
            ("Northeast (NY, MA, CT)", "$20,000", "$58,000", "1.15–1.35×"),
            ("West (CA, WA, OR)", "$22,000", "$65,000", "1.15–1.55×"),
        ],
        "faqs": [
            ("How long does a kitchen remodel take?", "A standard kitchen remodel takes 3–8 weeks. Custom cabinets have 4–8 week lead times. Budget 10–14 weeks for a full gut renovation with custom work."),
            ("What's the most expensive part of a kitchen remodel?", "Cabinets typically account for 30–40% of the total kitchen remodel cost. Labor is the second largest cost, comprising 35–50% of the budget."),
            ("Does a kitchen remodel add value to my home?", "Kitchen remodels return 60–80% of their cost at resale. A mid-range kitchen remodel adds an average of $18,000–$25,000 in home value in most US markets."),
            ("How can I reduce kitchen remodel costs?", "Keep the same layout to avoid moving plumbing/electrical. Choose semi-custom over full-custom cabinets (saves 30–50%). Reface existing cabinets instead of replacing. Use laminate countertops in rental properties."),
            ("Do I need permits for a kitchen remodel?", "Permits are required for electrical, plumbing, structural changes, and gas line work. A simple cosmetic refresh (paint, cabinet refacing) typically doesn't require permits."),
        ],
        "city_proj": "kitchen-remodel",
    },
    {
        "slug": "how-much-does-a-new-roof-cost",
        "title": "How Much Does a New Roof Cost? (2026)",
        "desc": "A new roof costs $8,000–$18,000 for a typical home. See full cost breakdowns by material, size, and US region — updated 2026 pricing.",
        "h1": "How Much Does a New Roof Cost?",
        "keywords": "how much does a new roof cost, roof replacement cost 2026, average cost of new roof, how much to replace a roof",
        "vol": 8100,
        "low": 5500, "mid": 11500, "high": 24000,
        "calc_slug": "roof-replacement",
        "intro": "A new roof costs <strong>$8,000–$18,000</strong> for a typical 2,000 sq ft home with asphalt shingles. Simple repairs start at $500; premium metal or tile roofs on large homes can exceed $40,000. Material choice and labor market are the biggest cost drivers.",
        "scope_rows": [
            ("Roof repair (limited damage)", "$500", "$2,500"),
            ("Asphalt shingle replacement (1,500 sqft)", "$5,500", "$9,000"),
            ("Standard replacement (2,000 sqft home)", "$8,000", "$14,000"),
            ("Metal or tile roof (2,000 sqft home)", "$14,000", "$30,000"),
        ],
        "component_rows": [
            ("Asphalt shingles (material)", "$1,500", "$4,500"),
            ("Labor (tear-off + install)", "$3,000", "$7,000"),
            ("Underlayment & ice shield", "$500", "$1,500"),
            ("Decking repair/replacement", "$500", "$2,000"),
            ("Flashing (chimney, valleys)", "$400", "$1,200"),
            ("Ridge cap & hip shingles", "$300", "$700"),
            ("Gutters (optional)", "$800", "$2,500"),
            ("Permits", "$200", "$600"),
        ],
        "region_rows": [
            ("South (TX, FL, GA)", "$6,000", "$12,000", "0.88–0.95×"),
            ("Midwest (OH, IL, MI)", "$7,000", "$13,000", "0.90–1.10×"),
            ("Mountain (CO, AZ, UT)", "$7,500", "$14,000", "0.95–1.05×"),
            ("Northeast (NY, MA, CT)", "$10,000", "$18,000", "1.15–1.35×"),
            ("West (CA, WA, OR)", "$11,000", "$22,000", "1.15–1.55×"),
        ],
        "faqs": [
            ("How long does a roof replacement take?", "Most roof replacements take 1–3 days for a standard 2,000 sqft home. Larger or more complex roofs (multiple valleys, steep pitch) can take 3–5 days."),
            ("How do I know if I need a new roof or just a repair?", "If damage covers less than 20% of the roof surface and the roof is under 15 years old, repair is usually more cost-effective. If the roof is 20+ years old or damage covers large areas, full replacement is better long-term value."),
            ("How long does an asphalt shingle roof last?", "Standard 3-tab shingles last 20–25 years. Architectural (dimensional) shingles last 30–40 years. Metal roofs last 40–70 years. Premium tile or slate can last 50–100 years."),
            ("What's the best roofing material?", "Asphalt shingles offer the best value ($3–5/sqft installed). Metal roofing ($8–15/sqft) lasts longer and may reduce energy costs. For coastal or high-humidity climates, impact-resistant shingles add storm protection."),
            ("Does homeowners insurance cover roof replacement?", "Insurance covers sudden storm/wind/hail damage, not normal wear. Most policies have wind/hail deductibles. Document damage immediately with photos and contact your insurer within 48 hours of a storm."),
        ],
        "city_proj": "roof-replacement",
    },
    {
        "slug": "how-much-does-window-replacement-cost",
        "title": "How Much Does Window Replacement Cost? (2026)",
        "desc": "Window replacement costs $400–$900 per window installed. Full home replacement runs $5,000–$20,000. 2026 pricing by type and US region.",
        "h1": "How Much Does Window Replacement Cost?",
        "keywords": "how much does it cost to replace windows, window replacement cost 2026, average window replacement cost, cost to replace windows",
        "vol": 8100,
        "low": 3500, "mid": 8000, "high": 20000,
        "calc_slug": "window-replacement",
        "intro": "Window replacement costs <strong>$400–$900 per window</strong> installed, including labor. Full home replacement for 10–15 windows typically runs <strong>$5,000–$15,000</strong>. Bay windows and specialty shapes cost significantly more.",
        "scope_rows": [
            ("Single double-hung vinyl window", "$400", "$900"),
            ("Small home (6–8 windows)", "$3,500", "$7,000"),
            ("Average home (8–12 windows)", "$5,500", "$11,000"),
            ("Large home (12–20 windows)", "$9,000", "$20,000"),
        ],
        "component_rows": [
            ("Double-hung vinyl (each)", "$300", "$700"),
            ("Casement window (each)", "$600", "$1,200"),
            ("Bay/bow window (each)", "$1,500", "$4,500"),
            ("Installation labor (each)", "$100", "$300"),
            ("Low-E glass upgrade (each)", "$80", "$150"),
            ("Frame removal & disposal (each)", "$50", "$100"),
            ("Interior trim finish (each)", "$80", "$200"),
        ],
        "region_rows": [
            ("South (TX, FL, GA)", "$300", "$700", "0.88–0.95×"),
            ("Midwest (OH, IL, MI)", "$350", "$800", "0.90–1.10×"),
            ("Mountain (CO, AZ, UT)", "$400", "$850", "0.95–1.05×"),
            ("Northeast (NY, MA, CT)", "$550", "$1,100", "1.15–1.35×"),
            ("West (CA, WA, OR)", "$550", "$1,200", "1.15–1.55×"),
        ],
        "faqs": [
            ("Is it worth replacing all windows at once?", "Yes — replacing all windows at once typically saves 10–15% vs. individual replacements, as contractors can price the job as a package. You'll also get consistent style and avoid mismatched energy ratings."),
            ("How much can I save on energy bills with new windows?", "Energy-efficient windows (double-pane Low-E) can reduce heating/cooling costs by 12–24%. In cold climates, the savings are higher. Payback period is typically 10–15 years based on energy savings alone."),
            ("What's the difference between vinyl and fiberglass windows?", "Vinyl is the most popular choice — affordable ($300–700/window), low-maintenance, 20–30 year lifespan. Fiberglass costs 20–30% more but lasts 30–40+ years and resists warping in extreme temperatures."),
            ("How long does window replacement take?", "A professional crew can replace 8–10 windows in a single day. The full home window replacement project typically takes 1–2 days depending on the number and complexity of windows."),
            ("Do I need a permit to replace windows?", "Like-for-like window replacement (same size opening) usually doesn't require a permit. Enlarging the opening or adding new windows requires a permit in most jurisdictions."),
        ],
        "city_proj": "window-replacement",
    },
    {
        "slug": "how-much-does-drywall-cost",
        "title": "How Much Does Drywall Installation Cost? (2026)",
        "desc": "Drywall installation costs $2.50–$5.50 per square foot. A full room runs $1,500–$4,000. 2026 pricing by room size and finish level.",
        "h1": "How Much Does Drywall Installation Cost?",
        "keywords": "how much does drywall cost, drywall installation cost 2026, cost to drywall a room, drywall cost per square foot",
        "vol": 1900,
        "low": 1500, "mid": 3800, "high": 9000,
        "calc_slug": "drywall-installation",
        "intro": "Drywall installation costs <strong>$2.50–$5.50 per square foot</strong> installed, including materials, labor, taping, and finishing. A standard bedroom runs <strong>$1,500–$3,000</strong>; full house drywall costs <strong>$8,000–$20,000</strong> depending on size and finish level.",
        "scope_rows": [
            ("Single room (200–400 sqft)", "$800", "$2,500"),
            ("Master bedroom / living room", "$1,500", "$4,000"),
            ("Open-plan space (800–1,500 sqft)", "$3,500", "$7,000"),
            ("Full house (1,500–3,000 sqft)", "$8,000", "$20,000"),
        ],
        "component_rows": [
            ("Drywall sheets (material)", "$0.40", "$0.80/sqft"),
            ("Hanging labor", "$0.80", "$1.40/sqft"),
            ("Taping & mudding", "$0.80", "$1.20/sqft"),
            ("Finishing (Level 4)", "$0.60", "$0.90/sqft"),
            ("Corner bead & trim", "$200", "$500 flat"),
            ("Texture (optional)", "$0.40", "$0.80/sqft"),
            ("Delivery & disposal", "$150", "$400 flat"),
        ],
        "region_rows": [
            ("South (TX, FL, GA)", "$1,200", "$3,000", "0.82–0.95×"),
            ("Midwest (OH, IL, MI)", "$1,400", "$3,500", "0.88–1.10×"),
            ("Mountain (CO, AZ, UT)", "$1,500", "$3,800", "0.95–1.05×"),
            ("Northeast (NY, MA, CT)", "$2,000", "$5,500", "1.12–1.35×"),
            ("West (CA, WA, OR)", "$2,200", "$6,000", "1.10–1.55×"),
        ],
        "faqs": [
            ("How much drywall do I need for a room?", "Calculate total wall area: perimeter × ceiling height, minus doors and windows. A typical 12×12 bedroom needs ~400 sqft of drywall. Add 10% for waste and cuts. Standard sheets are 4×8 ft (32 sqft each)."),
            ("What's the difference between drywall finish levels?", "Level 3: texture-ready. Level 4: paint-ready (standard for most rooms). Level 5: skim coat, required for high-gloss paint or critical lighting. Each level adds $0.50–$1.00/sqft to the cost."),
            ("Can I hang drywall myself to save money?", "DIY drywall hanging can save $0.80–$1.40/sqft in labor. Taping and finishing is harder — a poor tape job shows through paint. Most homeowners DIY the hanging and hire professionals for taping/finishing."),
            ("How long does drywall installation take?", "A single bedroom takes 1–2 days for hanging, plus 2–3 days for taping/finishing/drying. Full house drywall typically takes 1–3 weeks including drying time between mud coats."),
            ("What type of drywall should I use?", "Standard 1/2\" for most walls. 5/8\" Type X for fire-rated assemblies (garages, shared walls). Moisture-resistant (green board) for bathrooms/kitchens. Soundproof drywall for home theaters or bedrooms near noise sources."),
        ],
        "city_proj": "drywall-installation",
    },
    {
        "slug": "how-much-does-a-fence-cost",
        "title": "How Much Does a Fence Cost to Install? (2026)",
        "desc": "Fence installation costs $15–$40 per linear foot. A full yard (150–200 ft) runs $3,000–$8,000. 2026 pricing by fence type and material.",
        "h1": "How Much Does a Fence Cost to Install?",
        "keywords": "how much does a fence cost, fence installation cost 2026, average fence cost, cost to install fence",
        "vol": 4400,
        "low": 2000, "mid": 5500, "high": 14000,
        "calc_slug": "fence-installation",
        "intro": "Fence installation costs <strong>$15–$40 per linear foot</strong> installed, depending on material and fence type. A typical yard (150–200 linear feet) runs <strong>$3,000–$7,000</strong> for wood privacy fencing. Vinyl and metal options cost more but require less maintenance.",
        "scope_rows": [
            ("Chain-link fence (100–200 ft)", "$1,500", "$4,000"),
            ("Wood privacy fence (100–200 ft)", "$3,000", "$7,000"),
            ("Vinyl privacy fence (100–200 ft)", "$4,500", "$10,000"),
            ("Full yard perimeter (200–400 ft)", "$6,000", "$16,000"),
        ],
        "component_rows": [
            ("Wood fence (per linear foot)", "$18", "$30"),
            ("Vinyl fence (per linear foot)", "$28", "$42"),
            ("Chain-link (per linear foot)", "$12", "$20"),
            ("Aluminum/ornamental (per linear foot)", "$30", "$50"),
            ("Post holes & concrete", "$5", "$9/ft"),
            ("Walk gate (single)", "$200", "$500"),
            ("Drive gate (double)", "$600", "$1,500"),
            ("Old fence removal", "$4", "$7/ft"),
        ],
        "region_rows": [
            ("South (TX, FL, GA)", "$1,800", "$5,500", "0.82–0.95×"),
            ("Midwest (OH, IL, MI)", "$2,000", "$6,000", "0.88–1.10×"),
            ("Mountain (CO, AZ, UT)", "$2,200", "$6,500", "0.95–1.05×"),
            ("Northeast (NY, MA, CT)", "$3,000", "$9,000", "1.12–1.35×"),
            ("West (CA, WA, OR)", "$3,200", "$9,500", "1.10–1.55×"),
        ],
        "faqs": [
            ("How long does fence installation take?", "Most residential fence projects (100–200 ft) take 1–3 days. Larger perimeter fences or projects requiring permits can take 3–5 days plus permit wait time (1–3 weeks)."),
            ("What's the cheapest fence option?", "Chain-link is the most affordable at $12–20/linear foot installed. It's durable and low-maintenance but provides minimal privacy. Split-rail wood is the next most affordable at $14–22/ft."),
            ("Do I need a permit for a fence?", "Most municipalities require permits for fences over 6 feet tall, fences near property lines, or fences in front yards. Check with your local building department before installation — violations can result in costly removal orders."),
            ("What's the most durable fence material?", "Metal/aluminum fences last 50+ years with minimal maintenance. Vinyl fences last 20–30 years and resist rot and insects. Cedar wood lasts 15–25 years with periodic staining. Pressure-treated pine lasts 10–20 years."),
            ("How can I find my property line before installing a fence?", "Review your property survey (typically provided at closing). You can hire a licensed surveyor ($500–$1,000) for precision. Many municipalities offer free property line lookups via their GIS portal."),
        ],
        "city_proj": "fence-installation",
    },
    {
        "slug": "how-much-does-interior-painting-cost",
        "title": "How Much Does Interior Painting Cost? (2026)",
        "desc": "Interior painting costs $2–$6 per square foot. A full home runs $3,000–$9,000. 2026 pricing by room size and paint quality.",
        "h1": "How Much Does Interior Painting Cost?",
        "keywords": "how much does interior painting cost, interior painting cost 2026, average cost to paint interior of house, house painting cost",
        "vol": 1300,
        "low": 900, "mid": 3200, "high": 8500,
        "calc_slug": "interior-painting",
        "intro": "Interior painting costs <strong>$2–$6 per square foot</strong> depending on room size, paint quality, and surface prep required. A single room runs <strong>$350–$800</strong>; painting a full 3-bedroom home typically costs <strong>$3,000–$6,000</strong> including walls and ceilings.",
        "scope_rows": [
            ("Single room (walls only)", "$350", "$700"),
            ("Bedroom + bathroom (2 rooms)", "$700", "$1,500"),
            ("3-bedroom home (walls + ceilings)", "$2,500", "$5,000"),
            ("Full home with trim & doors", "$4,000", "$9,000"),
        ],
        "component_rows": [
            ("Labor (walls, 1 coat)", "$1.50", "$2.50/sqft"),
            ("Labor (walls, 2 coats)", "$2.50", "$4.00/sqft"),
            ("Ceiling painting", "$1.20", "$2.00/sqft"),
            ("Door painting (each)", "$80", "$180"),
            ("Trim & baseboards", "$1.50", "$2.50/lf"),
            ("Paint & primer (material)", "$30", "$80/gallon"),
            ("Surface prep & patching", "$0.50", "$1.50/sqft"),
        ],
        "region_rows": [
            ("South (TX, FL, GA)", "$800", "$3,500", "0.82–0.95×"),
            ("Midwest (OH, IL, MI)", "$1,000", "$4,000", "0.88–1.10×"),
            ("Mountain (CO, AZ, UT)", "$1,100", "$4,500", "0.95–1.05×"),
            ("Northeast (NY, MA, CT)", "$1,500", "$6,000", "1.12–1.35×"),
            ("West (CA, WA, OR)", "$1,600", "$6,500", "1.10–1.55×"),
        ],
        "faqs": [
            ("How much does it cost to paint a room?", "A typical 12×12 bedroom costs $350–$700 to paint walls only, or $500–$900 including ceiling, trim, and door. Larger rooms and rooms with high ceilings cost more."),
            ("How long does interior painting take?", "A single room takes 4–8 hours. A full 3-bedroom home takes 2–4 days for walls and ceilings. Add 1–2 days for trim, doors, and multiple coats."),
            ("How much does a painter charge per hour?", "Professional painters charge $40–$80/hour, but most interior painting jobs are priced per room or per square foot. Always get a fixed quote for interior work."),
            ("What's the best paint finish for different rooms?", "Flat/matte for ceilings and low-traffic bedrooms. Eggshell for living rooms and dining rooms. Satin for hallways and kids' rooms. Semi-gloss for kitchens, bathrooms, and trim."),
            ("How can I reduce painting costs?", "Move furniture yourself before painters arrive. Fill small holes and do minor prep work. Choose fewer colors (color changes add time). Get at least 3 quotes — painting prices vary widely between contractors."),
        ],
        "city_proj": "interior-painting",
    },
    {
        "slug": "how-much-does-siding-cost",
        "title": "How Much Does Siding Replacement Cost? (2026)",
        "desc": "Siding replacement costs $5–$15 per square foot. A full home runs $7,000–$25,000. 2026 pricing by material type and home size.",
        "h1": "How Much Does Siding Replacement Cost?",
        "keywords": "how much does siding cost, siding replacement cost 2026, average cost to replace siding, new siding cost",
        "vol": 1300,
        "low": 6500, "mid": 14000, "high": 32000,
        "calc_slug": "siding-replacement",
        "intro": "Siding replacement costs <strong>$5–$15 per square foot</strong> installed, depending on material. A typical 1,500 sqft home runs <strong>$7,000–$18,000</strong> for vinyl siding. Fiber cement (Hardie board) costs 30–50% more but lasts longer and looks better.",
        "scope_rows": [
            ("Vinyl siding — small home (1,000 sqft)", "$5,500", "$9,000"),
            ("Vinyl siding — average home (1,500 sqft)", "$7,000", "$13,000"),
            ("Fiber cement — average home (1,500 sqft)", "$11,000", "$18,000"),
            ("Large home or premium material (2,500 sqft)", "$16,000", "$35,000"),
        ],
        "component_rows": [
            ("Vinyl siding (standard)", "$3", "$7/sqft"),
            ("Vinyl siding (insulated)", "$5", "$9/sqft"),
            ("Fiber cement (Hardie board)", "$7", "$12/sqft"),
            ("Cedar wood siding", "$9", "$16/sqft"),
            ("Metal/steel siding", "$8", "$14/sqft"),
            ("Old siding removal", "$1", "$2/sqft"),
            ("House wrap/moisture barrier", "$0.50", "$1.20/sqft"),
        ],
        "region_rows": [
            ("South (TX, FL, GA)", "$5,500", "$14,000", "0.82–0.95×"),
            ("Midwest (OH, IL, MI)", "$6,500", "$16,000", "0.88–1.10×"),
            ("Mountain (CO, AZ, UT)", "$7,000", "$17,000", "0.95–1.05×"),
            ("Northeast (NY, MA, CT)", "$9,500", "$22,000", "1.12–1.35×"),
            ("West (CA, WA, OR)", "$10,000", "$24,000", "1.10–1.55×"),
        ],
        "faqs": [
            ("How long does siding replacement take?", "A full home siding replacement takes 3–7 days for a crew of 2–3. Smaller homes or partial replacements take 1–3 days. Weather delays are common — factor in extra time for scheduling."),
            ("Vinyl vs. fiber cement siding — which is better?", "Vinyl is cheaper ($3–7/sqft) and nearly maintenance-free. Fiber cement costs more ($7–12/sqft) but looks more like real wood, holds paint longer, and is more impact/fire resistant. For a home you plan to sell, fiber cement typically offers better ROI."),
            ("How long does siding last?", "Vinyl siding lasts 20–40 years. Fiber cement lasts 25–50 years. Cedar wood lasts 20–40 years with regular maintenance. Metal siding lasts 40–60+ years."),
            ("Should I repair or replace siding?", "Repair if damage is limited to less than 20% of the surface and underlying sheathing is sound. Replace if there's widespread rot, warping, high energy bills (poor insulation), or the siding is 25+ years old."),
            ("Can I put new siding over old siding?", "Yes — you can install new vinyl over old wood siding if the old siding is firmly attached and level. This saves removal costs ($1–2/sqft) but adds weight. Most contractors recommend full removal for better moisture management."),
        ],
        "city_proj": "siding-replacement",
    },
]


def make_guide(g):
    city_links = ""
    top_cities = [
        ("New York", "new-york"), ("Los Angeles", "los-angeles"), ("Chicago", "chicago"),
        ("Houston", "houston"), ("Phoenix", "phoenix"), ("San Diego", "san-diego"),
        ("Dallas", "dallas"), ("Seattle", "seattle"), ("Denver", "denver"),
        ("Atlanta", "atlanta"), ("Miami", "miami"), ("Boston", "boston"),
        ("Austin", "austin"), ("Portland", "portland"), ("Minneapolis", "minneapolis"),
        ("Nashville", "nashville"), ("Charlotte", "charlotte"), ("San Francisco", "san-francisco"),
        ("Las Vegas", "las-vegas"), ("Tampa", "tampa"), ("Philadelphia", "philadelphia"),
        ("San Antonio", "san-antonio"), ("Indianapolis", "indianapolis"), ("Columbus", "columbus"),
    ]
    for city, slug in top_cities:
        city_links += f'<a href="/tools/{g["city_proj"]}-cost-{slug}/" class="city-link">{city}</a>\n'

    scope_rows = "\n".join(f"<tr><td>{r[0]}</td><td>{r[1]}</td><td>{r[2]}</td></tr>" for r in g["scope_rows"])
    comp_rows  = "\n".join(f"<tr><td>{r[0]}</td><td>{r[1]}</td><td>{r[2]}</td></tr>" for r in g["component_rows"])
    reg_rows   = "\n".join(f"<tr><td>{r[0]}</td><td>{r[1]}</td><td>{r[2]}</td><td>{r[3]}</td></tr>" for r in g["region_rows"])
    faqs_html  = "\n".join(faq(q, a) for q, a in g["faqs"])

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{g["title"]}</title>
<meta name="description" content="{g["desc"]}">
<meta name="keywords" content="{g["keywords"]}">
<link rel="canonical" href="https://estimates-pro.com/guides/{g["slug"]}/">
<link rel="icon" type="image/x-icon" href="../../favicon.ico">
<meta property="og:title" content="{g["title"]}">
<meta property="og:description" content="{g["desc"]}">
<meta property="og:url" content="https://estimates-pro.com/guides/{g["slug"]}/">
<meta property="og:type" content="article">
<script type="application/ld+json">
{{
  "@context":"https://schema.org","@type":"Article",
  "headline":"{g["h1"]}",
  "description":"{g["desc"]}",
  "url":"https://estimates-pro.com/guides/{g["slug"]}/",
  "publisher":{{"@type":"Organization","name":"CostEstimator","url":"https://estimates-pro.com"}}
}}
</script>
{BASE_CSS}
</head>
<body>
{NAV.format(icon="../../images/icon.png")}
<div class="hero">
  <div class="breadcrumb"><a href="/">Home</a> › <a href="/guides/">Cost Guides</a> › {g["h1"]}</div>
  <h1>{g["h1"]}</h1>
  <p>{g["intro"]}</p>
  <div class="cost-pills">
    <div class="cost-pill"><span>Low</span>${fmt(g["low"])}</div>
    <div class="cost-pill"><span>Average</span>${fmt(g["mid"])}</div>
    <div class="cost-pill"><span>High</span>${fmt(g["high"])}</div>
  </div>
</div>
<div class="content">

  <div class="info-box">
    💡 Want a precise local estimate? <a href="/tools/{g["calc_slug"]}-cost-calculator/">Use our free {g["h1"].replace("How Much Does a ","").replace("How Much Does ","").replace(" Cost?","").replace("2026","").strip()} cost calculator</a> — adjusts for your city and scope of work.
  </div>

  <h2>Cost by Project Scope</h2>
  <table class="cost-table">
    <thead><tr><th>Scope</th><th>Low Estimate</th><th>High Estimate</th></tr></thead>
    <tbody>{scope_rows}</tbody>
  </table>

  <h2>Cost Breakdown by Component</h2>
  <table class="cost-table">
    <thead><tr><th>Component</th><th>Low</th><th>High</th></tr></thead>
    <tbody>{comp_rows}</tbody>
  </table>

  <h2>Cost by US Region</h2>
  <p>Labor rates and material costs vary significantly by location. Here's how costs differ across US regions:</p>
  <table class="cost-table region-table">
    <thead><tr><th>Region</th><th>Low</th><th>High</th><th>Multiplier</th></tr></thead>
    <tbody>{reg_rows}</tbody>
  </table>

  {app_cta(g["h1"].replace("How Much Does a ","").replace("How Much Does ","").replace(" Cost?","").strip())}

  <h2>Frequently Asked Questions</h2>
  {faqs_html}

  <h2>Calculate Your Local Cost</h2>
  <p>Costs vary by up to 80% depending on your city. Use our city-specific calculators for a more accurate estimate:</p>
  <div class="city-grid">
    {city_links}
  </div>

</div>
{FOOTER}
{FAQ_JS}
</body>
</html>'''


# ─────────────────────────────────────────────────────────────────────────────
# PART 2 — TEMPLATE PAGES
# ─────────────────────────────────────────────────────────────────────────────

TEMPLATES = [
    {
        "slug": "free-estimate-template",
        "title": "Free Contractor Estimate Template (Word, PDF, Excel) — 2026",
        "desc": "Download a free contractor estimate template in Word, PDF, or Excel. Professional format used by contractors, electricians, plumbers, and handymen.",
        "h1": "Free Contractor Estimate Template",
        "keywords": "free estimate template, contractor estimate template, construction estimate template, free estimate form",
        "trade": "general",
        "fields": ["Client name & address", "Project description", "Labor breakdown (hours × rate)", "Materials list with unit costs", "Subtotal, markup %, tax", "Total amount due", "Terms & signature line"],
        "tips": [
            ("Always itemize labor and materials separately", "Clients trust itemized estimates more — it shows you've actually thought through the job, not just guessed a number."),
            ("Include your markup clearly", "Most contractors include 15–25% overhead and profit. Be transparent about it — clients who understand the breakdown are less likely to haggle."),
            ("Set an expiration date", "Material costs change. Protect yourself by adding 'This estimate is valid for 30 days from the date above.'"),
            ("Get a signed approval before starting", "A signed estimate = a basic contract. It protects both you and the client if disputes arise later."),
        ],
    },
    {
        "slug": "roofing-estimate-template",
        "title": "Free Roofing Estimate Template (PDF, Word) — 2026",
        "desc": "Download a free roofing estimate template. Professional format covering materials, labor, tear-off, and permits for roofing contractors.",
        "h1": "Free Roofing Estimate Template",
        "keywords": "roofing estimate template, roof estimate form, free roofing quote template, roofing proposal template",
        "trade": "roofing",
        "fields": ["Roof size (squares)", "Pitch factor", "Shingle type & color", "Tear-off & disposal", "Underlayment & ice shield", "Flashing work", "Labor (per square)", "Permits & inspections", "Warranty terms"],
        "tips": [
            ("Measure in 'squares' (100 sqft)", "Roofing is priced per square. A 2,000 sqft roof = 20 squares. Add 10–15% for waste on complex roofs with multiple valleys or hips."),
            ("Always include decking conditions", "Note whether decking repair will be needed — rotted sheathing costs $80–$150/sheet to replace. This is a common source of 'surprise' charges."),
            ("List shingle brand and warranty", "Homeowners value manufacturer warranties (25–50 years). Specifying the brand protects you from clients claiming you installed cheaper material."),
            ("Include a photo inspection report", "Attach photos of the existing roof to your estimate. It documents the pre-work condition and protects against disputes after the job."),
        ],
    },
    {
        "slug": "construction-estimate-template",
        "title": "Free Construction Estimate Template (Excel, PDF) — 2026",
        "desc": "Download a free construction estimate template with line-item breakdown for labor, materials, subcontractors, and overhead. Updated 2026.",
        "h1": "Free Construction Estimate Template",
        "keywords": "construction estimate template, construction cost estimate template, building estimate template, general contractor estimate template",
        "trade": "construction",
        "fields": ["Division-based breakdown (CSI format)", "Labor hours × rate per trade", "Materials with quantity & unit cost", "Subcontractor line items", "General conditions (supervision, temp facilities)", "Overhead & profit (O&P)", "Allowances and exclusions", "Total contract value"],
        "tips": [
            ("Use CSI division format for larger projects", "The Construction Specifications Institute (CSI) MasterFormat divides work into 50 divisions. Using this structure makes your estimate look professional and makes it easier for owners to compare bids."),
            ("List exclusions explicitly", "What's NOT included is as important as what is. 'Excludes: permits, site work, existing structure demo' prevents scope creep disputes."),
            ("Add a contingency line", "Professional GCs include 5–10% contingency for unknowns. Show it as a separate line — it's honest, and most owners expect it."),
            ("Track budget vs. actual", "The best estimates become cost tracking tools. Use the same line items through the project to see where you're over/under budget."),
        ],
    },
    {
        "slug": "painting-estimate-template",
        "title": "Free Painting Estimate Template (PDF, Word) — 2026",
        "desc": "Download a free interior and exterior painting estimate template. Professional format with room-by-room breakdown for painting contractors.",
        "h1": "Free Painting Estimate Template",
        "keywords": "painting estimate template, painter estimate form, free painting quote template, interior painting estimate template",
        "trade": "painting",
        "fields": ["Room-by-room breakdown", "Ceiling height", "Number of coats", "Paint brand & finish", "Surface prep required", "Doors & trim (each)", "Labor hours per area", "Materials cost", "Total with markup"],
        "tips": [
            ("Quote by room, not just total sqft", "Clients understand room-by-room quotes better. It also protects you if they decide to cut scope — you can remove rooms from the quote easily."),
            ("Specify paint brand and sheen", "Don't just say 'quality paint.' Write 'Sherwin-Williams SuperPaint, eggshell finish.' It prevents disputes and lets clients verify what they're getting."),
            ("Charge separately for prep work", "Surface prep (patching holes, sanding, priming) is often underestimated. List it as a separate line — clients who see it understand why you can't just do '2 coats and done.'"),
            ("Include a number-of-coats guarantee", "State exactly how many coats are included. 'Minimum 2 coats, 3 coats if full color change' protects you and manages expectations."),
        ],
    },
    {
        "slug": "electrical-estimate-template",
        "title": "Free Electrical Estimate Template (PDF) — 2026",
        "desc": "Download a free electrical estimate template for electricians. Covers wiring, panel upgrades, fixtures, permits, and labor breakdown.",
        "h1": "Free Electrical Estimate Template",
        "keywords": "electrical estimate template, electrician estimate form, free electrical quote template, electrical bid template",
        "trade": "electrical",
        "fields": ["Panel upgrade / service work", "New circuits (each)", "Outlet & switch rough-in", "Fixture installation (each)", "Wire runs (by linear foot)", "Conduit & junction boxes", "Permit & inspection fees", "Labor (hours × journeyman rate)", "Apprentice labor (if applicable)"],
        "tips": [
            ("Always pull permits for electrical work", "Unpermitted electrical work creates liability and can void homeowners insurance. Always include permit cost in your estimate — clients who balk at permit fees are clients you don't want."),
            ("Break out permit fees separately", "Electrical permit fees vary widely ($50–$500+). List them as a pass-through so clients see it's a government fee, not your markup."),
            ("Include load calculations for panel work", "Document the existing load and new load for panel upgrades. This protects you if the client later adds more circuits and claims your work was undersized."),
            ("Specify wire gauge and type", "Write '12 AWG copper for 20A circuits, 14 AWG for 15A lighting circuits.' It demonstrates professionalism and prevents shortcuts from being demanded later."),
        ],
    },
]


def make_template_page(t):
    fields_html = "\n".join(f"<li>{f}</li>" for f in t["fields"])
    tips_html = "\n".join(f'''<div style="background:var(--white);border:1px solid var(--border);border-radius:10px;padding:16px 20px;margin-bottom:10px">
  <strong style="color:var(--blue-dark)">{tip[0]}</strong>
  <p style="margin:6px 0 0;font-size:14px">{tip[1]}</p>
</div>''' for tip in t["tips"])

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{t["title"]}</title>
<meta name="description" content="{t["desc"]}">
<meta name="keywords" content="{t["keywords"]}">
<link rel="canonical" href="https://estimates-pro.com/templates/{t["slug"]}/">
<link rel="icon" type="image/x-icon" href="../../favicon.ico">
<meta property="og:title" content="{t["title"]}">
<meta property="og:description" content="{t["desc"]}">
<meta property="og:url" content="https://estimates-pro.com/templates/{t["slug"]}/">
{BASE_CSS}
<style>
.template-preview{{background:var(--white);border:1px solid var(--border);border-radius:14px;padding:32px;margin:24px 0;font-size:14px}}
.template-preview .tp-header{{border-bottom:2px solid var(--blue);padding-bottom:16px;margin-bottom:20px;display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:12px}}
.tp-company{{font-size:18px;font-weight:800;color:var(--blue-dark)}}
.tp-label{{font-size:11px;text-transform:uppercase;letter-spacing:.8px;color:var(--text-sec);font-weight:700}}
.tp-table{{width:100%;border-collapse:collapse;margin:16px 0}}
.tp-table th{{background:#f1f5f9;padding:8px 12px;text-align:left;font-size:12px;text-transform:uppercase;letter-spacing:.5px;color:var(--text-sec)}}
.tp-table td{{padding:8px 12px;border-bottom:1px solid var(--border);font-size:13px}}
.tp-total{{text-align:right;font-size:16px;font-weight:800;color:var(--blue-dark);margin-top:12px;padding-top:12px;border-top:2px solid var(--blue)}}
.download-box{{background:var(--blue-light);border-radius:12px;padding:24px;text-align:center;margin:24px 0}}
.download-box h3{{color:var(--blue-dark);margin-bottom:8px}}
.download-box p{{font-size:14px;margin-bottom:16px}}
.dl-note{{font-size:12px;color:var(--text-sec);margin-top:10px}}
ul.fields{{list-style:none;padding:0;display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:8px;margin:12px 0}}
ul.fields li{{padding:8px 12px;background:var(--white);border:1px solid var(--border);border-radius:8px;font-size:14px;font-weight:600}}
ul.fields li::before{{content:"✓ ";color:var(--blue)}}
</style>
</head>
<body>
{NAV.format(icon="../../images/icon.png")}
<div class="hero">
  <div class="breadcrumb"><a href="/">Home</a> › <a href="/templates/">Templates</a> › {t["h1"]}</div>
  <h1>{t["h1"]}</h1>
  <p>Professional template with all the fields you need — free to use, no signup required.</p>
</div>
<div class="content">

  <div class="download-box">
    <h3>Get This Template in the App — Free</h3>
    <p>The Cost Estimator app generates professional estimates in this format automatically — just describe the job or snap a photo. No manual template filling needed.</p>
    <div class="cta-btns">
      <a class="cta-btn primary" href="https://apps.apple.com/us/app/cost-estimator-construction/id6758105341" style="display:inline-block;padding:12px 24px;background:var(--blue);color:#fff;border-radius:9px;font-weight:700;font-size:14px;text-decoration:none">Download Free — App Store</a>
      <a class="cta-btn" href="https://play.google.com/store/apps/details?id=com.britetodo.costestimator" style="display:inline-block;padding:12px 24px;background:#1a1a1a;color:#fff;border-radius:9px;font-weight:700;font-size:14px;text-decoration:none">Google Play — Free</a>
    </div>
    <p class="dl-note">Or copy the template below manually — it's free to use.</p>
  </div>

  <h2>What This Template Includes</h2>
  <ul class="fields">{fields_html}</ul>

  <h2>Template Preview</h2>
  <div class="template-preview">
    <div class="tp-header">
      <div>
        <div class="tp-company">Your Business Name</div>
        <div style="font-size:13px;color:var(--text-sec);margin-top:4px">License #: 000000 · Phone: (555) 000-0000</div>
        <div style="font-size:13px;color:var(--text-sec)">email@yourbusiness.com · yourbusiness.com</div>
      </div>
      <div style="text-align:right">
        <div class="tp-label">Estimate #</div>
        <div style="font-size:20px;font-weight:800;color:var(--blue)">EST-2026-001</div>
        <div style="font-size:13px;color:var(--text-sec);margin-top:4px">Date: {__import__("datetime").date.today().strftime("%B %d, %Y")}</div>
        <div style="font-size:13px;color:var(--text-sec)">Valid for 30 days</div>
      </div>
    </div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:20px;font-size:13px">
      <div><div class="tp-label" style="margin-bottom:4px">Client</div><strong>Client Name</strong><br>123 Main St<br>City, State ZIP</div>
      <div><div class="tp-label" style="margin-bottom:4px">Job Site</div><strong>Job Location</strong><br>Project description summary</div>
    </div>
    <table class="tp-table">
      <thead><tr><th>Description</th><th>Qty</th><th>Unit</th><th>Rate</th><th>Total</th></tr></thead>
      <tbody>
        <tr><td>Labor — [Trade] (Journeyman)</td><td>16</td><td>hrs</td><td>$85.00</td><td>$1,360.00</td></tr>
        <tr><td>Materials — [Item description]</td><td>1</td><td>lot</td><td>$850.00</td><td>$850.00</td></tr>
        <tr><td>Materials — [Item description]</td><td>24</td><td>units</td><td>$18.50</td><td>$444.00</td></tr>
        <tr><td>Permits & Inspections</td><td>1</td><td>lot</td><td>$250.00</td><td>$250.00</td></tr>
        <tr><td colspan="4" style="text-align:right;color:var(--text-sec)">Subtotal</td><td>$2,904.00</td></tr>
        <tr><td colspan="4" style="text-align:right;color:var(--text-sec)">Overhead & Profit (20%)</td><td>$580.80</td></tr>
        <tr><td colspan="4" style="text-align:right;color:var(--text-sec)">Tax (8.5%)</td><td>$294.30</td></tr>
      </tbody>
    </table>
    <div class="tp-total">TOTAL: $3,779.10</div>
    <div style="margin-top:20px;padding-top:16px;border-top:1px solid var(--border);font-size:12px;color:var(--text-sec)">
      <strong style="color:var(--text)">Terms:</strong> 50% deposit required to schedule. Balance due upon completion. This estimate is valid for 30 days.<br>
      <strong style="color:var(--text)">Exclusions:</strong> [List anything not included]<br><br>
      <div style="display:flex;gap:40px;margin-top:12px">
        <div>Client Signature: _________________ Date: _______</div>
        <div>Contractor Signature: _________________ Date: _______</div>
      </div>
    </div>
  </div>

  <h2>Pro Tips for Better Estimates</h2>
  {tips_html}

  {app_cta("Professional")}

  <h2>More Estimate Templates</h2>
  <div class="city-grid">
    <a href="/templates/free-estimate-template/" class="city-link">General Estimate Template</a>
    <a href="/templates/roofing-estimate-template/" class="city-link">Roofing Estimate</a>
    <a href="/templates/construction-estimate-template/" class="city-link">Construction Estimate</a>
    <a href="/templates/painting-estimate-template/" class="city-link">Painting Estimate</a>
    <a href="/templates/electrical-estimate-template/" class="city-link">Electrical Estimate</a>
  </div>

</div>
{FOOTER}
</body>
</html>'''


# ─── GENERATE ALL ────────────────────────────────────────────────────────────
def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

count = 0

# Guides
for g in GUIDES:
    path = os.path.join(BASE, "guides", g["slug"], "index.html")
    write(path, make_guide(g))
    count += 1
    print(f"  guide: {g['slug']}")

# Guides index
guides_links = "\n".join(
    f'<li><a href="/guides/{g["slug"]}/">{g["h1"]}</a> <span style="color:var(--text-sec);font-size:12px">{g["vol"]:,}/mo</span></li>'
    for g in GUIDES
)
write(os.path.join(BASE, "guides", "index.html"), f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Construction Cost Guides — How Much Does It Cost? (2026)</title>
<meta name="description" content="Free 2026 construction cost guides. How much does a bathroom remodel, kitchen remodel, new roof, window replacement, and more cost?">
<link rel="canonical" href="https://estimates-pro.com/guides/">
<link rel="icon" type="image/x-icon" href="../favicon.ico">
{BASE_CSS}
</head><body>
{NAV.format(icon="../images/icon.png")}
<div class="hero"><h1>Construction Cost Guides</h1><p>Updated 2026 pricing for every major home improvement project.</p></div>
<div class="content">
<ul style="list-style:none;padding:0;display:flex;flex-direction:column;gap:8px">{guides_links}</ul>
{app_cta("Your Project")}
</div>{FOOTER}</body></html>''')

# Templates
for t in TEMPLATES:
    path = os.path.join(BASE, "templates", t["slug"], "index.html")
    write(path, make_template_page(t))
    count += 1
    print(f"  template: {t['slug']}")

# Templates index
tmpl_links = "\n".join(
    f'<li><a href="/templates/{t["slug"]}/">{t["h1"]}</a></li>'
    for t in TEMPLATES
)
write(os.path.join(BASE, "templates", "index.html"), f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Free Contractor Estimate Templates — PDF, Word, Excel (2026)</title>
<meta name="description" content="Free professional estimate templates for contractors. Download roofing, painting, electrical, and construction estimate templates in PDF and Word format.">
<link rel="canonical" href="https://estimates-pro.com/templates/">
<link rel="icon" type="image/x-icon" href="../favicon.ico">
{BASE_CSS}
</head><body>
{NAV.format(icon="../images/icon.png")}
<div class="hero"><h1>Free Estimate Templates</h1><p>Professional contractor estimate templates — free to use, no signup required.</p></div>
<div class="content">
<ul style="list-style:none;padding:0;display:flex;flex-direction:column;gap:8px">{tmpl_links}</ul>
{app_cta("Professional")}
</div>{FOOTER}</body></html>''')

print(f"\nTotal: {count} pages generated")
print(f"  {len(GUIDES)} guides in /guides/")
print(f"  {len(TEMPLATES)} templates in /templates/")
