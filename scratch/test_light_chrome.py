import subprocess
import os

chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
out_img = os.path.abspath("scratch/light_screenshots/services_forced_light.png")
file_url = f"file:///{os.path.abspath('services.html')}".replace('\\', '/')
subprocess.run([
    chrome,
    "--headless=new",
    "--disable-gpu",
    "--force-prefers-color-scheme=light",
    "--window-size=1440,2400",
    f"--screenshot={out_img}",
    file_url
], check=True)
print("Done")
