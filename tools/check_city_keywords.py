#!/usr/bin/env python3
"""Check keyword volumes for city x project combinations via DataForSEO."""
import requests
import json
import time
from base64 import b64encode

LOGIN = "hello@britetodo.com"
PASSWORD = "17b4ff94bd5891ec"
AUTH = b64encode(f"{LOGIN}:{PASSWORD}".encode()).decode()

PROJECTS = [
    "bathroom remodel cost",
    "kitchen remodel cost",
    "roof replacement cost",
    "flooring installation cost",
    "concrete driveway cost",
]

CITIES = [
    "New York", "Los Angeles", "Chicago", "Houston", "Phoenix",
    "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose",
    "Austin", "Jacksonville", "Fort Worth", "Columbus", "Charlotte",
    "Indianapolis", "San Francisco", "Seattle", "Denver", "Nashville",
    "Oklahoma City", "El Paso", "Washington DC", "Las Vegas", "Boston",
    "Portland", "Memphis", "Louisville", "Baltimore", "Milwaukee",
    "Albuquerque", "Tucson", "Fresno", "Sacramento", "Mesa",
    "Atlanta", "Omaha", "Colorado Springs", "Raleigh", "Miami",
    "Minneapolis", "Tampa", "New Orleans", "Cleveland", "Bakersfield",
    "Honolulu", "Anaheim", "Riverside", "Corpus Christi", "Cincinnati",
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
    status_code = task.get('status_code', 0)
    if status_code != 20000:
        print(f"  API error {status_code}: {task.get('status_message', '')}")
        return {}
    results = task.get('result') or []
    return {r['keyword']: r.get('search_volume') or 0 for r in results}

# Build keyword list (batches of 10)
all_keywords = [f"{proj} {city}" for proj in PROJECTS for city in CITIES]
print(f"Total keywords to check: {len(all_keywords)}")

volumes = {}
batch_size = 10
RATE_LIMIT_DELAY = 6  # seconds between batches (max 12/min = 1 per 5s, use 6 to be safe)
for i in range(0, len(all_keywords), batch_size):
    batch = all_keywords[i:i+batch_size]
    print(f"Batch {i//batch_size + 1}/{(len(all_keywords) + batch_size - 1)//batch_size}: {batch[0]} ...")
    result = check_keywords(batch)
    volumes.update(result)
    time.sleep(RATE_LIMIT_DELAY)

# Print sorted results
print("\n=== RESULTS (sorted by volume) ===")
sorted_kws = sorted(volumes.items(), key=lambda x: x[1] or 0, reverse=True)
for kw, vol in sorted_kws:
    if vol and vol > 0:
        print(f"  {vol:6d}  {kw}")

# Summary by project
print("\n=== BY PROJECT ===")
for proj in PROJECTS:
    proj_vols = [(kw, v) for kw, v in volumes.items() if kw.startswith(proj) and v]
    total = sum(v or 0 for _, v in proj_vols)
    nonzero = [(kw, v) for kw, v in proj_vols if v > 0]
    print(f"\n{proj}:")
    print(f"  Total volume across {len(nonzero)} cities: {total:,}")
    top5 = sorted(proj_vols, key=lambda x: x[1], reverse=True)[:5]
    for kw, v in top5:
        city = kw.replace(proj + " ", "")
        print(f"    {v:5d}  {city}")

# Save raw results
with open("city_keywords_results.json", "w") as f:
    json.dump(volumes, f, indent=2)
print("\nSaved to city_keywords_results.json")
