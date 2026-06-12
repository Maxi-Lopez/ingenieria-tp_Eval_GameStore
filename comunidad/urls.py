from django.urls import path
from . import views
urlpatterns = [
    path('', views.posteos, name='posteos'),
    path('eliminar_posteo/<int:id>/', views.eliminar_posteo, name='eliminar_posteo'),
    path('editar_posteo/<int:id>/', views.editar_posteo, name='editar_posteo')
]