from django.db import models
from .product import Products
from .customer import Customer
import datetime


class Order(models.Model):
    id = models.IntegerField(primary_key=True)
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    address = models.CharField (max_length=50, default='', blank=True)
    Delivery_Pickup = models.CharField(max_length=10, default='Delivery', blank=False)
    date_order = models.DateField (default=datetime.datetime.today)
    date_delivery = models.DateField (default=datetime.datetime.today)
    time_delivery = models.CharField(max_length=5, default='00:00', blank=False)
    status = models.CharField (max_length=1, default=0)

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date_delivery')

