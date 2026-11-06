import subprocess
import os
from PIL import Image

chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
html_path = os.path.abspath('gallery.html').replace('\\', '/')

# 1. Desktop Standard 1440x900 viewport (Hero view)
subprocess.run([
    chrome, '--headless=new', '--disable-gpu',
    '--window-size=1440,900',
    f'--screenshot={os.path.abspath("scratch/gallery_desktop_hero.png")}',
    f'file:///{html_path}'
], timeout=20)

# 2. Desktop Full Page (to check entire page layout now that hero is clamped)
# Let's check with window height 900
subprocess.run([
    chrome, '--headless=new', '--disable-gpu',
    '--window-size=1440,900',
    '--hide-scrollbars',
    f'--screenshot={os.path.abspath("scratch/gallery_desktop_above_fold.png")}',
    f'file:///{html_path}'
], timeout=20)

# 3. Check Section 8 CTA in Light & Dark Mode
# We can create a test html targeting the CTA section with #gallery-final-cta
subprocess.run([
    chrome, '--headless=new', '--disable-gpu',
    '--window-size=1440,800',
    f'--screenshot={os.path.abspath("scratch/gallery_cta_view_light.png")}',
    f'file:///{html_path}#gallery-final-cta'
], timeout=20)

# 4. Mobile 390x844
subprocess.run([
    chrome, '--headless=new', '--disable-gpu',
    '--window-size=390,844',
    f'--screenshot={os.path.abspath("scratch/gallery_mobile_view.png")}',
    f'file:///{html_path}'
], timeout=20)

print("Screenshots taken!")
