from django.shortcuts import render, redirect, get_object_or_404
from .models import Juego, Oferta, Genero, Consola
from .forms import JuegoForm, GeneroForm, ConsolaForm
from django.contrib.auth.decorators import login_required, permission_required


@login_required
@permission_required('videojuegos.view_juego')
def juegos(request):
    juegos = Juego.objects.filter(activo=True).order_by('-id')
    return render(request,'videojuegos/juegos.html',{'juegos': juegos})


@login_required
def crear_juego(request):
    if request.method == 'POST' :
        form = JuegoForm(request.POST,request.FILES )
        if form.is_valid():
            form.save()
            return redirect('juegos')
    else:
        form = JuegoForm()
    return render(request,'videojuegos/crear_juego.html',{'form': form})


@login_required
def editar_juego(request, id):
    juego = get_object_or_404(Juego, id=id)
    if request.method == 'POST' :
        form = JuegoForm( request.POST, instance=juego)
        if form.is_valid():
            form.save()
            return redirect('juegos')
    else:
        form = JuegoForm(instance=juego)
    return render(request,'videojuegos/editar_juego.html',{'form': form,'juego': juego})

@login_required
def eliminar_juego(request, id):
    juego = get_object_or_404(Juego, id=id)
    if request.method == 'POST':
        juego.activo = False
        juego.save()
        return redirect('juegos')
    return render(request,'videojuegos/eliminar_juego.html',{'juego': juego})

@login_required
def agregar_oferta(request,id):
    juego = get_object_or_404(Juego, id=id)
    if request.method =='POST':
        oferta_existente = Oferta.objects.filter(juego=juego, activo=True).first()
        if oferta_existente:
            return redirect('juegos')    
        else:
            precio_oferta = juego.precio * 0.8 
            Oferta.objects.create(juego= juego, activo = True, precio_oferta = precio_oferta )
        return redirect('juegos')

@login_required
def quitar_oferta(request,id):
    juego = get_object_or_404(Oferta, id=id)
    if request.method =='POST':
        juego.activo = False
        juego.save()
        return redirect('oferta')

@login_required
def juegos_oferta(request):
    juegos = Oferta.objects.filter(activo=True).order_by('-id')
    return render(request, 'videojuegos/oferta.html', {'juegos':juegos})

@login_required
def agregar_genero(request):
    generos = Genero.objects.filter(activo = True)
    if request.method == 'POST':
        form = GeneroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_genero')
    else:
        form = GeneroForm()
    return render(request, 'videojuegos/agregar_genero.html', {'generos':generos, 'form':form})


@login_required
def agregar_consola(request):
    consolas = Consola.objects.filter(activo = True)
    if request.method == 'POST':
        form = ConsolaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_consola')
    else:
        form = GeneroForm()
    return render(request, 'videojuegos/agregar_consola.html', {'consolas':consolas, 'form':form})

@login_required
def detalle_juego(request, id):
    juego = get_object_or_404(Juego, id = id)
    return render (request, 'videojuegos/detalle_juego.html',{'juego':juego})