from django.contrib import admin

# Register your models here.
from .models import Establecimiento, Curso, Apoderado, Tesorero, Pago

admin.site.register(Establecimiento)
admin.site.register(Curso)
admin.site.register(Apoderado)
admin.site.register(Tesorero)
admin.site.register(Pago)