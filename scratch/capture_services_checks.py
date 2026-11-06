import subprocess
import os
from PIL import Image

chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
html = os.path.abspath('services.html').replace('\\', '/')

# 1. LIGHT MODE TEST
with open('services.html', 'r', encoding='utf-8') as f:
    c = f.read()

c_light = c.replace('<head>', '<head><script>localStorage.setItem("eol_theme_preference", "light");</script>')
with open('services_temp_light.html', 'w', encoding='utf-8') as f:
    f.write(c_light)

html_light = os.path.abspath('services_temp_light.html').replace('\\', '/')
out_tall_light = os.path.abspath('scratch/services_tall_light.png')

subprocess.run([
    chrome,
    '--headless=new',
    '--disable-gpu',
    '--window-size=1440,5500',
    f'--screenshot={out_tall_light}',
    f'file:///{html_light}'
], check=True)

if os.path.exists('services_temp_light.html'):
    os.remove('services_temp_light.html')

im_light = Image.open(out_tall_light)

# Hero section crop (y=0 to y=1050)
hero_light = im_light.crop((0, 0, 1440, 1050))
hero_light.save('scratch/services_live_hero_light.png')

# Final CTA section crop (y=4300 to y=5200)
cta_light = im_light.crop((0, 4400, 1440, 5200))
cta_light.save('scratch/services_live_cta_light.png')

# 2. DARK MODE TEST
c_dark = c.replace('<head>', '<head><script>localStorage.setItem("eol_theme_preference", "dark");</script>')
with open('services_temp_dark.html', 'w', encoding='utf-8') as f:
    f.write(c_dark)

html_dark = os.path.abspath('services_temp_dark.html').replace('\\', '/')
out_tall_dark = os.path.abspath('scratch/services_tall_dark.png')

subprocess.run([
    chrome,
    '--headless=new',
    '--disable-gpu',
    '--window-size=1440,5500',
    f'--screenshot={out_tall_dark}',
    f'file:///{html_dark}'
], check=True)

if os.path.exists('services_temp_dark.html'):
    os.remove('services_temp_dark.html')

im_dark = Image.open(out_tall_dark)
cta_dark = im_dark.crop((0, 4400, 1440, 5200))
cta_dark.save('scratch/services_live_cta_dark.png')

print("All section crops captured successfully!")
