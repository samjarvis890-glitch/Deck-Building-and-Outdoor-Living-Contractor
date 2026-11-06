import subprocess
import os
from PIL import Image

chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
html = os.path.abspath('about.html').replace('\\', '/')
full_png = os.path.abspath('scratch/about_tall.png')

cmd = [
    chrome,
    '--headless=new',
    '--disable-gpu',
    '--window-size=1440,5200',
    f'--screenshot={full_png}',
    f'file:///{html}'
]
subprocess.run(cmd, check=True)
print("Tall screenshot captured:", os.path.exists(full_png))

im = Image.open(full_png)
print("Dimensions:", im.size)

# Crop hero section (around y=300 to y=1400)
hero_crop = im.crop((0, 200, 1440, 1300))
hero_crop.save('scratch/section_hero_view.png')

# Crop philosophy section (around y=1300 to y=2200)
philosophy_crop = im.crop((0, 1200, 1440, 2100))
philosophy_crop.save('scratch/section_philosophy_view.png')

# Crop lifestyle section (around y=2100 to y=3100)
lifestyle_crop = im.crop((0, 2000, 1440, 3100))
lifestyle_crop.save('scratch/section_lifestyle_view.png')

print("Saved section crops successfully!")
