import subprocess
import os

chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
cwd = os.getcwd().replace('\\', '/')

js = """
<script>
window.addEventListener('load', function() {
    var sup = document.getElementById('faqSupport');
    var card = document.querySelector('.faq-support-card');
    var h3 = document.querySelector('.faq-support-content h3');
    var h2 = document.querySelector('.faq-support .faq-title');
    console.error('DARK_STYLES:' + JSON.stringify({
        htmlTheme: document.documentElement.getAttribute('data-theme'),
        supportBg: window.getComputedStyle(sup).backgroundColor,
        cardBg: window.getComputedStyle(card).backgroundColor,
        h3Color: window.getComputedStyle(h3).color,
        h2Color: window.getComputedStyle(h2).color,
    }));
});
</script>
"""

with open('faq.html', 'r', encoding='utf-8') as f:
    c = f.read().replace('</head>', f'{js}</head>')

dark_script = """<script>
try {
  localStorage.setItem('eol_theme_preference', 'dark');
  document.documentElement.setAttribute('data-theme', 'dark');
} catch(e){}
</script>"""
dark_c = c.replace(
    'var theme = savedTheme ? savedTheme : (prefersDark ? \'dark\' : \'light\');',
    'var theme = "dark";'
).replace('<head>', f'<head>{dark_script}')

with open('temp_dark_debug.html', 'w', encoding='utf-8') as f:
    f.write(dark_c)

cmd = [
    chrome, '--headless=new', '--disable-gpu', '--window-size=1440,900',
    '--enable-logging=stderr',
    f'--screenshot=scratch/temp_del2.png',
    f'file:///{cwd}/temp_dark_debug.html'
]

proc = subprocess.run(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True, encoding='utf-8')
for line in proc.stderr.split('\n'):
    if 'DARK_STYLES:' in line:
        print(line.strip())

if os.path.exists('temp_dark_debug.html'): os.remove('temp_dark_debug.html')
if os.path.exists('scratch/temp_del2.png'): os.remove('scratch/temp_del2.png')
