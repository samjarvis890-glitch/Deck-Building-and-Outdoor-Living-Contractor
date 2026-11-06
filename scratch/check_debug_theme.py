import subprocess
import os

chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
html = open('services.html', encoding='utf-8').read()

script_to_inject = """
<script>
  window.addEventListener('DOMContentLoaded', () => {
    const d = document.createElement('div');
    d.id = 'debug-theme-value';
    d.innerText = 'THEME IS: ' + document.documentElement.getAttribute('data-theme') + ' | PREFERS: ' + window.matchMedia('(prefers-color-scheme: dark)').matches;
    document.body.prepend(d);
  });
</script>
"""
idx = html.find('</body>')
test_html = html[:idx] + script_to_inject + html[idx:]
temp_file = os.path.abspath('scratch/test_theme_debug.html')
with open(temp_file, 'w', encoding='utf-8') as f:
    f.write(test_html)

out_img = os.path.abspath('scratch/theme_debug.png')
file_url = f"file:///{temp_file}".replace('\\', '/')

subprocess.run([
    chrome,
    "--headless=new",
    "--disable-gpu",
    "--window-size=1200,400",
    f"--screenshot={out_img}",
    file_url
], check=True)
print("Captured debug")
