import os
from PIL import Image

def get_fp(p):
    try:
        with Image.open(p) as im:
            return list(im.convert('RGB').resize((16, 16)).getdata())
    except:
        return None

used_fps = {}
for root, dirs, files in os.walk('assets/images'):
    for f in files:
        if f.endswith('.webp'):
            p = os.path.join(root, f)
            fp = get_fp(p)
            if fp:
                used_fps[p] = fp

def check(p):
    fp = get_fp(p)
    min_diff = 999
    closest = None
    for k, v in used_fps.items():
        diff = sum(abs(a[0]-b[0]) + abs(a[1]-b[1]) + abs(a[2]-b[2]) for a, b in zip(fp, v)) / len(fp)
        if diff < min_diff:
            min_diff = diff
            closest = k
    return min_diff, closest

brain_dir = r"C:\Users\Sam John\.gemini\antigravity\brain\aa3393d8-6479-4912-9a44-277395bd13ea"

targets = [
    os.path.join(brain_dir, "bespoke_deck_outdoor_living_1793873045878.jpg"),
    os.path.join(brain_dir, "serene_deck_garden_retreat_1793850797959.jpg"),
    "scratch/test_modern_villa_patio.jpg",
    "scratch/test_contemporary_patio.jpg",
    "scratch/test_modern_house_deck.jpg",
    "scratch/test_outdoor_bistro_lights.jpg",
    "scratch/test_terrace_dining_stone.jpg"
]

for t in targets:
    diff, closest = check(t)
    status = "100% UNIQUE" if diff >= 15 else f"REPEAT of {closest}"
    print(f"{os.path.basename(t)}: diff={diff:.1f} -> {status}")
