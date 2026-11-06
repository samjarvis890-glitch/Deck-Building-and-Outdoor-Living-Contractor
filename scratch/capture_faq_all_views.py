import subprocess
import os
from PIL import Image

chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

with open('faq.html', 'r', encoding='utf-8') as f:
    base_html = f.read()

# 1. LIGHT MODE
light_script = """<script>
localStorage.setItem('eol_theme_preference', 'light');
document.documentElement.setAttribute('data-theme', 'light');
</script>"""
light_html = base_html.replace('<head>', f'<head>{light_script}')
with open('scratch/temp_light.html', 'w', encoding='utf-8') as f:
    f.write(light_html)

tall_light_png = os.path.abspath('scratch/faq_tall_light.png')
subprocess.run([
    chrome, '--headless=new', '--disable-gpu',
    '--window-size=1440,5500',
    f'--screenshot={tall_light_png}',
    f'file:///{os.path.abspath("scratch/temp_light.html").replace(chr(92), "/")}'
], check=True)

# 2. DARK MODE
dark_script = """<script>
localStorage.setItem('eol_theme_preference', 'dark');
document.documentElement.setAttribute('data-theme', 'dark');
</script>"""
dark_html = base_html.replace('<head>', f'<head>{dark_script}')
with open('scratch/temp_dark.html', 'w', encoding='utf-8') as f:
    f.write(dark_html)

tall_dark_png = os.path.abspath('scratch/faq_tall_dark.png')
subprocess.run([
    chrome, '--headless=new', '--disable-gpu',
    '--window-size=1440,5500',
    f'--screenshot={tall_dark_png}',
    f'file:///{os.path.abspath("scratch/temp_dark.html").replace(chr(92), "/")}'
], check=True)

# 3. Clean temp
if os.path.exists('scratch/temp_light.html'): os.remove('scratch/temp_light.html')
if os.path.exists('scratch/temp_dark.html'): os.remove('scratch/temp_dark.html')

im_l = Image.open(tall_light_png)
im_d = Image.open(tall_dark_png)

# Hero: 0 to 950
im_l.crop((0, 0, 1440, 950)).save('scratch/faq_hero_exact_light.png')
im_d.crop((0, 0, 1440, 950)).save('scratch/faq_hero_exact_dark.png')

# Support: 3500 to 4150
im_l.crop((0, 3500, 1440, 4150)).save('scratch/faq_support_exact_light.png')
im_d.crop((0, 3500, 1440, 4150)).save('scratch/faq_support_exact_dark.png')

# CTA: 4050 to 4700
im_l.crop((0, 4050, 1440, 4700)).save('scratch/faq_final_cta_exact_light.png')
im_d.crop((0, 4050, 1440, 4700)).save('scratch/faq_final_cta_exact_dark.png')

# 4. Tablet
tablet_png = os.path.abspath('scratch/faq_tablet_820.png')
subprocess.run([
    chrome, '--headless=new', '--disable-gpu',
    '--window-size=820,1180',
    f'--screenshot={tablet_png}',
    f'file:///{os.path.abspath("faq.html").replace(chr(92), "/")}'
], check=True)

# 5. Mobile
mobile_png = os.path.abspath('scratch/faq_mobile_504.png')
subprocess.run([
    chrome, '--headless=new', '--disable-gpu',
    '--window-size=504,844',
    f'--screenshot={mobile_png}',
    f'file:///{os.path.abspath("faq.html").replace(chr(92), "/")}'
], check=True)

print("All exact FAQ views cropped and saved successfully!")
