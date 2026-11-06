import subprocess
import os
import re

chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
cwd = os.getcwd()

pages = [
    "about.html",
    "projects.html",
    "gallery.html",
    "home-2.html",
    "index.html",
    "blog.html",
    "faq.html",
    "contact.html"
]

for p in pages:
    base = os.path.splitext(p)[0]
    html_content = open(p, encoding='utf-8').read()
    dark_html = re.sub(r'data-theme=["\']light["\']', 'data-theme="dark"', html_content)
    dark_html = dark_html.replace("savedTheme === 'dark'", "true || savedTheme === 'dark'")
    
    temp_path = os.path.abspath(f"_temp_dark_{p}")
    with open(temp_path, "w", encoding='utf-8') as f:
        f.write(dark_html)
    
    out_img = os.path.abspath(f"scratch/dark_screenshots/{base}_full_dark.png")
    file_url = f"file:///{temp_path}".replace('\\', '/')
    
    subprocess.run([
        chrome,
        "--headless=new",
        "--disable-gpu",
        "--window-size=1440,5000",
        f"--screenshot={out_img}",
        file_url
    ], check=True)
    if os.path.exists(temp_path):
        os.remove(temp_path)
    print(f"Captured full: {base}_full_dark.png")
