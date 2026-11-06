import os
from PIL import Image

dirs_to_check = ['scratch', 'scratch/candidates', 'brain', 'assets/images/projects', 'assets/images/services', 'assets/images/gallery']
for d in ['scratch', 'scratch/candidates']:
    if os.path.exists(d):
        print(f"\n--- Directory: {d} ---")
        for f in os.listdir(d):
            if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
                p = os.path.join(d, f)
                try:
                    with Image.open(p) as im:
                        print(f"{f}: {im.size[0]}x{im.size[1]} ({im.format})")
                except Exception as e:
                    pass
