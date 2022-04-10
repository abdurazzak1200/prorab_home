from ckeditor.fields import RichTextField
from django.db import models


class Slider(models.Model):
    desc = models.CharField('Описание', max_length=30)
    title = models.CharField('Название', max_length=20)
    img = models.URLField('Ссылка на фото', max_length=256)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Слайдер'
        verbose_name_plural = 'Слайдеры'


class Category(models.Model):
    name = models.CharField('Название', max_length=50)
    slug = models.SlugField('slug', max_length=60)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'


class SubCategory(models.Model):
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    name = models.CharField('Название', max_length=50)
    slug = models.SlugField('slug', max_length=60)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подкатегорию'
        verbose_name_plural = 'Подкатегории'


class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, verbose_name='Подкатегория', on_delete=models.CASCADE)
    img = models.URLField('Ссылка на фото', max_length=256)
    name = models.CharField('Название', max_length=100)
    desc = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
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