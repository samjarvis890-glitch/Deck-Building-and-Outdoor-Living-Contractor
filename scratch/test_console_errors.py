import subprocess
import os

chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
cwd = os.getcwd()
file_url = f"file:///{cwd}/blog.html".replace('\\', '/')

# Run chrome with --enable-logging and console output
cmd = [
    chrome,
    "--headless=new",
    "--disable-gpu",
    "--dump-dom",
    file_url
]

result = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='ignore')
print(f"DOM output length: {len(result.stdout)}")
if "Uncaught" in result.stderr or "SyntaxError" in result.stderr:
    print(f"ERRORS FOUND in stderr: {result.stderr}")
else:
    print("NO console syntax errors or unhandled exceptions detected in headless run!")
