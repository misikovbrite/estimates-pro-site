#!/usr/bin/env python3
"""Generate comparison page + invoice template."""
import os

BASE = os.path.dirname(os.path.abspath(__file__))

# ─── CSS SHARED ────────────────────────────────────────────────────────────────
CSS = '''<style>
*,*::before,*::after{margin:0;padding:0;box-sizing:border-box}
:root{--blue:#1565C0;--blue-dark:#0D47A1;--blue-light:#E3F2FD;--text:#1C1C1E;--text-sec:#6E6E73;--border:#E5E7EB;--bg:#F9FAFB;--white:#fff;--green:#16a34a;--green-bg:#dcfce7}
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
.hero p{color:rgba(255,255,255,.8);max-width:620px;margin:0 auto 20px}
.breadcrumb{font-size:12px;color:rgba(255,255,255,.6);margin-bottom:14px}
.breadcrumb a{color:rgba(255,255,255,.7);text-decoration:none}
.content{max-width:920px;margin:0 auto;padding:40px 24px 80px}
.faq-item{border:1px solid var(--border);border-radius:10px;margin-bottom:10px;overflow:hidden}
.faq-q{padding:14px 18px;font-weight:700;font-size:15px;cursor:pointer;display:flex;justify-content:space-between;align-items:center;background:var(--white)}
.faq-q:hover{background:var(--bg)}
.faq-a{padding:0 18px 14px;font-size:14px;line-height:1.7;color:#374151;display:none}
.faq-item.open .faq-a{display:block}
.faq-item.open .faq-chevron{transform:rotate(180deg)}
.faq-chevron{transition:transform .2s;color:var(--text-sec)}
.app-cta{background:linear-gradient(135deg,var(--blue-dark),var(--blue));border-radius:14px;padding:32px 28px;text-align:center;margin:40px 0;color:#fff}
.app-cta h2{color:#fff;margin:0 0 8px}
.app-cta p{color:rgba(255,255,255,.8);margin-bottom:20px}
.cta-btns{display:flex;gap:12px;justify-content:center;flex-wrap:wrap}
.cta-btn{background:rgba(255,255,255,.15);border:1.5px solid rgba(255,255,255,.4);color:#fff;padding:10px 22px;border-radius:9px;font-weight:700;font-size:14px;text-decoration:none}
.cta-btn.primary{background:#fff;color:var(--blue-dark)}
.check{color:var(--green);font-weight:700}
.cross{color:#9ca3af;font-weight:700}
</style>'''

NAV = '''<nav>
  <a class="nav-logo" href="/"><img src="../../images/icon.png" alt="Cost Estimator">Cost<span>Estimator</span></a>
  <a class="nav-cta" href="https://apps.apple.com/us/app/cost-estimator-construction/id6758105341">Download Free</a>
</nav>'''

FOOTER = '''<footer>
  <div class="footer-logo">CostEstimator</div>
  <p style="margin-bottom:12px">Free construction estimating app for contractors</p>
  <div><a href="/">Home</a><a href="/tools/">Calculators</a><a href="/guides/">Cost Guides</a><a href="/templates/">Templates</a></div>
  <p style="margin-top:12px">© 2026 Brite Technologies LLC · hello@britetodo.com</p>
</footer>'''

FAQ_JS = '''<script>
document.querySelectorAll('.faq-q').forEach(q=>{
  q.addEventListener('click',()=>q.closest('.faq-item').classList.toggle('open'));
});
</script>'''

CHEVRON = '<svg class="faq-chevron" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>'

