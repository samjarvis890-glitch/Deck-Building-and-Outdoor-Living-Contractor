import subprocess
import os

chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

# Let's create an isolated test html file that has services.html but focuses on the CTA or crops to it
with open('services.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Create a small standalone page with the CTA section only so Chrome takes a direct screenshot of it
cta_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <link rel="stylesheet" href="assets/css/style.css">
  <link rel="stylesheet" href="assets/css/theme.css">
  <link rel="stylesheet" href="assets/css/services.css">
  <style>body { margin: 0; padding: 0; }</style>
</head>
<body>
""" + content[content.find('<section class="services-final-cta-section"'):content.find('</section>', content.find('<section class="services-final-cta-section"'))+10] + """
</body>
</html>
"""

with open('scratch/cta_light.html', 'w', encoding='utf-8') as f:
    f.write(cta_html)

with open('scratch/cta_dark.html', 'w', encoding='utf-8') as f:
    f.write(cta_html.replace('<html lang="en">', '<html lang="en" data-theme="dark">'))

out_light = os.path.abspath('scratch/cta_light.png')
out_dark = os.path.abspath('scratch/cta_dark.png')

subprocess.run([
    chrome, '--headless=new', '--disable-gpu', '--window-size=1400,600',
    f'--screenshot={out_light}',
    'file:///' + os.path.abspath('scratch/cta_light.html').replace('\\', '/')
], check=True)

subprocess.run([
    chrome, '--headless=new', '--disable-gpu', '--window-size=1400,600',
    f'--screenshot={out_dark}',
    'file:///' + os.path.abspath('scratch/cta_dark.html').replace('\\', '/')
], check=True)

print("Screenshots taken")
