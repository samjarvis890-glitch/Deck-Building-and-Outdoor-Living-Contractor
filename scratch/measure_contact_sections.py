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
    console.error('CONTACT_SECS:' + JSON.stringify({
        totalH: document.documentElement.scrollHeight,
        hero: getOffset('contactHero'),
        info: getOffset('contactInfo'),
        consultation: getOffset('consultation'),
        process: getOffset('contactProcess'),
        map: getOffset('contactMap'),
        checklist: getOffset('contactChecklist'),
        faq: getOffset('contactFaq'),
        cta: getOffset('contactFinalCta')
    }));
});
</script>
"""

with open('contact.html', 'r', encoding='utf-8') as f:
    c = f.read().replace('</head>', f'{js}</head>')

with open('temp_measure_contact.html', 'w', encoding='utf-8') as f:
    f.write(c)

cmd = [
    chrome, '--headless=new', '--disable-gpu', '--window-size=1440,900',
    '--enable-logging=stderr',
    f'--screenshot=scratch/temp_del_c.png',
    f'file:///{cwd}/temp_measure_contact.html'
]

proc = subprocess.run(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True, encoding='utf-8')
for line in proc.stderr.split('\n'):
    if 'CONTACT_SECS:' in line:
        print(line.strip())

if os.path.exists('temp_measure_contact.html'): os.remove('temp_measure_contact.html')
if os.path.exists('scratch/temp_del_c.png'): os.remove('scratch/temp_del_c.png')
