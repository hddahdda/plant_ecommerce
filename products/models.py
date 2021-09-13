from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)
    friendly_name = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category',
        null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=255)
    friendly_name = models.CharField(max_length=255, null=True, blank=True)
    sku = models.CharField(max_length=255, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(blank=True)
    product_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    name = models.CharField(max_length=300)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', default='default.jpg')

    def __str__(self):
        return self.name
