import urllib.request
import re

query = 'site:unsplash.com/photos "deck" "pergola" "backyard"'
url = f'https://html.duckduckgo.com/html/?q={urllib.parse.quote(query)}'

req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
try:
    with urllib.request.urlopen(req, timeout=10) as r:
        html = r.read().decode('utf-8')
    # look for unsplash photo links
    links = re.findall(r'unsplash\.com/photos/([a-zA-Z0-9_\-]+)', html)
    print("Found Unsplash photo slugs:", len(links))
    for l in set(links):
        print("Slug:", l)
except Exception as e:
    print("Search error:", e)
