// Local-only additions. Original UI bundles remain in build/assets.

// Ensure clean original theme (clear any legacy storage)
try {
  localStorage.removeItem('alira-theme');
  sessionStorage.removeItem('alira-theme');
  document.documentElement.removeAttribute('data-theme');
} catch (e) {}

// On browser refresh, redirect to home page and reset loader
try {
  var nav = performance.getEntriesByType && performance.getEntriesByType('navigation')[0];
  var isRel = (nav && nav.type === 'reload') || (performance.navigation && performance.navigation.type === 1);
  if (isRel) {
    sessionStorage.removeItem('pd-seen');
    document.documentElement.classList.remove('no-loader');
    if (window.location.pathname !== '/' && window.location.pathname !== '/index.html') {
      window.location.replace('/');
    }
  }
} catch (e) {}

if (new URLSearchParams(window.location.search).has('loader') || window.location.hash === '#loader') {
  try {
    sessionStorage.removeItem('pd-seen');
    document.documentElement.classList.remove('no-loader');
  } catch (e) {}
}

document.addEventListener('submit', function (event) {
  event.preventDefault(); event.stopImmediatePropagation();
  let message = event.target.querySelector('[data-demo-result]');
  if (!message) { message = document.createElement('p'); message.dataset.demoResult = ''; message.setAttribute('role', 'status'); event.target.append(message); }
  message.textContent = 'Demo only: your enquiry has not been sent. Connect your own contact service before publishing.';
}, true);

document.addEventListener('DOMContentLoaded', function () {
  const form = document.querySelector('#enquiry');
  if (form) { const note = document.createElement('p'); note.textContent = 'Local demonstration — this form does not send enquiries.'; note.style.cssText = 'padding:14px;border:1px solid #45b66b;border-radius:12px;margin-bottom:20px'; form.prepend(note); }
  document.querySelectorAll('a[href]').forEach(function(a) {
    if (/^https?:/.test(a.href) && a.origin !== location.origin) {
      a.title = (a.title ? a.title + ' — ' : '') + 'External link: requires internet';
      a.rel = 'noopener noreferrer';
    }
  });
});
