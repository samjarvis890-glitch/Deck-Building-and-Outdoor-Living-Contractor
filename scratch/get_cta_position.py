import subprocess
import os

js = """
var cta = document.getElementById('gallery-final-cta');
var r = cta.getBoundingClientRect();
console.log('CTA_POSITION:' + JSON.stringify({
    top: Math.round(r.top + window.scrollY),
    bottom: Math.round(r.bottom + window.scrollY),
    height: Math.round(r.height),
    docHeight: Math.max(document.body.scrollHeight, document.documentElement.scrollHeight)
}));
"""

with open('gallery.html', 'r', encoding='utf-8') as f:
    c = f.read()

injected = c.replace('</body>', f'<script>{js}</script></body>')
with open('temp_measure_cta.html', 'w', encoding='utf-8') as f:
    f.write(injected)

path = os.path.abspath('temp_measure_cta.html').replace('\\', '/')
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

if os.path.exists('temp_measure_cta.html'):
    os.remove('temp_measure_cta.html')

for line in (stderr + '\n' + stdout).splitlines():
    if 'CTA_POSITION:' in line:
        data = line.split('CTA_POSITION:')[1].split('", source:')[0].strip().rstrip('"')
        print(data)
