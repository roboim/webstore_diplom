from django.urls import path

from storebackend.views import ProductView

urlpatterns = [
    path('products/', ProductView.as_view()),
]
