from django.contrib import admin
from .models import Caja, ApoyoR, Apoyo

# Register your models here.


class CajaAdmin(admin.ModelAdmin):
    list_display = ["tipo_caja", "descripcion"]


class ApoyoRAdmin(admin.ModelAdmin):
    list_display = ["responsable_interno"]


class ApoyoAdmin(admin.ModelAdmin):
    list_display = ["titular", "cantidad", "fecha_pago"]


admin.site.register(Caja)
admin.site.register(ApoyoR)
admin.site.register(Apoyo)
