from django.shortcuts import render, redirect
from django.views import View
from store.models.customer import Customer
from store.models.product import Products
from store.models.orders import Order
from datetime import date


class CheckOut(View):
    def post(self, request):
        Delivery_Pickup = request.POST.get('Opt_Delivery_Pickup')
        address = request.POST.get('DeliveryAddress')
        date_delivery = request.POST.get('date_delivery')
        time_delivery = request.POST.get('time_delivery')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Products.get_products_by_id(list(cart.keys()))

        if ((Delivery_Pickup == 'Delivery' and len(address) > 0) or (Delivery_Pickup == 'Pickup')) and (date_delivery > str(date.today()) and time_delivery > '08:00'):
            for product in products:
                order = Order(customer=Customer(id=customer),
                              product=product,
                              price=product.price,
                              Delivery_Pickup=Delivery_Pickup,
                              address=address,
                              date_delivery=date_delivery,
                              time_delivery=time_delivery,
                              quantity=cart.get(str(product.id)))
                order.save()

                request.session['cart'] = {}

        return redirect('cart')