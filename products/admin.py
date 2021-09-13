from django.contrib import admin
from .models import Product, Category, Image

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'friendly_name',
        'name',
        ]


class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'category',
        'friendly_name',
        'sku',
        'price',
        'description',
        'product_image'
    ]
    list_filter = ('category',)
    ordering = ('sku',)


class AdminImage(admin.ModelAdmin):
    list_display = [
        'name',
        'image',
        'product'
    ]


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Image, AdminImage)
