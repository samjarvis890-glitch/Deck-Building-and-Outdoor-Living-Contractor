import subprocess
import os
from PIL import Image

chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
cwd = os.getcwd().replace('\\', '/')

with open('faq.html', 'r', encoding='utf-8') as f:
    base_html = f.read()

# 1. LIGHT MODE in root directory
light_script = """<script>
try {
  localStorage.setItem('eol_theme_preference', 'light');
  document.documentElement.setAttribute('data-theme', 'light');
} catch(e){}
</script>"""
light_html = base_html.replace(
    'var theme = savedTheme ? savedTheme : (prefersDark ? \'dark\' : \'light\');',
    'var theme = "light";'
).replace('<head>', f'<head>{light_script}')

with open('temp_faq_light.html', 'w', encoding='utf-8') as f:
    f.write(light_html)

tall_light_png = os.path.abspath('scratch/faq_tall_light.png')
subprocess.run([
    chrome, '--headless=new', '--disable-gpu',
    '--window-size=1440,5500',
    f'--screenshot={tall_light_png}',
    f'file:///{cwd}/temp_faq_light.html'
], check=True)

# 2. DARK MODE in root directory
dark_script = """<script>
try {
  localStorage.setItem('eol_theme_preference', 'dark');
  document.documentElement.setAttribute('data-theme', 'dark');
} catch(e){}
</script>"""
dark_html = base_html.replace(
    'var theme = savedTheme ? savedTheme : (prefersDark ? \'dark\' : \'light\');',
    'var theme = "dark";'
).replace('<head>', f'<head>{dark_script}')

with open('temp_faq_dark.html', 'w', encoding='utf-8') as f:
    f.write(dark_html)

tall_dark_png = os.path.abspath('scratch/faq_tall_dark.png')
subprocess.run([
    chrome, '--headless=new', '--disable-gpu',
    '--window-size=1440,5500',
    f'--screenshot={tall_dark_png}',
    f'file:///{cwd}/temp_faq_dark.html'
], check=True)

# Clean up root temp files
if os.path.exists('temp_faq_light.html'): os.remove('temp_faq_light.html')
if os.path.exists('temp_faq_dark.html'): os.remove('temp_faq_dark.html')

print("Generating exact crops...")
im_l = Image.open(tall_light_png)
im_d = Image.open(tall_dark_png)

print("Image sizes:", im_l.size, im_d.size)

# Find positions dynamically or crop sections
im_l.crop((0, 0, 1440, 950)).save('scratch/faq_hero_exact_light.png')
im_d.crop((0, 0, 1440, 950)).save('scratch/faq_hero_exact_dark.png')

# Support & CTA
# Let's save a preview strip of both tall images to verify exact positions
im_l.resize((360, round(im_l.size[1] * 360 / im_l.size[0]))).save('scratch/faq_tall_light_thumb.png')
im_d.resize((360, round(im_d.size[1] * 360 / im_d.size[0]))).save('scratch/faq_tall_dark_thumb.png')

print("Done! Tall screenshots and hero crops generated successfully.")
