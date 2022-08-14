from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    price = models.FloatField(null=False, blank=False,)
    desc = models.CharField(max_length=300, null=False, blank=False)
    sale = models.BooleanField(null=False, blank=False, default=False)
    sale_price = models.FloatField(null=False, blank=False,)