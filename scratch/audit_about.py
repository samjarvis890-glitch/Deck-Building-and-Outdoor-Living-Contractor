import glob
import os
import subprocess

images = sorted(glob.glob('assets/images/about/*.webp'))
cards = []
for img in images:
    name = os.path.basename(img)
    cards.append(f"""
    <div style="background:#2a2a2a; padding:12px; border-radius:8px; border:1px solid #444;">
        <img src="../{img.replace(chr(92), '/')}" style="width:100%; height:220px; object-fit:cover; border-radius:6px; display:block; margin-bottom:8px;">
        <div style="font-weight:bold; font-size:14px; color:#e0e0e0;">{name}</div>
        <div style="font-size:12px; color:#aaa; margin-top:4px;">Size: {os.path.getsize(img)//1024} KB</div>
    </div>
    """)

html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>About Images Audit - Updated</title>
<style>
body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #181818; color: #fff; padding: 30px; margin: 0; }}
.grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 20px; }}
</style>
</head>
<body>
<h1>Updated About Page Images Audit ({len(images)} images)</h1>
<div class="grid">
{''.join(cards)}
</div>
</body>
</html>
"""

with open('scratch/audit_about.html', 'w') as f:
    f.write(html)

chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
html_abs = os.path.abspath('scratch/audit_about.html').replace('\\', '/')
out_png = os.path.abspath('scratch/audit_about.png')
cmd = [chrome, '--headless=new', '--disable-gpu', '--window-size=1440,2200', f'--screenshot={out_png}', f'file:///{html_abs}']
subprocess.run(cmd, check=True)
print("Screenshot recreated:", os.path.exists(out_png))
