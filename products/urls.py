from django.conf.urls import url
from .views import *
from django.urls import path

urlpatterns = [
    path('getSubcategory/', get_subcategory),
    path('', HomeView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about')
]