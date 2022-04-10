from django.conf.urls import url
from .views import *
from django.urls import path

urlpatterns = [
    path('', ShopView.as_view(), name='shop_list'),
    path('<str:subcategory_slug>/', ShopView.as_view(), name='subcategory_list'),
    path('<str:category_slug>/', ShopView.as_view(), name='category_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='detail')
]