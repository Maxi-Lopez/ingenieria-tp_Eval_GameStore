from django.shortcuts import render, redirect, get_object_or_404
from .models import Juego
from .forms import JuegoForm
from django.contrib.auth.decorators import login_required


@login_required
def juegos(request):
    juegos = Juego.objects.filter(activo=True).order_by('-id')
    return render(
        request,
        'videojuegos/juegos.html',
        {'juegos': juegos}
    )


@login_required
def crear_juego(request):
    if request.method == 'POST':
        form = JuegoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('juegos')

    else:
        form = JuegoForm()

    return render(
        request,
        'videojuegos/crear_juego.html',
        {'form': form}
    )


@login_required
def editar_juego(request, id):
    juego = get_object_or_404(Juego, id=id)

    if request.method == 'POST':
        form = JuegoForm(
            request.POST,
            instance=juego
        )

        if form.is_valid():
            form.save()
            return redirect('juegos')

    else:
        form = JuegoForm(instance=juego)

    return render(
        request,
        'videojuegos/editar_juego.html',
        {
            'form': form,
            'juego': juego
        }
    )


@login_required
def eliminar_juego(request, id):
    juego = get_object_or_404(Juego, id=id)

    if request.method == 'POST':
        juego.activo = False
        juego.save()
        return redirect('juegos')

    return render(
        request,
        'videojuegos/eliminar_juego.html',
        {'juego': juego}
    )