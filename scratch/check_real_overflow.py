import subprocess
import os

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
console.log('REAL_OVERFLOW:' + JSON.stringify({
    docWidth: docWidth,
    scrollWidth: document.documentElement.scrollWidth,
    overflowing: overflowing
}));
"""

with open('gallery.html', 'r', encoding='utf-8') as f:
    c = f.read()

injected = c.replace('</body>', f'<script>{js}</script></body>')
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
    if 'REAL_OVERFLOW:' in line:
        data = line.split('REAL_OVERFLOW:')[1].split('", source:')[0].strip().rstrip('"')
        import json
        res = json.loads(data)
        print("Doc Width:", res['docWidth'], "Scroll Width:", res['scrollWidth'])
        print("Total overflowing:", len(res['overflowing']))
        for item in res['overflowing'][:10]:
            print("  ", item)
