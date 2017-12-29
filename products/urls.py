from django.urls import path
from products import views

urlpatterns = [
    path('', views.products, name='List Product'),
    path('product', views.product, name='Product'),
]
