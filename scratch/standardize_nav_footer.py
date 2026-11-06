import os
import re

PAGES = [
    'index.html',
    'home2.html',
    'home-2.html',
    'about.html',
    'services.html',
    'gallery.html',
    'projects.html',
    'blog.html',
    'faq.html',
    'contact.html'
]

def get_header_html(page_name):
    # Determines active states
    is_home = page_name in ('index.html', 'home2.html', 'home-2.html')
    is_about = page_name == 'about.html'
    is_services = page_name == 'services.html'
    is_gallery = page_name == 'gallery.html'
    is_projects = page_name == 'projects.html'
    is_blog = page_name == 'blog.html'
    is_faq = page_name == 'faq.html'
    is_contact = page_name == 'contact.html'

    # transparent hero pages vs scrolled
    header_cls = "site-header is-transparent" if page_name in ('index.html', 'blog.html', 'faq.html', 'contact.html', 'gallery.html') else "site-header is-scrolled"

    return f'''<header class="{header_cls}" id="siteHeader">
    <div class="nav-container">

      <!-- Brand Logo (Left) -->
      <a href="index.html" class="navbar-brand-link" aria-label="Evergreen Outdoor Living Home">
        <img src="assets/images/brand/logo.svg" alt="Evergreen Outdoor Living Logo" class="brand-logo-img brand-logo-dark">
        <img src="assets/images/brand/logo-white.svg" alt="Evergreen Outdoor Living Logo" class="brand-logo-img brand-logo-white">
      </a>

      <!-- Desktop Navigation Menu (1281px+) -->
      <nav class="navbar-desktop-nav" aria-label="Main Navigation">
        <!-- Home Dropdown -->
        <div class="nav-item-wrapper">
          <a href="index.html" class="nav-link-item{' active' if is_home else ''}" aria-expanded="false" aria-haspopup="true">
            <span>Home</span>
            <i data-lucide="chevron-down" class="dropdown-caret"></i>
          </a>
          <ul class="nav-dropdown-menu">
            <li><a href="index.html" class="dropdown-link-item"><i data-lucide="home"></i> Home 1 (Main)</a></li>
            <li><a href="home-2.html" class="dropdown-link-item"><i data-lucide="layers"></i> Home 2 (Architectural)</a></li>
          </ul>
        </div>

        <!-- About -->
        <div class="nav-item-wrapper">
          <a href="about.html" class="nav-link-item{' active' if is_about else ''}">About</a>
        </div>

        <!-- Services (Direct Link - NO DROPDOWN) -->
        <div class="nav-item-wrapper">
          <a href="services.html" class="nav-link-item{' active' if is_services else ''}">Services</a>
        </div>

        <!-- Gallery -->
        <div class="nav-item-wrapper">
          <a href="gallery.html" class="nav-link-item{' active' if is_gallery else ''}">Gallery</a>
        </div>

        <!-- Projects -->
        <div class="nav-item-wrapper">
          <a href="projects.html" class="nav-link-item{' active' if is_projects else ''}">Projects</a>
        </div>

        <!-- Blog -->
        <div class="nav-item-wrapper">
          <a href="blog.html" class="nav-link-item{' active' if is_blog else ''}">Blog</a>
        </div>

        <!-- FAQ -->
        <div class="nav-item-wrapper">
          <a href="faq.html" class="nav-link-item{' active' if is_faq else ''}">FAQ</a>
        </div>

        <!-- Contact -->
        <div class="nav-item-wrapper">
          <a href="contact.html" class="nav-link-item{' active' if is_contact else ''}">Contact</a>
        </div>
      </nav>

      <!-- Navbar Action Controls (Right) -->
      <div class="navbar-actions">
        <!-- 1. LTR / RTL Direction Toggle Icon -->
        <button type="button" class="nav-icon-btn dir-toggle-btn" aria-label="Toggle Text Direction" title="Toggle Text Direction">
          <span class="dir-badge-text font-bold text-xs" style="font-size: 0.75rem; font-weight: 700;">LTR</span>
        </button>

        <!-- 2. Dark Mode / Light Mode Icon -->
        <button type="button" class="nav-icon-btn theme-toggle-btn" aria-label="Toggle Dark / Light Theme" title="Toggle Theme">
          <span class="theme-icon-wrap">
            <svg xmlns="http://www.w3.org/2000/svg" width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-moon"><path d="M12 3a6 6 0 0 0 9 9 9 9 0 1 1-9-9Z"/></svg>
          </span>
        </button>

        <!-- 3. Desktop BOOK A CONSULTATION CTA Button -->
        <a href="contact.html#consultation" class="nav-cta-btn nav-cta-desktop">
          <span>Book Consultation</span>
          <i data-lucide="arrow-right"></i>
        </a>

        <!-- Hamburger Menu Button (Visible below 1281px on Mobile & Tablet) -->
        <button type="button" class="nav-hamburger-btn" id="navHamburgerBtn" aria-label="Open Navigation Menu" aria-expanded="false">
          <i data-lucide="menu"></i>
        </button>
      </div>

    </div>
  </header>'''

