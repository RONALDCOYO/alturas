from django import forms
from .models import PermisoAlturas

class PermisoAlturasForm(forms.ModelForm):
    class Meta:
        model = PermisoAlturas
        fields = ['empleado_id', 'nombre', 'cedula', 'fecha_nacimiento', 'carnet_alturas_numero', 'fecha_curso', 'entidad_curso']
