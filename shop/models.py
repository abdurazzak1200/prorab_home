from django.db import models


class Liter(models.Model):
    liter = models.IntegerField('Литр')

    def __str__(self):
        return f'{self.liter}'

    class Meta:
        verbose_name = 'Литр'


class Diameter(models.Model):
    diameter = models.DecimalField('Диаметр', max_digits=3, decimal_places=1)

    def __str__(self):
        return f'{self.diameter}'

    class Meta:
        verbose_name = 'Диаметр'


class Meter(models.Model):
    meter = models.DecimalField('Метр', max_digits=10, decimal_places=1)

    def __str__(self):
        return f'{self.meter}'

    class Meta:
        verbose_name = 'Метр'
