#!/usr/bin/env python3
"""Generate sitemap.xml for all programmatic pages."""
import os
from datetime import date

BASE_URL = "https://estimates-pro.com"
TODAY = date.today().isoformat()

# Collect all /tools/ directories that have index.html
script_dir = os.path.dirname(os.path.abspath(__file__))
tool_dirs = sorted([
    d for d in os.listdir(script_dir)
    if os.path.isdir(os.path.join(script_dir, d))
    and os.path.exists(os.path.join(script_dir, d, "index.html"))
])

urls = [
    f"  <url><loc>{BASE_URL}/</loc><changefreq>weekly</changefreq><priority>1.0</priority></url>",
    f"  <url><loc>{BASE_URL}/tools/</loc><changefreq>weekly</changefreq><priority>0.8</priority></url>",
    f"  <url><loc>{BASE_URL}/tools/bathroom-remodel-cost-calculator</loc><changefreq>monthly</changefreq><priority>0.8</priority></url>",
]

for d in tool_dirs:
    url = f"{BASE_URL}/tools/{d}/"
    urls.append(f"  <url><loc>{url}</loc><lastmod>{TODAY}</lastmod><changefreq>monthly</changefreq><priority>0.7</priority></url>")

sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n'
sitemap += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
sitemap += "\n".join(urls)
sitemap += "\n</urlset>\n"

out = os.path.join(os.path.dirname(script_dir), "sitemap.xml")
with open(out, "w") as f:
    f.write(sitemap)

print(f"sitemap.xml: {len(urls)} URLs")
