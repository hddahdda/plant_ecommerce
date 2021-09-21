from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Cart is empty.")
        return redirect(reverse('products'))
 
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JSKH4G7NidGju5aBLdP2G2amo4jbKbud5MQyNLyPF6gr5D79K3Iqf4Zq3xm3J0D2et6M6YNyevblS7rxAMUjvAL002IShuema',
        'client_secret': 'test',
    }

    return render(request, template, context)

