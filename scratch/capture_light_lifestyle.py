import subprocess
import os
from PIL import Image

chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
html = os.path.abspath('about.html').replace('\\', '/')
out_img = os.path.abspath('scratch/about_light_lifestyle.png')

with open('about.html', 'r', encoding='utf-8') as f:
    c = f.read()

c_light = c.replace('<head>', '<head><script>localStorage.setItem("eol_theme_preference", "light");</script>')
with open('about_temp_light2.html', 'w', encoding='utf-8') as f:
    f.write(c_light)

html_light = os.path.abspath('about_temp_light2.html').replace('\\', '/')
subprocess.run([
    chrome,
    '--headless=new',
    '--disable-gpu',
    '--window-size=1440,3600',
    f'--screenshot={out_img}',
    f'file:///{html_light}'
], check=True)

if os.path.exists('about_temp_light2.html'):
    os.remove('about_temp_light2.html')

im = Image.open(out_img)
# Crop the lifestyle section
crop = im.crop((0, 1850, 1440, 3100))
crop.save('scratch/about_light_lifestyle_crop.png')
print('Lifestyle light screenshot captured successfully!')
