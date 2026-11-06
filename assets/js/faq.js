/**
 * EVERGREEN OUTDOOR LIVING - FAQ PAGE CONTROLLER
 * Manages FAQ data, dynamic category question counts, live keyword search,
 * category filtering, and accessible single-open accordions.
 */

(function () {
  'use strict';

  /* --------------------------------------------------------------------------
     1. UNIFIED FAQ DATA REPOSITORY
     -------------------------------------------------------------------------- */
  const FAQ_ITEMS = [
    // Section 4: GENERAL QUESTIONS
    {
      id: 'q-gen-1',
      categoryId: 'general',
      categoryName: 'General Questions',
      sectionId: 'sectionGeneral',
      question: 'What does Evergreen Outdoor Living focus on?',
      answer: 'Evergreen Outdoor Living focuses on deck building and outdoor living spaces, including custom deck concepts, pergolas, covered outdoor areas, patio spaces, and outdoor entertainment environments.'
    },
    {
      id: 'q-gen-2',
      categoryId: 'general',
      categoryName: 'General Questions',
      sectionId: 'sectionGeneral',
      question: 'What types of outdoor spaces can I enquire about?',
      answer: 'You can enquire about timber decks, pergolas, covered outdoor living areas, patios, outdoor dining spaces, entertainment areas, and deck renovation ideas.'
    },
    {
      id: 'q-gen-3',
      categoryId: 'general',
      categoryName: 'General Questions',
      sectionId: 'sectionGeneral',
      question: 'Can I discuss an idea before deciding on a design?',
      answer: 'Yes. You can begin with an enquiry describing your ideas, the space you have, and what you would like the outdoor area to achieve. This can help establish the next steps for discussing your project.'
    },
    {
      id: 'q-gen-4',
      categoryId: 'general',
      categoryName: 'General Questions',
      sectionId: 'sectionGeneral',
      question: 'Do I need a complete design before making an enquiry?',
      answer: 'No. You can start with a general idea, photographs of your space, approximate measurements, or a description of what you would like to create.'
    },
    {
      id: 'q-gen-5',
      categoryId: 'general',
      categoryName: 'General Questions',
      sectionId: 'sectionGeneral',
      question: 'Can outdoor designs be tailored to my home?',
      answer: 'Outdoor design considerations can be discussed around the available space, the style of your home, your intended use, and your material preferences.'
    },

    // Section 5: DECKS, PERGOLAS & COVERED SPACES
    {
      id: 'q-dec-1',
      categoryId: 'deck-construction',
      categoryName: 'Deck Construction',
      sectionId: 'sectionStructures',
      question: 'What should I consider before building a deck?',
      answer: 'Consider the available area, ground conditions, access from the home, intended use, deck height, material options, drainage, and how the deck will connect with the garden.'
    },
    {
      id: 'q-dec-2',
      categoryId: 'deck-construction',
      categoryName: 'Deck Construction',
      sectionId: 'sectionStructures',
      question: 'What is the difference between a deck and a patio?',
      answer: 'A deck is generally an outdoor platform that may be raised or positioned at ground level and is commonly constructed using decking materials. A patio is typically a ground-level outdoor surface that may use stone, concrete, pavers, or other suitable finishes.'
    },
    {
      id: 'q-dec-3',
      categoryId: 'pergolas-covered',
      categoryName: 'Pergolas & Covered Spaces',
      sectionId: 'sectionStructures',
      question: 'What should I consider when planning a pergola?',
      answer: 'Consider its location, dimensions, intended purpose, shade requirements, structural design, materials, and relationship with nearby buildings and landscaping.'
    },
    {
      id: 'q-dec-4',
      categoryId: 'pergolas-covered',
      categoryName: 'Pergolas & Covered Spaces',
      sectionId: 'sectionStructures',
      question: 'Can a pergola be combined with a deck?',
      answer: 'A pergola and deck can be considered together as part of one outdoor living design. Their positioning, structural requirements, access, and intended use should be planned together.'
    },
    {
      id: 'q-dec-5',
      categoryId: 'pergolas-covered',
      categoryName: 'Pergolas & Covered Spaces',
      sectionId: 'sectionStructures',
      question: 'What is a covered outdoor living area?',
      answer: 'It is an outdoor space designed with a roof or suitable covering to provide shelter and create a more defined environment for seating, dining, or entertainment.'
    },
    {
      id: 'q-dec-6',
      categoryId: 'deck-construction',
      categoryName: 'Deck Construction',
      sectionId: 'sectionStructures',
      question: 'Can an existing deck be updated?',
      answer: 'An existing deck may be considered for renovation or improvement depending on its condition, structural suitability, materials, and the changes being considered. A proper assessment is important before deciding on renovation work.'
    },

    // Section 6: MATERIALS, FINISHES & MAINTENANCE
    {
      id: 'q-mat-1',
      categoryId: 'materials-finishes',
      categoryName: 'Materials & Finishes',
      sectionId: 'sectionMaterials',
      question: 'What materials are commonly considered for decking?',
      answer: 'Common options include natural timber and composite decking products. The appropriate choice depends on appearance, product specifications, installation requirements, exposure, maintenance preferences, and project suitability.'
    },
    {
      id: 'q-mat-2',
      categoryId: 'materials-finishes',
      categoryName: 'Materials & Finishes',
      sectionId: 'sectionMaterials',
      question: 'Is natural timber different from composite decking?',
      answer: 'Yes. Natural timber has natural grain and material variation, while composite decking is manufactured using a combination of materials. Compare the specific product specifications, appearance, maintenance requirements, and installation guidance before choosing.'
    },
    {
      id: 'q-mat-3',
      categoryId: 'maintenance-care',
      categoryName: 'Maintenance & Care',
      sectionId: 'sectionMaterials',
      question: 'Does outdoor timber need maintenance?',
      answer: "Outdoor timber may require periodic cleaning, inspection, and suitable maintenance depending on the timber type, finish, exposure, and manufacturer's recommendations."
    },
    {
      id: 'q-mat-4',
      categoryId: 'materials-finishes',
      categoryName: 'Materials & Finishes',
      sectionId: 'sectionMaterials',
      question: 'How should I choose an outdoor finish?',
      answer: 'Consider the overall design, material compatibility, exposure to weather, cleaning requirements, surface characteristics, and the intended use of the area.'
    },
    {
      id: 'q-mat-5',
      categoryId: 'maintenance-care',
      categoryName: 'Maintenance & Care',
      sectionId: 'sectionMaterials',
      question: 'How can I care for an outdoor deck?',
      answer: "Follow the product or material manufacturer's guidance. General care may include regular cleaning, removing accumulated debris, checking visible connections and surfaces, and addressing maintenance needs when identified."
    },
    {
      id: 'q-mat-6',
      categoryId: 'materials-finishes',
      categoryName: 'Materials & Finishes',
      sectionId: 'sectionMaterials',
      question: 'Which material is best for an outdoor project?',
      answer: 'There is no single material that is best for every outdoor space. The right option depends on the design, conditions, intended use, product specifications, maintenance preferences, and project requirements.'
    },

    // Section 7: PLANNING, PROCESS & CONSULTATIONS
    {
      id: 'q-plan-1',
      categoryId: 'consultations-enquiries',
      categoryName: 'Consultations & Enquiries',
      sectionId: 'sectionPlanning',
      question: 'What information should I prepare before an enquiry?',
      answer: 'It can be helpful to prepare your location at a general area level, photographs of the space, approximate dimensions, your intended use, preferred materials, and any design ideas you have.'
    },
    {
      id: 'q-plan-2',
      categoryId: 'project-planning',
      categoryName: 'Project Planning',
      sectionId: 'sectionPlanning',
      question: 'Can I share photographs of my backyard?',
      answer: 'Yes. Photographs can help communicate the existing space and your ideas. They do not replace an on-site assessment where one is required.'
    },
    {
      id: 'q-plan-3',
      categoryId: 'project-planning',
      categoryName: 'Project Planning',
      sectionId: 'sectionPlanning',
      question: 'Do I need exact measurements?',
      answer: 'Exact measurements are not necessary for an initial enquiry. Approximate measurements can help explain the space, while accurate measurements may be needed during later planning stages.'
    },
    {
      id: 'q-plan-4',
      categoryId: 'project-planning',
      categoryName: 'Project Planning',
      sectionId: 'sectionPlanning',
      question: 'What can affect the planning of an outdoor project?',
      answer: 'Factors may include site access, ground conditions, existing structures, levels, drainage, materials, design complexity, and applicable local requirements.'
    },
    {
      id: 'q-plan-5',
      categoryId: 'project-planning',
      categoryName: 'Project Planning',
      sectionId: 'sectionPlanning',
      question: 'Will building approvals or permits be required?',
      answer: 'Requirements depend on the proposed structure, its location, dimensions, site conditions, and applicable local regulations. Check with the relevant local authority or a suitably qualified professional before construction.'
    },
    {
      id: 'q-plan-6',
      categoryId: 'consultations-enquiries',
      categoryName: 'Consultations & Enquiries',
      sectionId: 'sectionPlanning',
      question: 'How do I get started?',
      answer: 'Use the Contact page to send an enquiry. Describe the type of outdoor space you are considering and include any useful photographs or initial information.'
    }
  ];

  /* --------------------------------------------------------------------------
     2. STATE & SELECTORS
     -------------------------------------------------------------------------- */
  let activeCategory = 'all';
  let activeSearchQuery = '';

  /* --------------------------------------------------------------------------
     3. INITIALIZATION
     -------------------------------------------------------------------------- */
  document.addEventListener('DOMContentLoaded', () => {
    calculateCategoryCounts();
    initAccordions();
    initSearch();
    initCategoryNavigation();
    initSuggestedTags();
  });

  /* --------------------------------------------------------------------------
     4. DYNAMIC CATEGORY COUNT CALCULATOR
     -------------------------------------------------------------------------- */
  function calculateCategoryCounts() {
    const counts = {};
    FAQ_ITEMS.forEach((item) => {
      counts[item.categoryId] = (counts[item.categoryId] || 0) + 1;
    });

    document.querySelectorAll('.faq-category-card').forEach((card) => {
      const catId = card.getAttribute('data-category');
      const badge = card.querySelector('.faq-category-count-badge');
      if (badge && catId) {
        if (catId === 'all') {
          badge.textContent = `${FAQ_ITEMS.length} Questions`;
        } else {
          const count = counts[catId] || 0;
          badge.textContent = `${count} ${count === 1 ? 'Question' : 'Questions'}`;
        }
      }
    });
  }

  /* --------------------------------------------------------------------------
     5. ACCORDION CONTROLLER (Accessible Single-Open Model)
     -------------------------------------------------------------------------- */
  function initAccordions() {
    const questionButtons = document.querySelectorAll('.faq-question-btn');

    questionButtons.forEach((btn) => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        const item = btn.closest('.faq-item');
        const panel = item.querySelector('.faq-answer-panel');
        const isExpanded = btn.getAttribute('aria-expanded') === 'true';

        // Single open per accordion group
        const groupAccordion = item.closest('.faq-group-accordion');
        if (groupAccordion) {
          groupAccordion.querySelectorAll('.faq-item').forEach((sibling) => {
            if (sibling !== item) {
              sibling.classList.remove('active');
              const sibBtn = sibling.querySelector('.faq-question-btn');
              const sibPanel = sibling.querySelector('.faq-answer-panel');
              if (sibBtn) sibBtn.setAttribute('aria-expanded', 'false');
              if (sibPanel) sibPanel.style.maxHeight = null;
            }
          });
        }

        if (isExpanded) {
          // Close
          item.classList.remove('active');
          btn.setAttribute('aria-expanded', 'false');
          panel.style.maxHeight = null;
        } else {
          // Open
          item.classList.add('active');
          btn.setAttribute('aria-expanded', 'true');
          panel.style.maxHeight = panel.scrollHeight + 'px';
        }
      });
    });
  }

  /* --------------------------------------------------------------------------
     6. SEARCH CONTROLLER
     -------------------------------------------------------------------------- */
  function initSearch() {
    const searchInput = document.getElementById('faqSearchInput');
    const clearBtn = document.getElementById('faqSearchClear');
    const emptyClearBtn = document.getElementById('faqEmptyClearBtn');

    if (!searchInput) return;

    searchInput.addEventListener('input', (e) => {
      activeSearchQuery = e.target.value.trim().toLowerCase();

      if (clearBtn) {
        if (activeSearchQuery.length > 0) {
          clearBtn.classList.add('visible');
        } else {
          clearBtn.classList.remove('visible');
        }
      }

      applyFiltersAndSearch();
    });

    if (clearBtn) {
      clearBtn.addEventListener('click', (e) => {
        e.preventDefault();
        searchInput.value = '';
        activeSearchQuery = '';
        clearBtn.classList.remove('visible');
        searchInput.focus();
        applyFiltersAndSearch();
      });
    }

    if (emptyClearBtn) {
      emptyClearBtn.addEventListener('click', (e) => {
        e.preventDefault();
        resetAllFilters();
      });
    }
  }

  /* --------------------------------------------------------------------------
     7. CATEGORY NAVIGATION CONTROLLER
     -------------------------------------------------------------------------- */
  function initCategoryNavigation() {
    const categoryCards = document.querySelectorAll('.faq-category-card');

    categoryCards.forEach((card) => {
      card.addEventListener('click', (e) => {
        e.preventDefault();
        const selectedCategory = card.getAttribute('data-category') || 'all';

        categoryCards.forEach((c) => c.classList.remove('active'));
        card.classList.add('active');

        activeCategory = selectedCategory;
        applyFiltersAndSearch();

        // Smooth scroll to questions area
        const firstVisibleSection = document.querySelector('.faq-group:not([style*="display: none"])');
        if (firstVisibleSection) {
          const headerHeight = document.querySelector('.site-header')?.offsetHeight || 80;
          const targetY = firstVisibleSection.getBoundingClientRect().top + window.pageYOffset - headerHeight - 20;
          window.scrollTo({
            top: targetY,
            behavior: 'smooth'
          });
        }
      });
    });
  }

  /* --------------------------------------------------------------------------
     8. SUGGESTED SEARCH PILLS CONTROLLER
     -------------------------------------------------------------------------- */
  function initSuggestedTags() {
    const tags = document.querySelectorAll('.faq-suggest-tag');
    const searchInput = document.getElementById('faqSearchInput');
    const clearBtn = document.getElementById('faqSearchClear');

    tags.forEach((tag) => {
      tag.addEventListener('click', (e) => {
        e.preventDefault();
        const term = tag.getAttribute('data-term') || tag.textContent.trim();
        if (searchInput) {
          searchInput.value = term;
          activeSearchQuery = term.toLowerCase();
          if (clearBtn) clearBtn.classList.add('visible');
          applyFiltersAndSearch();
        }
      });
    });
  }

  /* --------------------------------------------------------------------------
     9. RESET ALL FILTERS & SEARCH
     -------------------------------------------------------------------------- */
  function resetAllFilters() {
    const searchInput = document.getElementById('faqSearchInput');
    const clearBtn = document.getElementById('faqSearchClear');
    const categoryCards = document.querySelectorAll('.faq-category-card');

    if (searchInput) {
      searchInput.value = '';
      activeSearchQuery = '';
    }
    if (clearBtn) {
      clearBtn.classList.remove('visible');
    }

    activeCategory = 'all';
    categoryCards.forEach((card) => {
      if (card.getAttribute('data-category') === 'all') {
        card.classList.add('active');
      } else {
        card.classList.remove('active');
      }
    });

    applyFiltersAndSearch();
  }

  /* --------------------------------------------------------------------------
     10. COORDINATED FILTER & SEARCH APPLICATION
     -------------------------------------------------------------------------- */
  function applyFiltersAndSearch() {
    const items = document.querySelectorAll('.faq-item');
    const statusText = document.getElementById('faqResultsStatus');
    const emptyState = document.getElementById('faqEmptyState');
    let totalVisible = 0;

    // Track visible count per section
    const sectionVisibleMap = {
      sectionGeneral: 0,
      sectionStructures: 0,
      sectionMaterials: 0,
      sectionPlanning: 0
    };

    items.forEach((item) => {
      const itemId = item.getAttribute('id');
      const itemData = FAQ_ITEMS.find((d) => d.id === itemId);

      if (!itemData) return;

      const qText = itemData.question.toLowerCase();
      const aText = itemData.answer.toLowerCase();
      const catText = itemData.categoryName.toLowerCase();

      // Check category match
      const matchesCategory = (activeCategory === 'all' || itemData.categoryId === activeCategory);

      // Check search match
      const matchesSearch = !activeSearchQuery ||
        qText.includes(activeSearchQuery) ||
        aText.includes(activeSearchQuery) ||
        catText.includes(activeSearchQuery);

      if (matchesCategory && matchesSearch) {
        item.style.display = 'block';
        totalVisible++;
        if (sectionVisibleMap[itemData.sectionId] !== undefined) {
          sectionVisibleMap[itemData.sectionId]++;
        }
      } else {
        item.style.display = 'none';
        // Close collapsed panels
        item.classList.remove('active');
        const btn = item.querySelector('.faq-question-btn');
        const panel = item.querySelector('.faq-answer-panel');
        if (btn) btn.setAttribute('aria-expanded', 'false');
        if (panel) panel.style.maxHeight = null;
      }
    });

    // Toggle parent section visibility based on whether any questions inside are visible
    Object.keys(sectionVisibleMap).forEach((secId) => {
      const sectionEl = document.getElementById(secId);
      if (sectionEl) {
        if (sectionVisibleMap[secId] > 0) {
          sectionEl.style.display = 'block';
        } else {
          sectionEl.style.display = 'none';
        }
      }
    });

    // Update dynamic results counter label
    if (statusText) {
      if (activeSearchQuery && activeCategory !== 'all') {
        statusText.textContent = `Showing ${totalVisible} ${totalVisible === 1 ? 'question' : 'questions'} for "${activeSearchQuery}" in selected topic`;
      } else if (activeSearchQuery) {
        statusText.textContent = `Showing ${totalVisible} ${totalVisible === 1 ? 'question' : 'questions'} matching "${activeSearchQuery}"`;
      } else if (activeCategory !== 'all') {
        const catCard = document.querySelector(`.faq-category-card[data-category="${activeCategory}"]`);
        const catTitle = catCard ? catCard.querySelector('.faq-category-title')?.textContent : 'Selected Topic';
        statusText.textContent = `Showing ${totalVisible} ${totalVisible === 1 ? 'question' : 'questions'} in ${catTitle}`;
      } else {
        statusText.textContent = `Showing all ${totalVisible} questions`;
      }
    }

    // Toggle empty state
    if (emptyState) {
      if (totalVisible === 0) {
        emptyState.classList.add('active');
      } else {
        emptyState.classList.remove('active');
      }
    }
  }

  // Expose reset method if needed globally
  window.EOL_FAQ = {
    resetAllFilters,
    applyFiltersAndSearch
  };

})();