def get_drawer_html(page_name):
    is_home = page_name in ('index.html', 'home2.html', 'home-2.html')
    is_home1 = page_name == 'index.html'
    is_home2 = page_name in ('home2.html', 'home-2.html')
    is_about = page_name == 'about.html'
    is_services = page_name == 'services.html'
    is_gallery = page_name == 'gallery.html'
    is_projects = page_name == 'projects.html'
    is_blog = page_name == 'blog.html'
    is_faq = page_name == 'faq.html'
    is_contact = page_name == 'contact.html'

    return f'''<div class="drawer-backdrop" id="drawerBackdrop"></div>

  <aside class="mobile-drawer" id="mobileDrawer" aria-label="Mobile Navigation Drawer">
    <!-- Drawer Header -->
    <div class="drawer-header">
      <a href="index.html" class="navbar-brand-link" aria-label="Evergreen Outdoor Living Home">
        <img src="assets/images/brand/logo.svg" alt="Evergreen Outdoor Living" class="brand-logo-img brand-logo-dark" style="height: 34px;">
        <img src="assets/images/brand/logo-white.svg" alt="Evergreen Outdoor Living" class="brand-logo-img brand-logo-white" style="height: 34px;">
      </a>
      <button type="button" class="drawer-close-btn" id="drawerCloseBtn" aria-label="Close Navigation Menu">
        <i data-lucide="x"></i>
      </button>
    </div>

    <!-- Drawer Body (All Navigation Items Accessible) -->
    <div class="drawer-body">
      <ul class="drawer-nav-list">
        <!-- Home Accordion -->
        <li class="drawer-nav-item">
          <button type="button" class="drawer-link drawer-dropdown-toggle{' active' if is_home else ''}" data-target="drawerSubHome" aria-expanded="false">
            <span>Home</span>
            <i data-lucide="chevron-down"></i>
          </button>
          <ul class="drawer-submenu" id="drawerSubHome">
            <li><a href="index.html" class="drawer-sublink{' active' if is_home1 else ''}">Home 1 (Main Homepage)</a></li>
            <li><a href="home-2.html" class="drawer-sublink{' active' if is_home2 else ''}">Home 2 (Architectural Showcase)</a></li>
          </ul>
        </li>

        <!-- About -->
        <li class="drawer-nav-item">
          <a href="about.html" class="drawer-link{' active' if is_about else ''}">About</a>
        </li>

        <!-- Services (Direct Link - NO DROPDOWN) -->
        <li class="drawer-nav-item">
          <a href="services.html" class="drawer-link{' active' if is_services else ''}">Services</a>
        </li>

        <!-- Categories -->
        <li class="drawer-nav-item">
          <a href="services.html#categories" class="drawer-link">Categories</a>
        </li>

        <!-- Brands -->
        <li class="drawer-nav-item">
          <a href="services.html#brands" class="drawer-link">Brands</a>
        </li>

        <!-- Deals -->
        <li class="drawer-nav-item">
          <a href="services.html#deals" class="drawer-link">Deals</a>
        </li>

        <!-- Accessories -->
        <li class="drawer-nav-item">
          <a href="services.html#accessories" class="drawer-link">Accessories</a>
        </li>

        <!-- Gallery -->
        <li class="drawer-nav-item">
          <a href="gallery.html" class="drawer-link{' active' if is_gallery else ''}">Gallery</a>
        </li>

        <!-- Projects -->
        <li class="drawer-nav-item">
          <a href="projects.html" class="drawer-link{' active' if is_projects else ''}">Projects</a>
        </li>

        <!-- Blog -->
        <li class="drawer-nav-item">
          <a href="blog.html" class="drawer-link{' active' if is_blog else ''}">Blog</a>
        </li>

        <!-- FAQ -->
        <li class="drawer-nav-item">
          <a href="faq.html" class="drawer-link{' active' if is_faq else ''}">FAQ</a>
        </li>

        <!-- Contact -->
        <li class="drawer-nav-item">
          <a href="contact.html" class="drawer-link{' active' if is_contact else ''}">Contact</a>
        </li>
      </ul>
    </div>

    <!-- Drawer Footer (Controls & Consultation Button) -->
    <div class="drawer-footer">
      <div class="drawer-quick-controls">
        <!-- Dark Mode Toggle Button with Label -->
        <button type="button" class="drawer-control-pill theme-toggle-btn" aria-label="Toggle Dark / Light Theme">
          <span class="theme-icon-wrap">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-moon"><path d="M12 3a6 6 0 0 0 9 9 9 9 0 1 1-9-9Z"/></svg>
          </span>
          <span class="theme-label-text">Dark Mode</span>
        </button>

        <!-- Direction Toggle Button with Label -->
        <button type="button" class="drawer-control-pill dir-toggle-btn" aria-label="Toggle LTR / RTL Direction">
          <i data-lucide="languages"></i>
          <span class="dir-label-text">RTL Mode</span>
        </button>
      </div>

      <!-- Client Login & Consultation CTA Inside Mobile Drawer -->
      <div style="display: flex; flex-direction: column; gap: 0.5rem; width: 100%;">
        <a href="contact.html#consultation" class="drawer-cta-btn">
          <span>Book a Consultation</span>
          <i data-lucide="arrow-right"></i>
        </a>
        <a href="contact.html#login" class="drawer-control-pill" style="padding: 0.75rem; justify-content: center; font-weight: 600;">
          <i data-lucide="lock"></i>
          <span>Client Login</span>
        </a>
      </div>
    </div>
  </aside>'''

