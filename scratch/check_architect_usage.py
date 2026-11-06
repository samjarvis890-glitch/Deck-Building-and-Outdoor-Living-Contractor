import os
from PIL import Image

def get_fp(p):
    with Image.open(p) as im:
        return list(im.convert('RGB').resize((16, 16)).getdata())

target_fp = get_fp('scratch/test_architect_drawing_deck.jpg')

for root, dirs, files in os.walk('assets/images'):
    for f in files:
        if f.endswith('.webp'):
            p = os.path.join(root, f)
            fp = get_fp(p)
            diff = sum(abs(a[0]-b[0]) + abs(a[1]-b[1]) + abs(a[2]-b[2]) for a, b in zip(fp, target_fp)) / len(fp)
            if diff < 20:
                print(f"architect drawing matches {p} (diff: {diff:.1f})")
