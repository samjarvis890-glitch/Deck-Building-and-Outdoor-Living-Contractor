import subprocess
import os

chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
cwd = os.getcwd().replace('\\', '/')

with open('faq.html', 'r', encoding='utf-8') as f:
    base_html = f.read()

# 1. Desktop Light (Hero)
out_hero_light = os.path.abspath('scratch/faq_desktop_light.png')
subprocess.run([
    chrome, '--headless=new', '--disable-gpu', '--window-size=1440,900',
    f'--screenshot={out_hero_light}',
    f'file:///{cwd}/faq.html'
], check=True)

# 2. Desktop Dark (Hero)
dark_html = base_html.replace('<html>', '<html data-theme="dark">').replace('<html lang="en">', '<html lang="en" data-theme="dark">')
with open('scratch/faq_temp_dark.html', 'w', encoding='utf-8') as f:
    f.write(dark_html)

out_hero_dark = os.path.abspath('scratch/faq_desktop_dark.png')
subprocess.run([
    chrome, '--headless=new', '--disable-gpu', '--window-size=1440,900',
    f'--screenshot={out_hero_dark}',
    f'file:///{cwd}/scratch/faq_temp_dark.html'
], check=True)

# 3. Section 8 Support (Scroll to #faqSupport)
scroll_support_js = """
<script>
window.addEventListener('load', function() {
    var el = document.getElementById('faqSupport');
    if (el) el.scrollIntoView();
});
</script>
"""
support_light_html = base_html.replace('</body>', f'{scroll_support_js}</body>')
with open('scratch/faq_temp_support_light.html', 'w', encoding='utf-8') as f:
    f.write(support_light_html)

out_support_light = os.path.abspath('scratch/faq_support_light.png')
subprocess.run([
    chrome, '--headless=new', '--disable-gpu', '--window-size=1440,900',
    f'--screenshot={out_support_light}',
    f'file:///{cwd}/scratch/faq_temp_support_light.html'
], check=True)

# 4. Section 9 Final CTA (Scroll to #finalCta in Light and Dark)
scroll_cta_js = """
<script>
window.addEventListener('load', function() {
    var el = document.getElementById('finalCta');
    if (el) el.scrollIntoView();
});
</script>
"""
cta_light_html = base_html.replace('</body>', f'{scroll_cta_js}</body>')
with open('scratch/faq_temp_cta_light.html', 'w', encoding='utf-8') as f:
    f.write(cta_light_html)

out_cta_light = os.path.abspath('scratch/faq_final_cta_light.png')
subprocess.run([
    chrome, '--headless=new', '--disable-gpu', '--window-size=1440,800',
    f'--screenshot={out_cta_light}',
    f'file:///{cwd}/scratch/faq_temp_cta_light.html'
], check=True)

cta_dark_html = dark_html.replace('</body>', f'{scroll_cta_js}</body>')
with open('scratch/faq_temp_cta_dark.html', 'w', encoding='utf-8') as f:
    f.write(cta_dark_html)

out_cta_dark = os.path.abspath('scratch/faq_final_cta_dark.png')
subprocess.run([
    chrome, '--headless=new', '--disable-gpu', '--window-size=1440,800',
    f'--screenshot={out_cta_dark}',
    f'file:///{cwd}/scratch/faq_temp_cta_dark.html'
], check=True)

# 5. Tablet (820x1180)
out_tablet = os.path.abspath('scratch/faq_tablet_820.png')
subprocess.run([
    chrome, '--headless=new', '--disable-gpu', '--window-size=820,1180',
    f'--screenshot={out_tablet}',
    f'file:///{cwd}/faq.html'
], check=True)

# 6. Mobile (504x844)
out_mobile = os.path.abspath('scratch/faq_mobile_504.png')
subprocess.run([
    chrome, '--headless=new', '--disable-gpu', '--window-size=504,844',
    f'--screenshot={out_mobile}',
    f'file:///{cwd}/faq.html'
], check=True)

print("All FAQ screenshots captured successfully!")