# ─── PAGE 1: CONSTRUCTION ESTIMATING SOFTWARE COMPARISON ──────────────────────
def build_comparison():
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Best Construction Estimating Software 2026 — Free App vs Jobber vs Buildertrend</title>
<meta name="description" content="Compare the best construction estimating software for contractors in 2026. Free app vs Jobber, Buildertrend, and Excel — which is right for your business?">
<meta name="keywords" content="construction estimating software, best construction estimating software, free construction estimating software, contractor estimating app, jobber alternative, buildertrend alternative">
<link rel="canonical" href="https://estimates-pro.com/tools/construction-estimating-software/">
<link rel="icon" type="image/x-icon" href="../../favicon.ico">
<meta property="og:title" content="Best Construction Estimating Software 2026">
<meta property="og:description" content="Compare top construction estimating apps and software for small contractors — free app vs Jobber, Buildertrend, and Excel.">
<meta property="og:url" content="https://estimates-pro.com/tools/construction-estimating-software/">
<meta property="og:type" content="website">
<meta property="og:image" content="https://estimates-pro.com/images/screen1.png">
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Best Construction Estimating Software 2026",
  "description": "Comparison of top construction estimating apps for small contractors",
  "url": "https://estimates-pro.com/tools/construction-estimating-software/",
  "publisher": {{"@type": "Organization", "name": "CostEstimator", "url": "https://estimates-pro.com"}}
}}
</script>
{CSS}
<style>
.comp-table{{width:100%;border-collapse:collapse;margin:20px 0;font-size:14px;overflow-x:auto;display:block}}
.comp-table th{{background:var(--blue-dark);color:#fff;padding:12px 16px;text-align:left;font-size:12px;text-transform:uppercase;letter-spacing:.5px;white-space:nowrap}}
.comp-table th.highlight{{background:var(--blue)}}
.comp-table td{{padding:11px 16px;border-bottom:1px solid var(--border);vertical-align:middle}}
.comp-table tr:nth-child(even) td{{background:#f8fafc}}
.comp-table td.highlight{{background:var(--blue-light);font-weight:600}}
.comp-table tr:last-child td{{border-bottom:none}}
.winner-badge{{display:inline-block;background:var(--green);color:#fff;font-size:10px;font-weight:700;padding:2px 7px;border-radius:50px;margin-left:6px;letter-spacing:.5px;text-transform:uppercase;vertical-align:middle}}
.price-tag{{font-weight:800;color:var(--blue-dark)}}
.feature-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:16px;margin:20px 0}}
.feature-card{{background:var(--white);border:1px solid var(--border);border-radius:12px;padding:22px}}
.feature-card.featured{{border-color:var(--blue);box-shadow:0 4px 20px rgba(21,101,192,.1)}}
.feature-icon{{font-size:24px;margin-bottom:10px}}
.feature-card h3{{font-size:15px;font-weight:700;margin-bottom:6px}}
.feature-card p{{font-size:13px;color:var(--text-sec);line-height:1.6}}
.verdict-box{{background:var(--blue-light);border:1.5px solid var(--blue);border-radius:12px;padding:24px;margin:24px 0}}
.verdict-box h3{{color:var(--blue-dark);margin-bottom:8px}}
</style>
</head>
<body>
{NAV}

<div class="hero">
  <div class="breadcrumb"><a href="/">Home</a> › <a href="/tools/">Tools</a> › Construction Estimating Software</div>
  <h1>Best Construction Estimating Software for 2026</h1>
  <p>Comparing top options for small contractors, electricians, and handymen — from free apps to enterprise platforms.</p>
</div>

<div class="content">

  <p>The right construction estimating software can save you 10–15 hours per week and help you win more bids. But the options range from simple free apps to enterprise platforms costing $300+/month. Here's what you actually need based on business size.</p>

  <div class="verdict-box">
    <h3>🏆 Quick Verdict for Small Contractors (1–10 employees)</h3>
    <p><strong>Cost Estimator — Construction+</strong> is the best free construction estimating app for small contractors in 2026. It's mobile-first, uses AI photo analysis, and has local pricing for 1,000+ US cities. Enterprise software like Buildertrend and Jobber is overkill for most small shops — and costs $150–$400/month.</p>
  </div>

  <h2>Construction Estimating Software Comparison (2026)</h2>

  <div style="overflow-x:auto">
  <table class="comp-table">
    <thead>
      <tr>
        <th>Software</th>
        <th class="highlight">Cost Estimator <span class="winner-badge">Best Free</span></th>
        <th>Jobber</th>
        <th>Buildertrend</th>
        <th>Excel/Spreadsheet</th>
        <th>Pen & Paper</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Starting Price</strong></td>
        <td class="highlight"><span class="price-tag">Free</span> / $9.99/mo Pro</td>
        <td><span class="price-tag">$69/mo</span></td>
        <td><span class="price-tag">$199/mo</span></td>
        <td><span class="price-tag">Free</span> (manual)</td>
        <td><span class="price-tag">Free</span></td>
      </tr>
      <tr>
        <td><strong>AI Photo Estimation</strong></td>
        <td class="highlight"><span class="check">✓</span> Yes — snap & estimate</td>
        <td><span class="cross">✗</span> No</td>
        <td><span class="cross">✗</span> No</td>
        <td><span class="cross">✗</span> No</td>
        <td><span class="cross">✗</span> No</td>
      </tr>
      <tr>
        <td><strong>Local Pricing Database</strong></td>
        <td class="highlight"><span class="check">✓</span> 1,000+ US cities</td>
        <td><span class="cross">✗</span> Manual only</td>
        <td><span class="check">✓</span> Basic</td>
        <td><span class="cross">✗</span> Manual</td>
        <td><span class="cross">✗</span> None</td>
      </tr>
      <tr>
        <td><strong>Mobile App</strong></td>
        <td class="highlight"><span class="check">✓</span> iOS &amp; Android</td>
        <td><span class="check">✓</span> iOS &amp; Android</td>
        <td><span class="check">✓</span> iOS &amp; Android</td>
        <td><span class="check">✓</span> Limited</td>
        <td><span class="cross">✗</span> No</td>
      </tr>
      <tr>
        <td><strong>PDF Estimate Export</strong></td>
        <td class="highlight"><span class="check">✓</span> Free (Pro: no watermark)</td>
        <td><span class="check">✓</span> Yes</td>
        <td><span class="check">✓</span> Yes</td>
        <td><span class="check">✓</span> Manual</td>
        <td><span class="cross">✗</span> No</td>
      </tr>
      <tr>
        <td><strong>Client Invoicing</strong></td>
        <td class="highlight"><span class="check">✓</span> Pro plan</td>
        <td><span class="check">✓</span> Yes + payments</td>
        <td><span class="check">✓</span> Yes + payments</td>
        <td><span class="check">✓</span> Manual</td>
        <td><span class="cross">✗</span> No</td>
      </tr>
      <tr>
        <td><strong>Job Scheduling</strong></td>
        <td class="highlight"><span class="cross">✗</span> Not included</td>
        <td><span class="check">✓</span> Full scheduling</td>
        <td><span class="check">✓</span> Full scheduling</td>
        <td><span class="cross">✗</span> No</td>
        <td><span class="cross">✗</span> No</td>
      </tr>
      <tr>
        <td><strong>Time to First Estimate</strong></td>
        <td class="highlight"><span class="check">✓</span> Under 2 minutes</td>
        <td>15–30 min setup</td>
        <td>1–3 hrs setup</td>
        <td>30–60 min/estimate</td>
        <td>1–2 hrs/estimate</td>
      </tr>
      <tr>
        <td><strong>Best For</strong></td>
        <td class="highlight">Solo contractors, small crews</td>
        <td>Service businesses, 2–25 staff</td>
        <td>Builders, GCs 10+ employees</td>
        <td>Tech-savvy solos</td>
        <td>Occasional work only</td>
      </tr>
    </tbody>
  </table>
  </div>

  <h2>Detailed Breakdown</h2>

  <div class="feature-grid">
    <div class="feature-card featured">
      <div class="feature-icon">📱</div>
      <h3>Cost Estimator — Construction+ <span style="font-size:10px;background:#16a34a;color:#fff;padding:2px 6px;border-radius:50px;vertical-align:middle">FREE</span></h3>
      <p>AI-powered mobile app that turns job site photos into professional estimates in 60 seconds. Uses a database of 1,000+ US cities for accurate local pricing. Best for solo contractors and small crews who need to quote fast and look professional.</p>
      <p style="margin-top:8px;font-size:13px;color:var(--blue-dark);font-weight:700">$0 free / $9.99/mo Pro</p>
    </div>
    <div class="feature-card">
      <div class="feature-icon">🔧</div>
      <h3>Jobber</h3>
      <p>Full-featured field service management software with scheduling, quoting, invoicing, and CRM. Great for HVAC, plumbing, and landscaping businesses with 2–25 employees who need route optimization and client management. Overkill for solo operators.</p>
      <p style="margin-top:8px;font-size:13px;color:#374151;font-weight:700">From $69/month</p>
    </div>
    <div class="feature-card">
      <div class="feature-icon">🏗️</div>
      <h3>Buildertrend</h3>
      <p>Enterprise construction management platform with project scheduling, budget tracking, client portal, and takeoff tools. Designed for residential builders and GCs with active project teams. Heavy learning curve — not suited for quick on-site estimating.</p>
      <p style="margin-top:8px;font-size:13px;color:#374151;font-weight:700">From $199/month</p>
    </div>
    <div class="feature-card">
      <div class="feature-icon">📊</div>
      <h3>Excel / Google Sheets</h3>
      <p>Many contractors still estimate with spreadsheets. It's free and flexible, but requires manual price updates, creates no professional PDF output, and is slow on a job site. Works best for contractors who do 1–2 estimates per week maximum.</p>
      <p style="margin-top:8px;font-size:13px;color:#374151;font-weight:700">Free (but costs you time)</p>
    </div>
  </div>

  <h2>Who Should Use What</h2>

  <table class="comp-table" style="display:table">
    <thead>
      <tr>
        <th>Your Situation</th>
        <th>Best Choice</th>
        <th>Why</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Solo contractor, handyman, 1-person crew</td>
        <td><strong>Cost Estimator (Free)</strong></td>
        <td>Fast, accurate, mobile. Zero monthly cost.</td>
      </tr>
      <tr>
        <td>Small crew (2–5 people), high quote volume</td>
        <td><strong>Cost Estimator Pro</strong></td>
        <td>$9.99/mo for unlimited estimates, invoicing, branding</td>
      </tr>
      <tr>
        <td>Service business (HVAC, plumbing) 5–25 staff</td>
        <td><strong>Jobber</strong></td>
        <td>Scheduling + field service management worth the cost</td>
      </tr>
      <tr>
        <td>Residential builder, GC, 10+ staff</td>
        <td><strong>Buildertrend</strong></td>
        <td>Full project management, client portal, subcontractors</td>
      </tr>
      <tr>
        <td>Just need occasional estimates</td>
        <td><strong>Cost Estimator (Free)</strong></td>
        <td>No commitment, no credit card</td>
      </tr>
    </tbody>
  </table>

  <h2>Frequently Asked Questions</h2>

  <div class="faq-item">
    <div class="faq-q">What is the best free construction estimating software? {CHEVRON}</div>
    <div class="faq-a">Cost Estimator — Construction+ is the best free construction estimating app in 2026. It's the only free option with AI photo estimation and a built-in database of local labor and material prices for 1,000+ US cities. Download free on iOS and Android with no credit card required.</div>
  </div>
  <div class="faq-item">
    <div class="faq-q">Is Jobber worth it for small contractors? {CHEVRON}</div>
    <div class="faq-a">Jobber is worth it once you have 3+ field technicians and need scheduling, dispatch, and client management. At $69–$169/month, the ROI requires consistent volume. For smaller operations, a free app like Cost Estimator is a better starting point.</div>
  </div>
  <div class="faq-item">
    <div class="faq-q">What's the difference between estimating software and project management software? {CHEVRON}</div>
    <div class="faq-a">Estimating software focuses on quoting — turning project scope into a cost estimate and PDF. Project management software (Buildertrend, Procore) handles scheduling, budget tracking, change orders, and team coordination. Many contractors need estimating first; project management tools come later as you scale.</div>
  </div>
  <div class="faq-item">
    <div class="faq-q">Can I use construction estimating software on my phone? {CHEVRON}</div>
    <div class="faq-a">Yes. Cost Estimator is designed specifically for the job site — it runs on iPhone and Android. You can snap a photo of any room or project, and the AI generates a detailed cost estimate. Send the PDF to your client before you leave the driveway.</div>
  </div>
  <div class="faq-item">
    <div class="faq-q">How accurate is AI construction estimating? {CHEVRON}</div>
    <div class="faq-a">AI estimating accuracy depends on data quality. Cost Estimator uses a database of 1,000+ US cities with updated 2026 labor and material rates. Most users find AI estimates within 10–15% of their manual quotes — accurate enough to ballpark a job and generate a professional document to share with clients.</div>
  </div>

  <div class="app-cta">
    <h2>Try the Best Free Construction Estimating App</h2>
    <p>No monthly fee. No credit card. Snap a photo and get a professional estimate in 60 seconds.</p>
    <div class="cta-btns">
      <a class="cta-btn primary" href="https://apps.apple.com/us/app/cost-estimator-construction/id6758105341">Download on App Store</a>
      <a class="cta-btn" href="https://play.google.com/store/apps/details?id=com.britetodo.costestimator">Get on Google Play</a>
    </div>
  </div>

</div>

{FOOTER}
{FAQ_JS}
</body>
</html>'''


# ─── PAGE 2: CONTRACTOR INVOICE TEMPLATE ──────────────────────────────────────
def build_invoice_template():
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Free Contractor Invoice Template (2026) — Editable PDF</title>
<meta name="description" content="Download a free contractor invoice template for 2026. Professional invoice layout for contractors, electricians, plumbers, and handymen. Includes all required fields — editable PDF.">
<meta name="keywords" content="contractor invoice template, free contractor invoice template, construction invoice template, contractor invoice pdf, contractor billing template, invoice template for contractors">
<link rel="canonical" href="https://estimates-pro.com/templates/contractor-invoice-template/">
<link rel="icon" type="image/x-icon" href="../../favicon.ico">
<meta property="og:title" content="Free Contractor Invoice Template (2026)">
<meta property="og:description" content="Free professional invoice template for contractors. Download or generate in the app — send to clients as PDF in 60 seconds.">
<meta property="og:url" content="https://estimates-pro.com/templates/contractor-invoice-template/">
<meta property="og:type" content="website">
<meta property="og:image" content="https://estimates-pro.com/images/screen1.png">
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Free Contractor Invoice Template 2026",
  "description": "Professional invoice template for contractors and tradespeople",
  "url": "https://estimates-pro.com/templates/contractor-invoice-template/"
}}
</script>
{CSS}
<style>
.invoice-preview{{background:var(--white);border:1px solid var(--border);border-radius:16px;padding:0;overflow:hidden;margin:28px 0;box-shadow:0 4px 24px rgba(0,0,0,.08)}}
.inv-header{{background:var(--blue-dark);color:#fff;padding:28px 32px;display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:16px}}
.inv-company{{}}
.inv-company strong{{font-size:20px;font-weight:800;display:block;margin-bottom:4px}}
.inv-company span{{font-size:13px;opacity:.7}}
.inv-title-block{{text-align:right}}
.inv-title-block .inv-title{{font-size:28px;font-weight:900;letter-spacing:-1px}}
.inv-title-block .inv-num{{font-size:13px;opacity:.7;margin-top:4px}}
.inv-body{{padding:28px 32px}}
.inv-meta{{display:grid;grid-template-columns:1fr 1fr;gap:24px;margin-bottom:24px}}
.inv-meta-block label{{font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.8px;color:var(--text-sec);display:block;margin-bottom:4px}}
.inv-meta-block strong{{font-size:14px;color:var(--text)}}
.inv-meta-block span{{font-size:13px;color:var(--text-sec);display:block;line-height:1.6}}
.inv-table{{width:100%;border-collapse:collapse;margin:16px 0}}
.inv-table th{{background:var(--bg);padding:10px 14px;text-align:left;font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:.5px;color:var(--text-sec);border-bottom:2px solid var(--border)}}
.inv-table td{{padding:12px 14px;border-bottom:1px solid var(--border);font-size:14px}}
.inv-table tr:last-child td{{border-bottom:none}}
.inv-table td:last-child,.inv-table th:last-child{{text-align:right}}
.inv-totals{{margin-top:24px;margin-left:auto;max-width:300px}}
.inv-total-row{{display:flex;justify-content:space-between;padding:8px 0;font-size:14px;border-bottom:1px solid var(--border)}}
.inv-total-row:last-child{{border-bottom:none;font-size:17px;font-weight:800;color:var(--blue-dark)}}
.inv-notes{{background:var(--bg);border-radius:8px;padding:16px;margin-top:24px;font-size:13px;color:var(--text-sec)}}
.inv-notes strong{{color:var(--text);display:block;margin-bottom:4px}}
.inv-footer{{background:var(--blue-light);padding:16px 32px;text-align:center;font-size:12px;color:var(--blue-dark);font-weight:600}}
.field-list{{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:14px;margin:20px 0}}
.field-item{{background:var(--white);border:1px solid var(--border);border-radius:10px;padding:16px}}
.field-item strong{{font-size:14px;font-weight:700;display:block;margin-bottom:4px}}
.field-item span{{font-size:13px;color:var(--text-sec);line-height:1.5}}
.required-badge{{display:inline-block;background:#fef3c7;color:#92400e;font-size:10px;font-weight:700;padding:1px 6px;border-radius:4px;margin-left:4px;vertical-align:middle}}
.optional-badge{{display:inline-block;background:var(--bg);color:var(--text-sec);font-size:10px;font-weight:700;padding:1px 6px;border-radius:4px;margin-left:4px;vertical-align:middle}}
@media(max-width:600px){{
  .inv-header{{flex-direction:column}}
  .inv-title-block{{text-align:left}}
  .inv-meta{{grid-template-columns:1fr}}
}}
</style>
</head>
<body>
{NAV}

<div class="hero">
  <div class="breadcrumb"><a href="/">Home</a> › <a href="/templates/">Templates</a> › Contractor Invoice Template</div>
  <h1>Free Contractor Invoice Template (2026)</h1>
  <p>Professional invoice layout for contractors, electricians, plumbers, and handymen. Use the template below or generate invoices instantly in the app.</p>
</div>

<div class="content">

  <p>A professional invoice builds client trust and gets you paid faster. Below is a complete contractor invoice template with all required fields. Scroll down for a field-by-field breakdown and tips on what to include.</p>

  <!-- INVOICE PREVIEW -->
  <div class="invoice-preview">
    <div class="inv-header">
      <div class="inv-company">
        <strong>Your Company Name LLC</strong>
        <span>Licensed General Contractor</span>
        <span style="display:block;margin-top:8px;opacity:.8">123 Main Street, Austin, TX 78701<br>License #: GC-123456 · (512) 555-0100<br>hello@yourcompany.com</span>
      </div>
      <div class="inv-title-block">
        <div class="inv-title">INVOICE</div>
        <div class="inv-num">Invoice #: 2026-0142<br>Date: May 15, 2026<br>Due: June 14, 2026 (Net 30)</div>
      </div>
    </div>
    <div class="inv-body">
      <div class="inv-meta">
        <div class="inv-meta-block">
          <label>Bill To</label>
          <strong>John &amp; Sarah Miller</strong>
          <span>456 Oak Drive<br>Austin, TX 78702<br>john@email.com · (512) 555-0199</span>
        </div>
        <div class="inv-meta-block">
          <label>Project / Job Site</label>
          <strong>Kitchen Remodel</strong>
          <span>456 Oak Drive, Austin TX<br>Job #: JOB-2026-088<br>Dates: Apr 28 – May 14, 2026</span>
        </div>
      </div>

      <table class="inv-table">
        <thead>
          <tr>
            <th>Description</th>
            <th>Qty</th>
            <th>Unit Price</th>
            <th>Amount</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Cabinet installation (semi-custom, 18 units)<br><span style="font-size:12px;color:var(--text-sec)">Labor + materials included</span></td>
            <td>1</td>
            <td>$6,800.00</td>
            <td>$6,800.00</td>
          </tr>
          <tr>
            <td>Quartz countertop fabrication &amp; install<br><span style="font-size:12px;color:var(--text-sec)">Silestone Calacatta Gold, 42 sqft</span></td>
            <td>42 sqft</td>
            <td>$95.00</td>
            <td>$3,990.00</td>
          </tr>
          <tr>
            <td>Tile backsplash (subway 3x6, white)<br><span style="font-size:12px;color:var(--text-sec)">22 sqft · Labor included</span></td>
            <td>22 sqft</td>
            <td>$38.00</td>
            <td>$836.00</td>
          </tr>
          <tr>
            <td>Electrical — outlet relocation (3 outlets)<br><span style="font-size:12px;color:var(--text-sec)">Licensed electrician subcontract</span></td>
            <td>1</td>
            <td>$480.00</td>
            <td>$480.00</td>
          </tr>
          <tr>
            <td>Plumbing — sink &amp; dishwasher connection</td>
            <td>1</td>
            <td>$320.00</td>
            <td>$320.00</td>
          </tr>
          <tr>
            <td>Permit fee (City of Austin)</td>
            <td>1</td>
            <td>$285.00</td>
            <td>$285.00</td>
          </tr>
        </tbody>
      </table>

      <div class="inv-totals">
        <div class="inv-total-row"><span>Subtotal</span><span>$12,711.00</span></div>
        <div class="inv-total-row"><span>Tax (8.25%)</span><span>$1,048.66</span></div>
        <div class="inv-total-row"><span>Less Deposit Paid</span><span style="color:var(--green)">– $5,000.00</span></div>
        <div class="inv-total-row"><span>Balance Due</span><span>$8,759.66</span></div>
      </div>

      <div class="inv-notes">
        <strong>Payment Terms &amp; Notes</strong>
        Payment due within 30 days of invoice date. Accepted methods: check, ACH, Zelle, credit card (+3% fee).
        All work performed per signed contract dated April 25, 2026. 1-year workmanship warranty on all labor.
      </div>
    </div>
    <div class="inv-footer">
      Thank you for your business — we appreciate the opportunity to work on your home.
    </div>
  </div>

  <h2>What Every Contractor Invoice Must Include</h2>

  <div class="field-list">
    <div class="field-item">
      <strong>Your Business Info <span class="required-badge">Required</span></strong>
      <span>Legal business name, address, phone, email, license number. Builds trust and is required for payment.</span>
    </div>
    <div class="field-item">
      <strong>Invoice Number <span class="required-badge">Required</span></strong>
      <span>Unique sequential number (e.g. 2026-0142). Essential for accounting, tax records, and disputes.</span>
    </div>
    <div class="field-item">
      <strong>Invoice Date &amp; Due Date <span class="required-badge">Required</span></strong>
      <span>Date issued + payment due date. "Net 30" is standard for most residential work.</span>
    </div>
    <div class="field-item">
      <strong>Client Information <span class="required-badge">Required</span></strong>
      <span>Client name, address, and contact info. Must match who signed the contract.</span>
    </div>
    <div class="field-item">
      <strong>Itemized Work Description <span class="required-badge">Required</span></strong>
      <span>Each line item with quantity, unit price, and total. Vague descriptions ("labor") lead to disputes.</span>
    </div>
    <div class="field-item">
      <strong>Tax &amp; Total <span class="required-badge">Required</span></strong>
      <span>Subtotal, applicable tax rate, and final balance. Show deposits or partial payments already made.</span>
    </div>
    <div class="field-item">
      <strong>Payment Methods <span class="optional-badge">Recommended</span></strong>
      <span>List accepted payment methods: check, ACH, Zelle, credit card. Reduces payment delays.</span>
    </div>
    <div class="field-item">
      <strong>Job Reference / Contract Link <span class="optional-badge">Recommended</span></strong>
      <span>Reference the job number or contract date. Protects you legally if there's ever a dispute.</span>
    </div>
    <div class="field-item">
      <strong>Warranty Statement <span class="optional-badge">Optional</span></strong>
      <span>Brief note on workmanship warranty (e.g. "1-year labor warranty"). Differentiates pro contractors.</span>
    </div>
  </div>

  <h2>Pro Tips for Getting Paid Faster</h2>

  <p><strong>Send invoices the same day work is complete.</strong> The longer you wait, the longer your client waits to pay. Contractors who invoice same-day get paid an average of 8 days faster.</p>
  <p><strong>Use progress billing for larger jobs.</strong> Break payments into milestones: 30% deposit, 40% at mid-project, 30% on completion. This protects your cash flow and reduces risk.</p>
  <p><strong>Add a late payment policy.</strong> State clearly: "1.5% per month on balances over 30 days." Most clients won't invoke it, but it signals professionalism and protects you.</p>
  <p><strong>Accept multiple payment methods.</strong> Clients who can pay by Zelle or ACH pay faster than those who have to write checks. Credit card adds a small fee but eliminates friction.</p>
  <p><strong>Follow up on day 31.</strong> Set a calendar reminder. A polite "checking in on invoice #2026-0142 due yesterday" email gets 80% of late payments resolved within 48 hours.</p>

  <h2>Frequently Asked Questions</h2>

  <div class="faq-item">
    <div class="faq-q">What should a contractor invoice include? {CHEVRON}</div>
    <div class="faq-a">A contractor invoice must include: your business name and license number, invoice number and date, client name and address, itemized line items with quantities and prices, subtotal, tax, and total due, payment terms (due date, accepted methods), and your contact information. Including a reference to the original contract or estimate also protects you legally.</div>
  </div>
  <div class="faq-item">
    <div class="faq-q">Is there a free contractor invoice template I can use? {CHEVRON}</div>
    <div class="faq-a">Yes — the template on this page is free to use. You can also use the Cost Estimator app (free on iOS and Android) to generate professional invoices directly from your estimates. The app auto-fills client info, line items, and your business details — and lets you send the PDF to clients on the spot.</div>
  </div>
  <div class="faq-item">
    <div class="faq-q">What's the difference between a contractor estimate and an invoice? {CHEVRON}</div>
    <div class="faq-a">An estimate (or quote) is given before work begins — it's an approximation of costs. An invoice is issued after work is completed (or at a billing milestone) — it's a formal request for payment. Invoices should reference the original estimate or contract and reflect actual work performed.</div>
  </div>
  <div class="faq-item">
    <div class="faq-q">Do contractors need to charge sales tax? {CHEVRON}</div>
    <div class="faq-a">It depends on your state. Most states tax the sale of materials but not labor. Some states (Texas, for example) tax the entire contract price for certain project types. Check with your state's department of revenue or a CPA. Always display your tax calculations clearly on invoices.</div>
  </div>
  <div class="faq-item">
    <div class="faq-q">How long should I keep contractor invoices? {CHEVRON}</div>
    <div class="faq-a">Keep all invoices for at least 7 years for tax purposes (IRS can audit up to 6 years back). For larger commercial projects or government contracts, retain records for 10+ years. Digital storage in a cloud app is recommended over paper copies.</div>
  </div>

  <div class="app-cta">
    <h2>Generate Professional Invoices in 60 Seconds</h2>
    <p>Use Cost Estimator to create client-ready invoices with your logo and branding — directly from your estimate. Send PDF instantly from the job site.</p>
    <div class="cta-btns">
      <a class="cta-btn primary" href="https://apps.apple.com/us/app/cost-estimator-construction/id6758105341">App Store — Free</a>
      <a class="cta-btn" href="https://play.google.com/store/apps/details?id=com.britetodo.costestimator">Google Play — Free</a>
    </div>
  </div>

  <h2>More Free Templates</h2>
  <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:10px;margin-top:16px">
    <a href="/templates/free-estimate-template/" style="display:block;padding:14px;background:var(--white);border:1px solid var(--border);border-radius:10px;font-size:14px;font-weight:600;text-decoration:none;color:var(--blue)">📄 Free Estimate Template</a>
    <a href="/templates/roofing-estimate-template/" style="display:block;padding:14px;background:var(--white);border:1px solid var(--border);border-radius:10px;font-size:14px;font-weight:600;text-decoration:none;color:var(--blue)">🏠 Roofing Estimate Template</a>
    <a href="/templates/construction-estimate-template/" style="display:block;padding:14px;background:var(--white);border:1px solid var(--border);border-radius:10px;font-size:14px;font-weight:600;text-decoration:none;color:var(--blue)">🏗️ Construction Estimate Template</a>
    <a href="/templates/painting-estimate-template/" style="display:block;padding:14px;background:var(--white);border:1px solid var(--border);border-radius:10px;font-size:14px;font-weight:600;text-decoration:none;color:var(--blue)">🖌️ Painting Estimate Template</a>
    <a href="/templates/electrical-estimate-template/" style="display:block;padding:14px;background:var(--white);border:1px solid var(--border);border-radius:10px;font-size:14px;font-weight:600;text-decoration:none;color:var(--blue)">⚡ Electrical Estimate Template</a>
  </div>

</div>

{FOOTER}
{FAQ_JS}
</body>
</html>'''


# ─── WRITE FILES ──────────────────────────────────────────────────────────────
def main():
    # Comparison page → /tools/construction-estimating-software/
    comp_dir = os.path.join(BASE, "construction-estimating-software")
    os.makedirs(comp_dir, exist_ok=True)
    with open(os.path.join(comp_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(build_comparison())
    print("✓ tools/construction-estimating-software/index.html")

    # Invoice template → /templates/contractor-invoice-template/
    inv_dir = os.path.join(os.path.dirname(BASE), "templates", "contractor-invoice-template")
    os.makedirs(inv_dir, exist_ok=True)
    with open(os.path.join(inv_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(build_invoice_template())
    print("✓ templates/contractor-invoice-template/index.html")

if __name__ == "__main__":
    main()
