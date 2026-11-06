import os
import glob
from PIL import Image

for folder in ['index', 'home2', 'about', 'services', 'gallery', 'projects', 'blog', 'faq', 'contact']:
    path = os.path.join('assets', 'images', folder)
    if os.path.exists(path):
        files = glob.glob(os.path.join(path, '*.webp'))
        total_size = sum(os.path.getsize(f) for f in files)
        avg_size = total_size / len(files) if files else 0
        print(f"Folder '{folder}': {len(files)} webp files, avg size: {avg_size/1024:.1f} KB")
        # Sample one file
        if files:
            sample = files[0]
            print(f"   Sample: {os.path.basename(sample)} ({os.path.getsize(sample)/1024:.1f} KB)")
