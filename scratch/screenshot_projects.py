import subprocess
import os

chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
cwd = os.getcwd()
file_url = f"file:///{cwd}/projects.html".replace('\\', '/')

screens = [
    ("desktop", 1440, 900),
    ("tablet", 820, 1180),
    ("mobile", 375, 812)
]

for name, w, h in screens:
    out_png = os.path.abspath(f"scratch/projects_{name}.png")
    cmd = [
        chrome,
        "--headless=new",
        "--disable-gpu",
        f"--window-size={w},{h}",
        f"--screenshot={out_png}",
        file_url
    ]
    subprocess.run(cmd, check=True)
    print(f"Captured {name}: {out_png} exists: {os.path.exists(out_png)}")

# Dark and RTL tests
with open("projects.html", "r", encoding="utf-8") as f:
    html = f.read()

dark_html = html.replace('data-theme="light"', 'data-theme="dark"')
with open("scratch/projects_dark_temp.html", "w", encoding="utf-8") as f:
    f.write(dark_html)

rtl_html = html.replace('dir="ltr"', 'dir="rtl"')
with open("scratch/projects_rtl_temp.html", "w", encoding="utf-8") as f:
    f.write(rtl_html)

tests = [
    ("scratch/projects_dark_temp.html", "scratch/projects_dark.png", 1440, 900),
    ("scratch/projects_rtl_temp.html", "scratch/projects_rtl.png", 1440, 900)
]

for src, out_rel, w, h in tests:
    src_url = f"file:///{os.path.abspath(src)}".replace('\\', '/')
    out_png = os.path.abspath(out_rel)
    cmd = [
        chrome,
        "--headless=new",
        "--disable-gpu",
        f"--window-size={w},{h}",
        f"--screenshot={out_png}",
        src_url
    ]
    subprocess.run(cmd, check=True)
    print(f"Captured {out_rel}: exists={os.path.exists(out_png)}")

os.remove("scratch/projects_dark_temp.html")
os.remove("scratch/projects_rtl_temp.html")
print("Projects screenshot verification completed!")
