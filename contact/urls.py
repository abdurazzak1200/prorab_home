from django.conf.urls import url
from .views import *
from django.urls import path

urlpatterns = [
    path('', ContactView.as_view(), name='contact'),
]