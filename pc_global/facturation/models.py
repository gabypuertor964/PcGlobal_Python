from django.db import models
# importamos la clase de usuario
from landing.models import Users

# importamos todas las clases del inventario si se necesitan trabajar con ellas xd
from inventory.models import UnidadesProductos
from datetime import datetime


# Create your models here.

class FacturasCompra(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="id_facturas_compra", db_comment="Llave Primaria")
    # aca la verdad no se por que la fecha de compra es unica pero igual lo pondre xd
    fecha_compra = models.DateTimeField(null=False, unique=True, blank=False,
                                        db_comment="fecha y hora de ejecucion de la compra")
    fk_idTrabajador = models.ForeignKey(Users, on_delete=models.CASCADE, db_column="fk_id_trabajador_solicitante",
                                        db_comment="Fk Id Trabajador que realizo la compra",
                                        related_name="id_trabajador")

    fecha_recibido = models.DateTimeField(null=False, unique=True, db_comment="Fecha  y hora recepcion del pedido")
    fk_id_receptor = models.ForeignKey(Users, verbose_name="id_receptor",
                                       db_comment="Fk Id Trabajador que realiza el pedido",
                                       related_name="id_receptor", on_delete=models.CASCADE)
    subtotal = models.CharField(max_length=10, blank=False, null=False, verbose_name="subtotal",
                                db_comment="Subtotal factura")
    impuestos = models.CharField(max_length=10, blank=False, null=False, verbose_name="impuestos",
                                 db_comment="Valor impuestos")
    total = models.CharField(blank=True, verbose_name="total_compra", max_length=10, db_comment="Valor total compra")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id

    class Meta:
        """
        meta es para agregar configuraciones a nuestra tabla,
        en este caso solo la puse para cambiar el nombre de la tabla
        """
        db_table = "facturas_compra"


class FacturasVenta(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="id_facturas_Venta")
    fecha_venta = models.DateTimeField(null=False, blank=False, verbose_name="fecha_venta", unique=True)
    fk_id_cliente = models.ForeignKey(Users, null=False, on_delete=models.CASCADE, verbose_name="id_cliente")
    subtotal = models.CharField(max_length=10, blank=False, null=False, verbose_name="subtotal",
                                db_comment="Subtotal factura")
    iva = models.CharField(max_length=10, null=False, verbose_name="valor_iva", db_comment="Valor Iva", default="1.19")
    total = models.CharField(blank=True, verbose_name="total_factura_venta", max_length=10, db_comment="Valor total")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id

    class Meta:
        db_table = "facturas_venta"


class Direcciones(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="id_direcciones", db_comment="Llave Primaria")
    fk_id_cliente = models.ForeignKey(Users, db_comment="Fk id cliente", on_delete=models.CASCADE,
                                      verbose_name="fk_id_cliente", null=False)

    direccion = models.TextField(null=False, blank=False, db_comment="Direccion de cliente", verbose_name="direccion")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.direccion


class TipoEntrega:
    id = models.AutoField(primary_key=True, verbose_name="id_tipo_entregas", db_comment="Llave Primaria")
    nombre = models.CharField(unique=True, null=False, verbose_name="nombre_tipo_entrega",
                              db_comment="Nombre tipo de entrega")

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "tipos_entrega"


class Entregas(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="id_entregas", db_comment="Llave Primaria")
    fk_id_factura = models.ForeignKey(FacturasVenta, on_delete=models.CASCADE, null=False, verbose_name="id_factura",
                                      db_comment="Fk Id Factura")
    fk_id_trabajador = models.ForeignKey(Users, on_delete=models.CASCADE, null=False, verbose_name="id_trabajador",
                                         db_comment="Fk id trabajador")

    fk_id_tipo_entrega = models.ForeignKey(TipoEntrega, on_delete=models.CASCADE, null=False, verbose_name="id_tipo_entrega",
                                           db_comment="FK id tipo de entrega")

    fk_id_direccion = models.ForeignKey(Direcciones, on_delete=models.CASCADE, null=False, verbose_name="id_direccion"
                                        , db_comment="Fk id direcciones xd")

    fecha_entrega = models.DateTimeField(null=False, verbose_name="fecha_entrega", blank=False, db_comment="Fecha y hora de entrega")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    unidades_compras = models.ManyToManyField(UnidadesProductos, related_name="unidades_compras")

    def __str__(self):
        return self.id