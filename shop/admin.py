from django.contrib import admin
from .models import Liter, Diameter, Meter, Kg

# Register your models here.
admin.site.register(Liter)
admin.site.register(Diameter)
admin.site.register(Meter)
admin.site.register(Kg)