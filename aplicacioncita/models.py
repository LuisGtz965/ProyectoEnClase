from django.db import models


    #Modelo que representa a un usuario en la base de datos.
    #Campos:
    #    - nombre: Almacena el nombre del usuario (cadena de texto)
    #    - edad: Almacena la edad con precisión decimal
    #    - correo_electronico: Almacena el email (cadena de texto)
class Usuarios(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.DecimalField(max_digits=5, decimal_places=2)
    correo_electronico = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.nombre} {self.correo_electronico} {self.edad}"
    
    #Representación legible del objeto (usado en el admin de Django y shell).
    #Devuelve: "Nombre email edad" (ej: "Juan juan@example.com 25.50")
        


