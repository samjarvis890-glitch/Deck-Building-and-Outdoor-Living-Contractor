import glob
import re

html_files = sorted(glob.glob('*.html'))
for hf in html_files:
    with open(hf, 'r', encoding='utf-8') as f:
        content = f.read()
    
    header_cls = re.findall(r'<header[^>]*class=["\']([^"\']*)["\']', content)
    drawer_cls = re.findall(r'<(?:aside|div)[^>]*class=["\']([^"\']*(?:drawer|panel|menu)[^"\']*)["\']', content)
    footer_cls = re.findall(r'<footer[^>]*class=["\']([^"\']*)["\']', content)
    css_files = re.findall(r'<link[^>]*href=["\']([^"\']*\.css)["\']', content)
    
    # check dropdown in desktop nav for Services
    # Look for Services followed by dropdown
    has_services_dropdown = bool(re.search(r'href=["\']services\.html["\'][^>]*>.*?Services.*?<ul class=["\']nav-dropdown-menu["\']', content, re.DOTALL | re.IGNORECASE) or 
                                 re.search(r'Services\s*<svg[^>]*chevron-down', content, re.IGNORECASE) or
                                 re.search(r'class=["\']nav-dropdown-toggle["\'][^>]*>\s*Services', content, re.IGNORECASE) or
                                 re.search(r'Services\s*<span class=["\']dropdown-caret', content, re.IGNORECASE))
    
    # Also check if mobile drawer has services dropdown
    drawer_services_dropdown = bool(re.search(r'drawer-accordion-btn[^>]*>[\s\S]*?Services', content, re.IGNORECASE) or
                                    re.search(r'drawer-submenu[^>]*>[\s\S]*?Custom Decks', content, re.IGNORECASE))

    print(f"=== {hf} ===")
    print(f"  Header: {header_cls}")
    print(f"  Drawer: {drawer_cls}")
    print(f"  Footer: {footer_cls}")
    print(f"  CSS: {css_files}")
    print(f"  Desktop Services Dropdown: {has_services_dropdown}")
    print(f"  Drawer Services Dropdown: {drawer_services_dropdown}")
    print()

print("--- SCRIPTS AUDIT ---")
for hf in html_files:
    with open(hf, 'r', encoding='utf-8') as f:
        content = f.read()
    scripts = re.findall(r'<script[^>]*src=["\']([^"\']*)["\']', content)
    print(f"{hf}: {scripts}")
