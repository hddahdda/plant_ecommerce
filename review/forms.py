from django import forms
from .models import Review


class FormReview(forms.ModelForm):
    class Meta:
        model = Review
        exclude = (
            'added',
            'product',
            'user',
            'rating',
        )

        fields = ['subject', 'review']