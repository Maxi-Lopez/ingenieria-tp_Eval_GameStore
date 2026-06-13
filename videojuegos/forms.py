from django import forms
from .models import Juego, Consola, Genero

class JuegoForm(forms.ModelForm):
    class Meta:
        model = Juego
        fields = [
            'titulo',
            'desarrollador',
            'genero',
            'consola',
            'precio',
            'portada',
            'fecha_lanzamiento'
        ]

class ConsolaForm(forms.ModelForm):
    class Meta:
        model = Consola
        fields = [
            'nombre',
            'fabricante'
        ]

class GeneroForm(forms.ModelForm):
    class Meta:
        model = Genero
        fields = [
            'nombre',
        ]
