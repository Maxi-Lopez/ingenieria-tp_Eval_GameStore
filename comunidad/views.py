from django.shortcuts import render, redirect, get_object_or_404
from .forms import PosteoForm
from .models import Posteo
# Create your views here.
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
    posteos =Posteo.objects.filter(activo = True)
    
    return render(request, 'comunidad/posteos.html',{'form':form, 'posteos':posteos})