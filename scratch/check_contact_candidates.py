import os
from PIL import Image

def get_fp(p):
    try:
        with Image.open(p) as im:
            return list(im.convert('RGB').resize((16, 16)).getdata())
    except:
        return None

# Load fingerprints of all currently used webp images across the whole site
used_fps = {}
for root, dirs, files in os.walk('assets/images'):
    for f in files:
        if f.endswith('.webp'):
            p = os.path.join(root, f)
            fp = get_fp(p)
            if fp:
                used_fps[p] = fp

print(f"Total used webp images in assets: {len(used_fps)}")

def check_candidate(candidate_path):
    fp = get_fp(candidate_path)
    if not fp:
        return None
    min_diff = 999
    closest = None
    for p, ufp in used_fps.items():
        diff = sum(abs(a[0]-b[0]) + abs(a[1]-b[1]) + abs(a[2]-b[2]) for a, b in zip(fp, ufp)) / len(fp)
        if diff < min_diff:
            min_diff = diff
            closest = p
    return min_diff, closest

# Check candidates in scratch
candidates = [
    'test_modern_villa_patio.jpg',
    'test_outdoor_terrace_view.jpg',
    'test_alfresco_patio_stone.jpg',
    'test_luxury_timber_house.jpg',
    'test_cedar_wood_grain.jpg',
    'test_timber_wood_decking.jpg',
    'test_timber_planks_texture.jpg',
    'test_deck_construction_wood.jpg',
    'test_backyard_lawn_pergola.jpg',
    'test_garden_walkway_deck.jpg',
    'test_outdoor_sofa_patio.jpg',
    'test_stone_paver_terrace.jpg',
    'test_terrace_dining_stone.jpg'
]

print("\n--- Checking candidate uniqueness (diff > 15 means unique) ---")
for c in candidates:
    p = os.path.join('scratch', c)
    if os.path.exists(p):
        res = check_candidate(p)
        if res:
            diff, closest = res
            status = "UNIQUE" if diff >= 15 else f"REPEAT of {closest}"
            with Image.open(p) as im:
                w, h = im.size
            print(f"{c} ({w}x{h}): diff={diff:.1f} -> {status}")
