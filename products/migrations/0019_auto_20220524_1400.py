# Generated by Django 3.2.9 on 2022-05-24 14:00

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_size'),
        ('products', '0018_alter_product_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='diameter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.diameter', verbose_name='Диаметр'),
        ),
        migrations.AlterField(
            model_name='product',
            name='liter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.liter', verbose_name='Литр'),
        ),
        migrations.AlterField(
            model_name='product',
            name='meter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.meter', verbose_name='Метр'),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.size', verbose_name='Размер'),
        ),
    ]
