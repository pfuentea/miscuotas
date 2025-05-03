from django.db import models
from django.contrib.auth.models import User
from .apoderado import Apoderado
from .curso import Curso
from .conceptopago import ConceptoDePago

class Pago(models.Model):
    apoderado = models.ForeignKey(Apoderado, related_name='pagos', on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateField()
    fecha_limite = models.DateField()
    curso = models.ForeignKey(Curso, related_name='pagos', on_delete=models.CASCADE)
    concepto = models.ForeignKey(ConceptoDePago, related_name='pagos', on_delete=models.SET_NULL, null=True, blank=True)

    def esta_al_dia(self):
        return self.fecha_pago <= self.fecha_limite

    def __str__(self):
        return f"Pago de {self.apoderado.nombre} en {self.curso.nombre} - ${self.monto} el {self.fecha_pago}"