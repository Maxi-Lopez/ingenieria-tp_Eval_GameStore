from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from usuarios.models import UsuarioPersonalizado
from comunidad.models import Posteo
# Create your views here.


def inicio(request):
    return render (request, 'inicio/inicio.html')


def quienes_somos(request):
    return render(request, 'inicio/quienes_somos.html')

@login_required
def perfil(request):
    posteos = Posteo.objects.filter(usuario = request.user)
    return render(request, 'inicio/perfil.html', {'posteos':posteos})