import os
from PIL import Image

found = []
for root, dirs, files in os.walk('.'):
    if 'node_modules' in root or '.git' in root or 'scratch' in root:
        continue
    for f in files:
        if f.lower().endswith(('.webp', '.jpg', '.png')) and not f.startswith('.'):
            p = os.path.join(root, f)
            try:
                im = Image.open(p)
                found.append((p, im.size, im.mode, os.path.getsize(p)/1024))
            except:
                pass

# Also check brain
brain_dir = r"C:\Users\Sam John\.gemini\antigravity\brain\aa3393d8-6479-4912-9a44-277395bd13ea"
if os.path.exists(brain_dir):
    for f in os.listdir(brain_dir):
        if f.lower().endswith(('.webp', '.jpg', '.png')) and not f.startswith('.'):
            p = os.path.join(brain_dir, f)
            try:
                im = Image.open(p)
                found.append((p, im.size, im.mode, os.path.getsize(p)/1024))
            except:
                pass

print(f"Total images found: {len(found)}")
for p, sz, mode, kb in sorted(found):
    print(f"{p:<65} | {sz[0]}x{sz[1]} | {kb:.1f}KB")
