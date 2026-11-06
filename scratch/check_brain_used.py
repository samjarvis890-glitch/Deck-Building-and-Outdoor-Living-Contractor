import os, hashlib

existing_hashes = {}
for root, dirs, files in os.walk('assets/images'):
    for f in files:
        if f.lower().endswith(('.webp', '.jpg', '.jpeg', '.png')):
            p = os.path.join(root, f).replace('\\', '/')
            with open(p, 'rb') as fp:
                existing_hashes[hashlib.md5(fp.read()).hexdigest()] = p

brain_dir = r'C:\Users\Sam John\.gemini\antigravity\brain\aa3393d8-6479-4912-9a44-277395bd13ea'
for f in os.listdir(brain_dir):
    if f.endswith('.jpg') and not f.startswith('.'):
        p = os.path.join(brain_dir, f)
        with open(p, 'rb') as fp:
            h = hashlib.md5(fp.read()).hexdigest()
        if h in existing_hashes:
            print(f"Brain image {f} already used in {existing_hashes[h]}")
        else:
            print(f"Brain image {f} is UNUSED and AVAILABLE!")
