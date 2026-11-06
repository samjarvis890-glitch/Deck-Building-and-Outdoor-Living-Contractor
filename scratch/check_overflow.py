import subprocess
import json

js = """
var overflowing = [];
var docWidth = document.documentElement.clientWidth;
document.querySelectorAll('*').forEach(function(el) {
    var r = el.getBoundingClientRect();
    if (r.right > docWidth + 1 || r.width > docWidth + 1) {
        overflowing.push({
            tag: el.tagName,
            cls: el.className,
            id: el.id,
            width: r.width,
            right: r.right,
            docWidth: docWidth
        });
    }
});
console.log('OVERFLOW_ELEMENTS:' + JSON.stringify(overflowing));
"""

with open('gallery.html', 'r', encoding='utf-8') as f:
    c = f.read()

injected = c.replace('</body>', f'<script>{js}</script></body>')
with open('scratch/temp_overflow.html', 'w', encoding='utf-8') as f:
    f.write(injected)

import os
path = os.path.abspath('scratch/temp_overflow.html').replace('\\', '/')
cmd = [
    r'C:\Program Files\Google\Chrome\Application\chrome.exe',
    '--headless=new',
    '--disable-gpu',
    '--window-size=390,844',
    '--enable-logging=stderr',
    f'file:///{path}'
]

# We can run with timeout or dump console
proc = subprocess.Popen(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True, encoding='utf-8')
try:
    stdout, stderr = proc.communicate(timeout=5)
except subprocess.TimeoutExpired:
    proc.kill()
    stdout, stderr = proc.communicate()

for line in (stderr + '\n' + stdout).splitlines():
    if 'OVERFLOW_ELEMENTS:' in line:
        data = line.split('OVERFLOW_ELEMENTS:')[1]
        items = json.loads(data)
        print(f"Total overflowing elements: {len(items)}")
        for it in items[:15]:
            print(f"Tag: {it['tag']}, Cls: {it['cls'][:30]}, Width: {it['width']}, Right: {it['right']}")
