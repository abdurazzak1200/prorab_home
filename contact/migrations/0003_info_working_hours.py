# Generated by Django 3.2.9 on 2022-06-12 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_auto_20220528_1514'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='working_hours',
            field=models.CharField(default=1, max_length=40, verbose_name='Режим работы'),
            preserve_default=False,
        ),
    ]
