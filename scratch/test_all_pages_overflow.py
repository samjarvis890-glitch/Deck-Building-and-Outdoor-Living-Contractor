import subprocess
import os
import json

chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
pages = [
    'index.html', 'home-2.html', 'about.html', 'services.html',
    'gallery.html', 'projects.html', 'blog.html', 'faq.html', 'contact.html'
]

js_snippet = """
var overflowing = [];
var winW = window.innerWidth;
document.querySelectorAll('*').forEach(function(el) {
    if (el.closest('.mobile-drawer') || el.closest('.drawer-backdrop')) return;
    if (el.closest('.blog-filter-pills') || el.closest('.filter-container-scroll')) return;
    var r = el.getBoundingClientRect();
    if (r.right > winW + 2 || r.width > winW + 2) {
        overflowing.push(el.tagName + (el.className ? ('.' + el.className.split(' ').join('.')) : ''));
    }
});
console.log('PAGE_OVERFLOW_RESULT:' + JSON.stringify({
    winW: winW,
    scrollW: document.documentElement.scrollWidth,
    overflowingCount: overflowing.length,
    items: overflowing.slice(0, 3)
}));
"""

def test_page_at_width(page, width, height=844):
    with open(page, 'r', encoding='utf-8') as f:
        c = f.read()
    
    injected = c.replace('</body>', f'<script>{js_snippet}</script></body>')
    temp_file = f'temp_test_{width}_{os.path.basename(page)}.html'
    with open(temp_file, 'w', encoding='utf-8') as f:
        f.write(injected)
    
    path = os.path.abspath(temp_file).replace('\\', '/')
    cmd = [
        chrome,
        '--headless=new',
        '--disable-gpu',
        f'--window-size={width},{height}',
        '--enable-logging=stderr',
        f'file:///{path}'
    ]
    
    proc = subprocess.Popen(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True, encoding='utf-8')
    try:
        stdout, stderr = proc.communicate(timeout=6)
    except subprocess.TimeoutExpired:
        proc.kill()
        stdout, stderr = proc.communicate()
    
    if os.path.exists(temp_file):
        os.remove(temp_file)
    
    result = None
    output = (stderr or '') + '\n' + (stdout or '')
    for line in output.splitlines():
        if 'PAGE_OVERFLOW_RESULT:' in line:
            raw = line.split('PAGE_OVERFLOW_RESULT:')[1]
            if '", source:' in raw:
                raw = raw.split('", source:')[0].strip().rstrip('"')
            raw = raw.strip()
            try:
                result = json.loads(raw)
                break
            except Exception:
                pass
    return result

print(f"{'Page':<15} | {'Width':<6} | {'ScrollW':<8} | {'Status'}")
print("-" * 55)

all_passed = True
for page in pages:
    # 820px tablet test
    res_tab = test_page_at_width(page, 820)
    if res_tab:
        scroll = res_tab['scrollW']
        count = res_tab['overflowingCount']
        status = "PASS (0 overflow)" if count == 0 and scroll <= 822 else f"FAIL ({count} elements: {res_tab['items']})"
        print(f"{page:<15} | {'820':<6} | {scroll:<8} | {status}")
        if count > 0 or scroll > 822:
            all_passed = False
    else:
        print(f"{page:<15} | {'820':<6} | NO_LOG   | FAIL")
        all_passed = False

print("-" * 55)
print("ALL 9 PAGES TABLET (820px) PASSED:", all_passed)
