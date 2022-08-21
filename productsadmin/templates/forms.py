from socket import fromshare
from django import forms
from .models import Item

class ProdForm(forms.ProductForm):
    class Meta: 
        model = Item
        fields = ['name', 'price', 'desc', 'sale', 'sale_price']
        
