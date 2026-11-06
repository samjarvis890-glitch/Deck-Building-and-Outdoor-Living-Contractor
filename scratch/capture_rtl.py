import subprocess
import os

chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

# RTL test
with open('gallery.html', 'r', encoding='utf-8') as f:
    rtl_html = f.read().replace('dir="ltr"', 'dir="rtl"')
with open('temp_gallery_rtl.html', 'w', encoding='utf-8') as f:
    f.write(rtl_html)

out_rtl = os.path.abspath('scratch/gallery_rtl_verified.png')
subprocess.run([
    chrome, '--headless=new', '--disable-gpu',
    '--window-size=1440,900',
    f'--screenshot={out_rtl}',
    f'file:///{os.path.abspath("temp_gallery_rtl.html").replace(chr(92), "/")}'
], timeout=20)

if os.path.exists('temp_gallery_rtl.html'):
    os.remove('temp_gallery_rtl.html')

print("RTL screenshot taken!")
