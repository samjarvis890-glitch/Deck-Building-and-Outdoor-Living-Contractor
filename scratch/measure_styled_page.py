import subprocess
import os

chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
cwd = os.getcwd().replace('\\', '/')

js = """
<script>
window.addEventListener('load', function() {
    function getOffset(id) {
        var el = document.getElementById(id);
        if (!el) return null;
        var r = el.getBoundingClientRect();
        return { id: id, top: Math.round(r.top + window.scrollY), height: Math.round(r.height) };
    }
    console.error('STYLED_Y:' + JSON.stringify({
        totalH: document.documentElement.scrollHeight,
        support: getOffset('faqSupport'),
        cta: getOffset('finalCta')
    }));
});
</script>
"""

with open('faq.html', 'r', encoding='utf-8') as f:
    c = f.read().replace('</head>', f'{js}</head>')

with open('temp_measure_styled.html', 'w', encoding='utf-8') as f:
    f.write(c)

cmd = [
    chrome, '--headless=new', '--disable-gpu', '--window-size=1440,900',
    '--enable-logging=stderr',
    f'--screenshot=scratch/temp_del.png',
    f'file:///{cwd}/temp_measure_styled.html'
]

proc = subprocess.run(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True, encoding='utf-8')
for line in proc.stderr.split('\n'):
    if 'STYLED_Y:' in line:
        print(line.strip())

if os.path.exists('temp_measure_styled.html'): os.remove('temp_measure_styled.html')
if os.path.exists('scratch/temp_del.png'): os.remove('scratch/temp_del.png')
