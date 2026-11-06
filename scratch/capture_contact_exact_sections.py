import subprocess
import os
from PIL import Image

chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
cwd = os.getcwd().replace('\\', '/')

with open('contact.html', 'r', encoding='utf-8') as f:
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

with open('temp_contact_light.html', 'w', encoding='utf-8') as f:
    f.write(light_html)

tall_light_png = os.path.abspath('scratch/contact_tall_7600_light.png')
subprocess.run([
    chrome, '--headless=new', '--disable-gpu',
    '--window-size=1440,7600',
    f'--screenshot={tall_light_png}',
    f'file:///{cwd}/temp_contact_light.html'
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

with open('temp_contact_dark.html', 'w', encoding='utf-8') as f:
    f.write(dark_html)

tall_dark_png = os.path.abspath('scratch/contact_tall_7600_dark.png')
subprocess.run([
    chrome, '--headless=new', '--disable-gpu',
    '--window-size=1440,7600',
    f'--screenshot={tall_dark_png}',
    f'file:///{cwd}/temp_contact_dark.html'
], check=True)

# Clean up root temp files
if os.path.exists('temp_contact_light.html'): os.remove('temp_contact_light.html')
if os.path.exists('temp_contact_dark.html'): os.remove('temp_contact_dark.html')

im_l = Image.open(tall_light_png)
im_d = Image.open(tall_dark_png)

# 1. Hero: 0 to 900
im_l.crop((0, 0, 1440, 900)).save('scratch/contact_hero_exact_light.png')
im_d.crop((0, 0, 1440, 900)).save('scratch/contact_hero_exact_dark.png')

# 2. Consultation Form & Side Media: 1600 to 2950
im_l.crop((0, 1600, 1440, 2750)).save('scratch/contact_form_side_exact_light.png')
im_d.crop((0, 1600, 1440, 2750)).save('scratch/contact_form_side_exact_dark.png')

# 3. Map Section: 3550 to 4580
im_l.crop((0, 3550, 1440, 4580)).save('scratch/contact_map_exact_light.png')
im_d.crop((0, 3550, 1440, 4580)).save('scratch/contact_map_exact_dark.png')

# 4. Checklist Section: 4580 to 5560
im_l.crop((0, 4580, 1440, 5560)).save('scratch/contact_checklist_exact_light.png')
im_d.crop((0, 4580, 1440, 5560)).save('scratch/contact_checklist_exact_dark.png')

# 5. Final CTA: 6400 to 7000
im_l.crop((0, 6400, 1440, 7000)).save('scratch/contact_final_cta_exact_light.png')
im_d.crop((0, 6400, 1440, 7000)).save('scratch/contact_final_cta_exact_dark.png')

# 6. Tablet (820px)
out_tablet = os.path.abspath('scratch/contact_tablet_820.png')
subprocess.run([
    chrome, '--headless=new', '--disable-gpu',
    '--window-size=820,1180',
    f'--screenshot={out_tablet}',
    f'file:///{cwd}/contact.html'
], check=True)

# 7. Mobile (504px)
out_mobile = os.path.abspath('scratch/contact_mobile_504.png')
subprocess.run([
    chrome, '--headless=new', '--disable-gpu',
    '--window-size=504,844',
    f'--screenshot={out_mobile}',
    f'file:///{cwd}/contact.html'
], check=True)

print("All exact Contact sections and responsive screenshots captured successfully!")
