from django.db import models


class Liter(models.Model):
    liter = models.IntegerField('Литр')

    def __str__(self):
        return f'{self.liter}'

    class Meta:
        verbose_name = 'Литр'
        verbose_name_plural = 'Литр'


class Diameter(models.Model):
    diameter = models.DecimalField('Диаметр', max_digits=3, decimal_places=1)

    def __str__(self):
        return f'{self.diameter}'

    class Meta:
        verbose_name = 'Диаметр'
        verbose_name_plural = 'Диаметр'


class Meter(models.Model):
    meter = models.DecimalField('Метр', max_digits=10, decimal_places=1)

    def __str__(self):
        return f'{self.meter}'

    class Meta:
        verbose_name = 'Метр'
        verbose_name_plural = 'Метр'


class Size(models.Model):
    size = models.DecimalField('Размер', max_digits=10, decimal_places=1)

    def __str__(self):
        return f'{self.size}'

    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размер'



class Kg(models.Model):
    kg = models.DecimalField('Килограм', max_digits=10, decimal_places=1)

    def __str__(self):
        return f'{self.kg}'

    class Meta:
        verbose_name = 'Вес'
        verbose_name_plural = 'Вес'
