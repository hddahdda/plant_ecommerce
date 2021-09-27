from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Review
from .forms import FormReview
from profiles.models import UserProfile
from products.models import Product


# @login_required
# def add_review(request, product_id):

#     product = Product.objects.get(pk=product_id)
#     user = get_object_or_404(UserProfile, user=request.user)

#     if request.method == 'POST':
#         form = FormReview(request.POST)
#         if form.is_valid():
#             data = FormReview()
#             data.subject = form.cleaned_data['subject']
#             data.review = form.cleaned_data['review']
#             data.product_id = product_id
#             data.user = user
#             data.save()
#             return redirect(url)
#         else:
#             messages.error(request, 'There was an error with your form \
#                 Check your information')
#     else:
#         form = FormReview()
#     template = 'products/product_detail.html'
#     context = {
#         'form': form,
#         'product': product,
#     }
#     return render(request, template, context)
    
    # product = get_object_or_404(Product, pk=product_id)
    # user = get_object_or_404(UserProfile, user=request.user)

@login_required
def add_review(request, product_id):
    if request.method == 'POST':
        form = FormReview(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            review = form.cleaned_data['review']
            Review.objects.create(
                user=get_object_or_404(UserProfile, user=request.user),
                subject=subject,
                product=get_object_or_404(Product, pk=product_id),
                review=review,
            )
            return redirect(reverse('product_detail', args=[product_id]))
        else:
            form = FormReview()
            template = 'products/product_detail.html'
        return render(request, template, {"form": form})

