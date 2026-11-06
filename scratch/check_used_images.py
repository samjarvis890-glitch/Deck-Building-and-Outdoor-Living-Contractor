import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]
all_used_images = {}

for h in sorted(html_files):
    with open(h, 'r', encoding='utf-8') as f:
        content = f.read()
    imgs = re.findall(r'assets/images/[a-zA-Z0-9_\-\./]+', content)
    for img in imgs:
        # normalize
        img_clean = img.split('"')[0].split("'")[0].split(')')[0]
        if img_clean not in all_used_images:
            all_used_images[img_clean] = []
        all_used_images[img_clean].append(h)

print(f"Total unique image paths referenced in HTML: {len(all_used_images)}")
print("\nImages used in multiple HTML files:")
duplicates = {k: v for k, v in all_used_images.items() if len(v) > 1 and not k.startswith('assets/images/brand/')}
for k, v in duplicates.items():
    print(f"  {k} -> {v}")

print("\nImages in assets/images/faq/ currently:")
for f in os.listdir('assets/images/faq'):
    p = f"assets/images/faq/{f}"
    print(f"  {p} -> used in: {all_used_images.get(p, ['NONE'])}")
