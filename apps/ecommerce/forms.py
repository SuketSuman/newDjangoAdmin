from django import forms

from apps.ecommerce.models import Products


class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
