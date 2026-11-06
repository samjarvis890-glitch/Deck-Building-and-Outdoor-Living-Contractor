for path in ['services.html', 'projects.html', 'gallery.html']:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    old_script = """  <!-- Anti-Flash Theme & Direction Initializer -->
  <script>
    (function () {
      try {
        const savedTheme = localStorage.getItem('eol_theme');
        if (savedTheme === 'dark' || (!savedTheme && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
          document.documentElement.setAttribute('data-theme', 'dark');
        } else {
          document.documentElement.setAttribute('data-theme', 'light');
        }
        const savedDir = localStorage.getItem('eol_dir');
        if (savedDir === 'rtl') {
          document.documentElement.setAttribute('dir', 'rtl');
        } else {
          document.documentElement.setAttribute('dir', 'ltr');
        }
      } catch (e) {}
    })();
  </script>"""

    new_script = """  <!-- Anti-Flash Theme & Direction Initializer -->
  <script>
    (function () {
      try {
        var savedTheme = localStorage.getItem('eol_theme_preference') || localStorage.getItem('eol_theme');
        if (savedTheme === 'dark' || (!savedTheme && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
          document.documentElement.setAttribute('data-theme', 'dark');
        } else {
          document.documentElement.setAttribute('data-theme', 'light');
        }
        var savedDir = localStorage.getItem('eol_direction_preference') || localStorage.getItem('eol_dir') || 'ltr';
        document.documentElement.setAttribute('dir', savedDir);
      } catch (e) {}
    })();
  </script>"""

    # Normalize newlines for replacement
    content_norm = content.replace('\r\n', '\n')
    old_norm = old_script.replace('\r\n', '\n')
    new_norm = new_script.replace('\r\n', '\n')
    
    if old_norm in content_norm:
        content_norm = content_norm.replace(old_norm, new_norm)
        # Restore CRLF
        content_fixed = content_norm.replace('\n', '\r\n')
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content_fixed)
        print(f"Updated {path}")
    else:
        print(f"Old script pattern not found in {path}")
