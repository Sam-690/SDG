from django.shortcuts import render, redirect, get_object_or_404
from . import views
from .forms import ResponsableForm, InternoForm, FamiliaForm
from .models import Interno, ResponsableInterno, Familia
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework import viewsets
from .serializers import InternoSerializer

# Create your views here.


class InternoViewSet(viewsets.ModelViewSet):
    queryset = Interno.objects.all()
    serializer_class = InternoSerializer

# Interno section


@login_required
def home(request):
    internosR = Interno.objects.all()

    internos_count = internosR.count()

    context = {'internosR': internosR, 'internos_count': internos_count}

    return render(request, 'dashboard.html', context)

# creater


@login_required
@permission_required('social.add_interno')
def internos(request):
    internos = Interno.objects.all().order_by('-created_at')

    data = {
        'internos': internos
    }

    return render(request, 'internos.html', data)


@login_required
@permission_required('social.add_interno')
def formularioR(request):
    data = {
        'form': ResponsableForm()
    }
    if request.method == 'POST':
        formulario = ResponsableForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Registro de Responsable Guardado")
            return redirect('formularioF')
        data["form"] = formulario
    return render(request, 'formulario_responsable.html', data)


@login_required
@permission_required('social.add_interno')
def formularioF(request):
    data = {
        'form': FamiliaForm
    }
    if request.method == 'POST':
        formulario = FamiliaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Registro de Familia Terminado")
            return redirect('formularioI')
        data["form"] = formulario
    return render(request, 'formulario_familia.html', data)


@login_required
@permission_required('social.add_interno')
def formularioI(request):
    data = {
        'form': InternoForm
    }
    if request.method == 'POST':
        formulario = InternoForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Registro del Interno Guardado")
            return redirect('internos')
        data["form"] = formulario
    return render(request, 'formulario_interno.html', data)


# Modificadores
@login_required
@permission_required('social.add_interno')
def modificar_interno(request, id):
    internos = get_object_or_404(Interno, id=id)
    data = {
        'form': InternoForm(instance=internos)
    }

    if request.method == 'POST':
        formulario = InternoForm(
            data=request.POST, instance=internos, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Has editado un interno!")
            return redirect(to="internos")
        data["form"] = formulario

    return render(request, 'editar.html', data)


@login_required
@permission_required('social.add_interno')
def eliminar_interno(request, id):
    interno = get_object_or_404(Interno, id=id)
    interno.delete()
    messages.success(request, 'El interno ha sido elimniado.')
    return redirect(to="internos")


# details ingreso
@login_required
@permission_required('social.add_interno')
def DetailsInternos(request, pk_interno):
    detallesInterno = Interno.objects.get(id=pk_interno)

    detallesResponsable = ResponsableInterno.objects.get(id=pk_interno)

    detallesFamilia = Familia.objects.get(id=pk_interno)

    context = {'detallesInterno': detallesInterno,
               'detallesResponsable': detallesResponsable, 'detallesFamilia': detallesFamilia}

    return render(request, 'details_interno.html', context)
