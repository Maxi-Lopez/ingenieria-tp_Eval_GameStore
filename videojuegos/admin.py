from django.contrib import admin

# Register your models here.
from .models import Juego, Oferta, Consola,  Genero

admin.site.register(Juego)
admin.site.register(Oferta)
admin.site.register(Consola)
admin.site.register(Genero)
