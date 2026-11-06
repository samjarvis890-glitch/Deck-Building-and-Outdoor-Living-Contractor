import os
from PIL import Image

for f in sorted(os.listdir('scratch')):
    if (f.startswith('test_') or f.startswith('candidate_')) and f.lower().endswith(('.jpg', '.jpeg', '.webp', '.png')):
        p = os.path.join('scratch', f)
        if os.path.isfile(p):
            with Image.open(p) as im:
                print(f"{f}: {im.size[0]}x{im.size[1]} ({im.format})")
