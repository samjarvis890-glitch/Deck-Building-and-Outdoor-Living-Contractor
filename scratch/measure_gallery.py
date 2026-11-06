import subprocess
import json

# Let's write a script that measures the document height and section rects
js_code = """
window.__rects = {};
document.querySelectorAll('section, footer').forEach(function(el) {
    var r = el.getBoundingClientRect();
    window.__rects[el.className || el.tagName] = {
        top: r.top + window.scrollY,
        bottom: r.bottom + window.scrollY,
        height: r.height
    };
});
window.__docHeight = Math.max(
    document.body.scrollHeight, document.body.offsetHeight,
    document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight
);
console.log('MEASUREMENTS:' + JSON.stringify({height: window.__docHeight, rects: window.__rects}));
"""

with open('gallery.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Inject console logging
html_injected = html.replace('</body>', f'<script>{js_code}</script></body>')
with open('scratch/temp_measure.html', 'w', encoding='utf-8') as f:
    f.write(html_injected)

import os
html_path = os.path.abspath('scratch/temp_measure.html').replace('\\', '/')
cmd = [
    r'C:\Program Files\Google\Chrome\Application\chrome.exe',
    '--headless=new',
    '--disable-gpu',
    '--window-size=1440,1200',
    '--enable-logging=stderr',
    '--v=1',
    f'file:///{html_path}'
]

proc = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
# Print stdout and stderr
for line in (proc.stdout + '\n' + proc.stderr).splitlines():
    if 'MEASUREMENTS:' in line:
        data = line.split('MEASUREMENTS:')[1]
        print(data)
