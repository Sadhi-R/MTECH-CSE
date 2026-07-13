/* Client-side login gate (sessionStorage). Not server-grade security. */
(function () {
  const AUTH_KEY = 'mtech_cse_authenticated';
  const VALID_EMAIL = 'sadhiramtenki@gmail.com';
  const VALID_PASS = 'Sadhi@123$';

  function isLoginPage() {
    return document.body.classList.contains('login-page');
  }

  function isAuthenticated() {
    return sessionStorage.getItem(AUTH_KEY) === '1';
  }

  function siteRootUrl() {
    const p = window.location.pathname.replace(/\\/g, '/');
    if (p.includes('/subjects/')) return p.split('/subjects/')[0] + '/';
    if (p.includes('/search/')) return p.split('/search/')[0] + '/';
    const last = p.lastIndexOf('/');
    return last >= 0 ? p.slice(0, last + 1) : '/';
  }

  function loginUrl() {
    return siteRootUrl() + 'index.html';
  }

  function homeUrl() {
    return siteRootUrl() + 'home.html';
  }

  function requireAuth() {
    if (isLoginPage()) {
      if (isAuthenticated()) window.location.replace(homeUrl());
      return;
    }
    if (!isAuthenticated()) {
      window.location.replace(loginUrl());
    }
  }

  function setupLoginForm() {
    const form = document.getElementById('login-form');
    if (!form) return;

    const passInput = document.getElementById('login-password');
    const toggleBtn = document.getElementById('password-toggle');
    if (toggleBtn && passInput) {
      toggleBtn.addEventListener('click', function () {
        const show = passInput.type === 'password';
        passInput.type = show ? 'text' : 'password';
        toggleBtn.setAttribute('aria-label', show ? 'Hide password' : 'Show password');
        toggleBtn.innerHTML = show
          ? '<svg width="18" height="18" class="icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94"/><path d="M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19"/><line x1="1" y1="1" x2="23" y2="23"/></svg>'
          : '<svg width="18" height="18" class="icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg>';
      });
    }

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      const email = (document.getElementById('login-email')?.value || '').trim().toLowerCase();
      const pass = document.getElementById('login-password')?.value || '';
      const err = document.getElementById('login-error');
      if (email === VALID_EMAIL && pass === VALID_PASS) {
        sessionStorage.setItem(AUTH_KEY, '1');
        window.location.href = homeUrl();
        return;
      }
      if (err) {
        err.textContent = 'Invalid email or password. Please try again.';
        err.hidden = false;
      }
    });
  }

  function setupLogout() {
    document.querySelectorAll('[data-logout]').forEach(function (btn) {
      btn.addEventListener('click', function (e) {
        e.preventDefault();
        sessionStorage.removeItem(AUTH_KEY);
        window.location.href = loginUrl();
      });
    });
  }

  requireAuth();
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () {
      setupLoginForm();
      setupLogout();
    });
  } else {
    setupLoginForm();
    setupLogout();
  }
})();
