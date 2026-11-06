/**
 * EVERGREEN OUTDOOR LIVING - ABOUT US PAGE CONTROLLER
 * Handles scroll reveals, interactive timeline states, and page-specific interactions.
 */

(function () {
  'use strict';

  document.addEventListener('DOMContentLoaded', () => {
    // Respect reduced motion preference
    const prefersReducedMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (prefersReducedMotion) return;

    // Elements to reveal gracefully on About Us page
    const revealElements = document.querySelectorAll(
      '.about-philosophy-point, .about-insight-card, .about-principle-card, .about-craftsmanship-val-card, .about-timeline-step-card, .about-detail-item, .about-commitment-card'
    );

    if ('IntersectionObserver' in window) {
      const revealObserver = new IntersectionObserver(
        (entries) => {
          entries.forEach((entry) => {
            if (entry.isIntersecting) {
              const target = entry.target;
              const parent = target.parentElement;
              let delay = 0;
              if (parent) {
                const siblings = Array.from(parent.children);
                const idx = siblings.indexOf(target);
                delay = Math.min(idx * 75, 400);
              }

              setTimeout(() => {
                target.style.opacity = '1';
                target.style.transform = 'translateY(0)';
              }, delay);

              revealObserver.unobserve(target);
            }
          });
        },
        {
          rootMargin: '0px 0px -40px 0px',
          threshold: 0.1,
        }
      );

      revealElements.forEach((el) => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(20px)';
        el.style.transition = 'opacity 0.65s cubic-bezier(0.16, 1, 0.3, 1), transform 0.65s cubic-bezier(0.16, 1, 0.3, 1)';
        revealObserver.observe(el);
      });
    }
  });
})();
