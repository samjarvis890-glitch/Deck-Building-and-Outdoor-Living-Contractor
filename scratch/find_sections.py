from PIL import Image
import numpy as np
import os

p = os.path.abspath('scratch/gallery_tall_12000.png')
im = Image.open(p)
w, h = im.size
print(f"Loaded image {w}x{h}")

arr = np.array(im)

# Sample rows every 400px to see what sections are where
for y in range(0, h, 600):
    mid = arr[y, 720][:3]
    print(f"y={y:5d}: rgb=({mid[0]:3d}, {mid[1]:3d}, {mid[2]:3d})")
