import glob
import re

html_files = sorted(glob.glob('*.html'))
for hf in html_files:
    with open(hf, 'r', encoding='utf-8') as f:
        text = f.read()

    # Find header
    h_start = text.find('<header')
    h_end = text.find('</header>') + 9 if h_start != -1 else -1

    # Find drawer (could be backdrop or aside or nav-drawer)
    # Check for drawer backdrop or nav-drawer-overlay
    d_match = re.search(r'(<div class=[\"\'](?:drawer-backdrop|nav-drawer-overlay)[\"\'].*?</aside>)', text, re.DOTALL)
    
    # Find footer
    f_start = text.find('<footer')
    f_end = text.find('</footer>') + 9 if f_start != -1 else -1

    print(f"=== {hf} ===")
    print(f"  Header range: {h_start} to {h_end}")
    print(f"  Drawer found: {bool(d_match)}")
    if d_match:
        print(f"  Drawer length: {len(d_match.group(1))}")
    print(f"  Footer range: {f_start} to {f_end}")
    print()
