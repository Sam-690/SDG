from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Invetario(models.Model):
    nombre_entrega = models.CharField(max_length=60)
    nombre_recibe = models.CharField(max_length=60)
    nombre_interno = models.CharField(max_length=60, null=True)
    cosas_entregadas = models.TextField(blank=True)
    evidencias = models.ImageField(upload_to="evidencias", null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nombre_entrega
