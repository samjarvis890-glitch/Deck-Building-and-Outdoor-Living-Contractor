/**
 * EVERGREEN OUTDOOR LIVING - BLOG & JOURNAL INTERACTION CONTROLLER
 * Handles category filtering, live search, topic tile navigation,
 * accessible article detail modal, and newsletter validation.
 */

(function () {
  'use strict';

  /* --------------------------------------------------------------------------
     ARTICLE CONTENT REPOSITORY (Realistic, Educational Sample Articles)
     -------------------------------------------------------------------------- */
  const ARTICLE_DATA = {
    'featured': {
      category: 'OUTDOOR LIVING',
      title: 'How to Create an Outdoor Living Space That Feels Like an Extension of Home',
      readTime: '6 MIN READ',
      date: 'Editorial Issue • Vol. 04',
      image: 'assets/images/blog/blog-featured-article.webp',
      alt: 'Seamless indoor-outdoor living transition featuring wide cedar deck and garden connection',
      content: `
        <p>Creating a true sense of continuity between internal living areas and the landscape outside is one of the hallmarks of thoughtful residential architecture. When planned with care, an outdoor living space should not feel like an afterthought or a detached platform, but rather like a natural progression of your home's daily rhythm.</p>
        
        <h3>1. Establishing Continuous Flow and Sightlines</h3>
        <p>The journey from indoors to outdoors begins with visual alignment. Aligning decking board orientation with interior flooring, matching sill heights to eliminate trip hazards, and framing vistas toward focal points in the garden help blur the structural boundary. Wide sliding glass doors or bifold assemblies expand perceived interior volume and invite sunlight deep into the house.</p>

        <div class="blog-modal-callout">
          "The most successful outdoor rooms are those where the threshold between interior shelter and open garden becomes delightfully indistinct."
        </div>

        <h3>2. Material Resonance and Weather Resilience</h3>
        <p>Selecting materials that echo your home’s architectural palette creates instant cohesion. If your home features warm timber accents, carrying complementary timber varieties into deck decking boards, screening battens, and structural posts establishes immediate harmony. Pairing natural timber with neutral stone and powder-coated architectural elements provides depth while enduring seasonal climate shifts.</p>

        <h3>3. Functional Zoning for Real Daily Life</h3>
        <p>Consider how your family lives across different times of day. An effective outdoor layout designates clear, purposeful zones—such as an intimate morning coffee corner sheltered from wind, a spacious alfresco dining area shaded by an overhead pergola, and low-profile lounge seating surrounding soft evening illumination.</p>
      `,
      takeaways: [
        'Align threshold transitions and floor levels for uninterrupted indoor-outdoor movement.',
        'Use consistent material palettes that echo interior design tones.',
        'Create distinct zones for morning pause, shared dining, and evening relaxation.',
        'Incorporate overhead timber battens or pergolas to regulate daylight and shelter.'
      ]
    },
    'deck-planning': {
      category: 'DECK PLANNING',
      title: '7 Things to Consider Before Building a Timber Deck',
      readTime: '5 MIN READ',
      date: 'Planning Series • Issue 04',
      image: 'assets/images/blog/blog-article-deck-planning.webp',
      alt: 'Timber deck planning, subframe joists and leveling in garden environment',
      content: `
        <p>Building a timber deck is one of the most rewarding investments for any property. However, enduring craftsmanship depends far more on thorough groundwork and subframe engineering than just surface board selection.</p>
        
        <h3>1. Site Topography and Ground Moisture</h3>
        <p>Understanding natural slope, soil compaction, and drainage paths is essential. Inadequate ground clearance beneath joists restricts natural cross-ventilation, trapping moisture that can compromise substructure timbers over time.</p>

        <h3>2. Sun Orientation and Microclimate</h3>
        <p>A deck facing direct north or west requires different shade considerations and timber finishes than a shaded south-facing aspect. Factoring in seasonal sun paths dictates where dining tables, shade pergolas, and screening walls should be positioned.</p>

        <div class="blog-modal-callout">
          "A well-engineered subframe provides the invisible foundation that ensures your deck remains solid, level, and creak-free for decades."
        </div>

        <h3>3. Flow and Circulation Paths</h3>
        <p>Ensure wide, unencumbered circulation corridors between access doors, cooking stations, and garden steps. Plan at least 900mm of clearance around dining furniture so guests can move comfortably without stepping off the deck edge.</p>
      `,
      takeaways: [
        'Confirm adequate sub-floor clearance and cross-flow ventilation beneath the deck.',
        'Assess daily sun exposure to guide timber finish selection and shade placement.',
        'Maintain comfortable 900mm+ circulation walkways around seating arrangements.',
        'Always consult local statutory planning regulations and setback requirements.'
      ]
    },
    'pergola-style': {
      category: 'PERGOLA IDEAS',
      title: 'Choosing the Right Pergola Style for Your Garden',
      readTime: '4 MIN READ',
      date: 'Design Guide • Issue 04',
      image: 'assets/images/blog/blog-article-pergola-style.webp',
      alt: 'Architectural pergola structure casting geometric dappled shadows across stone patio',
      content: `
        <p>A pergola creates spatial definition without enclosing the outdoors. It acts as an open-air ceiling, framing the sky while providing essential architectural scale to gardens and courtyards.</p>
        
        <h3>1. Proportions and Ceiling Height</h3>
        <p>Pergola height should correspond to your home's rooflines and window headers. A structure that is too low feels cramped, while excessive height can feel ungrounded and fails to provide effective sun shading.</p>

        <h3>2. Timber Rafter Spacing & Blade Angles</h3>
        <p>The spacing and bevel of overhead rafters determine how light moves through the space. Closely spaced vertical louvers provide substantial midday solar deflection while casting beautiful architectural shadows that evolve throughout the afternoon.</p>

        <div class="blog-modal-callout">
          "The pergola transforms an open patio into an intimate outdoor room by introducing vertical rhythm and dappled natural daylight."
        </div>

        <h3>3. Integration with Climbing Botanicals</h3>
        <p>Integrating deciduous climbers such as wisteria, ornamental grapes, or bougainvillea offers natural climate control—luxuriant leafy shade in hot summer months and unobstructed warmth during cooler winter months.</p>
      `,
      takeaways: [
        'Match pergola eave heights with the home’s existing window and fascia lines.',
        'Angle overhead louvers to mitigate harsh midday glare while capturing breezes.',
        'Consider deciduous climbing vines for seasonal dynamic shading.',
        'Incorporate concealed cable conduits for ambient lighting during construction.'
      ]
    },
    'small-spaces': {
      category: 'SMALL SPACES',
      title: 'How to Make a Small Backyard Feel More Spacious',
      readTime: '6 MIN READ',
      date: 'Spatial Design • Issue 04',
      image: 'assets/images/blog/blog-article-small-backyard.webp',
      alt: 'Compact urban backyard featuring built-in bench seating, vertical living wall, and raised deck',
      content: `
        <p>A compact garden footprint does not restrict design ambition. In fact, smaller outdoor spaces often yield the most intimate, character-rich sanctuaries when every square metre is considered with purpose.</p>
        
        <h3>1. Built-in Bench Seating and Storage</h3>
        <p>Freestanding outdoor furniture with bulky chair backs can crowd a modest deck. Installing perimeter floating timber benches preserves open floor area while doubling as discreet storage for cushions, garden tools, and accessories.</p>

        <h3>2. Vertical Planting & Living Boundaries</h3>
        <p>When horizontal ground is limited, draw the eye upward. Vertical trellis screens, green living walls, and slender espaliered fruit trees soften boundary fences without stealing valuable walking area.</p>

        <div class="blog-modal-callout">
          "In smaller gardens, multi-functional elements and subtle level shifts create the perception of expansive luxury."
        </div>

        <h3>3. Strategic Multi-Level Terracing</h3>
        <p>Even a single low step separating a dining platform from an intimate lounge nook establishes distinct zones, giving the optical illusion of greater architectural depth.</p>
      `,
      takeaways: [
        'Incorporate integrated perimeter benches to maximise usable floor space.',
        'Use vertical greenery and living walls to soften boundary boundaries.',
        'Introduce subtle single-step level changes to demarcate distinct zones.',
        'Choose light-toned decking and reflective foliage to bounce natural daylight.'
      ]
    },
    'deck-materials': {
      category: 'MATERIAL GUIDE',
      title: 'Timber or Composite Decking: What Should You Consider?',
      readTime: '7 MIN READ',
      date: 'Material Insights • Issue 04',
      image: 'assets/images/blog/blog-article-deck-materials.webp',
      alt: 'Side-by-side comparison swatches of natural hardwood timber grain and modern composite decking',
      content: `
        <p>Choosing between natural timber and composite decking boards is one of the most common decisions facing property owners. Both options offer distinct aesthetic and functional characteristics.</p>
        
        <h3>1. Natural Hardwood: Authenticity and Character</h3>
        <p>Natural timbers such as spotted gum, blackbutt, and ironbark possess unmatched organic warmth, natural grain individuality, and tactile elegance. Timber responds to sunlight and develops a rich patina over time, requiring periodic cleaning and re-oiling to maintain its original lustre.</p>

        <h3>2. Composite Decking: Engineered Performance</h3>
        <p>Modern composite decking blends recycled wood fibres with durable polymers, creating boards that resist splintering, rot, and termite activity. While composite materials require minimal annual maintenance beyond regular washing, consideration should be given to surface heat retention in unshaded direct sun.</p>

        <div class="blog-modal-callout">
          "Neither material is objectively superior; the ideal choice balances your appreciation for natural timber character with your desired maintenance routine."
        </div>

        <h3>3. Environmental and Lifecycle Considerations</h3>
        <p>Sustainably harvested, certified Australian hardwoods support circular forestry lifecycles, whereas high-grade composites frequently repurpose recycled consumer plastics. Assessing your property's bushfire attack level (BAL rating) is also crucial when specifying materials.</p>
      `,
      takeaways: [
        'Natural hardwood offers unique organic grain and can be sanded and refinished.',
        'Composite decking minimizes ongoing sealing and resists splintering and weathering.',
        'Consider surface temperature differences in full-sun, unshaded applications.',
        'Verify BAL (Bushfire Attack Level) compliance for your specific property zone.'
      ]
    },
    'outdoor-dining': {
      category: 'OUTDOOR ENTERTAINING',
      title: 'Creating a Comfortable Outdoor Dining Area',
      readTime: '5 MIN READ',
      date: 'Entertaining • Issue 04',
      image: 'assets/images/blog/blog-article-outdoor-dining.webp',
      alt: 'Alfresco dining area with long teak dining table, stoneware plates and ambient twilight glow',
      content: `
        <p>Gathering around a table outdoors is one of life’s purest pleasures. A well-considered dining area balances social generosity with practical culinary workflow and atmospheric comfort.</p>
        
        <h3>1. Kitchen Proximity & Serving Flow</h3>
        <p>An outdoor dining table should connect logically to both the indoor kitchen and any exterior barbecue or prep counters. Minimizing awkward transitions through tight doorways ensures effortless hosting and food transport.</p>

        <h3>2. Sheltered Protection Against Sun and Breeze</h3>
        <p>Unprotected tables exposed to prevailing afternoon gusts or harsh setting sun quickly cut gatherings short. Consider integrated timber louvers or perimeter screening battens to baffle breezes while filtering golden afternoon light.</p>

        <div class="blog-modal-callout">
          "Atmosphere is crafted in the details: warm diffused lighting, natural textures, and comfortable seating that encourages guests to linger long after dessert."
        </div>

        <h3>3. Warm Evening Illumination</h3>
        <p>Avoid harsh overhead floodlighting. Instead, opt for low-glare pendant fittings positioned 750mm above the tabletop, supplemented by step riser LEDs and warm uplighting into nearby garden foliage.</p>
      `,
      takeaways: [
        'Locate dining zones near indoor service paths for seamless food and drink prep.',
        'Integrate wind baffles and pergola shading to maintain comfort in variable weather.',
        'Incorporate warm 2700K pendant lighting directly above the table.',
        'Choose weather-enduring dining chairs with ergonomic back support and breathable textiles.'
      ]
    },
    'natural-style': {
      category: 'DESIGN INSPIRATION',
      title: 'Simple Ways to Bring Natural Style Into Outdoor Design',
      readTime: '4 MIN READ',
      date: 'Inspiration • Issue 04',
      image: 'assets/images/blog/blog-article-natural-style.webp',
      alt: 'Natural outdoor style showcasing organic river boulders, ornamental grasses, and weathered timber',
      content: `
        <p>A natural outdoor aesthetic feels relaxed, timeless, and effortlessly connected to the Australian landscape. Rather than imposing rigid industrial geometries, this approach embraces organic textures and restrained earthy palettes.</p>
        
        <h3>1. Layering Natural Textures</h3>
        <p>Combine tactile finishes: silky oiled timber decking, rough-hewn sandstone boulders, honed bluestone pavers, and fine gravel pathways. The contrast between smooth and textured materials enriches sensory engagement.</p>

        <h3>2. Celebrating Native Plant Palettes</h3>
        <p>Soften crisp structural lines with massed native grasses (such as Lomandra and Poa), silver-foliaged shrubs, and sculptural feature trees. As breezes move through ornamental grasses, they introduce subtle sound and movement.</p>

        <div class="blog-modal-callout">
          "Natural design does not mean unstructured; it relies on purposeful restraint, quiet craftsmanship, and respect for site context."
        </div>

        <h3>3. Restrained, Earth-Derived Colour Schemes</h3>
        <p>Stick to a tight palette inspired by eucalyptus foliage, bark tones, warm sand, and charcoal shadows. Avoiding bright artificial pigments allows the organic hues of timber and plant life to take centre stage.</p>
      `,
      takeaways: [
        'Layer contrasting tactile textures: timber, stone, gravel, and woven textiles.',
        'Introduce native ornamental grasses for gentle acoustic and visual movement.',
        'Use an earthy palette of sage greens, sand beige, charcoal, and warm timber.',
        'Allow timber finishes to weather gracefully or maintain with natural penetrating oils.'
      ]
    },
    'guide-deck': {
      category: 'DECK PLANNING GUIDE',
      title: 'Complete Planning Guide: Building an Enduring Timber Deck',
      readTime: '8 MIN READ',
      date: 'Practical Guide • Vol. 04',
      image: 'assets/images/blog/blog-guide-deck-planning.webp',
      alt: 'Detailed deck planning elevation schematic and site layout',
      content: `
        <p>A successful deck project requires a clear, step-by-step planning roadmap before ordering materials or digging footings. Follow this structured approach to ensure optimal structural integrity and lifestyle enjoyment.</p>
        
        <h3>Step 1: Space & Setback Analysis</h3>
        <p>Measure boundary setbacks, underground utility easements, and verify compliance with local council residential development standards. Ensure adequate clearance from existing tree root zones.</p>

        <h3>Step 2: Subfloor Ventilation & Drainage</h3>
        <p>Design grading beneath the deck so surface water drains away from your home's foundation. Maintain minimum recommended clearances between timber bearers and bare soil.</p>

        <h3>Step 3: Access and Threshold Detailing</h3>
        <p>Consider flush threshold drain systems that eliminate step-downs between indoor living areas and exterior decking, creating modern accessibility for all family members.</p>
      `,
      takeaways: [
        'Identify all underground utility conduits before excavating footing piers.',
        'Design adequate natural subfloor ventilation to prevent moisture retention.',
        'Specify hot-dip galvanised or 316 marine-grade stainless steel fasteners.',
        'Schedule professional on-site engineering assessments for elevated decks.'
      ]
    },
    'guide-pergola': {
      category: 'PERGOLA PLANNING GUIDE',
      title: 'Architectural Pergola Planning Guide: Proportion, Shade & Form',
      readTime: '7 MIN READ',
      date: 'Practical Guide • Vol. 04',
      image: 'assets/images/blog/blog-guide-pergola-planning.webp',
      alt: 'Pergola sun angle study and architectural framing diagram',
      content: `
        <p>Pergolas serve as the architectural crown of an outdoor living space. Proper planning ensures your structure delivers shelter, beauty, and long-term durability in equal measure.</p>
        
        <h3>1. Primary Orientation & Daylight Modeling</h3>
        <p>Track how sunlight strikes your garden across summer and winter solstices. Angle overhead battens to block high-angle summer sun while admitting low-angled winter light.</p>

        <h3>2. Post Attachment and Structural Sizing</h3>
        <p>Calculate post and beam spans to prevent mid-span sagging over time. Select substantial post dimensions (such as 140x140mm or 190x190mm) to establish generous, grounded visual weight.</p>

        <h3>3. Future-Proofing for Services</h3>
        <p>Incorporate internal conduit routes for electrical wiring during fabrication, allowing seamless installation of ceiling fans, downlights, and infrared radiant heaters.</p>
      `,
      takeaways: [
        'Model seasonal solar azimuths to determine optimal louver spacing.',
        'Use generous post dimensions to achieve grounded architectural scale.',
        'Conceal electrical conduit pathways during initial timber framing.',
        'Verify wind rating requirements for your specific suburban or coastal zone.'
      ]
    },
    'guide-entertaining': {
      category: 'ENTERTAINING GUIDE',
      title: 'Outdoor Entertaining Area Planning: Capacity, Cooking & Ambience',
      readTime: '6 MIN READ',
      date: 'Practical Guide • Vol. 04',
      image: 'assets/images/blog/blog-guide-entertaining.webp',
      alt: 'Outdoor entertainment area showing outdoor kitchen prep and social circulation',
      content: `
        <p>Entertaining outdoors should feel effortless for the host and welcoming for guests. Thoughtful spatial planning prevents bottlenecks and keeps conversation flowing naturally.</p>
        
        <h3>1. Capacity and Seating Configurations</h3>
        <p>Determine your typical gathering size versus peak celebration numbers. Flexible modular seating, deep lounge benches, and movable occasional stools accommodate fluctuating guest counts without cluttering the space.</p>

        <h3>2. The Cooking Zone Work Triangle</h3>
        <p>Position barbecues and pizza ovens downwind from dining tables. Ensure heat-resistant benchtops flank the grill for food staging and serving platters.</p>

        <h3>3. Acoustic & Atmospheric Layering</h3>
        <p>Include weatherproof acoustic speakers, textured outdoor rugs to dampen footfalls, and soft perimeter ambient lighting that allows the starry night sky to remain visible.</p>
      `,
      takeaways: [
        'Design flexible seating arrangements that adapt to varying group sizes.',
        'Position cooking appliances downwind from social dining areas.',
        'Include durable weather-resistant food prep countertops adjacent to grills.',
        'Layer multi-circuit ambient lighting on dimmer controls.'
      ]
    }
  };

  /* --------------------------------------------------------------------------
     DOM INITIALIZATION
     -------------------------------------------------------------------------- */
  document.addEventListener('DOMContentLoaded', () => {
    initCategoryFilters();
    initArticleSearch();
    initTopicTileTriggers();
    initArticleModal();
    initNewsletterForm();
  });

  /* --------------------------------------------------------------------------
     1. ARTICLE CATEGORY FILTERING
     -------------------------------------------------------------------------- */
  let currentCategory = 'all';
  let currentSearchQuery = '';

  function initCategoryFilters() {
    const filterButtons = document.querySelectorAll('.blog-filter-btn');
    if (!filterButtons.length) return;

    filterButtons.forEach((btn) => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        const selectedCat = btn.getAttribute('data-filter') || 'all';

        // Update active class on buttons
        filterButtons.forEach((b) => b.classList.remove('active'));
        btn.classList.add('active');

        currentCategory = selectedCat;
        applyFiltersAndSearch();
      });
    });
  }

  /* --------------------------------------------------------------------------
     2. LIVE ARTICLE SEARCH
     -------------------------------------------------------------------------- */
  function initArticleSearch() {
    const searchInput = document.getElementById('blogSearchInput');
    const clearBtn = document.getElementById('blogSearchClear');
    const resetBtn = document.getElementById('blogResetFiltersBtn');

    if (!searchInput) return;

    searchInput.addEventListener('input', (e) => {
      currentSearchQuery = e.target.value.trim().toLowerCase();

      if (clearBtn) {
        if (currentSearchQuery.length > 0) {
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
        currentSearchQuery = '';
        clearBtn.classList.remove('visible');
        searchInput.focus();
        applyFiltersAndSearch();
      });
    }

    if (resetBtn) {
      resetBtn.addEventListener('click', (e) => {
        e.preventDefault();
        resetAllFilters();
      });
    }
  }

  function resetAllFilters() {
    const searchInput = document.getElementById('blogSearchInput');
    const clearBtn = document.getElementById('blogSearchClear');
    const filterButtons = document.querySelectorAll('.blog-filter-btn');

    if (searchInput) {
      searchInput.value = '';
      currentSearchQuery = '';
    }
    if (clearBtn) {
      clearBtn.classList.remove('visible');
    }

    currentCategory = 'all';
    filterButtons.forEach((btn) => {
      if (btn.getAttribute('data-filter') === 'all') {
        btn.classList.add('active');
      } else {
        btn.classList.remove('active');
      }
    });

    applyFiltersAndSearch();
  }

  /* --------------------------------------------------------------------------
     COORDINATED FILTER & SEARCH APPLICATION
     -------------------------------------------------------------------------- */
  function applyFiltersAndSearch() {
    const cards = document.querySelectorAll('.blog-article-card');
    const emptyState = document.getElementById('blogEmptyState');
    let visibleCount = 0;

    cards.forEach((card) => {
      const cardCategory = card.getAttribute('data-category') || '';
      const cardTitle = (card.getAttribute('data-title') || '').toLowerCase();
      const cardDesc = (card.getAttribute('data-desc') || '').toLowerCase();

      // Check category match
      const matchesCategory = (currentCategory === 'all' || cardCategory === currentCategory);

      // Check search match
      const matchesSearch = !currentSearchQuery ||
        cardTitle.includes(currentSearchQuery) ||
        cardDesc.includes(currentSearchQuery) ||
        cardCategory.toLowerCase().includes(currentSearchQuery);

      if (matchesCategory && matchesSearch) {
        card.style.display = 'flex';
        visibleCount++;
      } else {
        card.style.display = 'none';
      }
    });

    if (emptyState) {
      if (visibleCount === 0) {
        emptyState.classList.add('active');
      } else {
        emptyState.classList.remove('active');
      }
    }
  }

  /* --------------------------------------------------------------------------
     3. TOPIC TILE NAVIGATION TRIGGER
     Clicking a topic tile filters the Latest Articles section by that topic
     -------------------------------------------------------------------------- */
  function initTopicTileTriggers() {
    const topicCards = document.querySelectorAll('.blog-topic-card');
    const allTopicsResetBtn = document.getElementById('blogAllTopicsResetBtn');

    topicCards.forEach((tile) => {
      tile.addEventListener('click', (e) => {
        e.preventDefault();
        const targetCategory = tile.getAttribute('data-topic-filter');
        if (!targetCategory) return;

        // Activate matching category button
        const filterButtons = document.querySelectorAll('.blog-filter-btn');
        filterButtons.forEach((btn) => {
          if (btn.getAttribute('data-filter') === targetCategory) {
            btn.classList.add('active');
          } else {
            btn.classList.remove('active');
          }
        });

        currentCategory = targetCategory;
        applyFiltersAndSearch();

        // Smooth scroll to latest articles section
        const latestArticlesSection = document.getElementById('latestArticles');
        if (latestArticlesSection) {
          const headerHeight = document.querySelector('.site-header')?.offsetHeight || 80;
          const targetY = latestArticlesSection.getBoundingClientRect().top + window.pageYOffset - headerHeight;
          window.scrollTo({
            top: targetY,
            behavior: 'smooth'
          });
        }
      });
    });

    if (allTopicsResetBtn) {
      allTopicsResetBtn.addEventListener('click', (e) => {
        e.preventDefault();
        resetAllFilters();
        const latestArticlesSection = document.getElementById('latestArticles');
        if (latestArticlesSection) {
          const headerHeight = document.querySelector('.site-header')?.offsetHeight || 80;
          const targetY = latestArticlesSection.getBoundingClientRect().top + window.pageYOffset - headerHeight;
          window.scrollTo({
            top: targetY,
            behavior: 'smooth'
          });
        }
      });
    }
  }

  /* --------------------------------------------------------------------------
     4. ACCESSIBLE ARTICLE DETAIL MODAL
     -------------------------------------------------------------------------- */
  function initArticleModal() {
    const modalBackdrop = document.getElementById('blogArticleModal');
    const modalCloseBtn = document.getElementById('blogModalCloseBtn');

    if (!modalBackdrop) return;

    // Listen for clicks on Read Article buttons & clickable triggers
    document.addEventListener('click', (e) => {
      const trigger = e.target.closest('[data-article-id]');
      if (!trigger) return;

      e.preventDefault();
      const articleId = trigger.getAttribute('data-article-id');
      const articleData = ARTICLE_DATA[articleId];

      if (articleData) {
        openModal(articleData);
      }
    });

    // Close button
    if (modalCloseBtn) {
      modalCloseBtn.addEventListener('click', (e) => {
        e.preventDefault();
        closeModal();
      });
    }

    // Close on backdrop click (outside modal dialog)
    modalBackdrop.addEventListener('click', (e) => {
      if (e.target === modalBackdrop) {
        closeModal();
      }
    });

    // Close on Escape key press
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && modalBackdrop.classList.contains('active')) {
        closeModal();
      }
    });
  }

  function openModal(article) {
    const modalBackdrop = document.getElementById('blogArticleModal');
    if (!modalBackdrop) return;

    // Populate modal contents
    const catBadge = document.getElementById('blogModalCat');
    const titleEl = document.getElementById('blogModalTitle');
    const readTimeEl = document.getElementById('blogModalReadTime');
    const dateEl = document.getElementById('blogModalDate');
    const imgEl = document.getElementById('blogModalImg');
    const contentEl = document.getElementById('blogModalContent');
    const takeawaysList = document.getElementById('blogModalTakeawaysList');

    if (catBadge) catBadge.textContent = article.category;
    if (titleEl) titleEl.textContent = article.title;
    if (readTimeEl) readTimeEl.textContent = article.readTime;
    if (dateEl) dateEl.textContent = article.date;
    if (imgEl) {
      imgEl.src = article.image;
      imgEl.alt = article.alt || article.title;
    }
    if (contentEl) {
      contentEl.innerHTML = article.content;
    }

    if (takeawaysList && article.takeaways) {
      takeawaysList.innerHTML = article.takeaways
        .map((item) => `<li><i data-lucide="check"></i><span>${item}</span></li>`)
        .join('');
    }

    // Re-render lucide icons inside modal
    if (window.lucide && typeof window.lucide.createIcons === 'function') {
      window.lucide.createIcons();
    }

    // Show modal & prevent background scroll
    modalBackdrop.classList.add('active');
    document.body.style.overflow = 'hidden';

    // Focus close button for accessibility
    const modalCloseBtn = document.getElementById('blogModalCloseBtn');
    if (modalCloseBtn) modalCloseBtn.focus();
  }

  function closeModal() {
    const modalBackdrop = document.getElementById('blogArticleModal');
    if (!modalBackdrop) return;

    modalBackdrop.classList.remove('active');
    document.body.style.overflow = '';
  }

  /* --------------------------------------------------------------------------
     5. JOURNAL NEWSLETTER FORM VALIDATION
     Validates format and explains static architecture honesty (no fake submission)
     -------------------------------------------------------------------------- */
  function initNewsletterForm() {
    const form = document.getElementById('blogNewsletterForm');
    if (!form) return;

    const emailInput = document.getElementById('blogNewsletterEmail');
    const feedbackEl = document.getElementById('blogNewsletterFeedback');

    form.addEventListener('submit', (e) => {
      e.preventDefault();
      if (!emailInput || !feedbackEl) return;

      const email = emailInput.value.trim();
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

      feedbackEl.className = 'blog-newsletter-feedback';

      if (!email) {
        feedbackEl.textContent = 'Please enter your email address to subscribe.';
        feedbackEl.classList.add('active', 'error');
        emailInput.focus();
      } else if (!emailRegex.test(email)) {
        feedbackEl.textContent = 'Please provide a valid email address (e.g. name@domain.com).';
        feedbackEl.classList.add('active', 'error');
        emailInput.focus();
      } else {
        // Honest informative message respecting static architecture requirements
        feedbackEl.textContent = 'Thank you for your interest in The Evergreen Journal. (Frontend demo: Valid email format accepted. Automated email delivery is not connected in this static presentation).';
        feedbackEl.classList.add('active', 'notice');
        emailInput.value = '';

        setTimeout(() => {
          feedbackEl.classList.remove('active');
        }, 7000);
      }
    });
  }

})();
