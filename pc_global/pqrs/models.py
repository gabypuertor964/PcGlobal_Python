from django.db import models
from landing.models import States
from django.conf import settings
from datetime import datetime
from django.utils.text import slugify
from django.db.models.signals import pre_save

# Tabla: Tipo de PQRS
class PqrsTypes(models.Model):

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
class Pqrs(models.Model):

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
        PqrsTypes,
        on_delete=models.CASCADE,
        db_column='id_tipo_pqrs',
        db_comment="Id Tipo de PQRS",
        verbose_name="id tipo pqrs"
    )

    # Foreign Key tabla estados
    id_estado = models.ForeignKey(
        States,
        on_delete=models.CASCADE,
        db_column='id_estado',
        db_comment="Id Estado",
        verbose_name="id estado"
    )
    title = models.CharField(
        max_length=50,
        blank=False,
        verbose_name="Titulo del Reporte",
        db_column="tituloPqrs"
    )

    date_occurrence = models.DateField(
        default=datetime.now().strftime('%Y-%m-%d'),
        blank=True,
        verbose_name="Fecha del problema",
        db_column="fechaProblema"
    )
    # Campo Descripcion
    descripcion = models.TextField(
        db_comment="Descripcion de la PQRS",
        verbose_name="descripcion",
    )

    evidence = models.ImageField(
        upload_to='pqrs/static/evidence/reporte/%Y/%m/%d',
        null=True,
        blank=True,
        verbose_name="Foto de lo sucedido"
    )

    # Campo Respuesta
    respuesta = models.TextField(
        db_comment="Respuesta de la PQRS",
        verbose_name="respuesta",
        null=True,
        blank=True
    )
    
    # campo slug
    slug = models.SlugField(
        max_length=100,
        unique=True,
        verbose_name="slug",
        db_comment="Slug del pqrs"
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
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Pqrs, self).save(*args, **kwargs)

    # def set_slug(sender, instance, *args, **kwargs):
    #     instance.slug = slugify(instance.title)
    # pre_save.connect(set_slug, sender=Pqrs)
    
    def __str__(self):
        return f'{self.id_cliente} {self.title}'
    
    # Metadatos de la tabla
    class Meta:
        verbose_name = 'PQRS'
        verbose_name_plural = 'PQRS'

        db_table = 'pqrs'
        ordering = ['id']

