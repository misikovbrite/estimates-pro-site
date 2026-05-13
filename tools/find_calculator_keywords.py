#!/usr/bin/env python3
"""Find high-volume calculator keyword types for programmatic city pages."""
import requests
import json
import time
from base64 import b64encode

LOGIN = "hello@britetodo.com"
PASSWORD = "17b4ff94bd5891ec"
AUTH = b64encode(f"{LOGIN}:{PASSWORD}".encode()).decode()

# Phase 1: check national volume for project types (no city)
NATIONAL_KEYWORDS = [
    # Calculators (generic)
    "deck cost calculator",
    "fence cost calculator",
    "interior painting cost calculator",
    "HVAC installation cost calculator",
    "window replacement cost calculator",
    "siding replacement cost calculator",
    "basement finishing cost calculator",
    "flooring cost calculator",
    "driveway paving cost calculator",
    "garage conversion cost calculator",
    "room addition cost calculator",
    "landscaping cost calculator",
    "pool installation cost calculator",
    "tile installation cost calculator",
    "drywall cost calculator",
    # Cost (city-intent)
    "deck addition cost",
    "fence installation cost",
    "interior painting cost",
    "HVAC replacement cost",
    "window replacement cost",
    "siding replacement cost",
    "basement finishing cost",
    "hardwood flooring cost",
    "concrete driveway cost",
    "room addition cost",
    "pool installation cost",
    "tile installation cost",
    "drywall installation cost",
    "deck building cost",
    "fence replacement cost",
]

# Top 20 cities by population (for spot checks)
SPOT_CITIES = [
    "New York", "Los Angeles", "Chicago", "Houston", "Phoenix",
    "Philadelphia", "San Antonio", "San Diego", "Dallas", "Seattle",
    "Denver", "Atlanta", "Miami", "Boston", "Austin",
    "Portland", "Minneapolis", "Tampa", "Las Vegas", "Nashville",
]

def check_keywords(keywords):
    payload = [{"keywords": keywords, "location_code": 2840, "language_code": "en"}]
    resp = requests.post(
        "https://api.dataforseo.com/v3/keywords_data/google_ads/search_volume/live",
        headers={"Authorization": f"Basic {AUTH}", "Content-Type": "application/json"},
        json=payload,
        timeout=30
    )
    data = resp.json()
    task = data.get('tasks', [{}])[0]
    if task.get('status_code', 0) != 20000:
        print(f"  Error {task.get('status_code')}: {task.get('status_message','')}")
        return {}
    return {r['keyword']: r.get('search_volume') or 0 for r in (task.get('result') or [])}

print("=== Phase 1: National volumes ===")
all_vols = {}
for i in range(0, len(NATIONAL_KEYWORDS), 10):
    batch = NATIONAL_KEYWORDS[i:i+10]
    print(f"  Batch {i//10+1}: {batch[0]}...")
    vols = check_keywords(batch)
    all_vols.update(vols)
    time.sleep(6)

print("\nNational volumes (sorted):")
for kw, v in sorted(all_vols.items(), key=lambda x: x[1] or 0, reverse=True):
    if v:
        print(f"  {v:7,}  {kw}")

# Phase 2: top 5 project types × top cities
top_projects = [kw for kw, v in sorted(all_vols.items(), key=lambda x: x[1] or 0, reverse=True)[:8] if v]
print(f"\n=== Phase 2: City spot-check for top projects ===")
print(f"Top projects: {top_projects[:5]}")

city_kws = []
for proj in top_projects[:5]:
    for city in SPOT_CITIES[:15]:
        city_kws.append(f"{proj} {city}")

city_vols = {}
for i in range(0, len(city_kws), 10):
    batch = city_kws[i:i+10]
    print(f"  Batch {i//10+1}/{(len(city_kws)+9)//10}: {batch[0]}...")
    vols = check_keywords(batch)
    city_vols.update(vols)
    time.sleep(6)

print("\nCity keyword volumes (top 40):")
top_city = sorted(city_vols.items(), key=lambda x: x[1] or 0, reverse=True)[:40]
for kw, v in top_city:
    if v:
        print(f"  {v:6,}  {kw}")

# Summary: which projects are worth building city pages for?
print("\n=== Summary by project type ===")
for proj in top_projects[:5]:
    proj_vols = [(kw, v) for kw, v in city_vols.items() if kw.startswith(proj)]
    total = sum(v or 0 for _, v in proj_vols)
    nonzero = sum(1 for _, v in proj_vols if v and v > 0)
    nat_vol = all_vols.get(proj, 0)
    print(f"\n  {proj}")
    print(f"    National: {nat_vol:,}/mo | City total: {total:,}/mo across {nonzero} cities")

with open("calculator_keywords.json", "w") as f:
    json.dump({"national": all_vols, "cities": city_vols}, f, indent=2)
print("\nSaved to calculator_keywords.json")
