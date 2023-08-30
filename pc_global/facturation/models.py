from django.db import models
from django.conf import settings

from landing.models import states
from landing.models import addresses

# Tabla: Facturas Compra
class receiptBuy(models.Model):

    # Campo: Número de Factura
    numero_factura = models.CharField(
        max_length=15,
        verbose_name="numero de factura",
        db_comment="Número de la factura de compra",
        unique=True
    )

    # Campo: Fecha de Compra
    fecha_compra = models.DateField(
        verbose_name="fecha de compra",
        db_comment="Fecha de compra de la factura"
    )

    # Foreigh Key: Id Trabajador Solicitante
    id_trabajador_solicitante = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        db_column="id_trabajador_solicitante",
        db_comment="Id del trabajador solicita el pedido",
        verbose_name="id trabajador solicitante",
        related_name="id_trabajador_solicitante_compra"
    )

    # Campo: Fecha Recepcion
    fecha_recepcion = models.DateField(
        verbose_name="fecha de recepcion",
        db_comment="Fecha de recepción de la factura",
        null=True
    )

    # Foreigh Key: Id Trabajador receptor
    id_trabajador_receptor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        db_column="id_trabajador_receptor",
        db_comment="Id del trabajador que recibe el pedido",
        verbose_name="id trabajador receptor",
        related_name="id_trabajador_receptor_compra",
        null=True
    )

    # Campo: Subtotal
    subtotal = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="subtotal",
        db_comment="Subtotal de la factura"
    )

    # Campo: Impuestos
    impuestos = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="impuestos",
        db_comment="Impuestos de la factura"
    )

    # Campo: Total
    total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="total",
        db_comment="Total de la factura"
    )

    # Campo: Fecha de creacion
    fecha_creacion = models.DateTimeField(
        auto_now_add=True,
        db_comment="Fecha de creacion",
        verbose_name="Fecha de creacion"
    )

    # Campo: Fecha de actualizacion
    fecha_actualizacion = models.DateTimeField(
        auto_now=True,
        db_comment="Fecha de actualizacion",
        verbose_name="Fecha de actualizacion"
    )

    def __str__(self):
        return self.numero_factura
    
    # Metadatos de la tabla
    class Meta:
        db_table = "facturas_compra"
        verbose_name = "Factura de compra"
        verbose_name_plural = "Facturas de compra"
        ordering = ["id"]

# Tabla: Tipos de entrega
class deliveryTypes(models.Model):

    # Campo: Nombre
    nombre = models.CharField(
        max_length=50,
        verbose_name="nombre",
        db_comment="Nombre del tipo de entrega"
    )

    def __str__(self):
        return self.nombre
    
    # Metadatos de la tabla
    class Meta:
        db_table = "tipos_entrega"
        verbose_name = "Tipo de entrega"
        verbose_name_plural = "Tipos de entrega"
        ordering = ["id"]

# Tabla: Facturas Venta
class receiptSale(models.Model):

    # Campo: Fecha de venta
    fecha_venta = models.DateField(
        verbose_name="fecha de venta",
        db_comment="Fecha de venta de la factura"
    )

    # foreigh key: Id cliente
    id_cliente = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        db_column="id_cliente",
        db_comment="Id del cliente",
        verbose_name="id cliente",
        related_name="id_cliente_venta"
    )

    # Campo: Subtotal
    subtotal = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="subtotal",
        db_comment="Subtotal de la factura"
    )

    # Campo: IVA
    iva = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="iva",
        db_comment="IVA de la factura"
    )

    # Campo: Total
    total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="total",
        db_comment="Total de la factura"
    )

    # Campo: Fecha de creacion
    fecha_creacion = models.DateTimeField(
        auto_now_add=True,
        db_comment="Fecha de creacion",
        verbose_name="Fecha de creacion"
    )

    # Campo: Fecha de actualizacion
    fecha_actualizacion = models.DateTimeField(
        auto_now=True,
        db_comment="Fecha de actualizacion",
        verbose_name="Fecha de actualizacion"
    )

    def __str__(self):
        return self.fecha_venta
    
    # Metadatos de la tabla
    class Meta:
        db_table = "facturas_venta"
        verbose_name = "Factura de venta"
        verbose_name_plural = "Facturas de venta"
        ordering = ["id"]

# Tabla: Entregas
class deliveries(models.Model):

    # Foreigh Key: Id Factura
    id_factura = models.ForeignKey(
        receiptSale,
        on_delete=models.CASCADE,
        db_column="id_factura",
        db_comment="Id de la factura",
        verbose_name="id factura",
        related_name="id_factura_entrega"
    )

    # Foreigh Key: Id repartidor
    id_repartidor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        db_column="id_repartidor",
        db_comment="Id del repartidor",
        verbose_name="id repartidor",
        related_name="id_repartidor_entrega"
    )

    # Foreigh Key: Id tipo de entrega
    id_tipo_entrega = models.ForeignKey(
        deliveryTypes,
        on_delete=models.CASCADE,
        db_column="id_tipo_entrega",
        db_comment="Id del tipo de entrega",
        verbose_name="id tipo entrega",
        related_name="id_tipo_entrega_entrega"
    )

    # Foreigh Key: Id direccion
    id_direccion = models.ForeignKey(
        addresses,
        on_delete=models.CASCADE,
        db_column="id_direccion",
        db_comment="Id de la direccion",
        verbose_name="id direccion",
        related_name="id_direccion_entrega"
    )

    # Foreigh Key: Id estado
    id_estado = models.ForeignKey(
        states,
        on_delete=models.CASCADE,
        db_column="id_estado",
        db_comment="Id del estado",
        verbose_name="id estado",
        related_name="id_estado_entrega"
    )

    # Campo: Fecha de entrega
    fecha_entrega = models.DateField(
        verbose_name="fecha de entrega",
        db_comment="Fecha de entrega de la factura"
    )

    # Campo: Fecha de creacion
    fecha_creacion = models.DateTimeField(
        auto_now_add=True,
        db_comment="Fecha de creacion",
        verbose_name="Fecha de creacion"
    )

    # Campo: Fecha de actualizacion
    fecha_actualizacion = models.DateTimeField(
        auto_now=True,
        db_comment="Fecha de actualizacion",
        verbose_name="Fecha de actualizacion"
    )

    def __str__(self):
        return self.id_factura
    
    # Metadatos de la tabla
    class Meta:
        db_table = "entregas"
        verbose_name = "Entrega"
        verbose_name_plural = "Entregas"
        ordering = ["id"]