/**
 * Evergreen Outdoor Living - Services Page Controller
 * Handles page-specific scroll reveals, smooth anchor scrolling with header offset,
 * and interactive pathway interactions.
 */

(function () {
  'use strict';

  function initServices() {
    // 1. Smooth Scrolling for Internal Anchor Links with Sticky Header Offset
    const internalLinks = document.querySelectorAll('a[href^="#"], a[href^="services.html#"]');
    const header = document.getElementById('siteHeader');

    internalLinks.forEach(link => {
      link.addEventListener('click', function (e) {
        const href = this.getAttribute('href');
        const hashIndex = href.indexOf('#');
        if (hashIndex === -1) return;

        const targetId = href.substring(hashIndex + 1);
        if (!targetId) return;

        const targetElem = document.getElementById(targetId);
        if (targetElem) {
          e.preventDefault();
          const headerHeight = header ? header.offsetHeight : 80;
          const elementPosition = targetElem.getBoundingClientRect().top;
          const offsetPosition = elementPosition + window.pageYOffset - headerHeight - 16;

          window.scrollTo({
            top: offsetPosition,
            behavior: 'smooth'
          });

          // Update URL hash without instant jump
          if (history.pushState) {
            history.pushState(null, null, '#' + targetId);
          } else {
            window.location.hash = targetId;
          }
        }
      });
    });

    // 2. IntersectionObserver for Elegant Scroll Reveals
    if ('IntersectionObserver' in window) {
      const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

      if (!prefersReducedMotion) {
        const revealElements = document.querySelectorAll(
          '.service-overview-card, .service-comparison-card, .service-pathway-card, .service-deck-visual-stack, .service-patio-gallery-stack'
        );

        const observerOptions = {
          root: null,
          rootMargin: '0px 0px -60px 0px',
          threshold: 0.12
        };

        const revealObserver = new IntersectionObserver((entries, observer) => {
          entries.forEach(entry => {
            if (entry.isIntersecting) {
              entry.target.style.opacity = '1';
              entry.target.style.transform = 'translateY(0)';
              observer.unobserve(entry.target);
            }
          });
        }, observerOptions);

        revealElements.forEach(el => {
          el.style.opacity = '0';
          el.style.transform = 'translateY(24px)';
          el.style.transition = 'opacity 0.6s cubic-bezier(0.16, 1, 0.3, 1), transform 0.6s cubic-bezier(0.16, 1, 0.3, 1)';
          revealObserver.observe(el);
        });
      }
    }

    // 3. Lucide Icon Initialization if available
    if (window.lucide) {
      window.lucide.createIcons();
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initServices);
  } else {
    initServices();
  }
})();
