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

/* Buy Book from bookstore */

const paymentForms = document.querySelectorAll(".paymentForm"); // Get all elements with the class 'paymentForm'

// Loop through each form and attach the submit event listener
paymentForms.forEach((form) => {
  form.addEventListener(
    "submit",
    function (e) {
      e.preventDefault();

      const book_id = form.getAttribute("data-book-id"); // Get the book_id from the form's data attribute

      payWithPaystack(book_id); // Call payWithPaystack with the book_id
    },
    false
  );
});

function payWithPaystack(book_id) {
  console.log(book_id);
  let handler = PaystackPop.setup({
    key: "pk_test_244916c0bd11624711bdab398418c05413687296", // Replace with your public key
    email: document.getElementById("email-address" + book_id).value,
    amount: Number(document.getElementById("amount" + book_id).value) * 100,
    ref: "" + Math.floor(Math.random() * 1000000000 + 1),
    metadata: {
      book_id: book_id,
      custom_fields: [
        {
          display_name: "Buyer",
          variable_name: "buyer",
          value: document.getElementById("name" + book_id).value,
        },
        {
          display_name: "Book Title",
          variable_name: "book_title",
          value: document.getElementById("description" + book_id).value,
        },
      ],
    },
    onClose: function () {
      alert("Transaction Cancelled.");
    },
    callback: function (response) {
      let message =
        document.getElementById("description" + book_id).value +
        " Payment complete! Reference: " +
        response.reference;
      alert(message);
    },
  });

  handler.openIframe();
}

/* Make donation */
const donationForm = document.getElementById("donationForm");
donationForm.addEventListener("submit", donateWithPaystack, false);

function donateWithPaystack() {
  let handler = PaystackPop.setup({
    key: "pk_test_244916c0bd11624711bdab398418c05413687296", // Replace with your public key
    email: document.getElementById("donor-email").value,
    amount: Number(document.getElementById("donation-amount").value) * 100,
    ref: "" + Math.floor(Math.random() * 1000000000 + 1),
    metadata: {
      custom_fields: [
        {
          display_name: "Donor",
          variable_name: "Donor",
          value: document.getElementById("donor").value,
        },
        {
          display_name: "Donation Description",
          variable_name: "donation_description",
          value: document.getElementById("donation-description").value,
        },
      ],
    },
    onClose: function () {
      alert("Payment Cancelled.");
    },
    callback: function (response) {
      let message =
        document.getElementById("donation-description").value +
        " Payment complete! Reference: " +
        response.reference;
      alert(message);
    },
  });

  handler.openIframe();
}
