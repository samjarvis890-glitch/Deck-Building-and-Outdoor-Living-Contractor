import subprocess
import os

chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
html_path = os.path.abspath('gallery.html').replace('\\', '/')
out_mobile = os.path.abspath('scratch/gallery_iphone_mobile.png')

subprocess.run([
    chrome,
    '--headless=new',
    '--disable-gpu',
    '--window-size=390,844',
    '--use-mobile-user-agent',
    '--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
    f'--screenshot={out_mobile}',
    f'file:///{html_path}'
], timeout=20)

print("Saved scratch/gallery_iphone_mobile.png")
