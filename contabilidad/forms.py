from django import forms
from .models import Caja, ApoyoR, Apoyo


class CajaForm(forms.ModelForm):
    class Meta:
        model = Caja
        fields = '__all__'


class RegistroForm(forms.ModelForm):
    class Meta:
        model = ApoyoR
        fields = '__all__'


class ApoyoForm(forms.ModelForm):
    class Meta:
        model = Apoyo
        fields = '__all__'
