/*
 * Buy Book from bookstore
 */
const paymentForms = document.querySelectorAll('.paymentForm'); // Get all elements with the class 'paymentForm'

// Loop through each form and attach the submit event listener
paymentForms.forEach((form) => {
  form.addEventListener(
    'submit',
    function (e) {
      e.preventDefault();

      const book_id = form.getAttribute('data-book-id'); // Get the book_id from the form's data attribute

      payWithPaystack(book_id); // Call payWithPaystack with the book_id
    },
    false
  );
});

function payWithPaystack(book_id) {
  let handler = PaystackPop.setup({
    key: 'pk_test_244916c0bd11624711bdab398418c05413687296', // Replace with your public key
    email: document.getElementById('email-address' + book_id).value,
    amount: Number(document.getElementById('amount' + book_id).value) * 100,
    ref: '' + Math.floor(Math.random() * 1000000000 + 1),
    metadata: {
      book_id: book_id,
      custom_fields: [
        {
          display_name: 'Buyer',
          variable_name: 'buyer',
          value: document.getElementById('name' + book_id).value,
        },
        {
          display_name: 'Book Title',
          variable_name: 'book_title',
          value: document.getElementById('description' + book_id).value,
        },
      ],
    },
    onClose: function () {
      alert('Transaction Cancelled.');
    },
    callback: function (response) {
      let message =
        document.getElementById('description' + book_id).value +
        ' Payment complete! Check your e-mail... Reference: ' +
        response.reference;
      alert(message);
      let email = document.getElementById('email-address' + book_id).value;
      sendTransactionIdToBackend(response.reference, book_id, email);
    },
  });

  handler.openIframe();
}

// Frontend JavaScript code using jQuery for AJAX
function sendTransactionIdToBackend(transactionId, bookId, email) {
  // Get the CSRF token from the cookie
  var csrftoken = getCSRFToken();

  // Send the AJAX request
  sendAjaxRequest(
    '/books/handle_payment_success/',
    'POST',
    {
      transaction_id: transactionId,
      book_id: bookId,
      buyer_email: email,
    },
    csrftoken,
    function (response) {
      if (response.success) {
        alert(
          `Book purchase successful! Check ${buyer_email} for your book. Check spam if not found in inbox!`
        );
      } else {
        alert('Failed to purchase book: ' + response.error);
      }
    },
    function (xhr, status, error) {
      console.error('AJAX request failed:', error);
    }
  );
}

// Function to retrieve CSRF token from cookies
function getCSRFToken() {
  var csrftoken = null;
  var cookies = document.cookie.split(';');

  for (var i = 0; i < cookies.length; i++) {
    var cookie = cookies[i].trim();
    if (cookie.startsWith('csrftoken=')) {
      csrftoken = cookie.substring('csrftoken='.length);
      break;
    }
  }

  return csrftoken;
}

// Function to send AJAX request with CSRF token included
function sendAjaxRequest(
  url,
  method,
  data,
  csrftoken,
  successCallback,
  errorCallback
) {
  $.ajax({
    url: url,
    method: method,
    dataType: 'json',
    data: data,
    headers: {
      'X-CSRFToken': csrftoken,
    },
    success: successCallback,
    error: errorCallback,
  });
}

/*
 *  Make donation
 */
const donationForm = document.getElementById('donationForm');
donationForm.addEventListener('submit', donateWithPaystack, false);

function donateWithPaystack() {
  let handler = PaystackPop.setup({
    key: 'pk_test_244916c0bd11624711bdab398418c05413687296', // Replace with your public key
    email: document.getElementById('donor-email').value,
    amount: Number(document.getElementById('donation-amount').value) * 100,
    ref: '' + Math.floor(Math.random() * 1000000000 + 1),
    metadata: {
      custom_fields: [
        {
          display_name: 'Donor',
          variable_name: 'Donor',
          value: document.getElementById('donor').value,
        },
        {
          display_name: 'Donation Description',
          variable_name: 'donation_description',
          value: document.getElementById('donation-description').value,
        },
      ],
    },
    onClose: function () {
      alert('Payment Cancelled.');
    },
    callback: function (response) {
      let message =
        document.getElementById('donation-description').value +
        ' Payment complete! Reference: ' +
        response.reference;
      alert(message);
    },
  });

  handler.openIframe();
}
