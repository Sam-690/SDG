from django.urls import path
from .views import caja, cajaF, Contabilidad, RegistroApoyo, IngresoApoyo, DetallesApoyo

urlpatterns = [
    path('caja/', caja, name="caja"),
    path('cajaF/', cajaF, name="cajaF"),
    path('contabilidad/', Contabilidad, name="contabilidad"),
    path('registroApoyo/', RegistroApoyo, name="RegistroApoyo"),
    path('ingresoApoyo/', IngresoApoyo, name='IngresoApoyo'),
    path('detallesApoyo/<str:pk_detail>/', DetallesApoyo, name='detallesApoyo'),
]
