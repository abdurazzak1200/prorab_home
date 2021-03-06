# Generated by Django 3.2.9 on 2022-04-08 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_slider_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bg', models.URLField(verbose_name='Шапка')),
                ('img', models.URLField(verbose_name='Фото 720х866')),
                ('title', models.CharField(max_length=30, verbose_name='Заголовок')),
                ('text', models.TextField(verbose_name='Введите текст')),
            ],
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категорию', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='slider',
            options={'verbose_name': 'Слайдер', 'verbose_name_plural': 'Слайдеры'},
        ),
        migrations.AlterModelOptions(
            name='subcategory',
            options={'verbose_name': 'Подкатегорию', 'verbose_name_plural': 'Подкатегории'},
        ),
    ]
