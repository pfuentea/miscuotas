from django.db import models
from .apoderado import Apoderado

class Bonificacion(models.Model):
    apoderado = models.ForeignKey(Apoderado, related_name='bonificaciones', on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=255)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField()

    def __str__(self):
        return f"Bonificación {self.descripcion} - ${self.monto}"