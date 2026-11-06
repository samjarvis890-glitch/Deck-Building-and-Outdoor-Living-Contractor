import os
import urllib.request
from io import BytesIO
from PIL import Image

# Curated candidates from Unsplash architectural photography
candidates = {
    # Outdoor dining / pergola
    "candidate_dining_pergola": "https://images.unsplash.com/photo-1540555700478-4be289fbecef?w=1200&q=80",
    # Modern patio with pool / pavilion
    "candidate_modern_patio": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=1200&q=80",
    # Covered outdoor room / pavilion
    "candidate_covered_room": "https://images.unsplash.com/photo-1600566753376-12c8ab7fb75b?w=1200&q=80",
    # Backyard sanctuary deck
    "candidate_deck_sanctuary": "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=1200&q=80",
    # Alfresco patio lounge
    "candidate_patio_lounge": "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=1200&q=80",
    # Outdoor firepit lounge
    "candidate_firepit_deck": "https://images.unsplash.com/photo-1527030280862-64139fba04ca?w=1200&q=80",
    # Modern pavilion architecture
    "candidate_pavilion": "https://images.unsplash.com/photo-1600585154526-990dced4db0d?w=1200&q=80",
    # Garden deck morning
    "candidate_garden_deck": "https://images.unsplash.com/photo-1584622650111-993a426fbf0a?w=1200&q=80",
    # Courtyard timber deck
    "candidate_courtyard": "https://images.unsplash.com/photo-1558036117-15d82a90b9b1?w=1200&q=80",
    # Stone and timber terrace
    "candidate_stone_timber": "https://images.unsplash.com/photo-1600573472550-8090b5e0745e?w=1200&q=80",
    # Wood planks texture macro
    "candidate_wood_planks": "https://images.unsplash.com/photo-1546484396-fb3fc6f95f98?w=1200&q=80",
    # Rich wood grain texture
    "candidate_grain_texture": "https://images.unsplash.com/photo-1533090161767-e6ffed986c88?w=1200&q=80",
    # Natural stone wall / terrace
    "candidate_stone_wall": "https://images.unsplash.com/photo-1598928506311-c55ded91a20c?w=1200&q=80",
    # Lush green patio
    "candidate_lush_patio": "https://images.unsplash.com/photo-1590490360182-c33d57733427?w=1200&q=80",
    # Balcony timber deck
    "candidate_balcony_deck": "https://images.unsplash.com/photo-1540518614846-7ede433c4550?w=1200&q=80",
    # Sunken seating deck
    "candidate_sunken_deck": "https://images.unsplash.com/photo-1576013551627-0cc20b96c2a7?w=1200&q=80",
    # Weathered timber wood texture (for renovation existing condition)
    "candidate_weathered_wood": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=1200&q=80",
    # Fresh oiled cedar wood (for renovation refresh condition)
    "candidate_oiled_cedar": "https://images.unsplash.com/photo-1541123437800-1bb1317badc2?w=1200&q=80"
}

os.makedirs('scratch/candidates', exist_ok=True)
cards = []

for name, url in candidates.items():
    out_file = f'scratch/candidates/{name}.jpg'
    if not os.path.exists(out_file):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = resp.read()
            im = Image.open(BytesIO(data))
            if im.mode != 'RGB':
                im = im.convert('RGB')
            im.thumbnail((600, 400))
            im.save(out_file, 'JPEG', quality=85)
            print(f"Downloaded {name}")
        except Exception as e:
            print(f"Failed {name}: {e}")
            continue

    cards.append(f"""
    <div style="background:#222; padding:8px; border-radius:6px; border:1px solid #444;">
        <img src="../scratch/candidates/{name}.jpg" style="width:100%; height:150px; object-fit:cover; border-radius:4px; display:block; margin-bottom:4px;">
        <div style="font-weight:bold; font-size:11px; color:#ddd; word-break:break-all;">{name}</div>
    </div>
    """)

html = f"""<!DOCTYPE html><html><head><style>body {{ font-family:sans-serif; background:#111; color:#fff; padding:15px; }} .grid {{ display:grid; grid-template-columns:repeat(auto-fill, minmax(200px, 1fr)); gap:10px; }}</style></head>
<body><h2>Candidates Preview</h2><div class="grid">{''.join(cards)}</div></body></html>"""

with open('scratch/candidates_preview.html', 'w', encoding='utf-8') as f:
    f.write(html)

import subprocess
chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
html_abs = os.path.abspath('scratch/candidates_preview.html').replace('\\', '/')
out_png = os.path.abspath('scratch/candidates_preview.png')
cmd = [chrome, '--headless=new', '--disable-gpu', '--window-size=1400,1800', f'--screenshot={out_png}', f'file:///{html_abs}']
subprocess.run(cmd, check=True)
print("Candidates preview screenshot created:", os.path.exists(out_png))
