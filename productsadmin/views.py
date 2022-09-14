from email import message
from pickle import NONE
from urllib import request
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Product
# Create your views here.

def logout_user(request):
    logout(request)
    return redirect('show_prod')

def register_user(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password1")
        try: 
            check_mail = User.objects.get(email=email)
            messages.error(request, "Account with that email already exists. Please try again")
            return render(request, 'admin/register.html')      
        except User.DoesNotExist:
            pass
        newuser = User.objects.create_user(name,email, password, group=users)
        newuser.save()
        user_check = authenticate(request, username=name,password=password)
        try:
            login(request, user_check)
            return redirect('show_prod')
        except: 
            messages.error("Wrong login credentials. Try again.")
            return redirect('login_user')
    else: 
        return render(request, 'admin/register.html')


def update_profile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            name = request.POST.get("name")
            email = request.POST.get("email")
            password = request.POST.get("password1")
            user_id = request.POST.get("user_id")
            try: 
                update_user = User.objects.filter(pk=user_id).update(first_name=name,email=email,password=password)
            except User.DoesNotExist:
                messages.error(request, "Account with that email doesn't exist. Please try again")
                return render(request, 'admin/register.html')      
            # try:
            #     user_check = authenticate(request, username=name,password=password)
            #     login(request, user_check)
            #     messages.success(request, "You updated your profile information.")
            #     return redirect('show_prod')
            # except: 
            #     messages.error("Wrong login credentials. Try again.")
            #     return redirect('login_user')
        else:
            return render(request, 'admin/profile.html')
    else:
        messages.error(request, "You are not authorised for that page.")
        return redirect("show_prod")

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        try: 
            check_username = User.objects.get(username=username)
        except:
            messages.error(request, "Username doesn't exist. try again")
            return redirect('login_user')
        try:
            user = authenticate(request, username=username, password=password)
        except AssertionError as e: 
            messages.error(request, e)
            return redirect('login_user')
        try:
            login(request, user)
            return redirect('show_prod')
        except:
            messages.error(request, "Could not login. please try again")
            return redirect('login_user')
    else: 
        return render(request, 'login.html')


def show_prod(request):
    products = Product.objects.all()
    context = {
        'products' : products
    }
    return render(request, 'base.html', context)


def show(request):
    if request.user.is_superuser:
        products = Product.objects.all()
        context = {
            'products' : products
        }
        return render(request, 'admin/show_prod.html', context)
    else: 
        messages.error(request, "You are not authorized for this")
        return redirect('show_prod')

def add_prod(request):
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        desc = request.POST.get("desc")
        sale = 'sale' in request.POST
        sale_price = request.POST.get("sale_price")
        Product.objects.create(name=name, price=price, desc=desc, sale=sale, sale_price=sale_price)
        messages.error(request, 'Product added successfully!')
        return redirect('add_prod')
    return render(request, 'admin/add_prod.html')


def edit_prod(request, prod_id):
    if request.user.is_superuser:
        try:
            prod = get_object_or_404(Product, id=prod_id)
        except:
            messages.error(request, f"Product ID {prod_id} doesn't exist.")
            return redirect('show')
        if request.method == "POST":
            name = request.POST.get("name")
            price = request.POST.get("price")
            desc = request.POST.get("desc")
            sale = 'sale' in request.POST
            sale_price = request.POST.get("sale_price")
            Product.objects.filter(pk=prod_id).update(name=name, price=price, desc=desc, sale=sale, sale_price=sale_price)
            return redirect('show')
        context = {
            'id' : prod_id,
            'name' : prod.name,
            'price' : prod.price,
            'desc' : prod.desc,
            'sale' : prod.sale,
            'sale_price' : prod.sale_price
        }
        return render(request, 'admin/edit_prod.html', context)
    else:
        messages.error(request, "You are not authorized for that page.")
        return redirect('show_prod')

def remove_prod(request, prod_id):
    if request.user.is_superuser:
        prod = get_object_or_404(Product, id=prod_id)
        Product.objects.filter(pk=prod_id).delete()
        return redirect('show')
    else:
        messages.error(request, "You are not authorized for that page.")
        return redirect('show_prod')

def toggle_prod(request, prod_id):
    prod = get_object_or_404(Product, id=prod_id)
    prod.sale = not prod.sale
    prod.save()
    return redirect('show')
    

def error_404(request, exception):
    messages.error(request, "That page doesn't exist.")
    return redirect('show_prod')