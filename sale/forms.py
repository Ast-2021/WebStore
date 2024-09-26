from django import forms
from .models import Product


class CreateProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = ['title', 'image', 'description', 'category', 'author', 'phone_number', 'price']
