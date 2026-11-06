import os
from PIL import Image

def get_fp(p):
    with Image.open(p) as im:
        return list(im.convert('RGB').resize((16, 16)).getdata())

brain_dir = r"C:\Users\Sam John\.gemini\antigravity\brain\aa3393d8-6479-4912-9a44-277395bd13ea"

targets = {
    'indoor_outdoor': get_fp(os.path.join(brain_dir, 'indoor_outdoor_flow_deck_1793850483924.jpg')),
    'serene_retreat': get_fp(os.path.join(brain_dir, 'serene_deck_garden_retreat_1793850797959.jpg'))
}

for root, dirs, files in os.walk('assets/images'):
    for f in files:
        if f.endswith('.webp'):
            p = os.path.join(root, f)
            fp = get_fp(p)
            for name, tfp in targets.items():
                diff = sum(abs(a[0]-b[0]) + abs(a[1]-b[1]) + abs(a[2]-b[2]) for a, b in zip(fp, tfp)) / len(fp)
                if diff < 20:
                    print(f"{name} matches {p} (diff: {diff:.1f})")
