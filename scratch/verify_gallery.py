import os
import re

html_path = 'gallery.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Check all images in gallery.html exist
img_srcs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html)
print(f'Total img elements in gallery.html: {len(img_srcs)}')
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

# 2. Check all 31 gallery image filenames are referenced
gallery_imgs = [
    'gallery-hero.webp',
    'gallery-collection-deck.webp',
    'gallery-collection-pergola.webp',
    'gallery-collection-covered.webp',
    'gallery-collection-patio.webp',
    'gallery-collection-detail.webp',
    'gallery-collection-landscape.webp',
    'gallery-deck-contemporary.webp',
    'gallery-deck-natural.webp',
    'gallery-deck-levels.webp',
    'gallery-deck-garden.webp',
    'gallery-pergola-timber.webp',
    'gallery-pergola-modern.webp',
    'gallery-pergola-garden.webp',
    'gallery-covered-dining.webp',
    'gallery-covered-lounge.webp',
    'gallery-covered-architecture.webp',
    'gallery-patio-dining.webp',
    'gallery-patio-gathering.webp',
    'gallery-patio-relax.webp',
    'gallery-patio-entertainment.webp',
    'gallery-detail-timber.webp',
    'gallery-detail-decking.webp',
    'gallery-detail-structure.webp',
    'gallery-detail-stone.webp',
    'gallery-detail-lighting.webp',
    'gallery-moodboard-natural.webp',
    'gallery-moodboard-contemporary.webp',
    'gallery-moodboard-entertaining.webp',
    'gallery-moodboard-garden.webp',
    'gallery-final-cta.webp'
]

all_found = True
for f in gallery_imgs:
    if f not in html:
        print(f'Warning: {f} not in gallery.html')
        all_found = False
if all_found:
    print(f'All {len(gallery_imgs)} gallery images are properly referenced in gallery.html!')

# 3. Check section anchors
anchors = [
    'gallery-collection',
    'deck-inspiration',
    'pergola-architecture',
    'covered-environments',
    'patio-inspiration',
    'details-materials',
    'design-moodboard',
    'gallery-final-cta'
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
