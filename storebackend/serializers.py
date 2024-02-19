from rest_framework import serializers

from storebackend.models import Product, Shop


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('id', 'name', 'state')


class ProductSerializer(serializers.ModelSerializer):
    shop = serializers.StringRelatedField()
    class Meta:
        model = Product
        fields = ('id', 'name', 'category', 'description', 'quantity', 'price', 'shop')
