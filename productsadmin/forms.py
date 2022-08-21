from socket import fromshare
from django import forms
from .models import Product

class ProdForm(forms.ModelForm):
    class Meta: 
        model = Product
        fields = ['name', 'price', 'desc', 'sale', 'sale_price']
        
