from django.contrib import admin

from storebackend.models import User, Shop, Category, Product, ProductInfo


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields_user = ('email', 'company', 'position', 'username', 'is_active', 'type')
    list_display = fields_user
    list_filter = fields_user
    search_fields = fields_user


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    fields_shop = ('id', 'name', 'url', 'user', 'state')
    list_display = fields_shop
    list_filter = fields_shop
    search_fields = fields_shop


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields_category = ('id', 'name')
    list_display = fields_category
    list_filter = fields_category
    search_fields = fields_category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields_product = ('id', 'name', 'category')
    list_display = fields_product
    list_filter = fields_product
    search_fields = fields_product


@admin.register(ProductInfo)
class ProductInfoAdmin(admin.ModelAdmin):
    fields_product = ('id', 'model', 'external_id', 'product', 'shop', 'quantity', 'price', 'price_rrc')
    list_display = fields_product
    list_filter = fields_product
    search_fields = fields_product
