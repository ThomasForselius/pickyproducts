from django.shortcuts import render, redirect
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
    return render(request, 'productsadmin/edit_prod.html')