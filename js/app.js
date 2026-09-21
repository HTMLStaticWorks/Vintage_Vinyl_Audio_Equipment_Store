/* Needle & Groove — Luxury Vintage Vinyl & Audiophile Boutique JS */

document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  initRTL();
  initHeader();
  initActiveNav();
  initScrollToTop();
  initAudioPreviews();
  initForms();
  initTabs();
  initTimeline();
});

/* ----------------------------------------------------
   1. Theme Management (Dark / Light)
---------------------------------------------------- */
function initTheme() {
  const savedTheme = localStorage.getItem('ng_theme');
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  
  if (savedTheme === 'dark' || (!savedTheme && prefersDark)) {
    document.documentElement.classList.add('dark');
  } else {
    document.documentElement.classList.remove('dark');
  }

  const themeToggles = document.querySelectorAll('.theme-toggle-btn');
  themeToggles.forEach(btn => {
    btn.addEventListener('click', () => {
      const isDark = document.documentElement.classList.toggle('dark');
      localStorage.setItem('ng_theme', isDark ? 'dark' : 'light');
      showToast(isDark ? 'Dark Mode Activated' : 'Light Mode Activated', 'info');
    });
  });
}

/* ----------------------------------------------------
   2. RTL Management
---------------------------------------------------- */
function initRTL() {
  const savedRTL = localStorage.getItem('ng_rtl');
  if (savedRTL === 'rtl') {
    document.documentElement.setAttribute('dir', 'rtl');
  } else {
    document.documentElement.setAttribute('dir', 'ltr');
  }

  const rtlToggles = document.querySelectorAll('.rtl-toggle-btn');
  rtlToggles.forEach(btn => {
    btn.addEventListener('click', () => {
      const currentDir = document.documentElement.getAttribute('dir');
      const newDir = currentDir === 'rtl' ? 'ltr' : 'rtl';
      document.documentElement.setAttribute('dir', newDir);
      localStorage.setItem('ng_rtl', newDir);
      showToast(newDir === 'rtl' ? 'RTL Layout Enabled' : 'LTR Layout Enabled', 'info');
    });
  });
}

/* ----------------------------------------------------
   3. Header & Mobile Menu
---------------------------------------------------- */
function initHeader() {
  const header = document.getElementById('main-header');
  const mobileMenuBtn = document.getElementById('mobile-menu-btn');
  const mobileMenu = document.getElementById('mobile-menu');
  const mobileMenuClose = document.getElementById('mobile-menu-close');

  if (header) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 40) {
        header.classList.add('shadow-md', 'py-3');
        header.classList.remove('py-5');
      } else {
        header.classList.remove('shadow-md');
        header.classList.add('py-5');
        header.classList.remove('py-3');
      }
    });
  }

  if (mobileMenuBtn && mobileMenu) {
    mobileMenuBtn.addEventListener('click', () => {
      mobileMenu.classList.remove('hidden');
      document.body.style.overflow = 'hidden';
    });
  }

  if (mobileMenuClose && mobileMenu) {
    mobileMenuClose.addEventListener('click', () => {
      mobileMenu.classList.add('hidden');
      document.body.style.overflow = '';
    });
  }

  if (mobileMenu) {
    mobileMenu.addEventListener('click', (e) => {
      if (e.target === mobileMenu) {
        mobileMenu.classList.add('hidden');
        document.body.style.overflow = '';
      }
    });
  }
}

/* ----------------------------------------------------
   4. Active Navigation Indicator
---------------------------------------------------- */
function initActiveNav() {
  const currentPath = window.location.pathname.split('/').pop() || 'index.html';
  const navLinks = document.querySelectorAll('.nav-link');
  
  navLinks.forEach(link => {
    const href = link.getAttribute('href');
    if (href === currentPath || (currentPath === '' && href === 'index.html')) {
      link.classList.add('text-brass', 'font-semibold', 'active-link');
      link.setAttribute('aria-current', 'page');
    } else {
      link.classList.remove('text-brass', 'font-semibold', 'active-link');
      link.removeAttribute('aria-current');
    }
  });
}

/* ----------------------------------------------------
   5. Scroll to Top Button
---------------------------------------------------- */
function initScrollToTop() {
  let scrollBtn = document.getElementById('scroll-to-top');
  
  if (!scrollBtn) {
    scrollBtn = document.createElement('button');
    scrollBtn.id = 'scroll-to-top';
    scrollBtn.className = 'fixed bottom-6 right-6 z-50 p-3.5 rounded-full bg-brass text-white shadow-lg opacity-0 pointer-events-none transition-all duration-300 hover:bg-copper focus:outline-none focus:ring-2 focus:ring-brass';
    scrollBtn.setAttribute('aria-label', 'Scroll to top');
    scrollBtn.innerHTML = `
      <svg class="w-5 h-5 rtl-mirror" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 10l7-7m0 0l7 7m-7-7v18"/>
      </svg>
    `;
    document.body.appendChild(scrollBtn);
  }

  window.addEventListener('scroll', () => {
    if (window.scrollY > 350) {
      scrollBtn.classList.remove('opacity-0', 'pointer-events-none');
      scrollBtn.classList.add('opacity-100', 'pointer-events-auto');
    } else {
      scrollBtn.classList.add('opacity-0', 'pointer-events-none');
      scrollBtn.classList.remove('opacity-100', 'pointer-events-auto');
    }
  });

  scrollBtn.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
}

