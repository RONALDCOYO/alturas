from django.shortcuts import render, get_object_or_404, redirect
from .models import PermisoAlturas
from .forms import PermisoAlturasForm

def crear_permiso(request):
    if request.method == "POST":
        form = PermisoAlturasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_permisos')
    else:
        form = PermisoAlturasForm()
    return render(request, 'crear_permiso.html', {'form': form})

def listar_permisos(request):
    permisos = PermisoAlturas.objects.all()
    return render(request, 'gestion_permisos/listar_permisos.html', {'permisos': permisos})

def detalle_permiso(request, id):
    permiso = get_object_or_404(PermisoAlturas, pk=id)
    return render(request, 'detalle_permiso.html', {'permiso': permiso})
