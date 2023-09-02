from django.contrib import admin
from inventory.models import Categories, Brands, Products, UnitsProducts,UnitsBuy

from django.utils.text import slugify

class adminCategory(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nombre',)}

    def save_model(self, request, obj, form, change):
        if not obj.slug:
            obj.slug = slugify(obj.nombre)
        super().save_model(request, obj, form, change) 
        
class adminProduct(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('modelo',)}

    def save_model(self, request, obj, form, change):
        if not obj.slug:
            obj.slug = slugify(obj.nombre)
        super().save_model(request, obj, form, change) 

# Register your models here.
admin.site.register(Categories, adminCategory)
admin.site.register(Brands)
admin.site.register(Products, adminProduct)
admin.site.register(UnitsProducts)
admin.site.register(UnitsBuy)