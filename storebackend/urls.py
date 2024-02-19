from django.urls import path

from storebackend.views import ProductView

urlpatterns = [
    path('product/', ProductView.as_view()),
]