/* ----------------------------------------------------
   6. Audio Preview Widgets
---------------------------------------------------- */
let currentAudio = null;

function initAudioPreviews() {
  const playBtns = document.querySelectorAll('.play-preview-btn');
  
  playBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const card = btn.closest('.record-card') || btn.closest('.preview-container');
      const vinylDisc = card ? card.querySelector('.vinyl-disc') : null;
      const trackTitle = btn.dataset.track || 'Vinyl Sample Audio';
      
      const isPlaying = btn.classList.contains('playing');
      
      // Stop any other active buttons
      playBtns.forEach(b => {
        b.classList.remove('playing');
        b.innerHTML = `
          <svg class="w-4 h-4 text-current" fill="currentColor" viewBox="0 0 20 20">
            <path d="M6.3 2.841A1.5 1.5 0 004 4.11v11.78a1.5 1.5 0 002.3 1.269l9.344-5.89a1.5 1.5 0 000-2.538L6.3 2.84z"/>
          </svg>
          <span>Listen Sample</span>
        `;
        const c = b.closest('.record-card') || b.closest('.preview-container');
        const disc = c ? c.querySelector('.vinyl-disc') : null;
        if (disc) disc.classList.add('paused');
      });

      if (!isPlaying) {
        btn.classList.add('playing');
        btn.innerHTML = `
          <svg class="w-4 h-4 text-current animate-pulse" fill="currentColor" viewBox="0 0 20 20">
            <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zM7 8a1 1 0 012 0v4a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v4a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd"/>
          </svg>
          <span>Playing...</span>
        `;
        if (vinylDisc) vinylDisc.classList.remove('paused');
        showToast(`Playing high-fidelity sample: ${trackTitle}`, 'music');
      } else {
        if (vinylDisc) vinylDisc.classList.add('paused');
        showToast('Playback paused', 'info');
      }
    });
  });
}

/* ----------------------------------------------------
   7. Form Validation & Submissions
---------------------------------------------------- */
function initForms() {
  // Contact Form
  const contactForm = document.getElementById('contact-form');
  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const name = contactForm.querySelector('#contact-name')?.value.trim();
      const email = contactForm.querySelector('#contact-email')?.value.trim();
      const message = contactForm.querySelector('#contact-message')?.value.trim();

      if (!name || !email || !message) {
        showToast('Please fill out all required fields.', 'error');
        return;
      }

      if (!validateEmail(email)) {
        showToast('Please provide a valid email address.', 'error');
        return;
      }

      showToast('Thank you! Your enquiry has been received. Our curator will contact you shortly.', 'success');
      contactForm.reset();
    });
  }

  // Listening Room Form
  const listeningForm = document.getElementById('listening-room-form');
  if (listeningForm) {
    listeningForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const date = listeningForm.querySelector('#session-date')?.value;
      const guests = listeningForm.querySelector('#session-guests')?.value;

      if (!date) {
        showToast('Please select your preferred listening date.', 'error');
        return;
      }

      showToast(`Listening Lounge session reserved for ${guests || 1} guest(s). Confirmation sent to your email!`, 'success');
      listeningForm.reset();
    });
  }

  // Sell Collection Form
  const sellForm = document.getElementById('sell-collection-form');
  if (sellForm) {
    sellForm.addEventListener('submit', (e) => {
      e.preventDefault();
      showToast('Appraisal request submitted. Our senior cataloguer will review your records within 24 hours.', 'success');
      sellForm.reset();
    });
  }

  // Login Form
  const loginForm = document.getElementById('login-form');
  if (loginForm) {
    loginForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const email = loginForm.querySelector('#login-email')?.value.trim();
      const password = loginForm.querySelector('#login-password')?.value.trim();

      if (!email || !password) {
        showToast('Please enter both email and password.', 'error');
        return;
      }
      if (!validateEmail(email)) {
        showToast('Please enter a valid email address.', 'error');
        return;
      }

      showToast('Login successful! Welcome back to Needle & Groove.', 'success');
      setTimeout(() => {
        window.location.href = 'index.html';
      }, 1200);
    });
  }

  // Signup Form
  const signupForm = document.getElementById('signup-form');
  if (signupForm) {
    signupForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const name = signupForm.querySelector('#signup-name')?.value.trim();
      const email = signupForm.querySelector('#signup-email')?.value.trim();
      const pass = signupForm.querySelector('#signup-password')?.value;
      const confirmPass = signupForm.querySelector('#signup-confirm-password')?.value;
      const terms = signupForm.querySelector('#signup-terms')?.checked;

      if (!name || !email || !pass || !confirmPass) {
        showToast('Please fill in all mandatory fields.', 'error');
        return;
      }
      if (!validateEmail(email)) {
        showToast('Please enter a valid email address.', 'error');
        return;
      }
      if (pass.length < 8) {
        showToast('Password must be at least 8 characters long.', 'error');
        return;
      }
      if (pass !== confirmPass) {
        showToast('Passwords do not match.', 'error');
        return;
      }
      if (!terms) {
        showToast('Please accept the Collector Terms & Conditions.', 'error');
        return;
      }

      showToast('Account created successfully! Redirecting to boutique home...', 'success');
      setTimeout(() => {
        window.location.href = 'index.html';
      }, 1400);
    });
  }

  // Newsletter Forms
  const newsletterForms = document.querySelectorAll('.newsletter-form');
  newsletterForms.forEach(form => {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const input = form.querySelector('input[type="email"]');
      if (input && input.value && validateEmail(input.value)) {
        showToast('Welcome to the Needle & Groove Society newsletter.', 'success');
        input.value = '';
      } else {
        showToast('Please enter a valid email address.', 'error');
      }
    });
  });
}