def get_footer_html():
    return '''<footer class="site-footer" id="siteFooter" role="contentinfo">
    <div class="footer-container">
      <div class="footer-main-grid">

        <!-- Column 1: Brand -->
        <div class="footer-col-brand">
          <a href="index.html" class="navbar-brand-link" aria-label="Evergreen Outdoor Living Home">
            <img src="assets/images/brand/logo-white.svg" alt="Evergreen Outdoor Living" class="footer-brand-logo">
          </a>
          <div class="footer-brand-tagline">CRAFTED OUTDOOR SPACES. MADE FOR LIVING.</div>
          <p class="footer-brand-desc">
            Bespoke outdoor architecture, custom deck construction and refined pergola environments built to harmonize with nature and elevate your lifestyle.
          </p>
        </div>

        <!-- Column 2: Quick Links (Exactly 6) -->
        <div class="footer-col-links">
          <h4 class="footer-heading">Quick Links</h4>
          <ul class="footer-links-list">
            <li><a href="index.html" class="footer-link">Home</a></li>
            <li><a href="about.html" class="footer-link">About</a></li>
            <li><a href="services.html" class="footer-link">Services</a></li>
            <li><a href="gallery.html" class="footer-link">Gallery</a></li>
            <li><a href="projects.html" class="footer-link">Projects</a></li>
            <li><a href="contact.html" class="footer-link">Contact</a></li>
          </ul>
        </div>

        <!-- Column 3: Our Services (Exactly 6) -->
        <div class="footer-col-links">
          <h4 class="footer-heading">Our Services</h4>
          <ul class="footer-links-list">
            <li><a href="services.html#deck-construction" class="footer-link">Custom Decks</a></li>
            <li><a href="services.html#pergola-construction" class="footer-link">Pergolas</a></li>
            <li><a href="services.html#covered-outdoor-living" class="footer-link">Covered Outdoor Living</a></li>
            <li><a href="services.html#patio-spaces" class="footer-link">Patio Spaces</a></li>
            <li><a href="services.html#outdoor-entertainment" class="footer-link">Outdoor Entertainment</a></li>
            <li><a href="services.html#deck-renovation" class="footer-link">Deck Renovation</a></li>
          </ul>
        </div>

        <!-- Column 4: Explore (Exactly 6) -->
        <div class="footer-col-links">
          <h4 class="footer-heading">Explore</h4>
          <ul class="footer-links-list">
            <li><a href="home-2.html" class="footer-link">Home 2</a></li>
            <li><a href="gallery.html#decks" class="footer-link">Deck Design Ideas</a></li>
            <li><a href="gallery.html#pergolas" class="footer-link">Pergola Inspiration</a></li>
            <li><a href="gallery.html#living" class="footer-link">Outdoor Living Ideas</a></li>
            <li><a href="projects.html" class="footer-link">Project Gallery</a></li>
            <li><a href="blog.html" class="footer-link">Blog</a></li>
          </ul>
        </div>

        <!-- Column 5: Customer Support (Exactly 6) -->
        <div class="footer-col-links">
          <h4 class="footer-heading">Customer Support</h4>
          <ul class="footer-links-list">
            <li><a href="contact.html#consultation" class="footer-link">Book a Consultation</a></li>
            <li><a href="contact.html#enquiry" class="footer-link">Project Enquiry</a></li>
            <li><a href="faq.html#planning" class="footer-link">Planning Your Project</a></li>
            <li><a href="faq.html" class="footer-link">Frequently Asked Questions</a></li>
            <li><a href="contact.html" class="footer-link">Contact Us</a></li>
            <li><a href="privacy.html" class="footer-link">Privacy Policy</a></li>
          </ul>
        </div>

        <!-- Column 6: Newsletter -->
        <div class="footer-col-newsletter">
          <div class="footer-newsletter-box">
            <h4 class="footer-newsletter-title">GET OUTDOOR INSPIRATION.</h4>
            <p class="footer-newsletter-desc">
              Subscribe to receive seasonal design inspiration, materials guides and craftsmanship insights.
            </p>
            <form class="footer-newsletter-form" id="newsletterForm" novalidate>
              <div class="newsletter-input-group">
                <input type="email" class="newsletter-input" placeholder="Enter your email address" aria-label="Email address for newsletter" required>
              </div>
              <button type="submit" class="newsletter-submit-btn">
                <span>Subscribe</span>
                <i data-lucide="arrow-right"></i>
              </button>
              <div class="newsletter-feedback" role="alert" aria-live="polite"></div>
            </form>
          </div>
        </div>

        <!-- Column 7: Follow Us -->
        <div class="footer-col-social">
          <h4 class="footer-heading">Follow Us</h4>
          <ul class="footer-social-list">
            <li>
              <a href="https://instagram.com" target="_blank" rel="noopener noreferrer" class="footer-social-link" aria-label="Instagram">
                <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
                  <rect width="20" height="20" x="2" y="2" rx="5" ry="5"/>
                  <path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/>
                  <line x1="17.5" x2="17.51" y1="6.5" y2="6.5"/>
                </svg>
              </a>
            </li>
            <li>
              <a href="https://facebook.com" target="_blank" rel="noopener noreferrer" class="footer-social-link" aria-label="Facebook">
                <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/>
                </svg>
              </a>
            </li>
            <li>
              <a href="https://pinterest.com" target="_blank" rel="noopener noreferrer" class="footer-social-link" aria-label="Pinterest">
                <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
                  <line x1="12" y1="10" x2="12" y2="21"/>
                  <path d="M8 12.5a4 4 0 1 1 8 0c0 3-1.8 5-4.2 5a3.5 3.5 0 0 1-2.8-1.5"/>
                  <circle cx="12" cy="12" r="10"/>
                </svg>
              </a>
            </li>
            <li>
              <a href="https://youtube.com" target="_blank" rel="noopener noreferrer" class="footer-social-link" aria-label="YouTube">
                <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M2.5 17a24.12 24.12 0 0 1 0-10 2 2 0 0 1 1.4-1.4 49.56 49.56 0 0 1 16.2 0A2 2 0 0 1 21.5 7a24.12 24.12 0 0 1 0 10 2 2 0 0 1-1.4 1.4 49.55 49.55 0 0 1-16.2 0A2 2 0 0 1 2.5 17"/>
                  <polygon points="10 15 15 12 10 9" fill="currentColor"/>
                </svg>
              </a>
            </li>
          </ul>
        </div>

      </div>

      <!-- Footer Bottom Bar -->
      <div class="footer-bottom">
        <div class="footer-copyright">
          &copy; 2026 Evergreen Outdoor Living. All Rights Reserved.
        </div>

        <ul class="footer-legal-links">
          <li><a href="privacy.html" class="footer-legal-link">Privacy Policy</a></li>
          <li><a href="terms.html" class="footer-legal-link">Terms &amp; Conditions</a></li>
          <li><a href="cookies.html" class="footer-legal-link">Cookie Policy</a></li>
        </ul>

        <button type="button" class="back-to-top-btn" aria-label="Back to Top">
          <span>Back to Top</span>
          <i data-lucide="arrow-up"></i>
        </button>
      </div>
    </div>
  </footer>'''

