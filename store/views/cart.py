from ast import Delete
from django.shortcuts import render , redirect

from django.contrib.auth.hashers import  check_password
from store.models.customer import Customer
from django.views import  View
from store.models.product import Products

class Cart(View):
    
    def get(self , request):
        ids = list(request.session.get('cart').keys())
        products = Products.get_products_by_id(ids)
        customer = Customer.get_customer_by_id(request.session.get('customer'))

        return render(request , 'cart.html' , {'products' : products, 'usuario': customer.first_name} )


    def remove(request, ID):
        del request.session['cart'][str(ID)]
        request.session.modified = True

        return redirect("/cart")