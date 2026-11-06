import subprocess
import os

js = """
var el = document.querySelector(".blog-hero-h1");
var sheets = document.styleSheets;
var matches = [];
for (var i = 0; i < sheets.length; i++) {
    try {
        var rules = sheets[i].cssRules;
        for (var j = 0; j < rules.length; j++) {
            if (rules[j].selectorText && el.matches(rules[j].selectorText)) {
                matches.push({
                    href: sheets[i].href ? sheets[i].href.split("/").pop() : "inline",
                    selector: rules[j].selectorText,
                    color: rules[j].style.color
                });
            }
        }
    } catch(e) {}
}
console.log("MATCHES:" + JSON.stringify(matches));
"""

with open('blog.html', 'r', encoding='utf-8') as f:
    c = f.read()

injected = c.replace('</body>', f'<script>{js}</script></body>')
with open('temp_test_h1.html', 'w', encoding='utf-8') as f:
    f.write(injected)

path = os.path.abspath('temp_test_h1.html').replace('\\', '/')
cmd = [
    r'C:\Program Files\Google\Chrome\Application\chrome.exe',
    '--headless=new',
    '--disable-gpu',
    '--enable-logging=stderr',
    f'file:///{path}'
]

proc = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
if os.path.exists('temp_test_h1.html'): os.remove('temp_test_h1.html')

for l in (proc.stdout + '\n' + proc.stderr).splitlines():
    if 'MATCHES:' in l:
        print(l.split('MATCHES:')[1])
