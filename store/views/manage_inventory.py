from django.shortcuts import render, redirect
from django.views import View
from django.db import connection

class ManageInventoryView(View):

    def Inventory(request):
        
        ComandoSQL = "select P.name , I.qtde from store_products P , store_inventory I where P.id = I.id_product_id"

        cursor_manage_inventory = connection.cursor()
        cursor_manage_inventory.execute(ComandoSQL)
        data_manage_inventory = cursor_manage_inventory.fetchall()
        context = {'Inventory': data_manage_inventory}

        return render(request , 'manage_inventory.html'  , context)
