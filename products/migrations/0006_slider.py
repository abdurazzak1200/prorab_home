# Generated by Django 3.2.9 on 2022-03-31 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20220330_1353'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(max_length=30, verbose_name='Описание')),
                ('title', models.CharField(max_length=20, verbose_name='Название')),
            ],
        ),
    ]
