import subprocess
import os

chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
html_path = os.path.abspath('gallery.html').replace('\\', '/')

# Tablet 820x1180 (iPad Air)
subprocess.run([
    chrome, '--headless=new', '--disable-gpu',
    '--window-size=820,1180',
    f'--screenshot={os.path.abspath("scratch/gallery_tablet_820.png")}',
    f'file:///{html_path}'
], timeout=20)

# Window size 504,844 (Minimum headless Chrome on Windows)
subprocess.run([
    chrome, '--headless=new', '--disable-gpu',
    '--window-size=504,844',
    f'--screenshot={os.path.abspath("scratch/gallery_mobile_504.png")}',
    f'file:///{html_path}'
], timeout=20)

print("Screenshots taken!")
