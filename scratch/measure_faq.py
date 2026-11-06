import subprocess
import os

chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

js = """
<script>
window.addEventListener('load', function() {
    console.log('FAQ_PAGE_HEIGHT:' + document.documentElement.scrollHeight);
    console.log('HERO_POS:' + JSON.stringify(document.getElementById('faqHero').getBoundingClientRect()));
    console.log('SUPPORT_POS:' + JSON.stringify(document.getElementById('faqSupport').getBoundingClientRect()));
    console.log('CTA_POS:' + JSON.stringify(document.getElementById('finalCta').getBoundingClientRect()));
});
</script>
"""

with open('faq.html', 'r', encoding='utf-8') as f:
    c = f.read().replace('</body>', f'{js}</body>')

with open('scratch/temp_measure_faq.html', 'w', encoding='utf-8') as f:
    f.write(c)

cmd = [
    chrome, '--headless=new', '--disable-gpu', '--window-size=1440,900',
    '--enable-logging=stderr',
    f'file:///{os.path.abspath("scratch/temp_measure_faq.html").replace(chr(92), "/")}'
]

proc = subprocess.Popen(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True, encoding='utf-8')
try:
    stdout, stderr = proc.communicate(timeout=15)
    for line in stderr.split('\n'):
        if 'FAQ_PAGE_HEIGHT:' in line or '_POS:' in line:
            print(line.strip())
finally:
    proc.kill()
    if os.path.exists('scratch/temp_measure_faq.html'):
        os.remove('scratch/temp_measure_faq.html')
