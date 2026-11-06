import re

# 1. Update services.css
with open('assets/css/services.css', 'r', encoding='utf-8') as f:
    services_css = f.read()

# Fix wrapper
services_css = services_css.replace(
    '.services-page-wrapper {\n  background-color: var(--bg-body);',
    '.services-page-wrapper {\n  background-color: var(--bg-primary);'
).replace(
    '.services-page-wrapper {\r\n  background-color: var(--bg-body);',
    '.services-page-wrapper {\r\n  background-color: var(--bg-primary);'
)

# Fix .services-section
services_css = services_css.replace(
    '.services-section {\n  padding: clamp(3.25rem, 5.5vw, 5.5rem) 0;\n  position: relative;\n}',
    '.services-section {\n  padding: clamp(3.25rem, 5.5vw, 5.5rem) 0;\n  position: relative;\n  background-color: var(--bg-primary);\n}'
).replace(
    '.services-section {\r\n  padding: clamp(3.25rem, 5.5vw, 5.5rem) 0;\r\n  position: relative;\r\n}',
    '.services-section {\r\n  padding: clamp(3.25rem, 5.5vw, 5.5rem) 0;\r\n  position: relative;\r\n  background-color: var(--bg-primary);\r\n}'
)

# Add .btn-service-primary dark mode
btn_service_dark = '''
[data-theme="dark"] .btn-service-primary {
  background-color: #91B59A !important;
  border-color: #91B59A !important;
  color: #151D18 !important;
}

[data-theme="dark"] .btn-service-primary:hover {
  background-color: #a5c6ad !important;
  border-color: #a5c6ad !important;
  color: #151D18 !important;
}
'''
if '[data-theme="dark"] .btn-service-primary' not in services_css:
    services_css = services_css.replace('.btn-service-primary:hover {', btn_service_dark + '\n.btn-service-primary:hover {')

# Fix broken syntax at btn-cta-projects
broken_pattern = re.compile(
    r'\.btn-cta-projects:hover\s*\{[^}]*\}\s*border-radius:[^}]*\}\s*\.btn-cta-projects:hover\s*\{[^}]*\}',
    re.DOTALL
)
replacement_btn = '''.btn-cta-projects:hover {
  background-color: #FFFFFF;
  color: #18382C !important;
  border-color: #FFFFFF;
  transform: translateY(-2px);
}

[data-theme="dark"] .btn-cta-consult {
  background-color: #91B59A !important;
  border-color: #91B59A !important;
  color: #151D18 !important;
}

[data-theme="dark"] .btn-cta-consult:hover {
  background-color: #a5c6ad !important;
  border-color: #a5c6ad !important;
  color: #151D18 !important;
}

[data-theme="dark"] .btn-cta-projects:hover {
  background-color: #FFFFFF !important;
  border-color: #FFFFFF !important;
  color: #151D18 !important;
}'''
services_css = broken_pattern.sub(replacement_btn, services_css)

with open('assets/css/services.css', 'w', encoding='utf-8') as f:
    f.write(services_css)
print("Updated services.css")


# 2. Update gallery.css
with open('assets/css/gallery.css', 'r', encoding='utf-8') as f:
    gallery_css = f.read()

gallery_css = gallery_css.replace(
    '.gallery-page-wrapper {\n  background-color: var(--bg-body);',
    '.gallery-page-wrapper {\n  background-color: var(--bg-primary);'
).replace(
    '.gallery-page-wrapper {\r\n  background-color: var(--bg-body);',
    '.gallery-page-wrapper {\r\n  background-color: var(--bg-primary);'
)

gallery_css = gallery_css.replace(
    '.gallery-section {\n  padding: clamp(3.25rem, 5.5vw, 5.5rem) 0;\n  position: relative;\n}',
    '.gallery-section {\n  padding: clamp(3.25rem, 5.5vw, 5.5rem) 0;\n  position: relative;\n  background-color: var(--bg-primary);\n}'
).replace(
    '.gallery-section {\r\n  padding: clamp(3.25rem, 5.5vw, 5.5rem) 0;\r\n  position: relative;\r\n}',
    '.gallery-section {\r\n  padding: clamp(3.25rem, 5.5vw, 5.5rem) 0;\r\n  position: relative;\r\n  background-color: var(--bg-primary);\r\n}'
)

