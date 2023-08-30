from django.db import models
from django.contrib.auth.models import User

# Tabla: Tipos de Documento
class docTypes(models.Model):

    # Campo Nombre
    nombre = models.CharField(
        max_length=40, 
        unique=True, 
        db_comment="Nombre tipo documento",
        verbose_name="nombre",
        null=False
    )

    # Campo Siglas
    siglas = models.CharField(
        max_length=3, 
        unique=True, 
        db_comment="Abreviatura/Sigla Tipo Documento", null=False
    )

    def __str__(self):
        return self.nombre

    # Metadatos de la tabla
    class Meta:
        verbose_name = 'Tipo de Documento'
        verbose_name_plural = 'Tipos de Documento'

        db_table = 'tipos_documento'
        ordering = ['id']

# Tabla: Generos
class genders(models.Model):
  
    # Campos Personalizados
    nombre = models.CharField(
        max_length=10,
        verbose_name="nombre",
        db_comment="Nombre del género"
    )

    def __str__(self):
        return self.nombre
    
    # Metadatos de la tabla
    class Meta:
        verbose_name = 'Género'
        verbose_name_plural = 'Géneros'

        db_table = 'generos'
        ordering = ['id']

#Tabla: Areas
class areas(models.Model):

    # Campo Nombre
    nombre = models.CharField(
        max_length=20,
        verbose_name="nombre",
    )

    def __str__(self):
        return self.nombre
    
    # Metadatos de la tabla
    class Meta:
        verbose_name = 'Area'
        verbose_name_plural = 'Areas'

        db_table = 'areas'
        ordering = ['id']
    
#Tabla: estados
class states(models.Model):

    # Campo Nombre
    nombre = models.CharField(
        max_length=20
    )

    # Llave Foranea tabla areas
    id_area = models.ForeignKey(
        areas,
        on_delete=models.CASCADE,
        db_column='id_area',
        db_comment="Llave foranea tabla areas",
        verbose_name="id_area_estado"
    )

    def __str__(self):
        return self.nombre

    # Metadatos de la tabla
    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'

        db_table = 'estados'
        ordering = ['id']

#Tabla: Direcciones
class addresses(models.Model):

    # Foreign Key tabla users (id_cliente)
    id_cliente = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        db_column='id_cliente',
        db_comment="Id Cliente",
        verbose_name="id_cliente_direccion"
    )

    # Campo Direccion
    direccion = models.TextField(
        db_comment="Direccion del cliente",
        verbose_name="direccion",
    )

    # Fecha de creacion
    create_at = models.DateTimeField(
        auto_now_add=True,
        db_comment="Fecha de creacion",
        verbose_name="Fecha de creacion"
    )

    # Fecha de actualizacion
    updated_at = models.DateTimeField(
        auto_now=True,
        db_comment="Fecha de actualizacion",
        verbose_name="Fecha de actualizacion"
    )

    def __str__(self):
        return self.id_cliente
    
    # Metadatos de la tabla
    class Meta:
        verbose_name = 'Direccion'
        verbose_name_plural = 'Direcciones'

        db_table = 'direcciones'
        ordering = ['id']