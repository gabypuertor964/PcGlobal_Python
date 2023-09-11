from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from landing.models import Areas,States

# Register your models here.
# admin.site.register(Areas)
# admin.site.register(States)

@admin.register(Areas)
class AreasAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)
    list_display_links = ('nombre',)

@admin.register(States)
class StatesAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'get_area_nombre')
    list_editable = ('nombre',)
    search_fields = ('nombre', 'id_area__nombre')  # Cambiado a 'id_area__nombre'
    list_per_page = 4

    def get_area_nombre(self, obj):
        return obj.id_area.nombre if obj.id_area else ''

    get_area_nombre.short_description = 'Nombre de Área'
