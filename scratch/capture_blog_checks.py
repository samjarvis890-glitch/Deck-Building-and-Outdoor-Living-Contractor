import subprocess
import os
from PIL import Image

chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
html_path = os.path.abspath('blog.html').replace('\\', '/')

# 1. Desktop Standard 1440x900
desktop_hero = os.path.abspath('scratch/blog_desktop_hero.png')
subprocess.run([
    chrome, '--headless=new', '--disable-gpu',
    '--window-size=1440,900',
    f'--screenshot={desktop_hero}',
    f'file:///{html_path}'
], timeout=20)

# 2. Desktop Full Light
tall_light = os.path.abspath('scratch/blog_tall_light.png')
subprocess.run([
    chrome, '--headless=new', '--disable-gpu',
    '--window-size=1440,9000',
    f'--screenshot={tall_light}',
    f'file:///{html_path}'
], timeout=25)

# 3. Desktop Full Dark
with open('blog.html', 'r', encoding='utf-8') as f:
    dark_html = f.read().replace('data-theme="light"', 'data-theme="dark"')
with open('temp_blog_dark.html', 'w', encoding='utf-8') as f:
    f.write(dark_html)

tall_dark = os.path.abspath('scratch/blog_tall_dark.png')
subprocess.run([
    chrome, '--headless=new', '--disable-gpu',
    '--window-size=1440,9000',
    f'--screenshot={tall_dark}',
    f'file:///{os.path.abspath("temp_blog_dark.html").replace(chr(92), "/")}'
], timeout=25)

if os.path.exists('temp_blog_dark.html'):
    os.remove('temp_blog_dark.html')

# 4. Tablet 820x1180
subprocess.run([
    chrome, '--headless=new', '--disable-gpu',
    '--window-size=820,1180',
    f'--screenshot={os.path.abspath("scratch/blog_tablet_820.png")}',
    f'file:///{html_path}'
], timeout=20)

# 5. Mobile 504x844
subprocess.run([
    chrome, '--headless=new', '--disable-gpu',
    '--window-size=504,844',
    f'--screenshot={os.path.abspath("scratch/blog_mobile_504.png")}',
    f'file:///{html_path}'
], timeout=20)

# Measure Section 9 CTA position
im_l = Image.open(tall_light)
im_d = Image.open(tall_dark)

# Let's crop bottom 1200px above footer
h_l = im_l.size[1]
cta_l = im_l.crop((0, h_l - 1100, 1440, h_l - 380))
cta_l.save('scratch/blog_final_cta_light.png')

h_d = im_d.size[1]
cta_d = im_d.crop((0, h_d - 1100, 1440, h_d - 380))
cta_d.save('scratch/blog_final_cta_dark.png')

# Also crop Featured Article & Articles (y=900 to 2200)
articles_crop = im_l.crop((0, 900, 1440, 2200))
articles_crop.save('scratch/blog_articles_section.png')

print("All blog screenshots captured and cropped successfully!")
