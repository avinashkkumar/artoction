from django.contrib import admin
from .models import (
    Account,
    Address
) 
from django.contrib.auth import get_user_model
# Register your models here.


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['username', 'is_active']

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['__str__','is_verified','is_deneyed']

