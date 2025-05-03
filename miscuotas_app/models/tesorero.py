from django.db import models
from django.contrib.auth.models import User
from .curso import Curso

class Tesorero(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, related_name='tesoreros', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.curso.nombre}"