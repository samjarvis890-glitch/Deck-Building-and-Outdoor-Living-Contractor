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

pool = [
    'scratch/test_deck_pool_twilight.jpg',
    'scratch/test_outdoor_bistro_lights.jpg',
    'scratch/candidates/candidate_firepit_deck.jpg',
    'scratch/candidates/candidate_sunken_deck.jpg',
    'scratch/test_modern_villa_patio.jpg',
    'scratch/test_outdoor_terrace_view.jpg',
    'scratch/test_backyard_lawn_pergola.jpg',
    'scratch/test_deck_construction_wood.jpg',
    'scratch/test_timber_wood_decking.jpg'
]

for p in pool:
    if os.path.exists(p):
        diff, closest = check_candidate(p)
        status = "100% UNIQUE" if diff >= 15 else f"REPEAT of {closest}"
        print(f"{p}: diff={diff:.1f} -> {status}")
