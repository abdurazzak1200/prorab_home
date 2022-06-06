# Generated by Django 3.2.9 on 2022-06-02 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_size'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kg', models.DecimalField(decimal_places=1, max_digits=10, verbose_name='Килограм')),
            ],
            options={
                'verbose_name': 'Вес',
            },
        ),
    ]
