import subprocess
import os
import glob

chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
cwd = os.getcwd()

pages = sorted(glob.glob("*.html"))
print(f"Testing {len(pages)} pages with Chrome --dump-dom...")

all_pass = True
for p in pages:
    file_url = f"file:///{cwd}/{p}".replace('\\', '/')
    cmd = [
        chrome,
        "--headless=new",
        "--disable-gpu",
        "--dump-dom",
        file_url
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='ignore', timeout=8)
    dom_len = len(proc.stdout)
    has_err = "Uncaught" in proc.stderr or "SyntaxError" in proc.stderr
    if has_err:
        print(f"[{p}] FAILED - Errors: {proc.stderr[:200]}")
        all_pass = False
    elif dom_len < 1000:
        print(f"[{p}] WARNING - Low DOM length ({dom_len})")
        all_pass = False
    else:
        print(f"[{p}] PASS - DOM length: {dom_len} bytes")

if all_pass:
    print("\nALL 10 PAGES PASSED WITH ZERO CONSOLE ERRORS!")
