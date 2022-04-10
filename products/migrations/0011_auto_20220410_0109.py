# Generated by Django 3.2.9 on 2022-04-10 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_alter_about_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='diameter',
            field=models.BooleanField(default=False, verbose_name='Диаметр'),
        ),
        migrations.AddField(
            model_name='product',
            name='liter',
            field=models.BooleanField(default=False, verbose_name='Литр'),
        ),
        migrations.AddField(
            model_name='product',
            name='meter',
            field=models.BooleanField(default=False, verbose_name='Метр'),
        ),
    ]
