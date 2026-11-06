import glob
import re

css_files = sorted(glob.glob('assets/css/*.css'))

dark_text_patterns = [
    r'color:\s*var\(--color-charcoal\)',
    r'color:\s*var\(--color-forest\)',
    r'color:\s*var\(--color-deep-forest\)',
    r'color:\s*#292F2A',
    r'color:\s*#18382C',
    r'color:\s*#254B3B',
    r'color:\s*#151D18',
    r'color:\s*#1e3d30',
]

for f in css_files:
    content = open(f, encoding='utf-8').read()
    issues = []
    for pat in dark_text_patterns:
        matches = re.findall(r'([^{}]+)\{[^{}]*' + pat + r'[^{}]*\}', content, re.IGNORECASE)
        for m in matches:
            m_clean = m.strip().replace('\n', ' ')
            if '[data-theme="dark"]' not in m_clean:
                # Check if this file has a [data-theme="dark"] version of this selector
                sel = m_clean.split(',')[-1].strip()
                # simplified check
                if f'[data-theme="dark"] {sel}' not in content and f'[data-theme="dark"]  {sel}' not in content:
                    issues.append((sel, pat))
    if issues:
        print(f"=== {f}: Potential dark text without dark override ({len(issues)}) ===")
        for sel, pat in issues[:15]:
            print(f"   {sel} -> {pat}")
