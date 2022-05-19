from __future__ import unicode_literals
from django.db import models

# Create your models here.
from uuid import uuid4
from products.models import Product

class Customer(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    token = models.CharField(max_length=200, blank=True, editable=False, default=uuid4())

    def __unicode__(self):
        return self.content
    
    def __str__(self):
        return self.name


class Order(models.Model):
    name_receiver = models.CharField(max_length=50)
    phone_receiver = models.CharField(max_length=15)
    address_receiver = models.CharField(max_length=200)
    messages = models.CharField(max_length=200)
    status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now=True)
    total_price = models.IntegerField()
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name="Customer")

    def __unicode__(self):
        return self.content
    def PlaceOrder(self):
        self.save()
class OrderProduct(models.Model):
    order_id = models.IntegerField()
    product_name = models.CharField(max_length=50)
    quantity = models.IntegerField() 