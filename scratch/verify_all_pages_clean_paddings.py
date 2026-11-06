import subprocess, json, os

chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
pages = [
    'index.html', 'home-2.html', 'about.html', 'services.html',
    'gallery.html', 'projects.html', 'blog.html', 'faq.html', 'contact.html'
]

widths = [1440, 820, 504, 375]

results = []
for p in pages:
    page_res = {'page': p, 'widths': {}}
    for w in widths:
        # Check overflow using headless chrome
        js_cmd = (
            "console.log(JSON.stringify({"
            "innerWidth: window.innerWidth,"
            "docScrollWidth: document.documentElement.scrollWidth,"
            "bodyScrollWidth: document.body.scrollWidth,"
            "overflow: Math.max(document.documentElement.scrollWidth, document.body.scrollWidth) > window.innerWidth + 1"
            "}))"
        )
        
        # Simple test script
        test_script = f"""
const fs = require('fs');
// or use chrome via node or python
"""
        pass

print("Script template ready")
