from django.db import models

# Create your models here.


class ResponsableInterno(models.Model):
    nombre = models.CharField(max_length=60)
    apellidos = models.CharField(max_length=60)
    edad = models.IntegerField()
    parentesco = models.CharField(max_length=60)
    direccion = models.CharField(max_length=120)
    telefono = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
        return self.apellidos


class Familia(models.Model):
    padre = models.CharField(max_length=60)
    madre = models.CharField(max_length=60)
    conyuge = models.CharField(max_length=60)
    hijo1 = models.CharField(max_length=60)
    hijo2 = models.CharField(max_length=60)

    def __str__(self):
        return self.padre


class Interno(models.Model):
    nombre = models.CharField(max_length=60)
    apellidos = models.CharField(max_length=60)
    fecha_nacimiento = models.DateField()
    lugar_nacimiento = models.CharField(max_length=60)
    edad = models.IntegerField()
    sexo = models.CharField(max_length=50, null=True)
    profecion = models.CharField(max_length=50, null=True)
    adicciones = models.CharField(max_length=50)
    tiempo_adiccion = models.IntegerField()
    direccion = models.CharField(max_length=120)
    estado_civil = models.CharField(max_length=60)
    enfermedades = models.CharField(max_length=120)
    tratamiento = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    observaciones = models.TextField()
    imagen = models.ImageField(upload_to="internos", null=True, blank=True)
    familia = models.ForeignKey(Familia, on_delete=models.CASCADE)
    responsableInterno = models.ForeignKey(
        ResponsableInterno, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
