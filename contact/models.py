from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class Info(models.Model):
    phone = PhoneNumberField(verbose_name='Номер телефона')
    address = models.CharField(max_length=250, verbose_name='Адрес')

    class Meta:
        verbose_name = 'Контактную информацию'
        verbose_name_plural = 'Контактная информация'