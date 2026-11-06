import os
import re

html_path = 'projects.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Check all images in projects.html exist
img_srcs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html)
print(f'Total img elements in projects.html: {len(img_srcs)}')
missing_imgs = []
for src in img_srcs:
    if not src: continue
    clean_src = src.split('?')[0].split('#')[0]
    if not os.path.exists(clean_src):
        missing_imgs.append(clean_src)

if missing_imgs:
    print('MISSING IMAGES:', missing_imgs)
else:
    print('All img sources exist locally on disk!')

# 2. Check all 16 projects image filenames are referenced
projects_imgs = [
    'projects-hero.webp',
    'project-concept-timber-deck.webp',
    'project-concept-garden-pergola.webp',
    'project-concept-covered-lounge.webp',
    'project-concept-dining-courtyard.webp',
    'project-spotlight-deck.webp',
    'project-spotlight-pergola.webp',
    'project-design-planning.webp',
    'project-detail-timber.webp',
    'project-detail-structure.webp',
    'project-detail-stone.webp',
    'project-detail-lighting.webp',
    'project-direction-relax.webp',
    'project-direction-entertain.webp',
    'project-direction-extension.webp',
    'projects-final-cta.webp'
]

all_found = True
for f in projects_imgs:
    if f not in html:
        print(f'Warning: {f} not in projects.html')
        all_found = False
if all_found:
    print(f'All {len(projects_imgs)} project images are properly referenced in projects.html!')

# 3. Check section anchors
anchors = [
    'project-concepts',
    'spotlight-deck',
    'spotlight-pergola',
    'design-thinking',
    'detail-study',
    'project-direction',
    'projects-final-cta'
]
for a in anchors:
    if f'id="{a}"' in html:
        print(f'Section anchor found: #{a}')
    else:
        print(f'MISSING ANCHOR: #{a}')

# 4. Check H1 count
h1s = re.findall(r'<h1[^>]*>(.*?)</h1>', html, re.DOTALL)
print(f'H1 count: {len(h1s)}')
for h in h1s:
    print('  H1:', h.strip())

# 5. Check remote image URLs
remote = re.findall(r'https?://[^\s"\']+\.(?:png|jpg|jpeg|webp|gif|svg)', html)
print('Remote images found:', remote)
