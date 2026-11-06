import glob, os, subprocess

folder = 'home2'
images = sorted(glob.glob(f'assets/images/{folder}/*.webp'))
cards = []
for img in images:
    name = os.path.basename(img)
    cards.append(f"""
    <div style="background:#2a2a2a; padding:10px; border-radius:6px; border:1px solid #444;">
        <img src="../{img.replace(chr(92), '/')}" style="width:100%; height:160px; object-fit:cover; border-radius:4px; display:block; margin-bottom:6px;">
        <div style="font-weight:bold; font-size:12px; color:#e0e0e0; word-break:break-all;">{name}</div>
    </div>
    """)
html = f"""<!DOCTYPE html>
<html><head><style>body {{ font-family:sans-serif; background:#1a1a1a; color:#fff; padding:20px; }} .grid {{ display:grid; grid-template-columns:repeat(auto-fill, minmax(220px, 1fr)); gap:15px; }}</style></head>
<body><h2>{folder} ({len(images)} images)</h2><div class="grid">{''.join(cards)}</div></body></html>"""
with open(f'scratch/audit_{folder}.html', 'w') as f:
    f.write(html)

out_png = os.path.abspath(f'scratch/audit_{folder}.png')
html_abs = os.path.abspath(f'scratch/audit_{folder}.html').replace('\\', '/')
cmd = [r'C:\Program Files\Google\Chrome\Application\chrome.exe', '--headless=new', '--disable-gpu', '--window-size=1400,1200', f'--screenshot={out_png}', f'file:///{html_abs}']
subprocess.run(cmd, check=True)
print(f'Rendered {folder} audit screenshot.')
