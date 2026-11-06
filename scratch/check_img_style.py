import subprocess
import json

js = """
var img = document.querySelector('.gallery-final-cta-bg');
var cs = window.getComputedStyle(img);
console.log('IMG_COMPUTED:' + JSON.stringify({
    position: cs.position,
    width: cs.width,
    maxWidth: cs.maxWidth,
    height: cs.height,
    left: cs.left,
    top: cs.top,
    display: cs.display
}));
"""

with open('gallery.html', 'r', encoding='utf-8') as f:
    c = f.read()

injected = c.replace('</body>', f'<script>{js}</script></body>')
with open('scratch/temp_imgcheck.html', 'w', encoding='utf-8') as f:
    f.write(injected)

import os
path = os.path.abspath('scratch/temp_imgcheck.html').replace('\\', '/')
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
    if 'IMG_COMPUTED:' in line:
        data = line.split('IMG_COMPUTED:')[1].split('", source:')[0].strip().rstrip('"')
        print(data)
