from django.shortcuts import render
from django.views.generic import ListView

from .models import SubCategory, Category, Product
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