import os
import re

html_files = [f for f in sorted(os.listdir('.')) if f.endswith('.html')]

page_imgs = {}
for h in html_files:
    with open(h, 'r', encoding='utf-8') as f:
        c = f.read()
    imgs = set(re.findall(r'assets/images/[a-zA-Z0-9_\-\./]+', c))
    page_imgs[h] = [img for img in imgs if not img.startswith('assets/images/brand/')]

print("--- SITE-WIDE CONTENT IMAGE REPEAT CHECK ---")
all_found = {}
for h, imgs in page_imgs.items():
    for img in imgs:
        if img not in all_found:
            all_found[img] = []
        all_found[img].append(h)

cross_page_duplicates = {k: v for k, v in all_found.items() if len(set(v)) > 1 and not ('home-2.html' in v and 'home2.html' in v and len(set(v)) == 2)}

if not cross_page_duplicates:
    print("PERFECT: ZERO duplicate content image paths across different site pages!")
else:
    print(f"Found {len(cross_page_duplicates)} repeated paths across different pages:")
    for k, v in cross_page_duplicates.items():
        print(f"  {k} -> {set(v)}")
