from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: HttpResponseRedirect('/permisos/listar/')),  # Redirige la raíz a la vista de listado de permisos
    path('permisos/', include('gestion_permisos.urls')),
]
