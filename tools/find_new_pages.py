#!/usr/bin/env python3
"""Find next page opportunities via DataForSEO."""
import requests, time, json
from base64 import b64encode

AUTH = b64encode(b"hello@britetodo.com:17b4ff94bd5891ec").decode()

def check(keywords):
    resp = requests.post(
        "https://api.dataforseo.com/v3/keywords_data/google_ads/search_volume/live",
        headers={"Authorization": f"Basic {AUTH}", "Content-Type": "application/json"},
        json=[{"keywords": keywords, "location_code": 2840, "language_code": "en"}],
        timeout=30
    )
    task = resp.json().get("tasks", [{}])[0]
    if task.get("status_code") != 20000:
        print(f"  err {task.get('status_code')}: {task.get('status_message','')}")
        return {}
    return {r["keyword"]: r.get("search_volume") or 0 for r in (task.get("result") or [])}

batches = [
    # ── Estimate / invoice templates (contractors need these) ──
    ["free estimate template", "construction estimate template", "roofing estimate template",
     "contractor estimate template", "plumbing estimate template", "electrical estimate template",
     "painting estimate template", "hvac estimate template", "free invoice template contractor",
     "construction invoice template"],

    # ── Estimating software / app comparison ──
    ["construction estimating software", "best construction estimating software",
     "free construction estimating software", "construction estimating app",
     "roofing estimating software", "electrical estimating software",
     "plumbing estimating software", "contractor bidding software",
     "jobber alternative", "buildertrend alternative"],

    # ── How to estimate (guides) ──
    ["how to estimate a roofing job", "how to write a construction estimate",
     "how to estimate painting job", "how to estimate drywall job",
     "how to estimate plumbing job", "how to estimate electrical job",
     "how to bid a construction job", "construction estimate example",
     "roofing estimate example", "how to price a contracting job"],

    # ── State-level cost pages ──
    ["bathroom remodel cost California", "kitchen remodel cost Texas",
     "roof replacement cost Florida", "bathroom remodel cost New York state",
     "bathroom remodel cost Texas", "kitchen remodel cost California",
     "roof replacement cost California", "bathroom remodel cost Florida",
     "kitchen remodel cost Florida", "roof replacement cost Texas"],

    # ── Trade-specific calculator / app ──
    ["electrician estimate calculator", "plumbing cost calculator",
     "hvac installation cost calculator", "painting cost calculator",
     "roofing cost calculator", "landscaping cost calculator",
     "deck cost calculator", "basement finishing cost calculator",
     "home addition cost calculator", "pool cost calculator"],

    # ── Cost guides (informational high volume) ──
    ["how much does it cost to remodel a bathroom", "how much does a kitchen remodel cost",
     "how much does a new roof cost", "how much does drywall cost",
     "how much does it cost to replace windows", "how much does interior painting cost",
     "how much does a fence cost", "how much does siding cost",
     "average cost to remodel a bathroom", "average kitchen remodel cost"],
]

all_vols = {}
for i, batch in enumerate(batches):
    print(f"Batch {i+1}/{len(batches)}: {batch[0]}...")
    vols = check(batch)
    all_vols.update(vols)
    time.sleep(6)

print("\n=== ALL RESULTS (sorted) ===")
for kw, v in sorted(all_vols.items(), key=lambda x: x[1], reverse=True):
    if v >= 500:
        print(f"  {v:8,}  {kw}")

# Group by category
cats = {
    "Templates": ["template"],
    "Software/App": ["software", "app", "alternative", "bidding"],
    "How-to guides": ["how to", "how much", "average cost", "example"],
    "State pages": ["California", "Texas", "Florida", "New York"],
    "Trade calculators": ["calculator", "electrician", "plumbing", "hvac", "roofing", "landscaping", "deck", "pool"],
}
print("\n=== BY CATEGORY ===")
for cat, kws in cats.items():
    items = [(k, v) for k, v in all_vols.items() if any(w.lower() in k.lower() for w in kws) and v]
    total = sum(v for _, v in items)
    top3 = sorted(items, key=lambda x: x[1], reverse=True)[:3]
    print(f"\n{cat}: {total:,}/mo total")
    for k, v in top3:
        print(f"  {v:7,}  {k}")

with open("new_pages_keywords.json", "w") as f:
    json.dump(all_vols, f, indent=2)
print("\nSaved to new_pages_keywords.json")
