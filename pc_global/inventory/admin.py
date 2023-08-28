from django.contrib import admin
from .models import Categorias, Marcas, Productos, UnidadesProductos

admin.site.register(Categorias)
admin.site.register(Marcas)
admin.site.register(Productos)
admin.site.register(UnidadesProductos)