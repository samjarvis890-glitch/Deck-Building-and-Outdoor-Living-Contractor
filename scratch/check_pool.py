import glob, os, subprocess

folders = ['index', 'projects', 'about']
cards = []
for folder in folders:
    for img in sorted(glob.glob(f'assets/images/{folder}/*.webp')):
        name = os.path.basename(img)
        cards.append(f"""
        <div style="background:#222; padding:8px; border-radius:6px; border:1px solid #444;">
            <img src="../{img.replace(chr(92), '/')}" style="width:100%; height:150px; object-fit:cover; border-radius:4px; display:block; margin-bottom:4px;">
            <div style="font-weight:bold; font-size:11px; color:#ddd; word-break:break-all;">{folder}/{name}</div>
        </div>
        """)

# Also include the brain generated images
brain_dir = r"C:\Users\Sam John\.gemini\antigravity\brain\aa3393d8-6479-4912-9a44-277395bd13ea"
for f in sorted(glob.glob(os.path.join(brain_dir, "*.jpg"))):
    if not os.path.basename(f).startswith("media_"):
        cards.append(f"""
        <div style="background:#222; padding:8px; border-radius:6px; border:1px solid #444;">
            <img src="file:///{f.replace(chr(92), '/')}" style="width:100%; height:150px; object-fit:cover; border-radius:4px; display:block; margin-bottom:4px;">
            <div style="font-weight:bold; font-size:11px; color:#aaffaa; word-break:break-all;">brain/{os.path.basename(f)}</div>
        </div>
        """)

html = f"""<!DOCTYPE html><html><head><style>body {{ font-family:sans-serif; background:#111; color:#fff; padding:15px; }} .grid {{ display:grid; grid-template-columns:repeat(auto-fill, minmax(200px, 1fr)); gap:10px; }}</style></head>
<body><h2>Available Project Images</h2><div class="grid">{''.join(cards)}</div></body></html>"""

with open('scratch/pool_images.html', 'w', encoding='utf-8') as f:
    f.write(html)

chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
html_abs = os.path.abspath('scratch/pool_images.html').replace('\\', '/')
out_png = os.path.abspath('scratch/pool_images.png')
cmd = [chrome, '--headless=new', '--disable-gpu', '--window-size=1400,2400', f'--screenshot={out_png}', f'file:///{html_abs}']
subprocess.run(cmd, check=True)
print("Pool images screenshot created:", os.path.exists(out_png))
