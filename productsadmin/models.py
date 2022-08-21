from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    price = models.DecimalField(null=False, blank=False, max_digits=5, decimal_places=2)
    desc = models.CharField(max_length=300, null=False, blank=False)
    sale = models.BooleanField(null=False, blank=False, default=False)
    sale_price = models.DecimalField(null=False, blank=False, max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name # displays the item name in the Admin panel instead of 'Item /number'