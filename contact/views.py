from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Info


class ContactView(ListView):
    model = Info
    context_object_name = 'infos'
    template_name = 'contact.html'