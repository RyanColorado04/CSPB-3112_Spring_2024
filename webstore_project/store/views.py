from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Category, Product # import models

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def products(request, tag=None):
    category_page = None
    products = None
    if tag != None:
        category_page = get_object_or_404(Category, slug=tag)
        products = Product.objects.filter(category=category_page, available=True)
    else:
        products = Product.objects.filter(available=True)
    return render(request, 'products.html', {'category': category_page, 'products': products})

def product(request):
    return render(request, 'product.html')