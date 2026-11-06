/**
 * EVERGREEN OUTDOOR LIVING - MAIN APPLICATION SCRIPT
 * Coordinates icon initialization, newsletter validation, back to top, and smooth interactions.
 */

(function () {
  'use strict';

  document.addEventListener('DOMContentLoaded', () => {
    /* ------------------------------------------------------------------------
       1. Initialize Lucide Outline Icons
       ------------------------------------------------------------------------ */
    if (window.lucide && typeof window.lucide.createIcons === 'function') {
      window.lucide.createIcons();
    }

    /* ------------------------------------------------------------------------
       2. Back To Top Button
       ------------------------------------------------------------------------ */
    const backToTopBtn = document.querySelector('.back-to-top-btn');
    if (backToTopBtn) {
      backToTopBtn.addEventListener('click', (e) => {
        e.preventDefault();
        window.scrollTo({
          top: 0,
          behavior: 'smooth',
        });
      });
    }

    /* ------------------------------------------------------------------------
       3. Newsletter Client-Side Validation
       ------------------------------------------------------------------------ */
    const newsletterForm = document.querySelector('.footer-newsletter-form');
    if (newsletterForm) {
      const emailInput = newsletterForm.querySelector('.newsletter-input');
      const feedbackEl = newsletterForm.querySelector('.newsletter-feedback');

      newsletterForm.addEventListener('submit', (e) => {
        e.preventDefault();
        if (!emailInput || !feedbackEl) return;

        const email = emailInput.value.trim();
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

        feedbackEl.className = 'newsletter-feedback';

        if (!email) {
          feedbackEl.textContent = 'Please enter your email address.';
          feedbackEl.classList.add('error');
        } else if (!emailRegex.test(email)) {
          feedbackEl.textContent = 'Please provide a valid email address.';
          feedbackEl.classList.add('error');
        } else {
          // Frontend demonstration feedback as required by static architecture specifications
          feedbackEl.textContent = 'Frontend demo: Valid email format accepted. (Subscriptions are not stored without a backend integration).';
          feedbackEl.classList.add('success');
          emailInput.value = '';

          setTimeout(() => {
            feedbackEl.className = 'newsletter-feedback';
            feedbackEl.textContent = '';
          }, 6000);
        }
      });
    }

    /* ------------------------------------------------------------------------
       4. Smooth Scroll for Anchor Links
       ------------------------------------------------------------------------ */
    document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
      anchor.addEventListener('click', function (e) {
        const targetId = this.getAttribute('href');
        if (targetId && targetId !== '#') {
          const targetElement = document.querySelector(targetId);
          if (targetElement) {
            e.preventDefault();
            const headerHeight = document.querySelector('.site-header')?.offsetHeight || 80;
            const targetPosition = targetElement.getBoundingClientRect().top + window.pageYOffset - headerHeight;
            window.scrollTo({
              top: targetPosition,
              behavior: 'smooth',
            });
          }
        }
      });
    });
  });
})();
