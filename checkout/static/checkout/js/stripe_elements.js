/* Code for Stripe payments, js and css from:
 https://stripe.com/docs/payments/integration-builder
 + Code Institute Boutiqe Ado project
*/

var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey)
var elements = stripe.elements();

var style = {
    base: {
        color: "#32325d",
        fontFamily: 'Arial, sans-serif',
        fontSmoothing: "antialiased",
        fontSize: "16px",
        "::placeholder": {
            color: "#32325d"
        }
    },
    invalid: {
        fontFamily: 'Arial, sans-serif',
        color: "#fa755a",
        iconColor: "#fa755a"
    }
};
var card = elements.create('card', {style: style});
    // Stripe injects an iframe into the DOM
card.mount('#card-element');

// Handle realtime validation errors on the card element
card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});

// Form submission
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({ 'disabled': true}); //prevent multiple submissions
    $('#submit-button').attr('disabled', true);
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function(result) {
        if (result.error) {
            // Show error message 
            var errorDiv = document.getElementById('card-errors');
            var html = `
                <span>${result.error.message}</span>`;
            $(errorDiv).html(html);
            card.update({ 'disabled': false});
            $('#submit-button').attr('disabled', false);
        } else {
            // Payment has been processed
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});