from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView
from products.models import Product, Category, SubCategory

class ShopView(ListView, View):
    template_name = 'shop.html'
    model = Product
    context_object_name = 'products'

    def get_queryset(self):
        queryset = self.model.objects.filter(is_active=True)
        search_query = self.request.GET.get('search', '')

        category_slug = self.kwargs.get('category_slug')
        subcategory_slug = self.kwargs.get('subcategory_slug')
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            queryset = self.model.objects.filter(
                is_active=True,
                category=category)
            return queryset
        if subcategory_slug:
            subcategory = get_object_or_404(SubCategory, slug=subcategory_slug)
            queryset = self.model.objects.filter(
                is_active=True,
                subcategory=subcategory)
            return queryset
        return queryset


