/**
 * EVERGREEN OUTDOOR LIVING - CONTACT PAGE CONTROLLER
 * Manages the multi-step project enquiry form, location configuration & fallback,
 * interactive accordion, and static demo submission validation.
 */

(function () {
  'use strict';

  /* --------------------------------------------------------------------------
     1. CENTRALISED BUSINESS & MAP CONFIGURATION
     Configure verified business details here. Unconfigured values fall back
     cleanly to graceful placeholders without fabricating fake information.
     -------------------------------------------------------------------------- */
  const BUSINESS_CONFIG = {
    address: "ADD VERIFIED BUSINESS ADDRESS",
    locationName: "ADD VERIFIED BUSINESS LOCATION",
    mapUrl: "ADD VERIFIED GOOGLE MAPS URL",
    directionsUrl: "ADD VERIFIED DIRECTIONS URL",
    serviceArea: "ADD VERIFIED SERVICE AREA"
  };

  /* --------------------------------------------------------------------------
     2. FORM STATE REPOSITORY (In-Session Only - No LocalStorage Persistence)
     -------------------------------------------------------------------------- */
  const enquiryData = {
    fullName: '',
    email: '',
    phone: '',
    contactMethod: 'Email',
    location: '',
    projectTypes: [],
    spaceDescription: '',
    mainGoal: '',
    preferredMaterial: '',
    startingTimeframe: '',
    additionalMessage: '',
    consentAgreed: false
  };

  let currentStep = 1;

  /* --------------------------------------------------------------------------
     3. INITIALIZATION
     -------------------------------------------------------------------------- */
  document.addEventListener('DOMContentLoaded', () => {
    initLocationSection();
    initMultiStepForm();
    initProjectOptionCards();
    initContactAccordion();
  });

  /* --------------------------------------------------------------------------
     4. LOCATION & MAP FALLBACK CONTROLLER
     -------------------------------------------------------------------------- */
  function initLocationSection() {
    const locAddressEl = document.getElementById('contactLocAddress');
    const locServiceAreaEl = document.getElementById('contactLocServiceArea');
    const mapIframe = document.getElementById('contactMapIframe');
    const mapPlaceholder = document.getElementById('contactMapPlaceholder');
    const gmapsBtn = document.getElementById('contactGmapsBtn');
    const directionsBtn = document.getElementById('contactDirectionsBtn');

    // Check if verified address is configured
    const hasVerifiedAddress = BUSINESS_CONFIG.address && !BUSINESS_CONFIG.address.includes("ADD VERIFIED");
    const hasVerifiedServiceArea = BUSINESS_CONFIG.serviceArea && !BUSINESS_CONFIG.serviceArea.includes("ADD VERIFIED");
    const hasVerifiedMapUrl = BUSINESS_CONFIG.mapUrl && !BUSINESS_CONFIG.mapUrl.includes("ADD VERIFIED");
    const hasVerifiedDirections = BUSINESS_CONFIG.directionsUrl && !BUSINESS_CONFIG.directionsUrl.includes("ADD VERIFIED");

    if (locAddressEl) {
      if (hasVerifiedAddress) {
        locAddressEl.textContent = BUSINESS_CONFIG.address;
      } else {
        locAddressEl.textContent = "Business location details will be updated soon upon confirmation.";
      }
    }

    if (locServiceAreaEl) {
      if (hasVerifiedServiceArea) {
        locServiceAreaEl.textContent = BUSINESS_CONFIG.serviceArea;
      } else {
        locServiceAreaEl.textContent = "Service areas available upon project enquiry.";
      }
    }

    // Map embed vs. graceful placeholder
    if (mapIframe && mapPlaceholder) {
      if (hasVerifiedMapUrl) {
        mapIframe.src = BUSINESS_CONFIG.mapUrl;
        mapIframe.style.display = 'block';
        mapPlaceholder.style.display = 'none';
      } else {
        mapIframe.style.display = 'none';
        mapPlaceholder.style.display = 'flex';
      }
    }

    // External action links
    if (gmapsBtn) {
      if (hasVerifiedMapUrl) {
        gmapsBtn.href = BUSINESS_CONFIG.mapUrl;
      } else {
        gmapsBtn.style.opacity = '0.5';
        gmapsBtn.setAttribute('title', 'Map URL will be available once business location is confirmed');
        gmapsBtn.addEventListener('click', (e) => e.preventDefault());
      }
    }

    if (directionsBtn) {
      if (hasVerifiedDirections) {
        directionsBtn.href = BUSINESS_CONFIG.directionsUrl;
      } else {
        directionsBtn.style.opacity = '0.5';
        directionsBtn.setAttribute('title', 'Directions will be available once business location is confirmed');
        directionsBtn.addEventListener('click', (e) => e.preventDefault());
      }
    }
  }

  /* --------------------------------------------------------------------------
     5. MULTI-STEP PROJECT ENQUIRY FORM CONTROLLER
     -------------------------------------------------------------------------- */
  function initMultiStepForm() {
    // Step Elements
    const step1 = document.getElementById('contactStep1');
    const step2 = document.getElementById('contactStep2');
    const step3 = document.getElementById('contactStep3');
    const feedbackBox = document.getElementById('contactFormFeedback');

    // Progress Elements
    const progressFill = document.getElementById('contactProgressFill');
    const progressLabel = document.getElementById('contactProgressLabel');
    const progressStepText = document.getElementById('contactProgressStepText');

    // Action Buttons
    const btnToStep2 = document.getElementById('btnToStep2');
    const btnBackTo1 = document.getElementById('btnBackTo1');
    const btnToStep3 = document.getElementById('btnToStep3');
    const btnBackTo2 = document.getElementById('btnBackTo2');
    const btnSubmitEnquiry = document.getElementById('btnSubmitEnquiry');
    const btnEditEnquiry = document.getElementById('btnEditEnquiry');
    const btnResetForm = document.getElementById('btnResetForm');

    function updateStepView(targetStep) {
      currentStep = targetStep;

      // Toggle steps
      if (step1) step1.classList.toggle('active', currentStep === 1);
      if (step2) step2.classList.toggle('active', currentStep === 2);
      if (step3) step3.classList.toggle('active', currentStep === 3);
      if (feedbackBox) feedbackBox.classList.remove('active');

      // Update progress bar
      if (progressFill && progressLabel && progressStepText) {
        if (currentStep === 1) {
          progressFill.style.width = '33.33%';
          progressLabel.textContent = 'STEP 01 OF 03 – YOUR DETAILS';
          progressStepText.textContent = 'Contact & Location';
        } else if (currentStep === 2) {
          progressFill.style.width = '66.66%';
          progressLabel.textContent = 'STEP 02 OF 03 – YOUR PROJECT';
          progressStepText.textContent = 'Vision & Requirements';
        } else if (currentStep === 3) {
          progressFill.style.width = '100%';
          progressLabel.textContent = 'STEP 03 OF 03 – REVIEW YOUR ENQUIRY';
          progressStepText.textContent = 'Summary & Confirmation';
        }
      }

      // Smooth scroll back to form top if needed
      const formCard = document.querySelector('.contact-form-card');
      if (formCard) {
        const headerHeight = document.querySelector('.site-header')?.offsetHeight || 80;
        const formTop = formCard.getBoundingClientRect().top + window.pageYOffset - headerHeight - 20;
        if (window.scrollY > formTop) {
          window.scrollTo({ top: formTop, behavior: 'smooth' });
        }
      }
    }

    // Step 1 -> Step 2
    if (btnToStep2) {
      btnToStep2.addEventListener('click', (e) => {
        e.preventDefault();
        const nameInput = document.getElementById('enquiryFullName');
        const emailInput = document.getElementById('enquiryEmail');
        const phoneInput = document.getElementById('enquiryPhone');
        const locationInput = document.getElementById('enquiryLocation');
        const methodRadios = document.querySelectorAll('input[name="preferredContact"]');

        const name = nameInput ? nameInput.value.trim() : '';
        const email = emailInput ? emailInput.value.trim() : '';
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

        // Validation
        if (!name) {
          alert('Please enter your full name to continue.');
          if (nameInput) nameInput.focus();
          return;
        }

        if (!email || !emailRegex.test(email)) {
          alert('Please provide a valid email address.');
          if (emailInput) emailInput.focus();
          return;
        }

        enquiryData.fullName = name;
        enquiryData.email = email;
        enquiryData.phone = phoneInput ? phoneInput.value.trim() : '';
        enquiryData.location = locationInput ? locationInput.value.trim() : '';

        methodRadios.forEach((r) => {
          if (r.checked) enquiryData.contactMethod = r.value;
        });

        updateStepView(2);
      });
    }

    // Step 2 -> Step 1
    if (btnBackTo1) {
      btnBackTo1.addEventListener('click', (e) => {
        e.preventDefault();
        updateStepView(1);
      });
    }

    // Step 2 -> Step 3
    if (btnToStep3) {
      btnToStep3.addEventListener('click', (e) => {
        e.preventDefault();
        const spaceDesc = document.getElementById('enquirySpaceDesc');
        const mainGoal = document.getElementById('enquiryMainGoal');
        const material = document.getElementById('enquiryMaterial');
        const timeframe = document.getElementById('enquiryTimeframe');

        enquiryData.spaceDescription = spaceDesc ? spaceDesc.value.trim() : '';
        enquiryData.mainGoal = mainGoal ? mainGoal.value : '';
        enquiryData.preferredMaterial = material ? material.value : '';
        enquiryData.startingTimeframe = timeframe ? timeframe.value : '';

        // Collect project types
        enquiryData.projectTypes = [];
        document.querySelectorAll('.contact-project-option.selected').forEach((opt) => {
          const typeName = opt.getAttribute('data-project-type');
          if (typeName) enquiryData.projectTypes.push(typeName);
        });

        populateReviewSummary();
        updateStepView(3);
      });
    }

    // Step 3 -> Step 2
    if (btnBackTo2) {
      btnBackTo2.addEventListener('click', (e) => {
        e.preventDefault();
        updateStepView(2);
      });
    }

    // Step 3 Submit Enquiry (Static Demo Validation)
    if (btnSubmitEnquiry) {
      btnSubmitEnquiry.addEventListener('click', (e) => {
        e.preventDefault();
        const consentCheckbox = document.getElementById('enquiryConsent');
        const additionalMsg = document.getElementById('enquiryAdditionalMsg');

        if (!consentCheckbox || !consentCheckbox.checked) {
          alert('Please check the consent agreement to proceed with your enquiry.');
          if (consentCheckbox) consentCheckbox.focus();
          return;
        }

        enquiryData.additionalMessage = additionalMsg ? additionalMsg.value.trim() : '';
        enquiryData.consentAgreed = true;

        // Hide Step 3 and show honest static demonstration message
        if (step3) step3.classList.remove('active');
        if (feedbackBox) feedbackBox.classList.add('active');

        // Scroll into view
        feedbackBox.scrollIntoView({ behavior: 'smooth', block: 'center' });
      });
    }

    // Edit My Enquiry Button
    if (btnEditEnquiry) {
      btnEditEnquiry.addEventListener('click', (e) => {
        e.preventDefault();
        updateStepView(1);
      });
    }

    // Reset Form Button
    if (btnResetForm) {
      btnResetForm.addEventListener('click', (e) => {
        e.preventDefault();
        resetEnquiryForm();
      });
    }
  }

  /* --------------------------------------------------------------------------
     6. PROJECT OPTION CARDS SELECTION (Multiselect)
     -------------------------------------------------------------------------- */
  function initProjectOptionCards() {
    const optionCards = document.querySelectorAll('.contact-project-option');

    optionCards.forEach((card) => {
      card.addEventListener('click', (e) => {
        // Toggle selection
        card.classList.toggle('selected');
        const checkbox = card.querySelector('.contact-project-checkbox');
        if (checkbox) {
          checkbox.checked = card.classList.contains('selected');
        }
      });
    });
  }

  /* --------------------------------------------------------------------------
     7. POPULATE REVIEW SUMMARY
     -------------------------------------------------------------------------- */
  function populateReviewSummary() {
    const revName = document.getElementById('revName');
    const revEmail = document.getElementById('revEmail');
    const revPhone = document.getElementById('revPhone');
    const revMethod = document.getElementById('revMethod');
    const revLocation = document.getElementById('revLocation');
    const revProjects = document.getElementById('revProjects');
    const revGoal = document.getElementById('revGoal');
    const revMaterial = document.getElementById('revMaterial');
    const revTimeframe = document.getElementById('revTimeframe');
    const revSpace = document.getElementById('revSpace');

    if (revName) revName.textContent = enquiryData.fullName || '—';
    if (revEmail) revEmail.textContent = enquiryData.email || '—';
    if (revPhone) revPhone.textContent = enquiryData.phone || 'Not provided';
    if (revMethod) revMethod.textContent = enquiryData.contactMethod || 'Email';
    if (revLocation) revLocation.textContent = enquiryData.location || 'Not provided';

    if (revProjects) {
      revProjects.textContent = enquiryData.projectTypes.length > 0 
        ? enquiryData.projectTypes.join(', ') 
        : 'Not specified yet';
    }

    if (revGoal) revGoal.textContent = enquiryData.mainGoal || 'Exploring ideas';
    if (revMaterial) revMaterial.textContent = enquiryData.preferredMaterial || 'Not sure yet';
    if (revTimeframe) revTimeframe.textContent = enquiryData.startingTimeframe || 'Just exploring ideas';
    if (revSpace) revSpace.textContent = enquiryData.spaceDescription || 'No description provided';
  }

  /* --------------------------------------------------------------------------
     8. RESET ENQUIRY FORM
     -------------------------------------------------------------------------- */
  function resetEnquiryForm() {
    const form = document.getElementById('consultationForm');
    if (form) form.reset();

    // Deselect project cards
    document.querySelectorAll('.contact-project-option').forEach((card) => {
      card.classList.remove('selected');
      const chk = card.querySelector('.contact-project-checkbox');
      if (chk) chk.checked = false;
    });

    // Reset state
    enquiryData.fullName = '';
    enquiryData.email = '';
    enquiryData.phone = '';
    enquiryData.contactMethod = 'Email';
    enquiryData.location = '';
    enquiryData.projectTypes = [];
    enquiryData.spaceDescription = '';
    enquiryData.mainGoal = '';
    enquiryData.preferredMaterial = '';
    enquiryData.startingTimeframe = '';
    enquiryData.additionalMessage = '';
    enquiryData.consentAgreed = false;

    // Reset to step 1
    const step1 = document.getElementById('contactStep1');
    const step2 = document.getElementById('contactStep2');
    const step3 = document.getElementById('contactStep3');
    const feedbackBox = document.getElementById('contactFormFeedback');

    if (step1) step1.classList.add('active');
    if (step2) step2.classList.remove('active');
    if (step3) step3.classList.remove('active');
    if (feedbackBox) feedbackBox.classList.remove('active');

    const progressFill = document.getElementById('contactProgressFill');
    const progressLabel = document.getElementById('contactProgressLabel');
    const progressStepText = document.getElementById('contactProgressStepText');

    if (progressFill) progressFill.style.width = '33.33%';
    if (progressLabel) progressLabel.textContent = 'STEP 01 OF 03 – YOUR DETAILS';
    if (progressStepText) progressStepText.textContent = 'Contact & Location';
  }

  /* --------------------------------------------------------------------------
     9. ACCESSIBLE ACCORDION FOR CONTACT FAQS (Section 7)
     -------------------------------------------------------------------------- */
  function initContactAccordion() {
    const accordionButtons = document.querySelectorAll('.contact-faq-btn');

    accordionButtons.forEach((btn) => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        const item = btn.closest('.contact-faq-item');
        const panel = item.querySelector('.contact-faq-panel');
        const isExpanded = btn.getAttribute('aria-expanded') === 'true';

        // Single-open behavior
        const parentList = item.closest('.contact-faq-list');
        if (parentList) {
          parentList.querySelectorAll('.contact-faq-item').forEach((sib) => {
            if (sib !== item) {
              sib.classList.remove('active');
              const sibBtn = sib.querySelector('.contact-faq-btn');
              const sibPanel = sib.querySelector('.contact-faq-panel');
              if (sibBtn) sibBtn.setAttribute('aria-expanded', 'false');
              if (sibPanel) sibPanel.style.maxHeight = null;
            }
          });
        }

        if (isExpanded) {
          item.classList.remove('active');
          btn.setAttribute('aria-expanded', 'false');
          panel.style.maxHeight = null;
        } else {
          item.classList.add('active');
          btn.setAttribute('aria-expanded', 'true');
          panel.style.maxHeight = panel.scrollHeight + 'px';
        }
      });
    });
  }

})();
