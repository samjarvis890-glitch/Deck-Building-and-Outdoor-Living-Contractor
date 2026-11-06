import subprocess
import os

html_content = '''<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <link rel="stylesheet" href="vendor/bootstrap/css/bootstrap.min.css">
  <link rel="stylesheet" href="vendor/tailwind/tailwind.css">
  <link rel="stylesheet" href="assets/css/theme.css">
  <link rel="stylesheet" href="assets/css/navbar.css">
  <link rel="stylesheet" href="assets/css/style.css">
  <style>
    /* Simulate hover on the About link */
    #test-hover-link {
      color: #FFFFFF !important;
      background-color: rgba(145, 181, 154, 0.18) !important;
    }
  </style>
</head>
<body style="background-color: var(--bg-primary); min-height: 200px;">
  <header class="site-header is-scrolled" style="position: static;">
    <div class="nav-container">
      <a href="index.html" class="navbar-brand-link">
        <img src="assets/images/brand/logo-white.svg" alt="Evergreen" class="brand-logo-img">
      </a>
      <nav class="navbar-desktop-nav">
        <div class="nav-item-wrapper"><a href="index.html" class="nav-link-item"><span>Home</span></a></div>
        <div class="nav-item-wrapper"><a href="about.html" class="nav-link-item" id="test-hover-link">About (Simulated Hover)</a></div>
        <div class="nav-item-wrapper"><a href="services.html" class="nav-link-item active">Services (Active)</a></div>
        <div class="nav-item-wrapper"><a href="gallery.html" class="nav-link-item">Gallery</a></div>
        <div class="nav-item-wrapper"><a href="projects.html" class="nav-link-item">Projects</a></div>
      </nav>
      <div class="navbar-actions">
        <button class="nav-icon-btn"><span class="dir-badge-text">LTR</span></button>
        <button class="nav-icon-btn"><span class="theme-icon-wrap">☀️</span></button>
        <a href="#" class="nav-cta-btn nav-cta-desktop">Book Consultation</a>
      </div>
    </div>
  </header>
</body>
</html>'''

temp_file = "_test_navbar_hover.html"
with open(temp_file, "w", encoding="utf-8") as f:
    f.write(html_content)

chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
out_img = os.path.abspath("scratch/dark_screenshots/navbar_hover_verification.png")
file_url = f"file:///{os.path.abspath(temp_file)}".replace('\\', '/')

subprocess.run([
    chrome,
    "--headless=new",
    "--disable-gpu",
    "--window-size=1440,300",
    f"--screenshot={out_img}",
    file_url
], check=True)

if os.path.exists(temp_file):
    os.remove(temp_file)
print("Navbar hover test generated")
