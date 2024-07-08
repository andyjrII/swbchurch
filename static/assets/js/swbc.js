// smooth scroll
$(document).ready(function () {
  $('.navbar .nav-link').on('click', function (event) {
    if (this.hash !== '') {
      event.preventDefault();

      var hash = this.hash;

      $('html, body').animate(
        {
          scrollTop: $(hash).offset().top,
        },
        700,
        function () {
          window.location.hash = hash;
        }
      );
    }
  });
});

new WOW().init();

function toggleOverlay(imageContainer) {
  var overlay = imageContainer.querySelector('.large-overlay');
  var isVisible = overlay.classList.contains('visible');

  if (!isVisible) {
    overlay.classList.add('visible');
  } else {
    overlay.classList.remove('visible');
  }
}

document.addEventListener('DOMContentLoaded', function () {
  // Get references to the menu and toggle button
  var menu = document.getElementById('navbarSupportedContent');
  var toggleButton = document.getElementById('menu-toggle');

  // Add click event listener to each menu item
  var menuItems = menu.querySelectorAll('.nav-link');
  menuItems.forEach(function (item) {
    item.addEventListener('click', function () {
      // Check if menu is open (i.e., not collapsed into hamburger menu)
      if (menu.classList.contains('show')) {
        // Close the menu by removing the "show" class
        menu.classList.remove('show');
        toggleButton.classList.add('collapsed'); // Reset the collapsed state of the toggle button
      }
    });
  });

  // Add click event listener to the toggle button
  toggleButton.addEventListener('click', function () {
    // Toggle the "show" class on the menu to show/hide it
    menu.classList.toggle('show');
  });
});
