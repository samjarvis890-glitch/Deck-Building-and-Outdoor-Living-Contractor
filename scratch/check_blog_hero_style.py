import subprocess
import os
import json

js = """
var h1 = document.querySelector('.blog-hero-h1');
var hero = document.querySelector('.blog-hero');
var cs = window.getComputedStyle(h1);
var hcs = window.getComputedStyle(hero);
console.log('HERO_STYLES:' + JSON.stringify({
    theme: document.documentElement.getAttribute('data-theme'),
    h1_color: cs.color,
    hero_bg: hcs.backgroundColor,
    hero_bg_image: hcs.backgroundImage
}));
"""

with open('blog.html', 'r', encoding='utf-8') as f:
    c = f.read()

injected = c.replace('</body>', f'<script>{js}</script></body>')
with open('temp_check_blog_hero.html', 'w', encoding='utf-8') as f:
    f.write(injected)

path = os.path.abspath('temp_check_blog_hero.html').replace('\\', '/')
cmd = [
    r'C:\Program Files\Google\Chrome\Application\chrome.exe',
    '--headless=new',
    '--disable-gpu',
    '--window-size=1440,900',
    '--enable-logging=stderr',
    f'file:///{path}'
]

proc = subprocess.Popen(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True, encoding='utf-8')
try:
    stdout, stderr = proc.communicate(timeout=5)
except subprocess.TimeoutExpired:
    proc.kill()
    stdout, stderr = proc.communicate()

if os.path.exists('temp_check_blog_hero.html'):
    os.remove('temp_check_blog_hero.html')

for line in (stderr + '\n' + stdout).splitlines():
    if 'HERO_STYLES:' in line:
        data = line.split('HERO_STYLES:')[1].split('", source:')[0].strip().rstrip('"')
        print(data)
