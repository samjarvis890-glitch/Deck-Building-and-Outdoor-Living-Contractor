import subprocess
import os
from PIL import Image

chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
cwd = os.getcwd().replace('\\', '/')

with open('faq.html', 'r', encoding='utf-8') as f:
    base_html = f.read()

# 1. LIGHT MODE
light_html = base_html.replace(
    'var theme = savedTheme ? savedTheme : (prefersDark ? \'dark\' : \'light\');',
    'var theme = "light";'
).replace('<html lang="en" dir="ltr" data-theme="light">', '<html lang="en" dir="ltr" data-theme="light">')

with open('scratch/temp_faq_light.html', 'w', encoding='utf-8') as f:
    f.write(light_html)

out_tall_light = os.path.abspath('scratch/faq_tall_light.png')
subprocess.run([
    chrome, '--headless=new', '--disable-gpu',
    '--window-size=1440,9000',
    f'--screenshot={out_tall_light}',
    f'file:///{os.path.abspath("scratch/temp_faq_light.html").replace(chr(92), "/")}'
], check=True)

# 2. DARK MODE
dark_html = base_html.replace(
    'var theme = savedTheme ? savedTheme : (prefersDark ? \'dark\' : \'light\');',
    'var theme = "dark";'
).replace('<html lang="en" dir="ltr" data-theme="light">', '<html lang="en" dir="ltr" data-theme="dark">')

with open('scratch/temp_faq_dark.html', 'w', encoding='utf-8') as f:
    f.write(dark_html)

out_tall_dark = os.path.abspath('scratch/faq_tall_dark.png')
subprocess.run([
    chrome, '--headless=new', '--disable-gpu',
    '--window-size=1440,9000',
    f'--screenshot={out_tall_dark}',
    f'file:///{os.path.abspath("scratch/temp_faq_dark.html").replace(chr(92), "/")}'
], check=True)

# 3. Clean up temp files
for tf in ['scratch/temp_faq_light.html', 'scratch/temp_faq_dark.html']:
    if os.path.exists(tf): os.remove(tf)

print(f"Tall Light saved: {os.path.exists(out_tall_light)}, size: {os.path.getsize(out_tall_light)}")
print(f"Tall Dark saved: {os.path.exists(out_tall_dark)}, size: {os.path.getsize(out_tall_dark)}")
