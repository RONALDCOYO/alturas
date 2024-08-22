from django.db import models

class PermisoAlturas(models.Model):
    empleado_id = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    cedula = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()
    carnet_alturas_numero = models.CharField(max_length=50)
    fecha_curso = models.DateField()
    entidad_curso = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} - {self.carnet_alturas_numero}"
