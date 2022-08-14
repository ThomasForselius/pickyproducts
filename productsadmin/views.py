from django.shortcuts import render
# Create your views here.

def add_prod(request):
    return render(request, 'admin/add_prod.html')