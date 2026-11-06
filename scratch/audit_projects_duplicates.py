import os
import hashlib
from PIL import Image

def get_hash(path):
    with open(path, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()

proj_dir = 'assets/images/projects'
proj_files = [f for f in os.listdir(proj_dir) if f.endswith('.webp')]

all_other_files = {}
for folder in ['index', 'about', 'services', 'gallery']:
    fdir = os.path.join('assets/images', folder)
    if os.path.exists(fdir):
        for f in os.listdir(fdir):
            if f.endswith('.webp') or f.endswith('.jpg') or f.endswith('.png'):
                fp = os.path.join(fdir, f)
                h = get_hash(fp)
                all_other_files[h] = fp

print("=== CHECKING PROJECTS IMAGES ===")
for pf in sorted(proj_files):
    pfp = os.path.join(proj_dir, pf)
    ph = get_hash(pfp)
    size_kb = os.path.getsize(pfp) / 1024
    im = Image.open(pfp)
    match = all_other_files.get(ph)
    if match:
        print(f"DUPLICATE: {pf:<35} ({im.size[0]}x{im.size[1]}, {size_kb:.1f}KB) == DUPLICATE OF {match}")
    else:
        print(f"UNIQUE:    {pf:<35} ({im.size[0]}x{im.size[1]}, {size_kb:.1f}KB)")
