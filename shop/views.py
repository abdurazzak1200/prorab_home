from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView
from products.models import Product, Category, SubCategory

class ShopView(ListView, View):
    template_name = 'shop.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 10



    def get_queryset(self, **kwargs):
        search_query = self.request.GET.get('search', '')
        category_slug = self.kwargs.get("category_slug")
        subcategory_slug = self.kwargs.get("subcategory_slug")
        if subcategory_slug:
            subcategory = get_object_or_404(SubCategory, slug=subcategory_slug)
            queryset = self.model.objects.filter(is_active=True, subcategory=subcategory)
            return queryset
        elif category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            queryset = self.model.objects.filter(is_active=True, category=category)
            return queryset

        elif search_query:
            if search_query:
                queryset = self.model.objects.filter(name__icontains=self.request.GET.get('search', ''),
                                                     is_active=True
                                                     )
                return queryset
            else:
                return 'asd'
        queryset = self.model.objects.filter(is_active=True)
        return queryset

class ProductDetailView(DetailView):
    model = Product
    template_name = 'detail.html'
    context_object_name = 'product'
    # print('*********************************************')

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        tags = self.object.tags
        context['related'] = Product.objects.filter(tags=tags)
        print(context)
        return context
