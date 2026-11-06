import os
import re

html_path = 'services.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Check all images in services.html exist
img_srcs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html)
print(f'Total img elements: {len(img_srcs)}')
missing_imgs = []
for src in img_srcs:
    clean_src = src.split('?')[0].split('#')[0]
    if not os.path.exists(clean_src):
        missing_imgs.append(clean_src)

if missing_imgs:
    print('MISSING IMAGES:', missing_imgs)
else:
    print('All img sources exist locally!')

# 2. Check all 18 service image filenames are referenced
services_imgs = [
    'services-hero.webp',
    'service-overview-deck.webp',
    'service-overview-pergola.webp',
    'service-overview-covered.webp',
    'service-overview-patio.webp',
    'service-overview-renovation.webp',
    'service-deck-construction.webp',
    'service-deck-detail.webp',
    'service-pergola-construction.webp',
    'service-covered-outdoor.webp',
    'service-patio-design.webp',
    'service-entertainment-area.webp',
    'service-outdoor-dining.webp',
    'service-renovation-existing.webp',
    'service-renovation-refresh.webp',
    'service-choose-space.webp',
    'services-final-cta.webp',
    'service-material-detail.webp'
]
all_found = True
for f in services_imgs:
    if f not in html:
        print(f'Warning: {f} not in services.html')
        all_found = False
if all_found:
    print('All 18 service images are properly referenced in services.html!')

# 3. Check section anchors
anchors = [
    'service-overview',
    'custom-deck-construction',
    'pergola-construction',
    'covered-outdoor-living',
    'patio-entertainment-spaces',
    'deck-renovation',
    'choose-your-direction',
    'service-enquiry-cta'
]
for a in anchors:
    if f'id="{a}"' in html or f'id=\'{a}\'' in html:
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
