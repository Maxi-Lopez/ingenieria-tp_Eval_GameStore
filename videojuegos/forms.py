from django import forms
from .models import Juego

class JuegoForm(forms.ModelForm):
    class Meta:
        model = Juego
        fields = ['portada',
            'titulo',
            'desarrollador',
            'genero',
            'fecha_lanzamiento'
        ]

