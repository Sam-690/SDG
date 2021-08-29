from django.contrib import admin
from .models import *

# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    list_display = ["title"]


class InventarioAdmin(admin.ModelAdmin):
    list_display = ["nombre_entrega"]


admin.site.register(Task)
admin.site.register(Invetario)
