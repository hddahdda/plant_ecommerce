from django.shortcuts import render, get_object_or_404
from .models import Product, Image

# Create your views here.


def view_products(request):
    """ A view to show all products """

    products = Product.objects.all()

    # image = Image.objects.all()

    context = {
        'products': products,
        # 'images': image,
    }

    return render(request, 'products/products.html', context)

# def view_image(request, id):
#     product = get_object_or_404(Product, id=id)
#     images = Image.objects.filter(product=product)
#     return 
