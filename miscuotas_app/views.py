from django.shortcuts import render
from django.db.models import F
from .models import Pago, Apoderado, Bonificacion
# Create your views here.

def index(request):
    return render(request, 'index.html')


def pagos_apoderado(request):
    apoderado = Apoderado.objects.get(user=request.user)
    pagos = Pago.objects.filter(apoderado=apoderado)
    pagos_al_dia = pagos.filter(fecha_pago__lte=F('fecha_limite'))
    pagos_pendientes = pagos.filter(fecha_pago__gt=F('fecha_limite'))
    
    context = {
        'pagos_al_dia': pagos_al_dia,
        'pagos_pendientes': pagos_pendientes
    }
    
    #return render(request, 'app/pagos_apoderado.html', context)
    return render(request, 'pagos_apoderado.html', context)