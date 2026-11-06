import re
import os
import subprocess

with open('gallery.html', 'r', encoding='utf-8') as f:
    text = f.read()

imgs = re.findall(r'src="(assets/images/gallery/[^"]+)"', text)
unique = sorted(set(imgs))

cards = []
for rel in unique:
    name = os.path.basename(rel)
    abs_path = os.path.abspath(rel)
    exists = os.path.exists(abs_path)
    size_kb = os.path.getsize(abs_path) // 1024 if exists else 0
    cards.append(f"""
    <div style="background:#222; padding:10px; border-radius:6px; border:1px solid #444;">
        <img src="../{rel}" style="width:100%; height:160px; object-fit:cover; border-radius:4px; display:block; margin-bottom:6px;">
        <div style="font-weight:bold; font-size:12px; color:#ddd; word-break:break-all;">{name}</div>
        <div style="font-size:11px; color:#888;">{size_kb} KB</div>
    </div>
    """)

html = f"""<!DOCTYPE html><html><head><style>body {{ font-family:sans-serif; background:#111; color:#fff; padding:20px; }} .grid {{ display:grid; grid-template-columns:repeat(auto-fill, minmax(220px, 1fr)); gap:15px; }}</style></head>
<body><h2>Gallery HTML Referencing Images ({len(unique)} files)</h2><div class="grid">{''.join(cards)}</div></body></html>"""

with open('scratch/audit_gallery_html_imgs.html', 'w', encoding='utf-8') as f:
    f.write(html)

chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
html_abs = os.path.abspath('scratch/audit_gallery_html_imgs.html').replace('\\', '/')
out_png = os.path.abspath('scratch/audit_gallery_html_imgs.png')
cmd = [chrome, '--headless=new', '--disable-gpu', '--window-size=1400,2800', f'--screenshot={out_png}', f'file:///{html_abs}']
subprocess.run(cmd, check=True)
print("Screenshot created:", os.path.exists(out_png))
