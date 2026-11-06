import subprocess
import os
import json

js = """
var overflowing = [];
var winW = window.innerWidth;
document.querySelectorAll('*').forEach(function(el) {
    var r = el.getBoundingClientRect();
    // Ignore elements inside mobile-drawer or elements with display:none
    if (el.closest('.mobile-drawer') || el.closest('.drawer-backdrop')) return;
    
    if (r.right > winW + 2 || r.width > winW + 2) {
        overflowing.push({
            tag: el.tagName,
            cls: el.className,
            id: el.id,
            width: Math.round(r.width),
            right: Math.round(r.right),
            left: Math.round(r.left)
        });
    }
});
console.log('REAL_MOBILE_OVERFLOW:' + JSON.stringify({
    winW: winW,
    scrollWidth: document.documentElement.scrollWidth,
    bodyScrollW: document.body.scrollWidth,
    items: overflowing
}));
"""

with open('gallery.html', 'r', encoding='utf-8') as f:
    c = f.read()

injected = c.replace('</body>', f'<script>{js}</script></body>')
with open('temp_mobile_test.html', 'w', encoding='utf-8') as f:
    f.write(injected)

path = os.path.abspath('temp_mobile_test.html').replace('\\', '/')
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

if os.path.exists('temp_mobile_test.html'):
    os.remove('temp_mobile_test.html')

for line in (stderr + '\n' + stdout).splitlines():
    if 'REAL_MOBILE_OVERFLOW:' in line:
        data = line.split('REAL_MOBILE_OVERFLOW:')[1].split('", source:')[0].strip().rstrip('"')
        res = json.loads(data)
        print("Window innerWidth:", res['winW'])
        print("Doc scrollWidth:", res['scrollWidth'])
        print("Body scrollWidth:", res['bodyScrollW'])
        print(f"Total non-drawer overflowing elements: {len(res['items'])}")
        for it in res['items']:
            print("  ", it)
