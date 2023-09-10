from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from pqrs.models import Pqrs,PqrsTypes

# Register your models here.
# admin.site.register(Pqrs)
# admin.site.register(PqrsTypes)

@admin.register(PqrsTypes)
class PqrsTypesAdmin(ImportExportModelAdmin):
    list_display = ('id', 'nombre')
    list_display_links = ('nombre',)
    search_fields = ('nombre',)

class PqrsTypesResource(resources.ModelResource):

    class Meta:
        model = PqrsTypes

        fields = (
            'id',
            'nombre'
        )


@admin.register(Pqrs)
class PqrsAdmin(ImportExportModelAdmin):
    list_display = (
                    'id', 'id_cliente', 'title', 'date_occurrence', 'id_tipo_pqrs',
                    'descripcion', 'respuesta', 'fecha_creacion', 'id_estado'
                    )
    list_display_links = ('descripcion', 'title', 'fecha_creacion')
    list_editable = ('respuesta', 'id_estado')
    search_fields = ('title', 'id')
    list_filter = ('id_tipo_pqrs', 'id_estado')
    list_per_page = 10

class PqrsResource(resources.ModelResource):
    class Meta:
        model = Pqrs

        fields = (
            'id',
            'id_cliente',
            'id_tipo_pqrs',
            'title',
            'fecha_creacion',
            'id_estado',
            'descripcion',
            'respuesta'
        )