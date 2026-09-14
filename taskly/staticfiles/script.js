/* =========================================================
   Ledger — dark/light theme toggle
   This file does ONE job: switch data-theme and remember the
   choice. It never reads, sends, or mutates task data — every
   add/complete/delete action is a plain HTML form POST handled
   by Django views.
   ========================================================= */

(function () {
  const root = document.documentElement;
  const themeSwitch = document.getElementById('themeSwitch');
  const STORAGE_KEY = 'ledger-theme';

  function applyTheme(theme) {
    root.setAttribute('data-theme', theme);
    if (themeSwitch) {
      themeSwitch.setAttribute('aria-pressed', String(theme === 'dark'));
    }
  }

  const saved = localStorage.getItem(STORAGE_KEY);
  if (saved) {
    applyTheme(saved);
  } else if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
    applyTheme('dark');
  }

  if (themeSwitch) {
    themeSwitch.addEventListener('click', function () {
      const current = root.getAttribute('data-theme') === 'dark' ? 'dark' : 'light';
      const next = current === 'dark' ? 'light' : 'dark';
      applyTheme(next);
      localStorage.setItem(STORAGE_KEY, next);
    });
  }

  window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
    if (!localStorage.getItem(STORAGE_KEY)) {
      applyTheme(e.matches ? 'dark' : 'light');
    }
  });
})();
