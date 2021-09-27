from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404)

from products.models import Product


def cart(request):
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get("cart", {})

    if quantity > 0:
        cart[item_id] = quantity
    else:
        cart.pop(item_id)

    request.session['cart'] = cart
    return redirect(reverse('cart'))


def remove_item(request, item_id):

    cart = request.session.get("cart", {})
    try:
        cart.pop(item_id)
        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
