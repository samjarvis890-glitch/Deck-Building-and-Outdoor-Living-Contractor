import subprocess
import json

js = """
var big = [];
document.querySelectorAll('*').forEach(function(el) {
    if (el.scrollWidth >= 1500 || el.offsetWidth >= 1500) {
        big.push({
            tag: el.tagName,
            cls: el.className,
            id: el.id,
            scrollWidth: el.scrollWidth,
            offsetWidth: el.offsetWidth,
            html: el.outerHTML.slice(0, 150)
        });
    }
});
console.log('BIG_ELEMENTS:' + JSON.stringify(big));
"""

with open('gallery.html', 'r', encoding='utf-8') as f:
    c = f.read()

injected = c.replace('</body>', f'<script>{js}</script></body>')
with open('scratch/temp_findbig.html', 'w', encoding='utf-8') as f:
    f.write(injected)

import os
path = os.path.abspath('scratch/temp_findbig.html').replace('\\', '/')
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
    if 'BIG_ELEMENTS:' in line:
        data = line.split('BIG_ELEMENTS:')[1]
        if '", source:' in data:
            data = data.split('", source:')[0]
        # remove trailing quotes if any
        data = data.strip().rstrip('"').rstrip("'")
        items = json.loads(data)
        print(f"Total big elements: {len(items)}")
        for it in items:
            print(f"Tag: {it['tag']} | Cls: {it['cls']} | Id: {it['id']} | scrollW: {it['scrollWidth']} | offsetW: {it['offsetWidth']}")
            print(f"   HTML snippet: {it['html']}")
