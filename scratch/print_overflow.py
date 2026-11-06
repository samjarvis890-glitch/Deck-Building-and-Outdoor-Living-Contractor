import subprocess
import re

with open('scratch/temp_overflow.html', 'r', encoding='utf-8') as f:
    pass

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

proc = subprocess.Popen(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True, encoding='utf-8')
try:
    stdout, stderr = proc.communicate(timeout=5)
except subprocess.TimeoutExpired:
    proc.kill()
    stdout, stderr = proc.communicate()

m = re.search(r'OVERFLOW_ELEMENTS:(\[.*?\])', stderr + '\n' + stdout)
if m:
    import json
    items = json.loads(m.group(1))
    print(f"Total overflowing elements: {len(items)}")
    for it in items[:15]:
        print(f"Tag: {it['tag']}, Cls: {it['cls'][:40]}, Id: {it['id']}, Width: {it['width']}, Right: {it['right']}")
else:
    print("No match, searching raw:")
    for line in (stderr + stdout).splitlines():
        if 'OVERFLOW_ELEMENTS' in line:
            print(line[:200])
