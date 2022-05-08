from __future__ import unicode_literals
from django.db import models
from manufacturers.models import Manufacturer

# Create your models here.
from django.utils.html import mark_safe

class Product(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/products')
    description = models.TextField(max_length=1000)
    price = models.FloatField()
    display = models.CharField(max_length=50)
    os = models.CharField(max_length=50)
    main_camera = models.CharField(max_length=50)
    selfie_camera = models.CharField(max_length=50)
    chip = models.CharField(max_length=50)
    RAM = models.CharField(max_length=50)
    ROM = models.CharField(max_length=50)
    sim = models.CharField(max_length=50)
    battery = models.CharField(max_length=50)
    status = models.IntegerField(default=0, blank=True)
    manufacturer_id = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, verbose_name="Manafacturer")

    def __unicode__(self):
        return self.content

    def product_img(self):
        return mark_safe('<img src="{}" width="100" >'.format(self.image.url))
    product_img.short_description = "Image"
    product_img.allow_tags = True
    
    
    def __str__(self):
        return self.name
