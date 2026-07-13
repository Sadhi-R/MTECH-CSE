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
