from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from landing.models import Areas,States

# Register your models here.
@admin.register(Areas)
class AreasAdmin(ImportExportModelAdmin):
    
    #Campos a mostrar
    list_display = ("id", "nombre")

    #Campos empleados como link a la pagina de modificacion
    list_display_links = ("id",)

    #Items editables en el panel (Input)
    list_editable = ("nombre",)

    #Campos por los que se puede buscar
    search_fields = ("nombre",)

@admin.register(States)
class StatesAdmin(ImportExportModelAdmin):
    
    #Campos a mostrar
    list_display = ("id", "nombre", "id_area")

    #Campos empleados como link a la pagina de modificacion
    list_display_links = ("id",)

    #Items editables en el panel (Input)
    list_editable = ("nombre","id_area")

    #Campos por los que se puede buscar
    search_fields = ("nombre","id_area")