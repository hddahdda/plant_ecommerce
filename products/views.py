from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Image, Category

# Create your views here.


def products_all(request):
    """ A view to show all products """

    products = Product.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter a valid search criteria")
                return redirect(reverse('products'))
      
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
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


def images_all(request, id):
    product = get_object_or_404(Product, id=id)
    images = Image.objects.filter(product=product)

    context = {
        'images': images,
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)
