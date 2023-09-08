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
class GendersAdmin(admin.ModelAdmin):

    #Campos a mostrar
    list_display = ("id", "nombre")

    #Campos empleados como link a la pagina de modificacion
    list_display_links = ("id",)

    #Items editables en el panel (Input)
    list_editable = ("nombre",)

    #Campos por los que se puede buscar
    search_fields = ("nombre",)

@admin.register(Addresses)
class AddressesAdmin(admin.ModelAdmin):
    
    list_display = ("id","client_name", "direccion")
    list_editable = ("direccion",)
    search_fields = ("id_cliente__first_name", "id_cliente__last_name", "direccion")

    def client_name(self, obj):
        return f"{obj.id_cliente.first_name} {obj.id_cliente.last_name}"
    client_name.short_description = "Nombre del Cliente"

@admin.register(UserCustom)
class UserCustomAdmin(admin.ModelAdmin):
    pass