from django.contrib import admin
from .models import Interno, Familia, ResponsableInterno

# Register your models here.


class InternoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "adicciones"]


admin.site.register(ResponsableInterno)
admin.site.register(Interno, InternoAdmin)
admin.site.register(Familia)
