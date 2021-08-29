from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from . import views
from .forms import TaskForm, InventarioForm
from django.contrib import messages
from .models import Task, Invetario
from django.core.paginator import Paginator


# Create your views here.


@login_required
def agenda(request):
    tareas = Task.objects.all().order_by('-created_at')

    p = Paginator(Task.objects.all(), 2)
    page = request.GET.get('page')
    tasks = p.get_page(page)

    data = {
        'tareas': tareas,
        'tasks': tasks,
        'form': TaskForm
    }

    if request.method == 'POST':
        formulario = TaskForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Nueva tarea guardada")
            return redirect('agenda')
            data["form"] = formulario

    return render(request, 'agenda.html', data)


def Inventario(request):
    InventarioR = Invetario.objects.all()

    context = {'InventarioR': InventarioR}
    return render(request, 'inventario.html', context)


def inventarioForm(request):
    data = {
        'form': InventarioForm()
    }
    if request.method == 'POST':
        formulario = InventarioForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Pertenencias Recibidas")
            return redirect('inventario')
        data["form"] = formulario
    return render(request, 'inventarioForm.html', data)
