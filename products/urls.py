from django.conf.urls import url
from . import views
from django.urls import path
app_name = 'product'
urlpatterns = [
    path('getSubcategory/', views.get_subcategory),
    path('', views.HomeView.as_view(), name='index')
]