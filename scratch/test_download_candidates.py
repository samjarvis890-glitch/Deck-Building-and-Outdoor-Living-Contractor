import urllib.request
import os
from PIL import Image
from io import BytesIO

# Test candidate real outdoor living / architecture photo IDs on Unsplash
candidate_ids = [
    # Modern Decks & Patios
    ("deck_pool_twilight", "photo-1512917774080-9991f1c4c750"),
    ("modern_villa_patio", "photo-1600585154340-be6161a56a0c"),
    ("luxury_timber_house", "photo-1600596542815-ffad4c1539a9"),
    ("outdoor_terrace_view", "photo-1600607687939-ce8a6c25118c"),
    ("garden_deck_pergola", "photo-1591825729269-caeb344f6df2"),
    ("contemporary_patio", "photo-1600566753376-12c8ab7fb75b"),
    ("timber_wood_decking", "photo-1540555700478-4be289fbecef"),
    ("stone_paver_terrace", "photo-1600573472550-8090b5e0745e"),
    ("deck_construction_wood", "photo-1504148455328-c376907d081c"), # woodworking tools
    ("timber_planks_texture", "photo-1533090161767-e6ffed986c88"), # timber grain
    ("architect_drawing_deck", "photo-1503387762-592deb58ef4e"), # architect blueprint
    ("cedar_wood_grain", "photo-1546484396-fb3fc6f95f98"), # wood texture
    ("outdoor_bistro_lights", "photo-1527030280862-64139fba04ca"),
    ("terrace_dining_stone", "photo-1576013551627-0cc20b96c2a7"),
    ("modern_house_deck", "photo-1558036117-15d82a90b9b1"),
    ("garden_walkway_deck", "photo-1507089947368-19c1da9775ae"),
    ("backyard_lawn_pergola", "photo-1519710164239-da123dc03ef4"),
    ("outdoor_sofa_patio", "photo-1560448204-e02f11c3d0e2"),
    ("alfresco_patio_stone", "photo-1590490360182-c33d57733427")
]

results = []
for label, pid in candidate_ids:
    url = f"https://images.unsplash.com/photo-{pid.split('photo-')[-1]}?w=800&q=80"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=8) as r:
            data = r.read()
        im = Image.open(BytesIO(data))
        results.append((label, pid, im.size, len(data)))
        im.save(f"scratch/test_{label}.jpg")
    except Exception as e:
        results.append((label, pid, str(e), 0))

for r in results:
    print(r)
