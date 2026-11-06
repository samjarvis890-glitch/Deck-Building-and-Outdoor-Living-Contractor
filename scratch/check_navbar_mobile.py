import subprocess
import json

js = """
var b = document.querySelector('.navbar-brand-link').getBoundingClientRect();
var act = document.querySelector('.navbar-actions').getBoundingClientRect();
var ham = document.querySelector('.nav-hamburger-btn').getBoundingClientRect();
var nav = document.querySelector('.nav-container').getBoundingClientRect();
var hdr = document.querySelector('.site-header').getBoundingClientRect();
var hero = document.querySelector('.gallery-hero-section').getBoundingClientRect();
console.log('NAVBAR_RECTS:' + JSON.stringify({
    windowWidth: window.innerWidth,
    docScrollWidth: document.documentElement.scrollWidth,
    bodyScrollWidth: document.body.scrollWidth,
    header: hdr,
    navContainer: nav,
    brand: b,
    actions: act,
    hamburger: ham
}));
"""

with open('gallery.html', 'r', encoding='utf-8') as f:
    c = f.read()

injected = c.replace('</body>', f'<script>{js}</script></body>')
with open('scratch/temp_navcheck.html', 'w', encoding='utf-8') as f:
    f.write(injected)

import os
path = os.path.abspath('scratch/temp_navcheck.html').replace('\\', '/')
cmd = [
    r'C:\Program Files\Google\Chrome\Application\chrome.exe',
    '--headless=new',
    '--disable-gpu',
    '--window-size=390,844',
    '--enable-logging=stderr',
    f'file:///{path}'
]

proc = subprocess.Popen(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True, encoding='utf-8')
try:
    stdout, stderr = proc.communicate(timeout=5)
except subprocess.TimeoutExpired:
    proc.kill()
    stdout, stderr = proc.communicate()

for line in (stderr + '\n' + stdout).splitlines():
    if 'NAVBAR_RECTS:' in line:
        data = line.split('NAVBAR_RECTS:')[1]
        print(data)
