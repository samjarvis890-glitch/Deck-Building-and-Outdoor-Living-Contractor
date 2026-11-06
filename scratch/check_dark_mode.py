import glob
import re

for f in sorted(glob.glob('assets/css/*.css')):
    content = open(f, encoding='utf-8').read()
    rules = re.findall(r'\[data-theme=["\']?dark["\']?\]', content)
    print(f'{f}: {len(rules)} occurrences of dark theme')
