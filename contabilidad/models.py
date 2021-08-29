from django.db import models

# Create your models here.


class Caja(models.Model):
    TIPO_CAJA = (
        ('Ingreso', 'Ingreso'),
        ('Egreso', 'Egreso'),
    )
    tipo_caja = models.CharField(max_length=7, choices=TIPO_CAJA, null=True)
    descripcion = models.CharField(max_length=250)
    cantidad = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.descripcion


class ApoyoR(models.Model):
    responsable_interno = models.CharField(max_length=60)
    interno = models.CharField(max_length=60)
    contacto = models.CharField(max_length=25, null=True)
    apoyo_total = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.responsable_interno


class Apoyo(models.Model):
    titular = models.ForeignKey(ApoyoR, null=True, on_delete=models.SET_NULL)
    cantidad = models.IntegerField()
    fecha_pago = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titular
