from .models import Category, SubCategory


def get_category(request):
    category = Category.objects.all()
    subcategory = SubCategory.objects.all()
    context = {'categoryes': category, 'subcategoryes': subcategory}
    return context
