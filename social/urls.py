from django.urls import path, include
from .views import home, internos, formularioI, formularioR, formularioF, modificar_interno, eliminar_interno, DetailsInternos, InternoViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'interno', InternoViewSet)

urlpatterns = [
    path('', home, name='home'),
    path('internos/', internos, name='internos'),
    path('formularioR/', formularioR, name='formularioR'),
    path('formularioI/', formularioI, name='formularioI'),
    path('formularioF/', formularioF, name='formularioF'),
    path('modificar-interno/<id>', modificar_interno, name="modificar_interno"),
    path('eliminar-interno/<id>', eliminar_interno, name="eliminar_interno"),
    path('detallesInterno/<str:pk_interno>/',
         DetailsInternos, name="detallesInterno"),
    path('api/', include(router.urls)),
]
