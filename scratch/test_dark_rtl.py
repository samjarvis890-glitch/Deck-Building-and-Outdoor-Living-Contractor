import subprocess
import os

chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
cwd = os.getcwd()

# Create a temporary dark mode HTML for visual check
with open("services.html", "r", encoding="utf-8") as f:
    html = f.read()

dark_html = html.replace('data-theme="light"', 'data-theme="dark"')
with open("scratch/services_dark_temp.html", "w", encoding="utf-8") as f:
    f.write(dark_html)

rtl_html = html.replace('dir="ltr"', 'dir="rtl"')
with open("scratch/services_rtl_temp.html", "w", encoding="utf-8") as f:
    f.write(rtl_html)

tests = [
    ("scratch/services_dark_temp.html", "scratch/services_dark.png", 1440, 900),
    ("scratch/services_rtl_temp.html", "scratch/services_rtl.png", 1440, 900)
]

for src, out_rel, w, h in tests:
    file_url = f"file:///{os.path.abspath(src)}".replace('\\', '/')
    out_png = os.path.abspath(out_rel)
    cmd = [
        chrome,
        "--headless=new",
        "--disable-gpu",
        f"--window-size={w},{h}",
        f"--screenshot={out_png}",
        file_url
    ]
    subprocess.run(cmd, check=True)
    print(f"Captured {out_rel}: exists={os.path.exists(out_png)}")

# Remove temp files
os.remove("scratch/services_dark_temp.html")
os.remove("scratch/services_rtl_temp.html")
print("Temp test files cleaned up.")
