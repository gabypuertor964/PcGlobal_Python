from django.contrib import admin
from inventory.models import categories, brands, products, unitsProducts,unitsBuy

from django.utils.text import slugify

class adminCategory(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nombre',)}

    def save_model(self, request, obj, form, change):
        if not obj.slug:
            obj.slug = slugify(obj.nombre)
        super().save_model(request, obj, form, change) 

# Register your models here.
admin.site.register(categories, adminCategory)
admin.site.register(brands)
admin.site.register(products)
admin.site.register(unitsProducts)
admin.site.register(unitsBuy)