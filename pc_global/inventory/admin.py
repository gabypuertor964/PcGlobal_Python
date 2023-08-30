from django.contrib import admin
from .models import Categorias, Marcas, Productos, UnidadesProductos
from django.utils.text import slugify

class CategoriaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nombre_categoria',)}

    def save_model(self, request, obj, form, change):
        if not obj.slug:
            obj.slug = slugify(obj.nombre)
        super().save_model(request, obj, form, change)


admin.site.register(Categorias, CategoriaAdmin)
admin.site.register(Marcas)
admin.site.register(Productos)
admin.site.register(UnidadesProductos)