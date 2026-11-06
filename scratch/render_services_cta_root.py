import subprocess
import os

chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

with open('services.html', 'r', encoding='utf-8') as f:
    content = f.read()

cta_snippet = content[content.find('<section class="services-final-cta-section"'):content.find('</section>', content.find('<section class="services-final-cta-section"'))+10]

# Wrap in full head from services.html so all styles, fonts, and Lucide icons load
head_end = content.find('</head>')
full_head = content[:head_end]

test_html_light = f"""{full_head}
</head>
<body style="margin: 0; padding: 0;">
{cta_snippet}
</body>
</html>
"""

test_html_dark = f"""{full_head.replace('<html lang=\"en\"', '<html lang=\"en\" data-theme=\"dark\"')}
</head>
<body style="margin: 0; padding: 0;">
{cta_snippet}
</body>
</html>
"""

with open('temp_cta_light.html', 'w', encoding='utf-8') as f:
    f.write(test_html_light)

with open('temp_cta_dark.html', 'w', encoding='utf-8') as f:
    f.write(test_html_dark)

out_light = os.path.abspath('scratch/cta_light_exact.png')
out_dark = os.path.abspath('scratch/cta_dark_exact.png')

subprocess.run([
    chrome, '--headless=new', '--disable-gpu', '--window-size=1400,650',
    f'--screenshot={out_light}',
    'file:///' + os.path.abspath('temp_cta_light.html').replace('\\', '/')
], check=True)

subprocess.run([
    chrome, '--headless=new', '--disable-gpu', '--window-size=1400,650',
    f'--screenshot={out_dark}',
    'file:///' + os.path.abspath('temp_cta_dark.html').replace('\\', '/')
], check=True)

if os.path.exists('temp_cta_light.html'): os.remove('temp_cta_light.html')
if os.path.exists('temp_cta_dark.html'): os.remove('temp_cta_dark.html')

print("Captured correctly from root")
