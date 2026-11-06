import subprocess
import os
from PIL import Image

chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
html_path = os.path.abspath('blog.html').replace('\\', '/')

# 1. LIGHT MODE
tall_light = os.path.abspath('scratch/blog_tall_12100_light.png')
with open('blog.html', 'r', encoding='utf-8') as f:
    light_c = f.read().replace('var theme = savedTheme ? savedTheme : (prefersDark ? \'dark\' : \'light\');', 'var theme = "light";')
with open('temp_blog_light_tall.html', 'w', encoding='utf-8') as f:
    f.write(light_c)

subprocess.run([
    chrome, '--headless=new', '--disable-gpu',
    '--window-size=1440,12100',
    f'--screenshot={tall_light}',
    f'file:///{os.path.abspath("temp_blog_light_tall.html").replace(chr(92), "/")}'
], timeout=30)

# 2. DARK MODE
with open('blog.html', 'r', encoding='utf-8') as f:
    dark_c = f.read().replace('var theme = savedTheme ? savedTheme : (prefersDark ? \'dark\' : \'light\');', 'var theme = "dark";')
with open('temp_blog_dark_tall.html', 'w', encoding='utf-8') as f:
    f.write(dark_c)

tall_dark = os.path.abspath('scratch/blog_tall_12100_dark.png')
subprocess.run([
    chrome, '--headless=new', '--disable-gpu',
    '--window-size=1440,12100',
    f'--screenshot={tall_dark}',
    f'file:///{os.path.abspath("temp_blog_dark_tall.html").replace(chr(92), "/")}'
], timeout=30)

if os.path.exists('temp_blog_light_tall.html'): os.remove('temp_blog_light_tall.html')
if os.path.exists('temp_blog_dark_tall.html'): os.remove('temp_blog_dark_tall.html')

im_l = Image.open(tall_light)
im_d = Image.open(tall_dark)

# Crop CTA: top: 10815, bottom: 11360 -> crop 10750 to 11450
cta_l = im_l.crop((0, 10750, 1440, 11450))
cta_l.save('scratch/blog_final_cta_exact_light.png')

cta_d = im_d.crop((0, 10750, 1440, 11450))
cta_d.save('scratch/blog_final_cta_exact_dark.png')

print("Cropped Blog CTA in Light and Dark mode successfully!")
