import os
from PIL import Image

def inspect_folder(folder):
    print(f"=== Inspecting {folder} ===")
    for f in os.listdir(folder):
        p = os.path.join(folder, f)
        if os.path.isfile(p):
            try:
                with Image.open(p) as img:
                    print(f"{f}: {img.size}, {img.format}, {img.mode}")
            except Exception as e:
                print(f"{f}: {e}")

inspect_folder("assets/images/about")
inspect_folder("assets/images/services")
