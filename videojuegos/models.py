from django.db import models

# Create your models here.
class Consola(models.Model):
    nombre=models.CharField(max_length=100)
    fabricante = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)
    fecha = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.nombre

class Genero(models.Model):
    nombre=models.CharField(max_length=50)
    activo = models.BooleanField(default=True)
    fecha = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.nombre

class Juego(models.Model):
    titulo = models.CharField(max_length=100)
    desarrollador = models.CharField(max_length=100)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, blank=True, null=True)
    fecha_lanzamiento = models.DateField()
    fecha_carga = models.DateField(auto_now_add=True)
    activo = models.BooleanField(default=True)
    def __str__(self):
        return self.titulo


    