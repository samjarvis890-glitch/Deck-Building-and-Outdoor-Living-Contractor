import subprocess
import os

script_preload = """
localStorage.setItem('eol_theme_preference', 'light');
"""

chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
html = os.path.abspath('about.html').replace('\\', '/')
out_img = os.path.abspath('scratch/about_light_exact.png')

# Let's run a script that injects localStorage setting before load
with open('about.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace <head> with <head><script>localStorage.setItem('eol_theme_preference', 'light');</script>
c_light = c.replace('<head>', '<head><script>localStorage.setItem("eol_theme_preference", "light");</script>')
with open('about_temp_light.html', 'w', encoding='utf-8') as f:
    f.write(c_light)

html_light = os.path.abspath('about_temp_light.html').replace('\\', '/')
subprocess.run([
    chrome,
    '--headless=new',
    '--disable-gpu',
    '--window-size=1440,1100',
    f'--screenshot={out_img}',
    f'file:///{html_light}'
], check=True)

if os.path.exists('about_temp_light.html'):
    os.remove('about_temp_light.html')

print('Light exact screenshot captured:', os.path.exists(out_img))
