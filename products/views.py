from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView, TemplateView

from .models import SubCategory, Category, Product, Slider, About
from django.http import HttpResponse
import json
def get_subcategory(request):
    id = request.GET.get('id', '')
    result = list(SubCategory.objects.filter(
    category_id=int(id)).values('id', 'name'))
    return HttpResponse(json.dumps(result), content_type="application/json")

class HomeView(ListView):
    template_name = 'index.html'
    model = Product

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['sliders'] = Slider.objects.all()
        return context


class AboutView(ListView,View):
    template_name = 'about.html'
    model = About
    context_object_name = 'about'

class ContactView(TemplateView):
    template_name = 'contact.html'
