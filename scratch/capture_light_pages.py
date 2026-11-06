import subprocess
import os
import re

chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
cwd = os.getcwd()

pages = [
    "services.html",
    "projects.html",
    "gallery.html",
    "about.html",
    "index.html"
]

for p in pages:
    base = os.path.splitext(p)[0]
    html_content = open(p, encoding='utf-8').read()
    
    # Force light mode on html tag and in scripts
    light_html = re.sub(r'data-theme=["\']dark["\']', 'data-theme="light"', html_content)
    light_html = light_html.replace(
        "document.documentElement.setAttribute('data-theme', 'dark');",
        "document.documentElement.setAttribute('data-theme', 'light');"
    )
    light_html = light_html.replace(
        "const initialTheme = savedTheme ? savedTheme : (prefersDark ? 'dark' : 'light');",
        "const initialTheme = 'light';"
    )
    
    temp_path = os.path.abspath(f"_temp_light_{p}")
    with open(temp_path, "w", encoding='utf-8') as f:
        f.write(light_html)
    
    out_img = os.path.abspath(f"scratch/light_screenshots/{base}_true_light.png")
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
    print(f"Captured true light: {base}_true_light.png")
