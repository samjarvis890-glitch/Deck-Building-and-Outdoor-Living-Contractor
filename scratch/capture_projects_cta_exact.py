import subprocess
import os
from PIL import Image

chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
html_path = os.path.abspath('projects.html').replace('\\', '/')

# 1. LIGHT MODE
tall_light = os.path.abspath('scratch/projects_tall_8300_light.png')
subprocess.run([
    chrome, '--headless=new', '--disable-gpu',
    '--window-size=1440,8300',
    f'--screenshot={tall_light}',
    f'file:///{html_path}'
], timeout=25)

# 2. DARK MODE
with open('projects.html', 'r', encoding='utf-8') as f:
    dark_html = f.read().replace('data-theme="light"', 'data-theme="dark"')
with open('temp_dark_proj_8300.html', 'w', encoding='utf-8') as f:
    f.write(dark_html)

tall_dark = os.path.abspath('scratch/projects_tall_8300_dark.png')
subprocess.run([
    chrome, '--headless=new', '--disable-gpu',
    '--window-size=1440,8300',
    f'--screenshot={tall_dark}',
    f'file:///{os.path.abspath("temp_dark_proj_8300.html").replace(chr(92), "/")}'
], timeout=25)

if os.path.exists('temp_dark_proj_8300.html'):
    os.remove('temp_dark_proj_8300.html')

im_l = Image.open(tall_light)
im_d = Image.open(tall_dark)

# Crop CTA (6800 to 7550)
cta_l = im_l.crop((0, 6800, 1440, 7550))
cta_l.save('scratch/projects_cta_light_exact.png')

cta_d = im_d.crop((0, 6800, 1440, 7550))
cta_d.save('scratch/projects_cta_dark_exact.png')

print("Cropped Projects CTA in Light and Dark mode successfully!")
