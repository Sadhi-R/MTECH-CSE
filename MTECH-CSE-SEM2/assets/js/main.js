/* Shared site behavior */
(function () {
  const progress = document.getElementById('scroll-progress');
  const backTop = document.getElementById('back-top');
  const navToggle = document.getElementById('nav-toggle');
  const navLinks = document.getElementById('nav-links');
  const navbar = document.querySelector('.navbar');

  window.addEventListener('scroll', () => {
    const h = document.documentElement;
    const scrolled = (h.scrollTop / (h.scrollHeight - h.clientHeight)) * 100;
    if (progress) progress.style.width = scrolled + '%';
    if (backTop) backTop.classList.toggle('show', window.scrollY > 400);
    if (navbar) navbar.classList.toggle('scrolled', window.scrollY > 20);
  }, { passive: true });

  if (backTop) backTop.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));
  if (navToggle && navLinks) {
    navToggle.addEventListener('click', () => {
      const open = navLinks.classList.toggle('open');
      navToggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      navToggle.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    });
    navLinks.querySelectorAll('a').forEach((a) => {
      a.addEventListener('click', () => {
        navLinks.classList.remove('open');
        navToggle.setAttribute('aria-expanded', 'false');
        navToggle.setAttribute('aria-label', 'Open menu');
      });
    });
  }

  // Scroll reveal
  const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (!prefersReduced && 'IntersectionObserver' in window) {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add('visible');
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.08, rootMargin: '0px 0px -40px 0px' }
    );
    document.querySelectorAll('.reveal').forEach((el) => observer.observe(el));
  } else {
    document.querySelectorAll('.reveal').forEach((el) => el.classList.add('visible'));
  }

  // Tabs
  document.querySelectorAll('[data-tabs]').forEach((group) => {
    const buttons = group.querySelectorAll('.tab-btn');
    const panels = group.querySelectorAll('.tab-panel');
    buttons.forEach((btn) => {
      btn.addEventListener('click', () => {
        const id = btn.dataset.tab;
        buttons.forEach((b) => b.classList.remove('active'));
        panels.forEach((p) => p.classList.remove('active'));
        btn.classList.add('active');
        const panel = group.querySelector('#' + id);
        if (panel) panel.classList.add('active');
      });
    });
  });

  // Persist checklist state
  document.querySelectorAll('.checklist input[type=checkbox]').forEach((cb) => {
    const key = 'chk_' + (cb.id || cb.dataset.key || cb.nextSibling?.textContent?.slice(0, 40));
    if (localStorage.getItem(key) === '1') cb.checked = true;
    cb.addEventListener('change', () => localStorage.setItem(key, cb.checked ? '1' : '0'));
  });

  // Highlight active sidebar link by hash
  function syncSidebar() {
    const hash = location.hash;
    if (!hash) return;
    document.querySelectorAll('.sidebar a').forEach((a) => {
      a.classList.toggle('active', a.getAttribute('href') === hash);
    });
  }
  window.addEventListener('hashchange', syncSidebar);
  syncSidebar();
})();

function getBasePath() {
  const path = location.pathname.replace(/\\/g, '/');
  if (path.includes('/subjects/')) return '../../';
  if (path.includes('/search/')) return '../';
  return './';
}
