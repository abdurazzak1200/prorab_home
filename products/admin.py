from django.contrib import admin
from .models import Product, Category, SubCategory, Slider, About
# Register your models here.
@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_display_links = ('name', 'slug')
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ['name']

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'slug')
    list_filter = ('category__name', )
    search_fields = ['name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_filter = ('category__name', 'subcategory__name', 'is_active')
    search_fields = ('category__name', 'subcategory__name', 'name')
    list_display = ['name', 'category', 'subcategory', 'price', 'is_active']
    list_editable = ['price', 'is_active']

#
# @admin.register(About)
# class AboutAdmin(admin.ModelAdmin):
#     list_display = ('bg', 'img', 'title', 'text')