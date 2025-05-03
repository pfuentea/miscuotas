from django.db import models
from .establecimiento import Establecimiento 

class Curso(models.Model):
    nombre = models.CharField(max_length=255)
    establecimiento = models.ForeignKey(Establecimiento, related_name='cursos', on_delete=models.CASCADE)
    descripcion = models.TextField()

    def __str__(self):
        return f"{self.nombre} - {self.establecimiento.nombre}"