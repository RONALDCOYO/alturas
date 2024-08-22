from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.crear_permiso, name='crear_permiso'),
    path('listar/', views.listar_permisos, name='listar_permisos'),
    path('<int:id>/', views.detalle_permiso, name='detalle_permiso'),
]
