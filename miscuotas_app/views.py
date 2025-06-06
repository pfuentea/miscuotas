from django.shortcuts import render
from django.db.models import F
from .models import Pago, Apoderado, Bonificacion
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def index(request):
    return render(request, 'index.html')

@login_required
def pagos_apoderado(request):
    apoderado = Apoderado.objects.get(user=request.user)
    pagos = Pago.objects.filter(apoderado=apoderado)
    pagos_al_dia = pagos.filter(fecha_pago__lte=F('fecha_limite'))
    pagos_pendientes = pagos.filter(fecha_pago__gt=F('fecha_limite'))
    bonificaciones = Bonificacion.objects.filter(apoderado=apoderado)

    
    context = {
        'pagos_al_dia': pagos_al_dia,
        'pagos_pendientes': pagos_pendientes,
        'bonificaciones': bonificaciones,
    }
    
    return render(request, 'pagos_apoderado.html', context)