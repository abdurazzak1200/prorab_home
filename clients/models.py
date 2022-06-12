from django.db import models

# Create your models here.
class Clients(models.Model):
    img = models.ImageField('Лого клиента', upload_to='clients')

    class Meta:
        verbose_name = 'Клиента'
        verbose_name_plural = 'Клиенты'


