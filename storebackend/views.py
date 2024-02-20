from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from storebackend.models import Product, User
from storebackend.serializers import ProductSerializer


class ProductView(APIView):

    def get(self, request, *args, **kwargs):
        queryset = Product.objects.all().select_related('category')
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            product = serializer.save()
            return Response(ProductSerializer(product).data)
        else:
            return Response(serializer.errors)


def createsuperuser(request):
    su = UserManager()
    answer = su.create_superuser('ilya@admin.ru', 'admin')
    content = {'Message': 'ilya@admin.ru has successfully register'}
    return Response(content, status=status.HTTP_200_OK)
