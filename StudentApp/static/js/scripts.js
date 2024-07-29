// Dark-Mode
const toggleDarkMode = document.getElementById('toggleDarkMode');
const body = document.body;
const sidebarElement = document.querySelector('.sidebar');
const mainContent = document.querySelector('.main-content');
const toggleIcon = document.getElementById('toggleDark');

toggleDarkMode.addEventListener('click', function() {
  body.classList.toggle('dark-mode');
  sidebarElement.classList.toggle('dark-mode');
  mainContent.classList.toggle('dark-mode');

  if (body.classList.contains('dark-mode')) {
    toggleIcon.classList.replace('bi-moon-fill', 'bi-sun-fill');
  } else {
    toggleIcon.classList.replace('bi-sun-fill', 'bi-moon-fill');
  }
});