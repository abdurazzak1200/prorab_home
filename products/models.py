from ckeditor.fields import RichTextField
from django.db import models

from shop.models import Diameter, Liter, Meter, Size, Kg
from taggit.managers import TaggableManager


class Slider(models.Model):
    desc = models.CharField('Описание', max_length=30)
    title = models.CharField('Название', max_length=20)
    img = models.ImageField('Фото слайдера', max_length=256)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Слайдер'
        verbose_name_plural = 'Слайдеры'


class Category(models.Model):
    name = models.CharField('Название', max_length=50)
    slug = models.SlugField('slug', max_length=60)
    img = models.ImageField('фото категории', max_length=256, upload_to='category/%Y-%m-%d')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'


class SubCategory(models.Model):
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    name = models.CharField('Название', max_length=50)
    slug = models.SlugField('slug', max_length=60)
    liter = models.BooleanField('Литр', default=False)
    diameter = models.BooleanField('Диаметр', default=False)
    meter = models.BooleanField('Метр', default=False)
    size = models.BooleanField('Размер', default=False)
    kg = models.BooleanField('Вес/кг', default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подкатегорию'
        verbose_name_plural = 'Подкатегории'


class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, verbose_name='Подкатегория', on_delete=models.CASCADE)
    img = models.ImageField('Фото', max_length=256, upload_to='product/%Y-%m-%d')
    name = models.CharField('Название', max_length=100)
    desc = RichTextField('Описание', null=True, blank=True)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    kg = models.ForeignKey(Kg, verbose_name='Вес/кг', on_delete=models.SET_NULL, null=True, blank=True)
    diameter = models.ForeignKey(Diameter, verbose_name='Диаметр', on_delete=models.SET_NULL, null=True, blank=True)
    liter = models.ForeignKey(Liter, verbose_name='Литр', on_delete=models.SET_NULL, null=True, blank=True)
    meter = models.ForeignKey(Meter, verbose_name='Метр', on_delete=models.SET_NULL, null=True, blank=True)
    size = models.ForeignKey(Size, verbose_name='Размер', on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.TextField('Теги', help_text='Для отобрадения похожих постов.')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField('Активность', default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['-created']


class About(models.Model):
    bg = models.URLField('Шапка')
    img = models.URLField('Фото 720х866')
    title = models.CharField('Заголовок', max_length=30)
    text = RichTextField()