from django.shortcuts import render, redirect
from django.views import View
from django.db import connection

class ManageOrderView(View):

    def Orders(request, status=-1):
        
        ComandoSQL = f"select O.id , C.first_name , C.last_name , P.name , O.quantity , O.price , O.date_delivery, O.Delivery_Pickup , O.status , substr(O.address,1,50) "
        ComandoSQL += f" from store_order O , store_customer C , store_products P "
        ComandoSQL += f" where O.customer_id = C.id "
        ComandoSQL += f" and O.product_id = P.id "
        ComandoSQL += f" and O.status = {status}"
        ComandoSQL += f" order by C.first_name , O.date_delivery"

        cursor_manage_order = connection.cursor()
        cursor_manage_order.execute(ComandoSQL)
        data_manage_order = cursor_manage_order.fetchall()

        if status == 0:
            tipo_consulta = "New Orders"
        if status == 1:
            tipo_consulta = "In Preparation"
        if status == 2:
            tipo_consulta = "Ready"
        if status == 3:
            tipo_consulta = "Delivered"
        if status == 9:
            tipo_consulta = "Cancelled"

        context = {'manage_orders':data_manage_order, 'tipo_consulta':tipo_consulta}
        return render(request , 'manage_orders.html'  , context)


    def Update_Orders(request, ID, status):

        ComandoSQL = f"select status , quantity , product_id from store_order where ID = {ID}"
        cursor_manage_order = connection.cursor()
        cursor_manage_order.execute(ComandoSQL)
        dados = cursor_manage_order.fetchone()
        status_atual = dados[0]
        qtde = dados[1]
        id_produto = dados[2]
        cursor_manage_order.close
        
        cursor_manage_order2 = connection.cursor()
        ComandoSQL = f"update store_order set status = {status} where ID = {ID}"
        cursor_manage_order2.execute(ComandoSQL)
        cursor_manage_order2.close

        if status == 3:
            cursor_manage_inventoty = connection.cursor()
            ComandoSQL = f"update store_inventory set qtde = qtde - {qtde} where id_product_id = {id_produto}"
            cursor_manage_inventoty.execute(ComandoSQL)
            cursor_manage_inventoty.close


        if int(status_atual) == 0:
            return redirect(f"/manage_orders/0")

        if int(status_atual) == 1:
            return redirect(f"/manage_orders/1")
        
        if int(status_atual) == 2:
            return redirect(f"/manage_orders/2")

        if int(status_atual) == 3:
            return redirect(f"/manage_orders/3")

        if int(status_atual) == 9:
            return redirect(f"/manage_orders/9")
