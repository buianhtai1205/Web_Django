from __future__ import unicode_literals
from django.db import models

# Create your models here.
from uuid import uuid4


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

   