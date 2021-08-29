from django.urls import path
from .views import agenda, Inventario, inventarioForm


urlpatterns = [
    path('agenda/', agenda, name='agenda'),
    path('inventario/', Inventario, name='inventario'),
    path('inventarioForm/', inventarioForm, name='inventarioForm'),
]
