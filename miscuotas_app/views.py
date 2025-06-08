from django.shortcuts import render, redirect
from django.db.models import F
from .models import Pago, Apoderado, Bonificacion, Tesorero, Manager
from django.contrib.auth.decorators import login_required
# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            role = form.cleaned_data['role']
            nombre = form.cleaned_data.get('nombre')
            curso = form.cleaned_data.get('curso')
            if role == 'apoderado':
                Apoderado.objects.create(user=user, nombre=nombre, curso=curso)
            elif role == 'tesorero':
                Tesorero.objects.create(user=user, curso=curso)
            else:
                Manager.objects.create(user=user)
            login(request, user)
            return redirect('dashboard')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required
def dashboard(request):
    if hasattr(request.user, 'apoderado'):
        return render(request, 'apoderado/dashboard.html')
    if hasattr(request.user, 'tesorero'):
        return render(request, 'tesorero/dashboard.html')
    if hasattr(request.user, 'manager'):
        return render(request, 'manager/dashboard.html')
    return redirect('index')

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