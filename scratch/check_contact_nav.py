with open('contact.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
print("Desktop nav Contact:")
m = re.findall(r'<a[^>]+href="contact\.html"[^>]*>.*?</a>', text, re.DOTALL)
for item in m:
    print(" ", item.replace('\n', ' '))
