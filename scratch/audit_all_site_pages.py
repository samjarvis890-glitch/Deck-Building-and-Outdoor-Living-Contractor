import os
import re

pages = [
    'index.html',
    'home-2.html',
    'about.html',
    'services.html',
    'gallery.html',
    'projects.html',
    'blog.html',
    'faq.html',
    'contact.html'
]

results = []
for p in pages:
    if not os.path.exists(p):
        results.append((p, "MISSING FILE"))
        continue
    with open(p, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # check images
    srcs = re.findall(r'<img\b[^>]*src=["\']([^"\']+)["\']', html)
    missing_imgs = [s for s in set(srcs) if not os.path.exists(s.split('?')[0].split('#')[0])]
    
    # check stylesheets
    hrefs = re.findall(r'<link\b[^>]*href=["\']([^"\']+\.css)["\']', html)
    missing_css = [h for h in set(hrefs) if not os.path.exists(h.split('?')[0].split('#')[0])]
    
    # check scripts
    scripts = re.findall(r'<script\b[^>]*src=["\']([^"\']+\.js)["\']', html)
    missing_js = [s for s in set(scripts) if not os.path.exists(s.split('?')[0].split('#')[0])]
    
    results.append({
        'page': p,
        'imgs': len(srcs),
        'missing_imgs': len(missing_imgs),
        'css': len(hrefs),
        'missing_css': len(missing_css),
        'js': len(scripts),
        'missing_js': len(missing_js)
    })

print(f"{'Page':<15} | {'Imgs':<5} | {'Missing Img':<12} | {'CSS':<4} | {'Missing CSS':<12} | {'JS':<3} | {'Missing JS'}")
print("-" * 75)
for r in results:
    print(f"{r['page']:<15} | {r['imgs']:<5} | {r['missing_imgs']:<12} | {r['css']:<4} | {r['missing_css']:<12} | {r['js']:<3} | {r['missing_js']}")
