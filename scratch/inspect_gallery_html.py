import re

with open('gallery.html', 'r', encoding='utf-8') as f:
    text = f.read()

imgs = re.findall(r'src="(assets/images/gallery/[^"]+)"', text)
print(f"Total gallery image tags: {len(imgs)}")
unique = sorted(set(imgs))
print(f"Unique image files ({len(unique)}):")
for u in unique:
    print(" ", u)
