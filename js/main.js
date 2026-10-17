// Keep copyright dates current without manual edits.
document.querySelectorAll('[data-year]').forEach((element) => {
  element.textContent = new Date().getFullYear();
});

// Mobile navigation: update visual state and accessible expanded state together.
const menuButton = document.querySelector('.menu-toggle');
const menu = document.querySelector('#primary-nav');
if (menuButton && menu) {
  const closeMenu = () => {
    menu.classList.remove('open');
    menuButton.setAttribute('aria-expanded', 'false');
    menuButton.setAttribute('aria-label', 'Open navigation');
  };
  menuButton.addEventListener('click', () => {
    const isOpen = menu.classList.toggle('open');
    menuButton.setAttribute('aria-expanded', String(isOpen));
    menuButton.setAttribute('aria-label', isOpen ? 'Close navigation' : 'Open navigation');
  });
  menu.querySelectorAll('a').forEach((link) => link.addEventListener('click', closeMenu));
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') closeMenu();
  });
}

// Close the mobile menu when clicking outside it.
if (menuButton && menu) {
  document.addEventListener('click', (event) => {
    if (!menuButton.contains(event.target) && !menu.contains(event.target)) {
      menu.classList.remove('open');
      menuButton.setAttribute('aria-expanded', 'false');
      menuButton.setAttribute('aria-label', 'Open navigation');
    }
  });
}