function validateEmail(email) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

/* ----------------------------------------------------
   8. Tabs Systems (Genre Atlas, Blog Categories)
---------------------------------------------------- */
function initTabs() {
  const tabContainers = document.querySelectorAll('[data-tabs-container]');
  
  tabContainers.forEach(container => {
    const tabs = container.querySelectorAll('[data-tab-target]');
    const contents = container.querySelectorAll('[data-tab-content]');

    tabs.forEach(tab => {
      tab.addEventListener('click', () => {
        const target = tab.dataset.tabTarget;

        tabs.forEach(t => {
          t.classList.remove('bg-brass', 'text-white', 'border-brass');
          t.classList.add('bg-secondary', 'text-muted', 'border-border-color');
        });

        tab.classList.add('bg-brass', 'text-white', 'border-brass');
        tab.classList.remove('bg-secondary', 'text-muted', 'border-border-color');

        contents.forEach(c => {
          if (c.dataset.tabContent === target || target === 'all') {
            c.classList.remove('hidden');
          } else {
            c.classList.add('hidden');
          }
        });
      });
    });
  });
}

/* ----------------------------------------------------
   9. Home 2 Interactive Timeline
---------------------------------------------------- */
function initTimeline() {
  const timelineButtons = document.querySelectorAll('.timeline-era-btn');
  const eraPanels = document.querySelectorAll('.era-panel');

  if (timelineButtons.length > 0 && eraPanels.length > 0) {
    timelineButtons.forEach(btn => {
      btn.addEventListener('click', () => {
        const era = btn.dataset.era;

        timelineButtons.forEach(b => {
          b.classList.remove('border-brass', 'text-brass', 'bg-brass/10', 'font-bold');
          b.classList.add('border-transparent', 'text-muted');
        });

        btn.classList.add('border-brass', 'text-brass', 'bg-brass/10', 'font-bold');
        btn.classList.remove('border-transparent', 'text-muted');

        eraPanels.forEach(panel => {
          if (panel.id === `era-${era}`) {
            panel.classList.remove('hidden');
          } else {
            panel.classList.add('hidden');
          }
        });
      });
    });
  }
}

/* ----------------------------------------------------
   10. Toast Notification System
---------------------------------------------------- */
function showToast(message, type = 'info') {
  let container = document.getElementById('toast-container');
  if (!container) {
    container = document.createElement('div');
    container.id = 'toast-container';
    document.body.appendChild(container);
  }

  const toast = document.createElement('div');
  toast.className = 'toast';

  let icon = `
    <svg class="w-5 h-5 text-brass" fill="none" stroke="currentColor" viewBox="0 0 24 24">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
    </svg>
  `;

  if (type === 'success') {
    icon = `
      <svg class="w-5 h-5 text-emerald-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
      </svg>
    `;
  } else if (type === 'error') {
    icon = `
      <svg class="w-5 h-5 text-rose-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
      </svg>
    `;
  } else if (type === 'music') {
    icon = `
      <svg class="w-5 h-5 text-copper animate-bounce" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19V6l12-3v13M9 19c0 1.105-1.343 2-3 2s-3-.895-3-2 1.343-2 3-2 3 .895 3 2zm12 0c0 1.105-1.343 2-3 2s-3-.895-3-2 1.343-2 3-2 3 .895 3 2zM9 10l12-3"/>
      </svg>
    `;
  }

  toast.innerHTML = `
    ${icon}
    <span class="text-xs md:text-sm font-medium leading-tight">${message}</span>
  `;

  container.appendChild(toast);

  setTimeout(() => {
    toast.style.opacity = '0';
    toast.style.transform = 'translateY(20px)';
    toast.style.transition = 'all 0.3s ease';
    setTimeout(() => toast.remove(), 300);
  }, 4000);
}
