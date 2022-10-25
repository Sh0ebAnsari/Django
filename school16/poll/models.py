from unicodedata import decimal
from django.db import models

# Create your models here.


class Product(models.Model):
    name=models.CharField(max_length=30)
    price=models.DecimalField(decimal_places=2,max_digits=8)
    weight=models.IntegerField()
    brand=models.CharField(max_length=30)

    # def __str__(self):
    #     return self.name