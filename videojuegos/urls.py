from django.urls import path
from . import views

urlpatterns = [
    path('', views.juegos, name='juegos'),
    path('juegos/', views.juegos, name='juegos'),
    path('crear/', views.crear_juego, name='crear_juego'),
    path('editar/<int:id>/', views.editar_juego, name='editar_juego'),
    path('eliminar/<int:id>/', views.eliminar_juego, name='eliminar_juego'),
    path('agregar_oferta/<int:id>/', views.agregar_oferta, name='agregar_oferta'),
    path('quitar_oferta/<int:id>/', views.quitar_oferta, name='quitar_oferta'),
    path('oferta/', views.juegos_oferta, name='oferta')
]