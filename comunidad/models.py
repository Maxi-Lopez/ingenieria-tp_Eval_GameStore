from django.db import models
from videojuegos.models import Juego
from usuarios.models import UsuarioPersonalizado
# Create your models here.

class Posteo(models.Model):
    usuario = models.ForeignKey(UsuarioPersonalizado, on_delete=models.CASCADE, related_name='posteos')
    contenido = models.CharField(max_length=500)
    foto_posteo = models.ImageField(upload_to='posteo_fp', null=True, blank=True)
    juego = models.ForeignKey(Juego, on_delete=models.CASCADE, null=True, blank=True)
    activo = models.BooleanField(default=1, null=True, blank=True)
    
