/**
 * EVERGREEN OUTDOOR LIVING - THEME & DIRECTION CONTROLLER
 * Controls Dark / Light Mode and LTR / RTL Direction with LocalStorage Persistence
 */

(function () {
  'use strict';

  const THEME_STORAGE_KEY = 'eol_theme_preference';
  const DIR_STORAGE_KEY = 'eol_direction_preference';

  /**
   * Initialize theme immediately to prevent FOIT (Flash of Incorrect Theme)
   */
  function initTheme() {
    const savedTheme = localStorage.getItem(THEME_STORAGE_KEY);
    const prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
    const initialTheme = savedTheme ? savedTheme : (prefersDark ? 'dark' : 'light');

    document.documentElement.setAttribute('data-theme', initialTheme);
    updateThemeIcons(initialTheme);
  }

  /**
   * Initialize text direction (LTR / RTL)
   */
  function initDirection() {
    const savedDir = localStorage.getItem(DIR_STORAGE_KEY) || 'ltr';
    document.documentElement.setAttribute('dir', savedDir);
    updateDirButtons(savedDir);
  }

  /**
   * Toggle between light and dark theme
   */
  function toggleTheme() {
    const currentTheme = document.documentElement.getAttribute('data-theme') || 'light';
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';

    document.documentElement.setAttribute('data-theme', newTheme);
    localStorage.setItem(THEME_STORAGE_KEY, newTheme);
    localStorage.setItem('eol_theme', newTheme);
    updateThemeIcons(newTheme);

    // Re-render lucide icons if available
    if (window.lucide && typeof window.lucide.createIcons === 'function') {
      window.lucide.createIcons();
    }
  }

  /**
   * Update theme toggle button icons and accessible labels
   */
  function updateThemeIcons(theme) {
    const themeButtons = document.querySelectorAll('.theme-toggle-btn');
    themeButtons.forEach((btn) => {
      const isDark = theme === 'dark';
      btn.setAttribute('aria-label', isDark ? 'Switch to Light Mode' : 'Switch to Dark Mode');
      btn.setAttribute('title', isDark ? 'Switch to Light Mode' : 'Switch to Dark Mode');

      // Update icon container with direct inline SVGs for instant rendering
      const iconWrap = btn.querySelector('.theme-icon-wrap') || btn;
      if (isDark) {
        iconWrap.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-sun"><circle cx="12" cy="12" r="4"/><path d="M12 2v2"/><path d="M12 20v2"/><path d="m4.93 4.93 1.41 1.41"/><path d="m17.66 17.66 1.41 1.41"/><path d="M2 12h2"/><path d="M20 12h2"/><path d="m6.34 17.66-1.41 1.41"/><path d="m19.07 4.93-1.41 1.41"/></svg>';
      } else {
        iconWrap.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-moon"><path d="M12 3a6 6 0 0 0 9 9 9 9 0 1 1-9-9Z"/></svg>';
      }

      // Update text label if present (in mobile drawer)
      const labelText = btn.querySelector('.theme-label-text');
      if (labelText) {
        labelText.textContent = isDark ? 'Light Mode' : 'Dark Mode';
      }
    });

    if (window.lucide && typeof window.lucide.createIcons === 'function') {
      window.lucide.createIcons();
    }
  }

  /**
   * Toggle between LTR and RTL direction
   */
  function toggleDirection() {
    const currentDir = document.documentElement.getAttribute('dir') || 'ltr';
    const newDir = currentDir === 'rtl' ? 'ltr' : 'rtl';

    document.documentElement.setAttribute('dir', newDir);
    localStorage.setItem(DIR_STORAGE_KEY, newDir);
    localStorage.setItem('eol_dir', newDir);
    updateDirButtons(newDir);

    // Re-render lucide icons
    if (window.lucide && typeof window.lucide.createIcons === 'function') {
      window.lucide.createIcons();
    }
  }

  /**
   * Update direction toggle buttons and labels
   */
  function updateDirButtons(dir) {
    const dirButtons = document.querySelectorAll('.dir-toggle-btn');
    dirButtons.forEach((btn) => {
      const isRtl = dir === 'rtl';
      btn.setAttribute('aria-label', isRtl ? 'Switch to LTR Mode' : 'Switch to RTL Mode');
      btn.setAttribute('title', isRtl ? 'Switch to LTR Mode' : 'Switch to RTL Mode');

      // Update button text or badge
      const labelBadge = btn.querySelector('.dir-badge-text');
      if (labelBadge) {
        labelBadge.textContent = isRtl ? 'LTR' : 'RTL';
      }

      const labelText = btn.querySelector('.dir-label-text');
      if (labelText) {
        labelText.textContent = isRtl ? 'LTR Mode' : 'RTL Mode';
      }
    });
  }

  // Run initializations
  initTheme();
  initDirection();

  // Attach event listeners once DOM is ready
  document.addEventListener('DOMContentLoaded', () => {
    const currentTheme = document.documentElement.getAttribute('data-theme') || 'light';
    const currentDir = document.documentElement.getAttribute('dir') || 'ltr';
    updateThemeIcons(currentTheme);
    updateDirButtons(currentDir);

    // Theme toggle buttons
    document.querySelectorAll('.theme-toggle-btn').forEach((btn) => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        toggleTheme();
      });
    });

    // Direction toggle buttons
    document.querySelectorAll('.dir-toggle-btn').forEach((btn) => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        toggleDirection();
      });
    });

    // Listen to system theme changes if user has not explicitly set a preference
    if (window.matchMedia) {
      window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
        if (!localStorage.getItem(THEME_STORAGE_KEY)) {
          const newSysTheme = e.matches ? 'dark' : 'light';
          document.documentElement.setAttribute('data-theme', newSysTheme);
          updateThemeIcons(newSysTheme);
        }
      });
    }
  });

  // Expose global methods if needed
  window.EOL_THEME = {
    toggleTheme,
    toggleDirection,
  };
})();
