from django.urls import path
from . import views

urlpatterns = [
    path('', views.juegos, name='juegos'),
    path('juegos/', views.juegos, name='juegos'),
    path('crear/', views.crear_juego, name='crear_juego'),
]