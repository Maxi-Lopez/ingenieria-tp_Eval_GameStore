from django.shortcuts import render, redirect, get_object_or_404
from .forms import PosteoForm
from .models import Posteo
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def posteos(request):
    if request.method == 'POST':
        form = PosteoForm(request.POST, request.FILES)

        if form.is_valid():
            posteo = form.save(commit=False)
            posteo.usuario = request.user
            posteo.save()
            return redirect('posteos')
    else:
        form = PosteoForm()
    posteos =Posteo.objects.filter(activo = True).order_by('-id')
    
    return render(request, 'comunidad/posteos.html',{'form':form, 'posteos':posteos})

@login_required
def eliminar_posteo(request, id):
    posteo = get_object_or_404(Posteo, id=id)
    if request.method == 'POST':
        posteo.activo = False
        posteo.save()
        return redirect('posteos')
    return render(request, 'comunidad/eliminar_posteo.html', {'posteo':posteo})

@login_required
def editar_posteo(request,id):
    posteo = get_object_or_404(Posteo, id=id)
    if request.method == 'POST':
        form = PosteoForm( request.POST, instance=posteo)
        
        if form.is_valid():
            form.save()
            return redirect('posteos')
    else:
        form = PosteoForm(instance=posteo)
    return render(request, 'comunidad/editar_posteo.html',{'posteo':posteo, 'form':form})