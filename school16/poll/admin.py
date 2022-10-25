from itertools import product
from django.contrib import admin
from .models import Product
# Register your models here.

# admin.site.register(Product)
admin.site.site_header = "poll Project"

# class ModeladminProduct(admin.ModelAdmin):
#     list_display=('id','name','price','weight','brand')
# admin.site.register(Product,ModeladminProduct)


@admin.register(Product)
class ModeladminProduct(admin.ModelAdmin):
    list_display=('id','name','price','weight','brand')


    
