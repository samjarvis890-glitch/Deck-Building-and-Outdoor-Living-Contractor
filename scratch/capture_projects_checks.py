import subprocess
import os
from PIL import Image

chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
html_path = os.path.abspath('projects.html').replace('\\', '/')

# 1. Desktop Standard 1440x900
desktop_hero = os.path.abspath('scratch/projects_desktop_hero.png')
subprocess.run([
    chrome, '--headless=new', '--disable-gpu',
    '--window-size=1440,900',
    f'--screenshot={desktop_hero}',
    f'file:///{html_path}'
], timeout=20)

# 2. Desktop Full Light
tall_light = os.path.abspath('scratch/projects_tall_light.png')
subprocess.run([
    chrome, '--headless=new', '--disable-gpu',
    '--window-size=1440,7000',
    f'--screenshot={tall_light}',
    f'file:///{html_path}'
], timeout=25)

# 3. Desktop Full Dark
with open('projects.html', 'r', encoding='utf-8') as f:
    dark_html = f.read().replace('data-theme="light"', 'data-theme="dark"')
with open('temp_projects_dark.html', 'w', encoding='utf-8') as f:
    f.write(dark_html)

tall_dark = os.path.abspath('scratch/projects_tall_dark.png')
subprocess.run([
    chrome, '--headless=new', '--disable-gpu',
    '--window-size=1440,7000',
    f'--screenshot={tall_dark}',
    f'file:///{os.path.abspath("temp_projects_dark.html").replace(chr(92), "/")}'
], timeout=25)

if os.path.exists('temp_projects_dark.html'):
    os.remove('temp_projects_dark.html')

# 4. Tablet 820x1180
subprocess.run([
    chrome, '--headless=new', '--disable-gpu',
    '--window-size=820,1180',
    f'--screenshot={os.path.abspath("scratch/projects_tablet_820.png")}',
    f'file:///{html_path}'
], timeout=20)

# 5. Mobile 504x844
subprocess.run([
    chrome, '--headless=new', '--disable-gpu',
    '--window-size=504,844',
    f'--screenshot={os.path.abspath("scratch/projects_mobile_504.png")}',
    f'file:///{html_path}'
], timeout=20)

# Crop Final CTA section from tall images
im_l = Image.open(tall_light)
im_d = Image.open(tall_dark)

# Let's crop bottom 1200px above footer (footer is approx 450px)
h_l = im_l.size[1]
cta_l = im_l.crop((0, h_l - 1200, 1440, h_l - 420))
cta_l.save('scratch/projects_final_cta_light.png')

h_d = im_d.size[1]
cta_d = im_d.crop((0, h_d - 1200, 1440, h_d - 420))
cta_d.save('scratch/projects_final_cta_dark.png')

print("All screenshots captured and cropped successfully!")
