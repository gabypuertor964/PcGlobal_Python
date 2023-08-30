from django.db import models
from facturation.models import receiptBuy

# Tabla: Categorias
class categories(models.Model):

    # Campo Nombre
    nombre = models.CharField(
        max_length=20,
        verbose_name="nombre",
        db_comment="Nombre de la categoria"
    )

    # Slug de la categoria
    slug = models.SlugField(
        max_length=100,
        verbose_name="slug",
        db_comment="Slug de la categoria"
    )

    def __str__(self):
        return self.nombre
    
    # Metadatos de la tabla
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

        db_table = 'categorias'
        ordering = ['id']
    
# Tabla: marcas
class brands(models.Model):

    # Campo Nombre
    nombre = models.CharField(
        max_length=50,
        verbose_name="nombre",
        db_comment="Nombre de la marca"
    )

    def __str__(self):
        return self.nombre
    
    # Metadatos de la tabla
    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

        db_table = 'marcas'
        ordering = ['id']
    
# Tabla: Productos
class products(models.Model):

    # Foreing Key: Id Categoria
    categoria = models.ForeignKey(
        categories,
        on_delete=models.CASCADE,
        db_column='id_categoria',
        db_comment="Id Categoria",
        verbose_name="id_categoria_producto"
    )

    # Foreing Key: Id Marca
    marca = models.ForeignKey(
        brands,
        on_delete=models.CASCADE,
        db_column='id_marca',
        db_comment="Id Marca",
        verbose_name="id_marca_producto"
    )

    # Campo: Modelo
    modelo = models.CharField(
        max_length=255,
        verbose_name="modelo",
        db_comment="Modelo del producto"
    )

    # Campo: URL Imagen
    imagen = models.TextField(
        verbose_name="URL Imagen",
        db_comment="Imagen del producto"
    )

    # Campo: Descripcion 1
    descripcion_1 = models.TextField(
        verbose_name="descripcion 1",
        db_comment="Descripcion 1 del producto"
    )

    # Campo: Descripcion 2
    descripcion_2 = models.TextField(
        verbose_name="descripcion 2",
        db_comment="Descripcion 2 del producto",
        null=True,
        blank=True
    )

    # Campo: Precio
    precio = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="precio",
        db_comment="Precio del producto"
    )

    # Campo: Slug del producto
    slug = models.SlugField(
        max_length=100,
        verbose_name="slug",
        db_comment="Slug del producto"
    )

    # Campo: Fecha de creacion
    create_at = models.DateTimeField(
        auto_now_add=True,
        db_comment="Fecha de creacion",
        verbose_name="Fecha de creacion"
    )

    # Campo: Fecha de actualizacion
    update_at = models.DateTimeField(
        auto_now=True,
        db_comment="Fecha de actualizacion",
        verbose_name="Fecha de actualizacion"
    )

    def __str__(self):
        return self.modelo
    
    # Metadatos de la tabla
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

        db_table = 'productos'
        ordering = ['id']

# Tabla: Unidades de Productos
class unitsProducts(models.Model):
    
    # Foreing Key: Id Producto
    id_producto = models.ForeignKey(
        products,
        on_delete=models.CASCADE,
        db_column='id_producto',
        db_comment="Id Producto",
        verbose_name="id_producto_unidad"
    )

    # Campo: Serial
    serial = models.CharField(
        max_length=255,
        verbose_name="serial",
        db_comment="Serial del producto"
    )

    # Foreing Key: Id Factura Compra
    id_factura_compra = models.ForeignKey(
        receiptBuy,
        on_delete=models.CASCADE,
        db_column='id_factura_compra',
        db_comment="Id Factura Compra",
        verbose_name="id_factura_compra_unidad"
    )

    # Campo: Fecha de creacion
    create_at = models.DateTimeField(
        auto_now_add=True,
        db_comment="Fecha de creacion",
        verbose_name="Fecha de creacion"
    )

    # Campo: Fecha de actualizacion
    update_at = models.DateTimeField(
        auto_now=True,
        db_comment="Fecha de actualizacion",
        verbose_name="Fecha de actualizacion"
    )

    def __str__(self):
        return self.id_producto
    
    # Metadatos de la tabla
    class Meta:
        verbose_name = 'Unidad de producto'
        verbose_name_plural = 'Unidades de productos'

        db_table = 'unidades_productos'
        ordering = ['id']

# Tabla unidades Compra
class unitsBuy(models.Model):

    # Foreigh Key: Id Factura
    id_factura = models.ForeignKey(
        receiptBuy,
        on_delete=models.CASCADE,
        db_column="id_factura",
        db_comment="Id de la factura",
        verbose_name="id factura",
        related_name="id_factura_unidad_compra"
    )

    # Foreigh Key: Id Producto
    id_producto = models.ForeignKey(
        unitsProducts,
        on_delete=models.CASCADE,
        db_column="id_producto",
        db_comment="Id del producto",
        verbose_name="id producto",
        related_name="id_producto_unidad_compra",
    )

    def __str__(self):
        return self.id_factura
    
    # Metadatos de la tabla
    class Meta:
        db_table = "unidades_compra"
        verbose_name = "Unidad de compra"
        verbose_name_plural = "Unidades de compra"
        ordering = ["id"]