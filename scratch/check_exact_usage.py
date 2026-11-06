import os
from PIL import Image

def get_fingerprint(path):
    try:
        with Image.open(path) as im:
            im = im.convert('RGB').resize((16, 16))
            return list(im.getdata())
    except:
        return None

brain_dir = r"C:\Users\Sam John\.gemini\antigravity\brain\aa3393d8-6479-4912-9a44-277395bd13ea"
targets = {
    'hero_deck': get_fingerprint(os.path.join(brain_dir, 'hero_deck_outdoor_living_1793850319432.jpg')),
    'indoor_outdoor': get_fingerprint(os.path.join(brain_dir, 'indoor_outdoor_flow_deck_1793850483924.jpg')),
    'serene_retreat': get_fingerprint(os.path.join(brain_dir, 'serene_deck_garden_retreat_1793850797959.jpg')),
}

for root, dirs, files in os.walk('assets/images'):
    for f in files:
        if f.endswith('.webp'):
            p = os.path.join(root, f)
            fp = get_fingerprint(p)
            if fp:
                for name, target_fp in targets.items():
                    if target_fp:
                        diff = sum(abs(a[0]-b[0]) + abs(a[1]-b[1]) + abs(a[2]-b[2]) for a, b in zip(fp, target_fp)) / len(fp)
                        if diff < 15: # very close match
                            print(f"Match found: {name} in {p} (diff: {diff:.1f})")