gallery_dark_extra = '''
[data-theme="dark"] .gallery-filter-btn {
  background-color: #243229 !important;
  border-color: #425247 !important;
  color: #F1F4EE !important;
}

[data-theme="dark"] .gallery-filter-btn:hover {
  border-color: #91B59A !important;
  color: #91B59A !important;
}

[data-theme="dark"] .btn-gallery-primary {
  background-color: #91B59A !important;
  border-color: #91B59A !important;
  color: #151D18 !important;
}

[data-theme="dark"] .btn-gallery-primary:hover {
  background-color: #a5c6ad !important;
  border-color: #a5c6ad !important;
  color: #151D18 !important;
}
'''
if '[data-theme="dark"] .gallery-filter-btn {' not in gallery_css:
    gallery_css += '\n' + gallery_dark_extra

with open('assets/css/gallery.css', 'w', encoding='utf-8') as f:
    f.write(gallery_css)
print("Updated gallery.css")


# 3. Update projects.css
with open('assets/css/projects.css', 'r', encoding='utf-8') as f:
    projects_css = f.read()

projects_css = projects_css.replace(
    '.projects-page-wrapper {\n  background-color: var(--bg-body);',
    '.projects-page-wrapper {\n  background-color: var(--bg-primary);'
).replace(
    '.projects-page-wrapper {\r\n  background-color: var(--bg-body);',
    '.projects-page-wrapper {\r\n  background-color: var(--bg-primary);'
)

projects_css = projects_css.replace(
    '.projects-section {\n  padding: clamp(3.25rem, 5.5vw, 5.5rem) 0;\n  position: relative;\n}',
    '.projects-section {\n  padding: clamp(3.25rem, 5.5vw, 5.5rem) 0;\n  position: relative;\n  background-color: var(--bg-primary);\n}'
).replace(
    '.projects-section {\r\n  padding: clamp(3.25rem, 5.5vw, 5.5rem) 0;\r\n  position: relative;\r\n}',
    '.projects-section {\r\n  padding: clamp(3.25rem, 5.5vw, 5.5rem) 0;\r\n  position: relative;\r\n  background-color: var(--bg-primary);\r\n}'
)

projects_dark_extra = '''
[data-theme="dark"] .btn-project-primary {
  background-color: #91B59A !important;
  border-color: #91B59A !important;
  color: #151D18 !important;
}

[data-theme="dark"] .btn-project-primary:hover {
  background-color: #a5c6ad !important;
  border-color: #a5c6ad !important;
  color: #151D18 !important;
}
'''
if '[data-theme="dark"] .btn-project-primary {' not in projects_css:
    projects_css += '\n' + projects_dark_extra

with open('assets/css/projects.css', 'w', encoding='utf-8') as f:
    f.write(projects_css)
print("Updated projects.css")


# 4. Update about.css
with open('assets/css/about.css', 'r', encoding='utf-8') as f:
    about_css = f.read()

about_css = about_css.replace(
    '.about-page-wrapper {\n  background-color: var(--bg-body);',
    '.about-page-wrapper {\n  background-color: var(--bg-primary);'
).replace(
    '.about-page-wrapper {\r\n  background-color: var(--bg-body);',
    '.about-page-wrapper {\r\n  background-color: var(--bg-primary);'
)

about_dark_extra = '''
[data-theme="dark"] .about-btn-primary {
  background-color: #91B59A !important;
  border-color: #91B59A !important;
  color: #151D18 !important;
}

[data-theme="dark"] .about-btn-primary:hover {
  background-color: #a5c6ad !important;
  border-color: #a5c6ad !important;
  color: #151D18 !important;
}
'''
if '[data-theme="dark"] .about-btn-primary {' not in about_css:
    about_css += '\n' + about_dark_extra

with open('assets/css/about.css', 'w', encoding='utf-8') as f:
    f.write(about_css)
print("Updated about.css")
