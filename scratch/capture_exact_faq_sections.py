import subprocess
import os
from PIL import Image

chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
cwd = os.getcwd().replace('\\', '/')

with open('faq.html', 'r', encoding='utf-8') as f:
    base_html = f.read()

# 1. LIGHT MODE
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

tall_light_png = os.path.abspath('scratch/faq_tall_8400_light.png')
subprocess.run([
    chrome, '--headless=new', '--disable-gpu',
    '--window-size=1440,8400',
    f'--screenshot={tall_light_png}',
    f'file:///{cwd}/temp_faq_light.html'
], check=True)

# 2. DARK MODE
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

tall_dark_png = os.path.abspath('scratch/faq_tall_8400_dark.png')
subprocess.run([
    chrome, '--headless=new', '--disable-gpu',
    '--window-size=1440,8400',
    f'--screenshot={tall_dark_png}',
    f'file:///{cwd}/temp_faq_dark.html'
], check=True)

# Clean up
if os.path.exists('temp_faq_light.html'): os.remove('temp_faq_light.html')
if os.path.exists('temp_faq_dark.html'): os.remove('temp_faq_dark.html')

im_l = Image.open(tall_light_png)
im_d = Image.open(tall_dark_png)

# 1. Hero
im_l.crop((0, 0, 1440, 950)).save('scratch/faq_hero_exact_light.png')
im_d.crop((0, 0, 1440, 950)).save('scratch/faq_hero_exact_dark.png')

# 2. Support Section 8 (top 6125, height 946) -> crop 6100 to 7070
im_l.crop((0, 6100, 1440, 7070)).save('scratch/faq_support_exact_light.png')
im_d.crop((0, 6100, 1440, 7070)).save('scratch/faq_support_exact_dark.png')

# 3. Final CTA Section 9 (top 7071, height 576) -> crop 7065 to 7660
im_l.crop((0, 7065, 1440, 7660)).save('scratch/faq_final_cta_exact_light.png')
im_d.crop((0, 7065, 1440, 7660)).save('scratch/faq_final_cta_exact_dark.png')

print("All exact FAQ sections cropped and saved successfully!")
