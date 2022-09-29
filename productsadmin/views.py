from email import message
from pickle import NONE
from urllib import request
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Product
# Create your views here.


'''
Logs out a user
'''
def logout_user(request):
    logout(request)
    messages.success(request, "You logged out!")
    return redirect('show_prod')


'''
Registers a new user
'''
def register_user(request):
    if request.method == "POST":
        name = request.POST.get("name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password1")
        try:
            check_mail = User.objects.get(email=email)
            messages.error(
                request,
                "Account with that email already exists. Please try again"
            )
            return render(request, 'admin/register.html')
        except User.DoesNotExist:
            pass
        newuser = User.objects.create_user(username=username, password=password, first_name=name, email=email)
        newuser.save()
        user_check = authenticate(
            request,
            username=username,
            password=password
        )
        try:
            login(request, user_check)
            return redirect('show_prod')
        except:
            messages.error("Wrong login credentials. Try again.")
            return redirect('login_user')
    else:
        return render(request, 'admin/register.html')


'''
Updates user Name and Email
'''
def update_profile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            name = request.POST.get("name")
            email = request.POST.get("email")
            user_id = request.POST.get("user_id")
            try:
                update_user = User.objects.filter(pk=user_id).update(first_name=name, email=email)
                messages.success(request, "Successfully updated profile.")
                return redirect("show_prod")
            except ValueError as e:
                messages.error(e)
                return render(request, 'admin/register.html')
        else:
            return render(request, 'admin/profile.html')
    else:
        messages.error(request, "You are not authorised for that page.")
        return redirect("show_prod")



'''
Logs the user in
'''
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
            login(request, user)
            messages.success(request, f"You are logged in as {username}")
            return redirect('show_prod')
        except:
            messages.error(request, "Wrong login credentials. Try again")
            return redirect('login_user')
    else:
        return render(request, 'login.html')


'''
Shows the products in the product database
'''
def show_prod(request):
    products = Product.objects.all().order_by('id')
    context = {
        'products': products
    }
    return render(request, 'base.html', context)


'''
Shows the product list in the admin section of the page
'''
def show(request):
    if request.user.is_superuser:
        products = Product.objects.all().order_by('id')
        context = {
            'products': products
        }
        return render(request, 'admin/show_prod.html', context)
    else:
        messages.warning(request, "You are not authorized for this")
        return redirect('show_prod')



'''
Adds a new product to the database
'''
def add_prod(request):
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        desc = request.POST.get("desc")
        sale = 'sale' in request.POST
        sale_price = request.POST.get("sale_price")
        Product.objects.create(
            name=name,
            price=price,
            desc=desc,
            sale=sale,
            sale_price=sale_price
            )
        messages.success(request, 'Product added successfully!')
        return redirect('show')
    return render(request, 'admin/add_prod.html')



'''
Edits an existing product
'''
def edit_prod(request, prod_id):
    if request.user.is_superuser:
        try:
            prod = get_object_or_404(Product, id=prod_id)
        except:
            messages.warning(request, f"Product ID {prod_id} doesn't exist.")
            return redirect('show')
        if request.method == "POST":
            name = request.POST.get("name")
            price = request.POST.get("price")
            desc = request.POST.get("desc")
            sale = 'sale' in request.POST
            sale_price = request.POST.get("sale_price")
            Product.objects.filter(pk=prod_id).update(
                name=name,
                price=price,
                desc=desc,
                sale=sale,
                sale_price=sale_price
                )
            return redirect('show')
        context = {
            'id': prod_id,
            'name': prod.name,
            'price': prod.price,
            'desc': prod.desc,
            'sale': prod.sale,
            'sale_price': prod.sale_price
        }
        messages.success(request, "Product updated successfully")
        return render(request, 'admin/edit_prod.html', context)
    else:
        messages.warning(request, "You are not authorized for that page.")
        return redirect('show_prod')



'''
Removes a product
'''
def remove_prod(request, prod_id):
    if request.user.is_superuser:
        try: 
            prod = get_object_or_404(Product, id=prod_id)
            Product.objects.filter(pk=prod_id).delete()
            messages.success(request, "You removed the product successfully")
            return redirect('show')
        except: 
            messages.error("Something went wrong. Go back and try again.")
            return redirect('show')
    else:
        messages.warning(request, "You are not authorized for that page.")
        return redirect('show_prod')


def toggle_prod(request, prod_id):
    prod = get_object_or_404(Product, id=prod_id)
    prod.sale = not prod.sale
    prod.save()
    return redirect('show')


def error_404(request, exception):
    messages.error(request, "That page doesn't exist.")
    return redirect('show_prod')
