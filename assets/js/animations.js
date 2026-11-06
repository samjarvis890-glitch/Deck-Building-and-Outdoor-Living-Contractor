/**
 * EVERGREEN OUTDOOR LIVING - ANIMATIONS & SCROLL OBSERVER
 * Subtle, luxury entrance animations and micro-interactions
 * Fully honors prefers-reduced-motion
 */

(function () {
  'use strict';

  document.addEventListener('DOMContentLoaded', () => {
    // Check if user prefers reduced motion
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (prefersReducedMotion) return;

    // Elements to reveal gracefully on scroll
    const animatedElements = document.querySelectorAll(
      '.benefit-card, .solution-card, .showcase-card, .craft-feature-item, .journey-step-card, .philosophy-point-item'
    );

    // Apply base initial styles
    animatedElements.forEach((el, index) => {
      el.style.opacity = '0';
      el.style.transform = 'translateY(24px)';
      el.style.transition = 'opacity 0.6s cubic-bezier(0.16, 1, 0.3, 1), transform 0.6s cubic-bezier(0.16, 1, 0.3, 1)';
    });

    // IntersectionObserver to trigger animations
    if ('IntersectionObserver' in window) {
      const observer = new IntersectionObserver(
        (entries) => {
          entries.forEach((entry) => {
            if (entry.isIntersecting) {
              const target = entry.target;
              // Stagger slightly based on sibling index if in same grid
              const parent = target.parentElement;
              let delay = 0;
              if (parent) {
                const siblings = Array.from(parent.children);
                const idx = siblings.indexOf(target);
                delay = Math.min(idx * 80, 400);
              }

              setTimeout(() => {
                target.style.opacity = '1';
                target.style.transform = 'translateY(0)';
              }, delay);

              observer.unobserve(target);
            }
          });
        },
        {
          rootMargin: '0px 0px -60px 0px',
          threshold: 0.1,
        }
      );

      animatedElements.forEach((el) => observer.observe(el));
    } else {
      // Fallback for older browsers
      animatedElements.forEach((el) => {
        el.style.opacity = '1';
        el.style.transform = 'none';
      });
    }
  });
})();