def update_page(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Replace header
    new_header = get_header_html(filename)
    header_pattern = re.compile(r'<header[^>]*class=["\']site-header[^>]*>.*?</header>', re.DOTALL)
    if not header_pattern.search(content):
        # Fallback search for any site-header
        header_pattern = re.compile(r'<header[^>]*id=["\']siteHeader[^>]*>.*?</header>', re.DOTALL)

    content, n_h = header_pattern.subn(new_header, content, count=1)
    if n_h == 0:
        print(f"FAILED to replace header in {filename}")

    # 2. Replace drawer
    new_drawer = get_drawer_html(filename)
    drawer_pattern = re.compile(r'(?:<div class=["\'](?:drawer-backdrop|nav-drawer-overlay)["\'][^>]*></div>\s*)?<aside[^>]*class=["\'](?:mobile-drawer|nav-drawer-panel)["\'][^>]*>.*?</aside>', re.DOTALL)
    content, n_d = drawer_pattern.subn(new_drawer, content, count=1)
    if n_d == 0:
        print(f"FAILED to replace drawer in {filename}")

    # 3. Replace footer
    new_footer = get_footer_html()
    footer_pattern = re.compile(r'<footer[^>]*class=["\']site-footer["\'][^>]*>.*?</footer>', re.DOTALL)
    content, n_f = footer_pattern.subn(new_footer, content, count=1)
    if n_f == 0:
        print(f"FAILED to replace footer in {filename}")

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Successfully updated {filename} (header:{n_h}, drawer:{n_d}, footer:{n_f})")

for page in PAGES:
    update_page(page)
