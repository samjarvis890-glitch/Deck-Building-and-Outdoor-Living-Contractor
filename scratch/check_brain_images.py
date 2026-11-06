import os
from PIL import Image

brain_dir = r"C:\Users\Sam John\.gemini\antigravity\brain\aa3393d8-6479-4912-9a44-277395bd13ea"

images = []
for f in os.listdir(brain_dir):
    if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
        p = os.path.join(brain_dir, f)
        try:
            with Image.open(p) as im:
                images.append((f, im.size[0], im.size[1]))
        except:
            pass

print(f"Total images in brain: {len(images)}")
for f, w, h in images:
    print(f"  {f} ({w}x{h})")
