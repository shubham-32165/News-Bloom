let isScrolling;
window.addEventListener('scroll', function () {
  window.clearTimeout(isScrolling);
  document.documentElement.style.setProperty('--scrollbar-color', 'var(--text)');
  isScrolling = setTimeout(function () {
    document.documentElement.style.setProperty('--scrollbar-color', 'transparent');
  }, 300); 
});