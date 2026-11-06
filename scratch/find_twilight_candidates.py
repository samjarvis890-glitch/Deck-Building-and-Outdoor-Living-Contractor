import os
from PIL import Image

# Let's inspect all candidates and scratch files
files_to_check = []
for d in ['scratch', 'scratch/candidates']:
    for f in os.listdir(d):
        if f.lower().endswith(('.jpg', '.jpeg', '.webp', '.png')):
            p = os.path.join(d, f)
            if not f.startswith('verify_') and not f.startswith('audit_') and not f.startswith('temp_'):
                files_to_check.append(p)

print(f"Total potential files: {len(files_to_check)}")
for p in files_to_check:
    if any(k in p.lower() for k in ['twilight', 'fire', 'night', 'evening', 'bistro', 'pavilion', 'outdoor', 'terrace', 'patio', 'lawn', 'wood', 'deck', 'sunken']):
        try:
            with Image.open(p) as im:
                print(f"{p}: {im.size[0]}x{im.size[1]}")
        except:
            pass
