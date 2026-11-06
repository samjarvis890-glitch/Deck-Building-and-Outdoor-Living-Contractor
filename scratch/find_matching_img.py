import os
from PIL import Image

# Let's find all images and check if one matches the bright image in screenshot 4
target_files = []
for root, dirs, files in os.walk('assets/images'):
    for f in files:
        if f.lower().endswith(('.webp', '.jpg', '.jpeg', '.png')):
            target_files.append(os.path.join(root, f))

print(f"Total images found: {len(target_files)}")
