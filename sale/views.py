from itertools import product

from django.shortcuts import render
from .models import Product, Category


def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'sale/index.html', context)