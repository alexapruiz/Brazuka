from django.contrib import admin
from django.urls import path

from .views.home import Index , store
from .views.signup import Signup
from .views.login import Login , logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView
from .views.manage_orders import ManageOrderView
from .views.manage_payments import ManagePaymentsView
from .views.manage_inventory import ManageInventoryView
from .middlewares.auth import auth_middleware


urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('store', store , name='store'),
    
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout , name='logout'),
    
    path('cart', auth_middleware(Cart.as_view()) , name='cart'),
    path('cart/remove/<int:ID>', Cart.remove , name='cart'),
    
    path('check-out', CheckOut.as_view() , name='checkout'),
    
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
    
    path('manage_orders/', ManageOrderView.Orders, name='manage_orders'),
    path('manage_orders/<int:status>', ManageOrderView.Orders , name='manage_orders'),
    path('manage_orders/update/<int:ID>/<int:status>', ManageOrderView.Update_Orders, name='manage_orders'),
    
    path('manage_payments/', ManagePaymentsView.Payments, name='manage_payments'),
    
    path('manage_inventory/', ManageInventoryView.Inventory, name='manage_inventory'),
    path('manage_inventory/add/<int:ID>/<int:qtde>', ManageInventoryView.Add_Inventory, name='manage_inventory'),
    path('manage_inventory/subtract/<int:ID>/<int:qtde>',ManageInventoryView.Sub_Inventory, name='manage_inventory'),
]
