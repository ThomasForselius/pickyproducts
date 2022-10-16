from tkinter import CASCADE
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from urllib import request

from django.shortcuts import get_object_or_404


# Create your database models here.


'''
Defines a product class
'''
class Product(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    price = models.DecimalField(null=False, blank=False, max_digits=5, decimal_places=2)
    desc = models.CharField(max_length=300, null=False, blank=False)
    pic = models.CharField(max_length=30, null=False, blank=False, default='pic.jpg')
    sale = models.BooleanField(null=False, blank=False, default=False)
    sale_price = models.DecimalField(null=False, blank=False, max_digits=5, decimal_places=2)
    likes = models.ManyToManyField(User, related_name="likes", blank=True) 

    def __str__(self):
        return self.name # displays the item name in the Admin panel instead of 'Item /number'

    def num_likes(self):
        return self.likes.count() # counts the number of likes