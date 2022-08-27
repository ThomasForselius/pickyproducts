from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
# Create your views here.


def show_prod(request):
    products = Product.objects.all()
    context = {
        'products' : products
    }
    return render(request, 'admin/show_prod.html', context)
