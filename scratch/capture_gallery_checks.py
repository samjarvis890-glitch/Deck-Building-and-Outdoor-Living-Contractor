import subprocess
import os
from PIL import Image

chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

# 1. LIGHT MODE
with open('gallery.html', 'r', encoding='utf-8') as f:
    c = f.read()

c_light = c.replace('<head>', '<head><script>localStorage.setItem("eol_theme_preference", "light");</script>')
with open('temp_gallery_light.html', 'w', encoding='utf-8') as f:
    f.write(c_light)

out_tall_light = os.path.abspath('scratch/gallery_tall_light.png')
html_light = os.path.abspath('temp_gallery_light.html').replace('\\', '/')

subprocess.run([
    chrome,
    '--headless=new',
    '--disable-gpu',
    '--window-size=1440,9000',
    f'--screenshot={out_tall_light}',
    f'file:///{html_light}'
], check=True)

if os.path.exists('temp_gallery_light.html'):
    os.remove('temp_gallery_light.html')

im_light = Image.open(out_tall_light)

# Hero section crop (y=0 to y=1000)
hero_light = im_light.crop((0, 0, 1440, 1000))
hero_light.save('scratch/gallery_live_hero_light.png')

# Collection grid crop (y=900 to y=2000)
grid_light = im_light.crop((0, 900, 1440, 2100))
grid_light.save('scratch/gallery_live_grid_light.png')

# Final CTA section crop (bottom 1000px above footer)
h = im_light.size[1]
cta_light = im_light.crop((0, h - 1400, 1440, h - 350))
cta_light.save('scratch/gallery_live_cta_light.png')

# 2. DARK MODE
c_dark = c.replace('<head>', '<head><script>localStorage.setItem("eol_theme_preference", "dark");</script>')
with open('temp_gallery_dark.html', 'w', encoding='utf-8') as f:
    f.write(c_dark)

out_tall_dark = os.path.abspath('scratch/gallery_tall_dark.png')
html_dark = os.path.abspath('temp_gallery_dark.html').replace('\\', '/')

subprocess.run([
    chrome,
    '--headless=new',
    '--disable-gpu',
    '--window-size=1440,9000',
    f'--screenshot={out_tall_dark}',
    f'file:///{html_dark}'
], check=True)

if os.path.exists('temp_gallery_dark.html'):
    os.remove('temp_gallery_dark.html')

im_dark = Image.open(out_tall_dark)
cta_dark = im_dark.crop((0, h - 1400, 1440, h - 350))
cta_dark.save('scratch/gallery_live_cta_dark.png')

print("All gallery screenshots captured successfully!")
