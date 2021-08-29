from django.shortcuts import render, redirect, get_object_or_404
from . import views
from .models import Caja, Apoyo, ApoyoR
from .forms import CajaForm, RegistroForm, ApoyoForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, permission_required


# Create your views here.
@login_required
@permission_required('contabilidad.add_caja')
def caja(request):
    caja = Caja.objects.all().order_by('-fecha')

    data = {
        'caja': caja,
    }
    return render(request, 'caja.html', data)


@login_required
@permission_required('contabilidad.add_caja')
def cajaF(request):
    data = {
        'form': CajaForm()
    }
    if request.method == 'POST':
        formulario = CajaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Registro de entrada realizado")
            return redirect('caja')
        data["form"] = formulario
    return render(request, 'cajaF.html', data)


@login_required
@permission_required('contabilidad.add_caja')
def Contabilidad(request):
    titulares = ApoyoR.objects.all()

    context = {'titulares': titulares}

    return render(request, 'contabilidad.html', context)


@login_required
@permission_required('contabilidad.add_caja')
def RegistroApoyo(request):
    data = {
        'form': RegistroForm()
    }

    if request.method == 'POST':
        formulario = RegistroForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Nuevo Usuario Registrado")
            return redirect('contabilidad')
            data["form"] = formulario
    return render(request, 'registroApoyo.html', data)


@login_required
@permission_required('contabilidad.add_caja')
def IngresoApoyo(request):
    data = {
        'form': ApoyoForm()
    }

    if request.method == 'POST':
        formulario = ApoyoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Apoyo Realizado")
            return redirect('contabilidad')
        data["form"] = formulario
    return render(request, 'ingresoApoyo.html', data)


@login_required
@permission_required('contabilidad.add_caja')
def DetallesApoyo(request, pk_detail):
    apoyosR = ApoyoR.objects.get(id=pk_detail)

    apoyos = apoyosR.apoyo_set.all().order_by('-fecha_pago')

    apoyo_count = apoyos.count()

    context = {'apoyosR': apoyosR, 'apoyos': apoyos,
               'apoyo_count': apoyo_count}
    return render(request, 'detallesApoyo.html', context)
