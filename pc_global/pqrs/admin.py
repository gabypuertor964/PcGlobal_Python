from django.contrib import admin
from pqrs.models import Pqrs,PqrsTypes

# Register your models here.
# admin.site.register(Pqrs)
# admin.site.register(PqrsTypes)

@admin.register(PqrsTypes)
class PqrsTypesAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    list_display_links = ('nombre',)
    search_fields = ('nombre',)


@admin.register(Pqrs)
class PqrsAdmin(admin.ModelAdmin):
    list_display = (
                    'id', 'id_cliente', 'title', 'date_occurrence', 'id_tipo_pqrs',
                    'descripcion', 'respuesta', 'fecha_creacion', 'id_estado'
                    )
    list_display_links = ('descripcion', 'title', 'fecha_creacion')
    list_editable = ('respuesta', 'id_estado')
    search_fields = ('title', 'id')
    list_filter = ('id_tipo_pqrs', 'id_estado')
    list_per_page = 10
