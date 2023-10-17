from django.shortcuts import render, redirect
from django.views import View
from django.db import connection

class ManageInventoryView(View):

    def Inventory(request):
    
        ComandoSQL = "select P.id , P.name , I.qtde from store_products P , store_inventory I where P.id = I.id_product_id"

        cursor_manage_inventory = connection.cursor()
        cursor_manage_inventory.execute(ComandoSQL)
        data_manage_inventory = cursor_manage_inventory.fetchall()
        context = {'Inventory': data_manage_inventory}

        return render(request , 'manage_inventory.html', context)


    def Add_Inventory(request, ID , qtde):
        ComandoSQL = f"update store_inventory set qtde = qtde + {qtde} where id_product_id = {ID}"

        cursor_atualiza_qtde = connection.cursor()
        cursor_atualiza_qtde.execute(ComandoSQL)

        return redirect('/manage_inventory')


    def Sub_Inventory(request, ID , qtde):
        ComandoSQL = f"select qtde from store_inventory where id_product_id = {ID}"
        cursor_pesquisa_estoque = connection.cursor()
        cursor_pesquisa_estoque.execute(ComandoSQL)
        data_pesquisa_estoque = cursor_pesquisa_estoque.fetchall()

        if (data_pesquisa_estoque[0][0] - qtde) >= 0:

            ComandoSQL = f"update store_inventory set qtde = qtde - {qtde} where id_product_id = {ID}"

            cursor_atualiza_qtde = connection.cursor()
            cursor_atualiza_qtde.execute(ComandoSQL)

        return redirect('/manage_inventory')
