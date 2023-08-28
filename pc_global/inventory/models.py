from django.db import models
from landing.models import Users, Estado
# from datetime import datetime

class Marcas(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="id_marcas", db_comment="Llave Primaria")
    nombre = models.CharField(unique=True, max_length=50, db_comment="Nombre Marca", verbose_name="nombre_marca", null=False)

    def __str__(self):
        return self.nombre


class Categorias(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="id_categorias")
    nombre_categoria = models.CharField(max_length=50, db_comment="Nombre de la Categoría", unique=True,
                                        verbose_name="nombre_categoria", null=False)

    def __str__(self):
        return self.nombre_categoria


class Productos(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="id_categorias")
    fk_id_marcas = models.ForeignKey(Marcas, on_delete=models.CASCADE, verbose_name="id_marcas", null=False,
                                     blank=False)
    fk_id_categorias = models.ForeignKey(Categorias, on_delete=models.CASCADE, null=False,
                                         blank=False, verbose_name="id_categorias")
    modelo = models.CharField(max_length=55, unique=True, blank=False, null=False, verbose_name="modelo")
    # imagen_producto = models.ImageField(upload_to="img_producto/%Y/%m/%d", null=True, blank=False)
    imagen_producto = models.TextField(null=False, blank=False, db_column="imagen", verbose_name="imagen_producto",
                                       db_comment="Imagen del Producto")
    descripcion = models.TextField(null=False, blank=False, verbose_name="descripcion",
                                   db_comment="Descripcion del Producto")
    precio = models.CharField(max_length=10, null=False, blank=False, verbose_name="precio",
                              db_comment="Precio unitario del producto")
    date_creation = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.modelo


class UnidadesProductos(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="id_unidades_productos")
    fk_id_producto = models.ForeignKey(Productos, on_delete=models.CASCADE, null=False)
    serial = models.CharField(max_length=255, unique=True, null="False", blank=False, verbose_name="serial",
                              db_comment="Serial Unidad del producto")
    # id_factura = models.ForeignKey(FacturasCompra, on_delete=models.CASCADE, null=False)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id

    class Meta:
        # nombre de la tabla en base de datos
        db_table = "unidades_producto"
