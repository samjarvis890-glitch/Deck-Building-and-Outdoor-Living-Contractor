import subprocess
import os

with open('about.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Force light theme attribute
c_light = c.replace('<html lang="en"', '<html lang="en" data-theme="light"')
with open('scratch/about_light_test.html', 'w', encoding='utf-8') as f:
    f.write(c_light)

chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
html = os.path.abspath('scratch/about_light_test.html').replace('\\', '/')
out_light = os.path.abspath('scratch/live_about_light.png')

subprocess.run([
    chrome,
    '--headless=new',
    '--disable-gpu',
    '--window-size=1440,1100',
    f'--screenshot={out_light}',
    f'file:///{html}'
], check=True)
print('Light screenshot captured:', os.path.exists(out_light))
