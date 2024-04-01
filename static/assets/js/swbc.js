// smooth scroll
$(document).ready(function () {
  $(".navbar .nav-link").on("click", function (event) {
    if (this.hash !== "") {
      event.preventDefault();

      var hash = this.hash;

      $("html, body").animate(
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
  var overlay = imageContainer.querySelector(".large-overlay");
  var isVisible = overlay.classList.contains("visible");

  if (!isVisible) {
    overlay.classList.add("visible");
  } else {
    overlay.classList.remove("visible");
  }
}