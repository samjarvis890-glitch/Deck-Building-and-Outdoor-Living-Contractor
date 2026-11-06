import subprocess
import os

chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

js = """
<script>
window.addEventListener('load', function() {
    function getOffset(id) {
        var el = document.getElementById(id);
        if (!el) return null;
        var r = el.getBoundingClientRect();
        return { id: id, top: Math.round(r.top + window.scrollY), height: Math.round(r.height) };
    }
    console.error('SEC_Y:' + JSON.stringify([
        getOffset('faqHero'),
        getOffset('faqSearch'),
        getOffset('faqCategories'),
        getOffset('faqSupport'),
        getOffset('finalCta')
    ]));
});
</script>
"""

with open('faq.html', 'r', encoding='utf-8') as f:
    c = f.read().replace('</head>', f'{js}</head>')

with open('scratch/temp_y.html', 'w', encoding='utf-8') as f:
    f.write(c)

cmd = [
    chrome, '--headless=new', '--disable-gpu', '--window-size=1440,9000',
    '--enable-logging=stderr',
    f'--screenshot=scratch/temp_y.png',
    f'file:///{os.path.abspath("scratch/temp_y.html").replace(chr(92), "/")}'
]

proc = subprocess.run(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True, encoding='utf-8')
for line in proc.stderr.split('\n'):
    if 'SEC_Y:' in line:
        print(line.strip())

if os.path.exists('scratch/temp_y.html'): os.remove('scratch/temp_y.html')
if os.path.exists('scratch/temp_y.png'): os.remove('scratch/temp_y.png')
