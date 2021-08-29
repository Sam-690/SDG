from django import forms
from .models import *


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = '__all__'


class InventarioForm(forms.ModelForm):

    class Meta:
        model = Invetario
        fields = '__all__'
