import subprocess
import os

js = """
var img = document.querySelector('.gallery-final-cta-bg');
var cs = window.getComputedStyle(img);
console.log('REAL_IMG_COMPUTED:' + JSON.stringify({
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
# Write in root so all relative assets/ links resolve perfectly!
with open('temp_test_root.html', 'w', encoding='utf-8') as f:
    f.write(injected)

path = os.path.abspath('temp_test_root.html').replace('\\', '/')
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

if os.path.exists('temp_test_root.html'):
    os.remove('temp_test_root.html')

for line in (stderr + '\n' + stdout).splitlines():
    if 'REAL_IMG_COMPUTED:' in line:
        data = line.split('REAL_IMG_COMPUTED:')[1].split('", source:')[0].strip().rstrip('"')
        print(data)
