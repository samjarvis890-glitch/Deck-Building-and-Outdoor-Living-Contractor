import subprocess
import os

chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

# 1. Desktop Light Mode
with open('blog.html', 'r', encoding='utf-8') as f:
    light_c = f.read().replace('var theme = savedTheme ? savedTheme : (prefersDark ? \'dark\' : \'light\');', 'var theme = "light";')
with open('temp_blog_light.html', 'w', encoding='utf-8') as f:
    f.write(light_c)

subprocess.run([
    chrome, '--headless=new', '--disable-gpu',
    '--window-size=1440,900',
    f'--screenshot={os.path.abspath("scratch/blog_desktop_light.png")}',
    f'file:///{os.path.abspath("temp_blog_light.html").replace(chr(92), "/")}'
], timeout=20)

# 2. Desktop Dark Mode
with open('blog.html', 'r', encoding='utf-8') as f:
    dark_c = f.read().replace('var theme = savedTheme ? savedTheme : (prefersDark ? \'dark\' : \'light\');', 'var theme = "dark";')
with open('temp_blog_dark.html', 'w', encoding='utf-8') as f:
    f.write(dark_c)

subprocess.run([
    chrome, '--headless=new', '--disable-gpu',
    '--window-size=1440,900',
    f'--screenshot={os.path.abspath("scratch/blog_desktop_dark.png")}',
    f'file:///{os.path.abspath("temp_blog_dark.html").replace(chr(92), "/")}'
], timeout=20)

# 3. Tablet (820x1180)
subprocess.run([
    chrome, '--headless=new', '--disable-gpu',
    '--window-size=820,1180',
    f'--screenshot={os.path.abspath("scratch/blog_tablet_820_v2.png")}',
    f'file:///{os.path.abspath("temp_blog_light.html").replace(chr(92), "/")}'
], timeout=20)

# 4. Mobile (504x844)
subprocess.run([
    chrome, '--headless=new', '--disable-gpu',
    '--window-size=504,844',
    f'--screenshot={os.path.abspath("scratch/blog_mobile_504_v2.png")}',
    f'file:///{os.path.abspath("temp_blog_light.html").replace(chr(92), "/")}'
], timeout=20)

if os.path.exists('temp_blog_light.html'): os.remove('temp_blog_light.html')
if os.path.exists('temp_blog_dark.html'): os.remove('temp_blog_dark.html')

print("Captured all responsive blog views successfully!")
