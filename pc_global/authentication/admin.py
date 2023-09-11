from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from authentication.models import DocTypes,Genders,Addresses,UserCustom

@admin.register(DocTypes)
class DocTypeAdmin(ImportExportModelAdmin):

    #Campos a mostrar
    list_display = ("id", "nombre", "siglas")

    #Campos empleados como link a la pagina de modificacion
    list_display_links = ("id",)

    #Items editables en el panel (Input)
    list_editable = ("nombre", "siglas")

    #Campos por los que se puede buscar
    search_fields = ("nombre", "siglas")

@admin.register(Genders)
class GendersAdmin(ImportExportModelAdmin):

    #Campos a mostrar
    list_display = ("id", "nombre")

    #Campos empleados como link a la pagina de modificacion
    list_display_links = ("id",)

    #Items editables en el panel (Input)
    list_editable = ("nombre",)

    #Campos por los que se puede buscar
    search_fields = ("nombre",)

@admin.register(Addresses)
class AddressesAdmin(ImportExportModelAdmin):
    
    list_display = ("id","client_name", "direccion")
    list_editable = ("direccion",)
    search_fields = ("id_cliente__first_name", "id_cliente__last_name", "direccion")

    # Obtener el nombre del cliente o su nombre de usuario
    def client_name(self, obj):
        return obj.id_cliente

    # Cambiar el nombre de la columna client_name
    client_name.short_description = "Nombre del Cliente"

@admin.register(UserCustom)
class UserCustomAdmin(ImportExportModelAdmin):

    list_display = ("id","client_name","num_doc")
    search_fields = ("client_name","num_doc")

    # Obtener el nombre del cliente o su nombre de usuario
    def client_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"

    # Cambiar el nombre de la columna client_name
    client_name.short_description = "Nombre Completo"