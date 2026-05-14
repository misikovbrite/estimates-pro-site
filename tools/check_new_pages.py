#!/usr/bin/env python3
"""Check DataForSEO volumes for potential new page types."""
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
    # ── State-level cost pages ──
    ["bathroom remodel cost California", "kitchen remodel cost Texas",
     "roof replacement cost Florida", "bathroom remodel cost New York",
     "bathroom remodel cost Texas", "kitchen remodel cost California",
     "roof replacement cost California", "kitchen remodel cost Florida",
     "bathroom remodel cost Florida", "roof replacement cost Texas"],

    # ── New project types (national) ──
    ["home addition cost", "home addition cost calculator",
     "deck cost calculator", "deck installation cost",
     "hvac replacement cost", "hvac installation cost calculator",
     "landscaping cost calculator", "landscaping cost",
     "pool installation cost", "pool cost calculator"],

    # ── New project types (city level) ──
    ["home addition cost Los Angeles", "deck installation cost calculator",
     "hvac replacement cost calculator", "landscaping cost per square foot",
     "home addition calculator", "room addition cost calculator",
     "patio installation cost calculator", "pergola cost calculator",
     "fence cost calculator", "concrete patio cost calculator"],

    # ── How-to guides ──
    ["how to write a construction estimate", "how to estimate a roofing job",
     "how to bid a construction job", "construction estimate example",
     "how to price a contracting job", "how to start a contracting business",
     "how to estimate plumbing job", "how to estimate painting job",
     "contractor invoice template", "construction bid template"],

    # ── Software / comparison ──
    ["construction estimating software", "best construction estimating software",
     "free construction estimating software", "jobber alternative",
     "buildertrend alternative", "contractor estimate software",
     "construction takeoff software", "estimating software for contractors",
     "procore alternative", "houzz pro alternative"],
]

all_vols = {}
for i, batch in enumerate(batches):
    print(f"Batch {i+1}/{len(batches)}: {batch[0]}...")
    vols = check(batch)
    all_vols.update(vols)
    if i < len(batches) - 1:
        time.sleep(6)

print("\n=== ALL RESULTS (sorted by volume) ===")
for kw, v in sorted(all_vols.items(), key=lambda x: x[1] or 0, reverse=True):
    if v >= 200:
        print(f"  {v:8,}  {kw}")

cats = {
    "State pages": ["California", "Texas", "Florida", "New York"],
    "New project types": ["home addition", "deck", "hvac", "landscaping", "pool", "patio", "pergola", "concrete", "room addition"],
    "How-to guides": ["how to", "how much", "example", "template", "bid"],
    "Software/comparison": ["software", "alternative", "procore", "houzz", "jobber", "buildertrend", "takeoff"],
}

print("\n=== BY CATEGORY ===")
for cat, kws in cats.items():
    items = [(k, v) for k, v in all_vols.items()
             if any(w.lower() in k.lower() for w in kws) and (v or 0) > 0]
    total = sum(v or 0 for _, v in items)
    top5 = sorted(items, key=lambda x: x[1] or 0, reverse=True)[:5]
    print(f"\n{cat}: {total:,}/mo total")
    for k, v in top5:
        print(f"  {v:7,}  {k}")

with open("new_pages_v2.json", "w") as f:
    json.dump(all_vols, f, indent=2)
print("\nSaved → new_pages_v2.json")
