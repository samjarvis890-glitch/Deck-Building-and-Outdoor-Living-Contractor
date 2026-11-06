import subprocess
import os

chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
html = os.path.abspath('about.html').replace('\\', '/')

script_find_overflow = """
const docWidth = document.documentElement.offsetWidth;
const elements = document.querySelectorAll('*');
const overflowers = [];
for (const el of elements) {
    const rect = el.getBoundingClientRect();
    if (rect.right > docWidth + 1) {
        overflowers.push({
            tag: el.tagName,
            cls: el.className,
            id: el.id,
            right: rect.right,
            width: rect.width
        });
    }
}
console.log('DOC WIDTH:', docWidth);
console.log('OVERFLOWERS:', JSON.stringify(overflowers.slice(0, 10)));
"""

with open('scratch/find_overflow.js', 'w') as f:
    f.write(script_find_overflow)

# We can run headless chrome with remote debugging or a quick script
print("Check script created")
