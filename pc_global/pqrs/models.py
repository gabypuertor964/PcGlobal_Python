from django.db import models
from landing.models import states
from django.conf import settings

# Tabla: Tipo de PQRS
class pqrs_types(models.Model):

    # Campo Nombre
    nombre = models.CharField(
        max_length=15,
        verbose_name="nombre",
        db_comment="Nombre del tipo de PQRS"
    )

    def __str__(self):
        return self.nombre
    
    # Metadatos de la tabla
    class Meta:
        verbose_name = 'Tipo de PQRS'
        verbose_name_plural = 'Tipos de PQRS'

        db_table = 'tipos_pqrs'
        ordering = ['id']

# Tabla: PQRS
class pqrs(models.Model):

    # Foreign Key tabla users (id_cliente)
    id_cliente = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        db_column='id_cliente',
        db_comment="Id Cliente",
        verbose_name="id cliente",
        related_name="id_cliente_pqrs"
    )

    # Foreign Key tabla users (id_trabajador)
    id_trabajador = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        db_column='id_trabajador',
        db_comment="Id Trabajador",
        verbose_name="id trabajador",
        related_name="id_trabajador_pqrs"
    )

    # Foreign Key tipo de PQRS
    id_tipo_pqrs = models.ForeignKey(
        pqrs_types,
        on_delete=models.CASCADE,
        db_column='id_tipo_pqrs',
        db_comment="Id Tipo de PQRS",
        verbose_name="id tipo pqrs"
    )

    # Foreign Key tabla estados
    id_estado = models.ForeignKey(
        states,
        on_delete=models.CASCADE,
        db_column='id_estado',
        db_comment="Id Estado",
        verbose_name="id estado"
    )

    # Campo Descripcion
    descripcion = models.TextField(
        db_comment="Descripcion de la PQRS",
        verbose_name="descripcion"
    )

    # Campo Respuesta
    respuesta = models.TextField(
        db_comment="Respuesta de la PQRS",
        verbose_name="respuesta"
    )

    # Campo Fecha de creacion
    fecha_creacion = models.DateTimeField(
        auto_now_add=True,
        db_comment="Fecha de creacion",
        verbose_name="Fecha de creacion"
    )

    # Campo Fecha de actualizacion
    fecha_actualizacion = models.DateTimeField(
        auto_now=True,
        db_comment="Fecha de actualizacion",
        verbose_name="Fecha de actualizacion"
    )

    def __str__(self):
        return self.id_cliente
    
    # Metadatos de la tabla
    class Meta:
        verbose_name = 'PQRS'
        verbose_name_plural = 'PQRS'

        db_table = 'pqrs'
        ordering = ['id']

