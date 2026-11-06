/**
 * EVERGREEN OUTDOOR LIVING - HOME 2 PAGE SPECIFIC CONTROLLER
 * Handles Home 2 animations, smooth interactive behaviors, and editorial scroll reveals
 */

(function () {
  'use strict';

  document.addEventListener('DOMContentLoaded', () => {
    // Check if user prefers reduced motion
    const prefersReducedMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (prefersReducedMotion) return;

    // Elements to reveal gracefully on Home 2
    const animatedCards = document.querySelectorAll(
      '.home2-experience-panel, .home2-material-card, .home2-season-card, .home2-journal-card, .home2-hero-content, .home2-hero-visual'
    );

    if ('IntersectionObserver' in window) {
      const cardObserver = new IntersectionObserver(
        (entries) => {
          entries.forEach((entry) => {
            if (entry.isIntersecting) {
              const target = entry.target;
              const parent = target.parentElement;
              let delay = 0;
              if (parent) {
                const siblings = Array.from(parent.children);
                const idx = siblings.indexOf(target);
                delay = Math.min(idx * 70, 350);
              }

              setTimeout(() => {
                target.style.opacity = '1';
                target.style.transform = 'translateY(0)';
              }, delay);

              cardObserver.unobserve(target);
            }
          });
        },
        {
          rootMargin: '0px 0px -50px 0px',
          threshold: 0.1,
        }
      );

      animatedCards.forEach((el) => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(22px)';
        el.style.transition = 'opacity 0.6s cubic-bezier(0.16, 1, 0.3, 1), transform 0.6s cubic-bezier(0.16, 1, 0.3, 1)';
        cardObserver.observe(el);
      });
    }
  });
})();
