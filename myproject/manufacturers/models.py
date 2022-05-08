from __future__ import unicode_literals
from django.db import models

# Create your models here.
from django.utils.html import mark_safe

class Manufacturer(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/manufacturers')
    status = models.IntegerField(default=0, blank=True)

    def __unicode__(self):
        return self.content
    
    def manufacturer_img(self):
        return mark_safe('<img src="{}" width="100" >'.format(self.image.url))
    manufacturer_img.short_description = "Image"
    manufacturer_img.allow_tags = True
    
    def __str__(self):
        return self.name

    
    
    
    


