from django.db import models
from .product import Products


class Inventory(models.Model):
    id_product = models.ForeignKey(Products,primary_key=True,on_delete=models.CASCADE,default=1 )
    qtde = models.IntegerField(default=0)
    

    @staticmethod
    def get_inventory_by_product(id):
        return Inventory.objects.filter (id_product = id)
    

    @staticmethod
    def get_all_inventory():
        return Inventory.objects.all()
