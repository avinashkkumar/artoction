from django.contrib import admin
from .models import Product

# Register your models here.



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','base_price', 'current_price', 'isUpcoming', 'isOngoing', 'isSold']


    

