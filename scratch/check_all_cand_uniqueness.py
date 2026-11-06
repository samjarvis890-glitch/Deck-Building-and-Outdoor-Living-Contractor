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

for f in sorted(os.listdir('scratch/candidates')):
    if f.endswith(('.jpg', '.jpeg', '.webp', '.png')):
        p = os.path.join('scratch/candidates', f)
        diff, closest = check(p)
        status = "100% UNIQUE" if diff >= 15 else f"REPEAT of {closest}"
        print(f"{f}: diff={diff:.1f} -> {status}")
