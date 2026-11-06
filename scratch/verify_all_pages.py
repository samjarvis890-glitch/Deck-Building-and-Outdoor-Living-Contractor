import subprocess
import os

chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
cwd = os.getcwd()

pages_to_verify = [
    ("index", "index.html"),
    ("home2", "home2.html"),
    ("about", "about.html"),
    ("services", "services.html"),
    ("projects", "projects.html"),
    ("gallery", "gallery.html")
]

for name, filename in pages_to_verify:
    file_url = f"file:///{cwd}/{filename}".replace('\\', '/')
    out_desktop = os.path.abspath(f"scratch/verify_{name}_desktop.png")
    out_mobile = os.path.abspath(f"scratch/verify_{name}_mobile.png")
    
    # Desktop
    subprocess.run([
        chrome,
        "--headless=new",
        "--disable-gpu",
        "--window-size=1440,900",
        f"--screenshot={out_desktop}",
        file_url
    ], check=True)
    
    # Mobile
    subprocess.run([
        chrome,
        "--headless=new",
        "--disable-gpu",
        "--window-size=375,812",
        f"--screenshot={out_mobile}",
        file_url
    ], check=True)
    
    print(f"Verified {filename}: Desktop ({os.path.exists(out_desktop)}), Mobile ({os.path.exists(out_mobile)})")

print("\nAll verification screenshots generated successfully!")
