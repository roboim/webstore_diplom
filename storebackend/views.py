from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from storebackend.models import Product
from storebackend.serializers import ProductSerializer


class ProductView(APIView):

    def get(self, request, *args, **kwargs):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)