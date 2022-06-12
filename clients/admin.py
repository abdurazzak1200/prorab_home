from django.contrib import admin
from .models import *

@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ('img',)

