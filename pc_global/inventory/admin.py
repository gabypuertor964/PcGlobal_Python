from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from inventory.models import Categories, Brands, Products, UnitsProducts,UnitsBuy
from django.utils.text import slugify



class CategoryAdmin(ImportExportModelAdmin):
    
    #Campos a mostrar
    list_display = ("id", "nombre", "slug")

    #Campos empleados como link a la pagina de modificacion
    list_display_links = ("id",)

    #Items editables en el panel (Input)
    list_editable = ("nombre", "slug")

    #Campos por los que se puede buscar
    search_fields = ("nombre", "slug")
    
    list_per_page = 10
    
    # Variable para el slugify
    prepopulated_fields = {'slug': ('nombre',)}

    def save_model(self, request, obj, form, change):
        if not obj.slug:
            obj.slug = slugify(obj.nombre)
        super().save_model(request, obj, form, change) 
        
admin.site.register(Categories, CategoryAdmin)


@admin.register(Brands)
class BrandsAdmin(ImportExportModelAdmin):
    #Campos a mostrar
    list_display = ("id", "nombre")

    #Campos empleados como link a la pagina de modificacion
    list_display_links = ("id",)

    #Items editables en el panel (Input)
    list_editable = ("nombre",)

    #Campos por los que se puede buscar
    search_fields = ("nombre",)
    
    list_per_page = 12

class ProductsAdmin(ImportExportModelAdmin):
    #Campos a mostrar
    list_display = ("id", "modelo", "precio", "slug")

    #Campos empleados como link a la pagina de modificacion
    list_display_links = ("id",)

    #Items editables en el panel (Input)
    list_editable = ("modelo", "precio", "slug")

    #Campos por los que se puede buscar
    search_fields = ("modelo", "precio")
    
    list_per_page = 12
    
    # Variable para el slugify
    prepopulated_fields = {'slug': ('modelo',)}

    def save_model(self, request, obj, form, change):
        if not obj.slug:
            obj.slug = slugify(obj.nombre)
        super().save_model(request, obj, form, change) 
        
admin.site.register(Products, ProductsAdmin)
        
admin.site.register(UnitsProducts)
admin.site.register(UnitsBuy)