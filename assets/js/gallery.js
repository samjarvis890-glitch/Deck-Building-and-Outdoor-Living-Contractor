/**
 * Evergreen Outdoor Living - Gallery Page Controller
 * Handles Category Filtering, Responsive Masonry Display,
 * Accessible Fullscreen Lightbox Modal, and Keyboard / Touch Navigation.
 */

(function () {
  'use strict';

  function initGallery() {
    // ------------------------------------------------------------------------
    // 1. Category Filtering for Main Collection
    // ------------------------------------------------------------------------
    const filterButtons = document.querySelectorAll('.gallery-filter-btn');
    const collectionItems = document.querySelectorAll('.gallery-collection-item');

    if (filterButtons.length && collectionItems.length) {
      filterButtons.forEach(btn => {
        btn.addEventListener('click', function () {
          const filterValue = this.getAttribute('data-filter');

          // Update active filter button state
          filterButtons.forEach(b => {
            b.classList.remove('active');
            b.setAttribute('aria-pressed', 'false');
          });
          this.classList.add('active');
          this.setAttribute('aria-pressed', 'true');

          // Filter gallery items
          collectionItems.forEach(item => {
            const itemCat = item.getAttribute('data-category');
            if (filterValue === 'all' || itemCat === filterValue) {
              item.classList.remove('is-hidden');
              item.style.opacity = '1';
              item.style.transform = 'scale(1)';
            } else {
              item.classList.add('is-hidden');
              item.style.opacity = '0';
              item.style.transform = 'scale(0.95)';
            }
          });
        });
      });
    }

    // ------------------------------------------------------------------------
    // 2. Fullscreen Lightbox Modal
    // ------------------------------------------------------------------------
    const lightboxOverlay = document.getElementById('galleryLightbox');
    const lightboxImg = document.getElementById('lightboxImg');
    const lightboxTitle = document.getElementById('lightboxTitle');
    const lightboxDesc = document.getElementById('lightboxDesc');
    const lightboxCounter = document.getElementById('lightboxCounter');
    const closeBtn = document.getElementById('lightboxClose');
    const prevBtn = document.getElementById('lightboxPrev');
    const nextBtn = document.getElementById('lightboxNext');

    let activeItems = [];
    let currentIndex = 0;

    // Register all clickable gallery cards
    const clickableCards = document.querySelectorAll('[data-gallery-item]');

    function openLightbox(index, itemsList) {
      activeItems = itemsList || Array.from(clickableCards);
      currentIndex = index;

      if (!activeItems[currentIndex]) return;
      updateLightboxContent();

      lightboxOverlay.classList.add('is-active');
      lightboxOverlay.setAttribute('aria-hidden', 'false');
      document.body.classList.add('lightbox-open');

      // Focus close button for accessibility
      if (closeBtn) closeBtn.focus();
    }

    function closeLightbox() {
      lightboxOverlay.classList.remove('is-active');
      lightboxOverlay.setAttribute('aria-hidden', 'true');
      document.body.classList.remove('lightbox-open');
    }

    function updateLightboxContent() {
      const item = activeItems[currentIndex];
      if (!item) return;

      const imgSrc = item.getAttribute('data-img-src') || item.querySelector('img')?.src;
      const title = item.getAttribute('data-img-title') || item.querySelector('h3, h4')?.textContent || 'Evergreen Outdoor Living';
      const desc = item.getAttribute('data-img-desc') || item.querySelector('p')?.textContent || '';

      if (lightboxImg) {
        lightboxImg.src = imgSrc;
        lightboxImg.alt = title;
      }
      if (lightboxTitle) lightboxTitle.textContent = title;
      if (lightboxDesc) lightboxDesc.textContent = desc;
      if (lightboxCounter) {
        lightboxCounter.textContent = `Image ${currentIndex + 1} of ${activeItems.length}`;
      }
    }

    function showNext() {
      const isRTL = document.documentElement.getAttribute('dir') === 'rtl';
      if (isRTL) {
        currentIndex = (currentIndex - 1 + activeItems.length) % activeItems.length;
      } else {
        currentIndex = (currentIndex + 1) % activeItems.length;
      }
      updateLightboxContent();
    }

    function showPrev() {
      const isRTL = document.documentElement.getAttribute('dir') === 'rtl';
      if (isRTL) {
        currentIndex = (currentIndex + 1) % activeItems.length;
      } else {
        currentIndex = (currentIndex - 1 + activeItems.length) % activeItems.length;
      }
      updateLightboxContent();
    }

    // Attach click listeners to gallery elements
    clickableCards.forEach((card, idx) => {
      card.addEventListener('click', function (e) {
        e.preventDefault();
        // If clicking a collection item, only cycle through currently visible items
        const visibleCollection = Array.from(document.querySelectorAll('.gallery-collection-item:not(.is-hidden)'));
        if (visibleCollection.includes(card)) {
          const visibleIdx = visibleCollection.indexOf(card);
          openLightbox(visibleIdx, visibleCollection);
        } else {
          openLightbox(idx, Array.from(clickableCards));
        }
      });

      // Keyboard activation via Enter or Space
      card.addEventListener('keydown', function (e) {
        if (e.key === 'Enter' || e.key === ' ') {
          e.preventDefault();
          this.click();
        }
      });
    });

    if (closeBtn) closeBtn.addEventListener('click', closeLightbox);
    if (nextBtn) nextBtn.addEventListener('click', showNext);
    if (prevBtn) prevBtn.addEventListener('click', showPrev);

    // Close on overlay backdrop click
    if (lightboxOverlay) {
      lightboxOverlay.addEventListener('click', function (e) {
        if (e.target === lightboxOverlay) {
          closeLightbox();
        }
      });
    }

    // Keyboard Navigation (Escape, ArrowLeft, ArrowRight)
    document.addEventListener('keydown', function (e) {
      if (!lightboxOverlay || !lightboxOverlay.classList.contains('is-active')) return;

      if (e.key === 'Escape') {
        closeLightbox();
      } else if (e.key === 'ArrowRight') {
        showNext();
      } else if (e.key === 'ArrowLeft') {
        showPrev();
      }
    });

    // Touch Swipe Gesture Support
    let touchStartX = 0;
    let touchEndX = 0;

    if (lightboxOverlay) {
      lightboxOverlay.addEventListener('touchstart', function (e) {
        touchStartX = e.changedTouches[0].screenX;
      }, { passive: true });

      lightboxOverlay.addEventListener('touchend', function (e) {
        touchEndX = e.changedTouches[0].screenX;
        handleSwipe();
      }, { passive: true });
    }

    function handleSwipe() {
      const threshold = 50;
      if (touchEndX < touchStartX - threshold) {
        showNext();
      } else if (touchEndX > touchStartX + threshold) {
        showPrev();
      }
    }

    // ------------------------------------------------------------------------
    // 3. Smooth Anchor Scrolling for #gallery-collection
    // ------------------------------------------------------------------------
    const internalLinks = document.querySelectorAll('a[href^="#"]');
    const header = document.getElementById('siteHeader');

    internalLinks.forEach(link => {
      link.addEventListener('click', function (e) {
        const href = this.getAttribute('href');
        if (href.length > 1 && href.startsWith('#')) {
          const target = document.querySelector(href);
          if (target) {
            e.preventDefault();
            const headerHeight = header ? header.offsetHeight : 80;
            const elementPosition = target.getBoundingClientRect().top;
            const offsetPosition = elementPosition + window.pageYOffset - headerHeight - 16;

            window.scrollTo({
              top: offsetPosition,
              behavior: 'smooth'
            });

            if (history.pushState) {
              history.pushState(null, null, href);
            }
          }
        }
      });
    });

    // ------------------------------------------------------------------------
    // 4. Lucide Icons Initialization
    // ------------------------------------------------------------------------
    if (window.lucide) {
      window.lucide.createIcons();
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initGallery);
  } else {
    initGallery();
  }
})();
