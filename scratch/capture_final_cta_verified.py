import subprocess
import os
from PIL import Image

chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
html_path = os.path.abspath('gallery.html').replace('\\', '/')

# Let's take full height screenshot with standard 1440 width and window size 1440,6500 (since hero was clamped, total height is around 5500-6000)
# Light Mode
tall_light = os.path.abspath('scratch/gallery_tall_v2_light.png')
subprocess.run([
    chrome, '--headless=new', '--disable-gpu',
    '--window-size=1440,7500',
    f'--screenshot={tall_light}',
    f'file:///{html_path}'
], timeout=25)

# Dark Mode
with open('gallery.html', 'r', encoding='utf-8') as f:
    dark_html = f.read().replace('data-theme="light"', 'data-theme="dark"')
with open('temp_gallery_dark_v2.html', 'w', encoding='utf-8') as f:
    f.write(dark_html)

tall_dark = os.path.abspath('scratch/gallery_tall_v2_dark.png')
subprocess.run([
    chrome, '--headless=new', '--disable-gpu',
    '--window-size=1440,7500',
    f'--screenshot={tall_dark}',
    f'file:///{os.path.abspath("temp_gallery_dark_v2.html").replace(chr(92), "/")}'
], timeout=25)

if os.path.exists('temp_gallery_dark_v2.html'):
    os.remove('temp_gallery_dark_v2.html')

im_l = Image.open(tall_light)
im_d = Image.open(tall_dark)
print("Light height:", im_l.size, "Dark height:", im_d.size)

# Find bottom where CTA is
# CTA is above the footer (footer is approx 450px)
h = im_l.size[1]
cta_crop_l = im_l.crop((0, h - 1300, 1440, h - 450))
cta_crop_l.save('scratch/gallery_final_cta_light_verified.png')

cta_crop_d = im_d.crop((0, h - 1300, 1440, h - 450))
cta_crop_d.save('scratch/gallery_final_cta_dark_verified.png')

print("Saved verified CTA crops!")
