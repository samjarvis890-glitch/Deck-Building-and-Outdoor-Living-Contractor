/**
 * EVERGREEN OUTDOOR LIVING - NAVBAR & MOBILE DRAWER CONTROLLER
 * Handles sticky scroll transitions, desktop hover/keyboard dropdowns,
 * full-width/mobile drawer toggles, and accessible navigation.
 */

(function () {
  'use strict';

  document.addEventListener('DOMContentLoaded', () => {
    const siteHeader = document.querySelector('.site-header');
    const hamburgerBtn = document.querySelector('.nav-hamburger-btn');
    const drawer = document.querySelector('.mobile-drawer');
    const drawerBackdrop = document.querySelector('.drawer-backdrop');
    const drawerCloseBtn = document.querySelector('.drawer-close-btn');
    const drawerLinks = document.querySelectorAll('.mobile-drawer a');
    const drawerDropdownToggles = document.querySelectorAll('.drawer-dropdown-toggle');

    /* ------------------------------------------------------------------------
       1. Sticky Header Scroll Transition
       ------------------------------------------------------------------------ */
    function handleHeaderScroll() {
      if (!siteHeader) return;
      const scrollY = window.scrollY || window.pageYOffset;

      if (scrollY > 40) {
        siteHeader.classList.add('is-scrolled');
      } else {
        siteHeader.classList.remove('is-scrolled');
      }
    }

    window.addEventListener('scroll', handleHeaderScroll, { passive: true });
    handleHeaderScroll(); // Run on init

    /* ------------------------------------------------------------------------
       2. Mobile & Tablet Drawer Open / Close
       ------------------------------------------------------------------------ */
    function openDrawer() {
      if (!drawer || !drawerBackdrop) return;
      drawer.classList.add('active');
      drawerBackdrop.classList.add('active');
      document.body.style.overflow = 'hidden'; // Prevent background scrolling
      if (hamburgerBtn) hamburgerBtn.setAttribute('aria-expanded', 'true');
      if (drawerCloseBtn) drawerCloseBtn.focus();
    }

    function closeDrawer() {
      if (!drawer || !drawerBackdrop) return;
      drawer.classList.remove('active');
      drawerBackdrop.classList.remove('active');
      document.body.style.overflow = '';
      if (hamburgerBtn) {
        hamburgerBtn.setAttribute('aria-expanded', 'false');
        hamburgerBtn.focus();
      }
    }

    if (hamburgerBtn) {
      hamburgerBtn.addEventListener('click', (e) => {
        e.preventDefault();
        openDrawer();
      });
    }

    if (drawerCloseBtn) {
      drawerCloseBtn.addEventListener('click', (e) => {
        e.preventDefault();
        closeDrawer();
      });
    }

    if (drawerBackdrop) {
      drawerBackdrop.addEventListener('click', closeDrawer);
    }

    // Close on Escape key press
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && drawer && drawer.classList.contains('active')) {
        closeDrawer();
      }
    });

    // Close drawer when an internal link is clicked
    drawerLinks.forEach((link) => {
      if (!link.classList.contains('drawer-dropdown-toggle')) {
        link.addEventListener('click', () => {
          closeDrawer();
        });
      }
    });

    /* ------------------------------------------------------------------------
       3. Drawer Submenu Accordions
       ------------------------------------------------------------------------ */
    drawerDropdownToggles.forEach((btn) => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        const targetId = btn.getAttribute('data-target');
        const submenu = document.getElementById(targetId);

        if (submenu) {
          const isExpanded = btn.getAttribute('aria-expanded') === 'true';
          btn.setAttribute('aria-expanded', !isExpanded);
          submenu.classList.toggle('show', !isExpanded);
        }
      });
    });

    /* ------------------------------------------------------------------------
       4. Desktop Keyboard Accessibility for Dropdowns
       ------------------------------------------------------------------------ */
    const desktopDropdownWrappers = document.querySelectorAll('.navbar-desktop-nav .nav-item-wrapper');

    desktopDropdownWrappers.forEach((wrapper) => {
      const toggle = wrapper.querySelector('.nav-link-item');
      const menu = wrapper.querySelector('.nav-dropdown-menu');

      if (toggle && menu) {
        toggle.addEventListener('keydown', (e) => {
          if (e.key === 'ArrowDown' || e.key === 'Enter' || e.key === ' ') {
            e.preventDefault();
            menu.classList.add('show');
            const firstLink = menu.querySelector('a');
            if (firstLink) firstLink.focus();
          }
        });

        wrapper.addEventListener('keydown', (e) => {
          if (e.key === 'Escape') {
            menu.classList.remove('show');
            toggle.focus();
          }
        });
      }
    });

    // Close open desktop dropdowns when clicking outside
    document.addEventListener('click', (e) => {
      if (!e.target.closest('.nav-item-wrapper')) {
        document.querySelectorAll('.nav-dropdown-menu.show').forEach((m) => {
          m.classList.remove('show');
        });
      }
    });
  });
})();
