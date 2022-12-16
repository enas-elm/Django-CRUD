from django.contrib import admin
from .models import Item

class ItemAdmin(admin.ModelAdmin):
    fields = ['name', 'price', 'stock', 'image']

admin.site.register(Item)