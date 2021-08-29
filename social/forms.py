from django import forms
from .models import ResponsableInterno, Interno, Familia


class ResponsableForm(forms.ModelForm):
    class Meta:
        model = ResponsableInterno
        fields = '__all__'


class InternoForm(forms.ModelForm):
    class Meta:
        model = Interno
        fields = '__all__'


class FamiliaForm(forms.ModelForm):
    class Meta:
        model = Familia
        fields = '__all__'
