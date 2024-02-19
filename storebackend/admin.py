from django.contrib import admin

from storebackend.models import Product, Shop


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'state')
    list_filter = ('id', 'name', 'state')
    search_fields = ('id', 'name', 'state')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'description', 'quantity', 'price', 'shop')
    list_filter = ('id', 'name', 'category', 'price', 'shop')
    search_fields = ('id', 'name', 'category', 'price', 'shop')
