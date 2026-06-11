from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render (request, 'inicio/inicio.html')


def quienes_somos(request):
    return render(request, 'inicio/quienes_somos.html')