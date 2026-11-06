import subprocess
import os
from PIL import Image

chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
html_path = os.path.abspath('gallery.html').replace('\\', '/')

# 1. LIGHT MODE
tall_light = os.path.abspath('scratch/gallery_tall_full_light.png')
subprocess.run([
    chrome, '--headless=new', '--disable-gpu',
    '--window-size=1440,10200',
    f'--screenshot={tall_light}',
    f'file:///{html_path}'
], timeout=25)

# 2. DARK MODE
with open('gallery.html', 'r', encoding='utf-8') as f:
    dark_html = f.read().replace('data-theme="light"', 'data-theme="dark"')
with open('temp_dark_full.html', 'w', encoding='utf-8') as f:
    f.write(dark_html)

tall_dark = os.path.abspath('scratch/gallery_tall_full_dark.png')
subprocess.run([
    chrome, '--headless=new', '--disable-gpu',
    '--window-size=1440,10200',
    f'--screenshot={tall_dark}',
    f'file:///{os.path.abspath("temp_dark_full.html").replace(chr(92), "/")}'
], timeout=25)

if os.path.exists('temp_dark_full.html'):
    os.remove('temp_dark_full.html')

im_l = Image.open(tall_light)
im_d = Image.open(tall_dark)

# Crop CTA (top: 8852, bottom: 9485) -> crop 8800 to 9550
cta_light = im_l.crop((0, 8800, 1440, 9550))
cta_light.save('scratch/gallery_final_cta_light_exact.png')

cta_dark = im_d.crop((0, 8800, 1440, 9550))
cta_dark.save('scratch/gallery_final_cta_dark_exact.png')

print("Cropped CTA in Light and Dark mode successfully!")
