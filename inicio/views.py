from django.shortcuts import render
from usuarios.models import UsuarioPersonalizado
# Create your views here.
def inicio(request):
    return render (request, 'inicio/inicio.html')

def quienes_somos(request):
    return render(request, 'inicio/quienes_somos.html')

def perfil(request):
    return render(request, 'inicio/perfil.html')