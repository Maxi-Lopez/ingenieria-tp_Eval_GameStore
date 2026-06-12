from django.urls import path
from . import views
urlpatterns = [
    path('', views.posteos, name='posteos'),
]