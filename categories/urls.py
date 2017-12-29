from django.conf.urls import url
from django.urls import path, re_path
from django.views.generic import DetailView

from categories import views
from products.models import ShopProducts

urlpatterns = [
    re_path(r'^$', views.home, name='index'),
    path('categories/', views.category, name='Category'),
    re_path(r'categories/(?P<pk>[a-z0-9]+)/$', DetailView.as_view(model=ShopProducts, template_name='products/product.html')),
    re_path(r'^(?P<page>[a-z0-9/]+)/$', views.home, name='index'),
]
