from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio' ),
    path('quienes_somos/', views.quienes_somos, name='quienes_somos' ),
    path('perfil/', views.perfil, name='perfil')
]