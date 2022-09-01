from pickle import NONE
from urllib import request
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Product
# Create your views here.

def logout_user(request):
    logout(request)
    messages.success(request, ("You successfully logged out."))
    return redirect('show_prod')

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = Users.objects.get(username=username)
            print(email)
        except:
            messages.error(request, 'Username does not exist!')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            print("success")
            return redirect('show_prod')
        else: 
            print("wrong login")
            return redirect('login_user')
    else: 
        return render(request, 'login.html', {})


def show_prod(request):
    products = Product.objects.all()
    context = {
        'products' : products
    }
    #return render(request, 'admin/show_prod.html', context)
    return render(request, 'base.html', context)


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
        'id' : prod_id,
        'name' : prod.name,
        'price' : prod.price,
        'desc' : prod.desc,
        'sale' : prod.sale,
        'sale_price' : prod.sale_price
    }
    return render(request, 'admin/edit_prod.html', context)


def remove_prod(request, prod_id):
    prod = get_object_or_404(Product, id=prod_id)
    Product.objects.filter(pk=prod_id).delete()
    return redirect('show_prod')
    

def toggle_prod(request, prod_id):
    prod = get_object_or_404(Product, id=prod_id)
    prod.sale = not prod.sale
    prod.save()
    return redirect('show_prod')
    