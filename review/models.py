from django.db import models

from products.models import Product
from profiles.models import UserProfile

# Create your models here.
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    subject = models.CharField(max_length=40, blank=True)
    review = models.TextField(max_length=600, blank=True)
    rating = models.FloatField()
    added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject
