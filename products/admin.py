from django.contrib import admin

# Register your models here.
from products.models import Product
class SettingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'product_img', 'price', 'manufacturer_id')
    list_display_links = ('id', 'name', 'product_img', 'price', 'manufacturer_id')
    list_per_page = 5
    sortable_by = ('id')
    list_filter = ('manufacturer_id', )

admin.site.register(Product, SettingAdmin)