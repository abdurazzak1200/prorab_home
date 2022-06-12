from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView, TemplateView
from shop.models import Liter, Diameter, Meter
from .models import SubCategory, Category, Product, Slider, About

from clients.models import Clients
from django.http import HttpResponse
import json


def get_subcategory(request):
    id = request.GET.get('id', '')
    result = list(SubCategory.objects.filter(
    category_id=int(id)).values('id', 'name'))
    return HttpResponse(json.dumps(result), content_type="application/json")


def get_options(request):
    id = request.GET.get('id', '')
    subcategory = SubCategory.objects.get(id=int(id))
    options = {}
    if subcategory.meter == False:
        options['meter'] = 'False'
    if subcategory.liter == False:
        options['liter'] = 'False'
    if subcategory.diameter == False:
        options['diameter'] = 'False'
    if subcategory.size == False:
        options['size'] = 'False'

    print(json.dumps(options))
    return HttpResponse(json.dumps(options), content_type="application/json")


class HomeView(ListView):
    template_name = 'index.html'
    model = Product

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['sliders'] = Slider.objects.all()
        context['clients'] = Clients.objects.all()
        return context



