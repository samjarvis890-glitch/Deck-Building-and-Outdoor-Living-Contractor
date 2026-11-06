import subprocess
import os

chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
temp_dir = os.path.abspath("scratch/temp_chrome_profile")
os.makedirs(temp_dir, exist_ok=True)

out_img = os.path.abspath("scratch/light_screenshots/services_isolated_light.png")
file_url = f"file:///{os.path.abspath('services.html')}".replace('\\', '/')

subprocess.run([
    chrome,
    "--headless=new",
    "--disable-gpu",
    f"--user-data-dir={temp_dir}",
    "--force-prefers-color-scheme=light",
    "--window-size=1440,2400",
    f"--screenshot={out_img}",
    file_url
], check=True)
print("Done isolated light")
