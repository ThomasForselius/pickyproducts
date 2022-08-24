from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
# Create your views here.


def show_prod(request):
    products = Product.objects.all()
    context = {
        'products' : products
    }
    return render(request, 'admin/show_prod.html', context)


def add_prod(request):
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        desc = request.POST.get("desc")
        sale = 'sale' in request.POST
        sale_price = request.POST.get("sale_price")
        Product.objects.create(name=name, price=price, desc=desc, sale=sale, sale_price=sale_price)
        return redirect('show_prod')
    return render(request, 'admin/add_prod.html')


def edit_prod(request, prod_id):
    prod = get_object_or_404(Product, id=prod_id)
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        desc = request.POST.get("desc")
        sale = 'sale' in request.POST
        sale_price = request.POST.get("sale_price")
        Product.objects.filter(pk=prod_id).update(name=name, price=price, desc=desc, sale=sale, sale_price=sale_price)
        return redirect('show_prod')
    context = {
        'name' : prod.name,
        'price' : prod.price,
        'desc' : prod.desc,
        'sale' : prod.sale,
        'sale_price' : prod.sale_price
    }
    return render(request, 'admin/edit_prod.html', context)


def remove_prod(request, prod_id):
    prod = get_object_or_404(Product, id=prod_id)
    if request.method == "POST":
        Product.objects.filter(pk=prod_id).delete()
        return redirect('show_prod')
    context = {
        'name' : prod.name,
        'price' : prod.price,
        'desc' : prod.desc,
        'sale' : prod.sale,
        'sale_price' : prod.sale_price
    }
    return render(request, 'admin/remove_prod.html', context)