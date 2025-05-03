from django.db import models
from django.contrib.auth.models import User
from .curso import Curso

class Apoderado(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    curso = models.ForeignKey(Curso, related_name='apoderados', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} - {self.curso.nombre}"