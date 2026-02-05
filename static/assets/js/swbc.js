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
  // Close mobile menu when a nav link is clicked (Bootstrap 5 handles the toggler itself)
  var menu = document.getElementById('navbarSupportedContent');
  if (!menu) return;

  var menuItems = menu.querySelectorAll('.nav-link');
  menuItems.forEach(function (item) {
    item.addEventListener('click', function () {
      if (window.bootstrap && menu.classList.contains('show')) {
        var collapse = bootstrap.Collapse.getInstance(menu);
        if (collapse) collapse.hide();
      }
    });
  });
});
