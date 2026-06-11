from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group


# Create your models here.
class UsuarioPersonalizado(AbstractUser):
    telefono = models.CharField(max_length = 20, null= True, blank=True)
    foto_perfil = models.ImageField(upload_to='users_fp', null=True, blank=True)
    rol_usuario = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True, default=1)
    def __str__(self):
        return f"{self.first_name} - {self.last_name}"
    