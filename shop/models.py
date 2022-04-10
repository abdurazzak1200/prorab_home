from django.db import models


class Liter(models.Model):
    liter = models.IntegerField('Литр')


class Diameter(models.Model):
    diameter = models.DecimalField('Диаметр', max_digits=3, decimal_places=1)


class Meter(models.Model):
    meter = models.DecimalField('Метр', max_digits=10, decimal_places=1)