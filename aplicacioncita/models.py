from django.db import models

class Usuarios(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.DecimalField(max_digits=5, decimal_places=2)
    correo_electronico = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.nombre} {self.correo_electronico} {self.edad}"