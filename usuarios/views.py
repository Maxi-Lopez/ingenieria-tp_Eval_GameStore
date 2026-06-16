from django.shortcuts import render, redirect
from .forms import UsuarioPersonalizadoForm
from django.contrib.auth import login
from django.contrib.auth.models import Group


def register(request):
    if request.method == 'POST':
        form = UsuarioPersonalizadoForm(request.POST, request.FILES)

        if form.is_valid():
            usuario = form.save()

            grupo_comun = Group.objects.filter(
                name='usuario_comun'
            ).first()

            if grupo_comun:
                usuario.groups.add(grupo_comun)
                usuario.rol_usuario = grupo_comun
                usuario.save()

            login(request, usuario)

            return redirect('inicio')

    else:
        form = UsuarioPersonalizadoForm()

    return render(
        request,
        'registration/register.html',
        {'form': form}
    )