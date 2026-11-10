// Local portfolio interactivity: theme toggle and ScrollReveal initialization.
document.addEventListener('DOMContentLoaded', () => {
  const root = document.documentElement;
  const toggle = document.getElementById('theme-toggle');
  const label = document.getElementById('theme-label');
  const icon = document.getElementById('theme-icon');
  const storageKey = 'portfolio-theme';
  const systemTheme = window.matchMedia('(prefers-color-scheme: dark)');

  function readSavedTheme() {
    try {
      const saved = localStorage.getItem(storageKey);
      return saved === 'dark' || saved === 'light' ? saved : null;
    } catch {
      return null;
    }
  }

  function setTheme(theme) {
    const dark = theme === 'dark';
    root.dataset.theme = theme;
    toggle.setAttribute('aria-pressed', String(dark));
    toggle.setAttribute('aria-label', dark ? 'Switch to light mode' : 'Switch to dark mode');
    label.textContent = dark ? 'Light mode' : 'Dark mode';
    icon.textContent = dark ? '☀' : '☾';
    const meta = document.querySelector('meta[name="theme-color"]');
    if (meta) meta.setAttribute('content', dark ? '#12382e' : '#18453b');
  }

  if (toggle && label && icon) {
    setTheme(readSavedTheme() || (systemTheme.matches ? 'dark' : 'light'));
    toggle.addEventListener('click', () => {
      const next = root.dataset.theme === 'dark' ? 'light' : 'dark';
      setTheme(next);
      try {
        localStorage.setItem(storageKey, next);
      } catch {
        // Continue without persistence if storage is disabled.
      }
    });
  }

  // Respect the user's reduced-motion preference.
  if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches && typeof ScrollReveal === 'function') {
    const sr = ScrollReveal({ reset: false, distance: '16px', duration: 650, easing: 'ease-out', viewFactor: 0.08 });
    sr.reveal('#about, #contact');
    sr.reveal('#projects article', { interval: 90, origin: 'bottom' });
  }
});
