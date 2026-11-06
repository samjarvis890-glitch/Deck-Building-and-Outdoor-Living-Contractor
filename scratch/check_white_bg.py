import glob
import re

css_files = sorted(glob.glob('assets/css/*.css'))

for f in css_files:
    content = open(f, encoding='utf-8').read()
    # Check if there are any hardcoded background: #fff or #ffffff or white without dark mode override
    white_bg = re.findall(r'([^{}]+)\{[^{}]*background(?:-color)?:\s*(?:#fff\b|#ffffff\b|white\b)[^{}]*\}', content, re.IGNORECASE)
    if white_bg:
        print(f"=== {f} has white background in: ===")
        for s in white_bg:
            s_clean = s.strip().replace('\n', ' ')
            if '[data-theme="dark"]' not in s_clean:
                print("  ", s_clean)
