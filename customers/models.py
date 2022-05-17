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

'''
Table Order_Product tạo trực tiếp trong databases
Câu SQL: 

CREATE TABLE `customers_orderproduct` (
	`order_id` BIGINT(20) NULL DEFAULT NULL,
	`product_id` BIGINT(20) NULL DEFAULT NULL,
	`quantity` INT(11) NULL DEFAULT NULL,
	INDEX `FK_customers_orderproduct_customers_order` (`order_id`) USING BTREE,
	INDEX `FK_customers_orderproduct_products_product` (`product_id`) USING BTREE,
	CONSTRAINT `FK_customers_orderproduct_customers_order` FOREIGN KEY (`order_id`) REFERENCES `python_web`.`customers_order` (`id`) ON UPDATE RESTRICT ON DELETE RESTRICT,
	CONSTRAINT `FK_customers_orderproduct_products_product` FOREIGN KEY (`product_id`) REFERENCES `python_web`.`products_product` (`id`) ON UPDATE RESTRICT ON DELETE RESTRICT
)
COLLATE='utf8mb4_general_ci'
ENGINE=InnoDB
;


'''
   