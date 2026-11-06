import subprocess
import os
import re

chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
cwd = os.getcwd()

pages = [
    "index.html",
    "home-2.html",
    "about.html",
    "services.html",
    "projects.html",
    "gallery.html",
    "blog.html",
    "faq.html",
    "contact.html"
]

os.makedirs("scratch/dark_screenshots", exist_ok=True)

for p in pages:
    base = os.path.splitext(p)[0]
    html_content = open(p, encoding='utf-8').read()
    
    # Replace data-theme="light" with data-theme="dark" and ensure localStorage/antiflash sets dark
    dark_html = re.sub(r'data-theme=["\']light["\']', 'data-theme="dark"', html_content)
    # Ensure anti-flash defaults to dark
    dark_html = dark_html.replace("savedTheme === 'dark'", "true || savedTheme === 'dark'")
    
    temp_path = os.path.abspath(f"_temp_dark_{p}")
    with open(temp_path, "w", encoding='utf-8') as f:
        f.write(dark_html)
    
    out_img = os.path.abspath(f"scratch/dark_screenshots/{base}_dark.png")
    file_url = f"file:///{temp_path}".replace('\\', '/')
    
    subprocess.run([
        chrome,
        "--headless=new",
        "--disable-gpu",
        "--window-size=1440,2400",
        f"--screenshot={out_img}",
        file_url
    ], check=True)
    if os.path.exists(temp_path):
        os.remove(temp_path)
    print(f"Captured {base}_dark.png")
