from itertools import product
from django.shortcuts import render
from .models import Product

def home_view(request):
    feture_products = Product.objects.filter(is_fetured=True)
    context = {
        'feture_products': feture_products,
    }
    return render(request, 'home.html', context)

def product_view(request, pk):
    product = Product.objects.get(pk=pk)
    context = {
        'product': product,
    }
    return render(request, 'product.html', context)
