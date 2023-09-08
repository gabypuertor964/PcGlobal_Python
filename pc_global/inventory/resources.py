from import_export import resources
from django.utils.text import slugify
from inventory.models import Products, Categories, Brands

class ProductsResource(resources.ModelResource):
    class Meta:
        model = Products
        fields = ('categoria', 'marca', 'modelo', 'imagen', 'descripcion_1', 'descripcion_2', 'precio', 'slug', 'created_at', 'updated_at')

class CategoriesResource(resources.ModelResource):
    class Meta:
        model = Categories
        fields = ('nombre', 'slug')
        
class BrandsResource(models.ModelResource):
    class Meta:
        model = Brands
        fields = ('nombre')