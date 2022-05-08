from django.contrib import admin

# Register your models here.
from manufacturers.models import Manufacturer


class SettingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'address', 'manufacturer_img', 'status')
    list_display_links = ('id', 'name', 'phone', 'address', 'manufacturer_img', 'status')
    list_filter = ('status',)
    list_per_page = 5
    ordering = ['id']
    search_fields = ('name',)
    
    
admin.site.register(Manufacturer, SettingAdmin)