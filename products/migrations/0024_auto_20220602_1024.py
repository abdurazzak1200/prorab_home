# Generated by Django 3.2.9 on 2022-06-02 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0023_subcategory_kg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='img',
            field=models.ImageField(max_length=256, upload_to='category/%Y-%m-%d', verbose_name='фото категории'),
        ),
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(max_length=256, upload_to='product/%Y-%m-%d', verbose_name='Фото'),
        ),
    ]
