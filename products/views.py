from django.shortcuts import render, get_object_or_404
from .models import Product, Image

# Create your views here.


def view_products(request):
    """ A view to show all products """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    # images = Image.objects.filter(product_id)

    context = {
        'product': product,
        # 'images': images,
    }

    return render(request, 'products/product_detail.html', context)


# def all_images(request, product_id):

#     product_image = get_object_or_404(Product, pk=product_id)                   
#     detailed_images = image_set.all() 

#     context = {
#         'product_images': product_images,
#         'detailed_images': detailed_images,
#     }

#     return render(request, 'products/product_detail.html', context)


def view_image(request, id):
    product = get_object_or_404(Product, id=id)
    images = Image.objects.filter(product=product)

    context = {
        'images': images,
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)
