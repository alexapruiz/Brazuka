from django.contrib import admin
from .models.product import Products
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order
from .models.inventory import Inventory


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


class AdminCategory(admin.ModelAdmin):
    list_display = ['id','name']


class AdminCustomer(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','phone','email']


class AdminOrder(admin.ModelAdmin):
    list_display = ['customer',Products,'quantity','price','address','date_order','date_delivery','status']


class AdminInventory(admin.ModelAdmin):
    list_display = [Products,'qtde']


# Register your models here.
admin.site.register(Products,AdminProduct)
admin.site.register(Category,AdminCategory)
admin.site.register(Customer,AdminCustomer)
admin.site.register(Order,AdminOrder)
admin.site.register(Inventory,AdminInventory)

