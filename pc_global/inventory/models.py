from django.db import models
from landing.models import Users, Estado
# from datetime import datetime

class Marcas(models.Model):
    nombre = models.CharField(unique=True, max_length=50, db_comment="Nombre Marca", verbose_name="Nombre de la marca")

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"
        db_table ="marcas"
        ordering = ["id"]


class Categorias(models.Model):
    
    
    nombre_categoria = models.CharField(max_length=50, db_comment="Nombre de la Categoría", unique=True,
                                        verbose_name="nombre de la categoría")

    def __str__(self):
        return self.nombre_categoria
    
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorías"
        db_table = "categorias"
        ordering = ["id"]


class Productos(models.Model):
    marcas = models.ForeignKey(Marcas, on_delete=models.CASCADE, verbose_name="id_marcas", null=False, blank=False)
    categorias = models.ForeignKey(Categorias, on_delete=models.CASCADE, verbose_name="id_categorias", null=False, blank=False)
    modelo = models.CharField(max_length=55, unique=True, verbose_name="modelo")
    # imagen_producto = models.ImageField(upload_to="img_producto/%Y/%m/%d", null=True, blank=False)
    imagen_producto = models.TextField(db_column="imagen", verbose_name="Imágen del producto",db_comment="Imágen del producto")
    descripcion = models.TextField( verbose_name="Descripción", db_comment="Descripción del producto")
    precio = models.CharField(max_length=10, verbose_name="precio", db_comment="Precio unitario del producto")
    date_creation = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.modelo
    
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        db_table = "productos"
        ordering = ["id"]


class UnidadesProductos(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="id_unidades_productos")
    id_producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    serial = models.CharField(max_length=255, unique=True, null="False", verbose_name="seriales", db_comment= "Serial Unidad del producto")
    # id_factura = models.ForeignKey(FacturasCompra, on_delete=models.CASCADE, null=False)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = "Unidad producto"
        verbose_name_plural = "Unidades productos"
        db_table = "unidades_productos"
        ordering = ["id"]
