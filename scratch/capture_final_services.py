import subprocess
import os
from PIL import Image

chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

# Let's take screenshot with localStorage light
with open('services.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Put temp file in ROOT DIRECTORY
c_light = c.replace('<head>', '<head><script>localStorage.setItem("eol_theme_preference", "light");</script>')
with open('temp_services_light.html', 'w', encoding='utf-8') as f:
    f.write(c_light)

out_light = os.path.abspath('scratch/services_full_light.png')
html_light = os.path.abspath('temp_services_light.html').replace('\\', '/')

subprocess.run([
    chrome,
    '--headless=new',
    '--disable-gpu',
    '--window-size=1440,7500',
    f'--screenshot={out_light}',
    f'file:///{html_light}'
], check=True)

if os.path.exists('temp_services_light.html'):
    os.remove('temp_services_light.html')

im = Image.open(out_light)
print("Rendered full light image size:", im.size)

# Also let's measure where .services-final-cta-section is exactly
# Save hero crop
hero_crop = im.crop((0, 0, 1440, 950))
hero_crop.save('scratch/final_services_hero_view.png')

# Save bottom CTA crop (above footer, approximately bottom 1800px to bottom 400px)
h = im.size[1]
cta_crop = im.crop((0, h - 1750, 1440, h - 350))
cta_crop.save('scratch/final_services_cta_view_light.png')

# Now let's do the same for DARK MODE
c_dark = c.replace('<head>', '<head><script>localStorage.setItem("eol_theme_preference", "dark");</script>')
with open('temp_services_dark.html', 'w', encoding='utf-8') as f:
    f.write(c_dark)

out_dark = os.path.abspath('scratch/services_full_dark.png')
html_dark = os.path.abspath('temp_services_dark.html').replace('\\', '/')

subprocess.run([
    chrome,
    '--headless=new',
    '--disable-gpu',
    '--window-size=1440,7500',
    f'--screenshot={out_dark}',
    f'file:///{html_dark}'
], check=True)

if os.path.exists('temp_services_dark.html'):
    os.remove('temp_services_dark.html')

im_dark = Image.open(out_dark)
cta_dark = im_dark.crop((0, h - 1750, 1440, h - 350))
cta_dark.save('scratch/final_services_cta_view_dark.png')

print("Saved all final services crops!")
