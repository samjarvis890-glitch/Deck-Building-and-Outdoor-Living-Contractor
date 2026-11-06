import subprocess
import os

chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
cwd = os.getcwd().replace('\\', '/')

js = """
<script>
window.addEventListener('load', function() {
    var sup = document.getElementById('faqSupport');
    var card = document.querySelector('.faq-support-card');
    
    // Check var(--bg-surface) and var(--bg-card) values
    var htmlStyle = window.getComputedStyle(document.documentElement);
    console.error('VARS:' + JSON.stringify({
        bgSurface: htmlStyle.getPropertyValue('--bg-surface'),
        bgCard: htmlStyle.getPropertyValue('--bg-card'),
        bgPrimary: htmlStyle.getPropertyValue('--bg-primary'),
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

with open('temp_dark_vars.html', 'w', encoding='utf-8') as f:
    f.write(dark_c)

cmd = [
    chrome, '--headless=new', '--disable-gpu', '--window-size=1440,900',
    '--enable-logging=stderr',
    f'--screenshot=scratch/temp_del3.png',
    f'file:///{cwd}/temp_dark_vars.html'
]

proc = subprocess.run(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True, encoding='utf-8')
for line in proc.stderr.split('\n'):
    if 'VARS:' in line:
        print(line.strip())

if os.path.exists('temp_dark_vars.html'): os.remove('temp_dark_vars.html')
if os.path.exists('scratch/temp_del3.png'): os.remove('scratch/temp_del3.png')
