from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Tabla: Tipos de Documento
class docTypes(models.Model):

    # Campo Nombre
    nombre = models.CharField(
        max_length=40, 
        unique=True, 
        db_comment="Nombre tipo documento",
        verbose_name="nombre",
        null=True
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

# Tabla: Usuarios
class userCustom(AbstractUser):

    # Foreign Key: id genero
    id_genero = models.ForeignKey(
        genders,
        on_delete=models.CASCADE,
        db_column='id_genero',
        db_comment="Llave foranea tabla generos",
        verbose_name="id genero usuario",
        related_name="id_genero_usuario",
        null=True
    )

    # Foreign key: Id tipo documento
    id_tipo_documento = models.ForeignKey(
        docTypes,
        on_delete=models.CASCADE,
        db_column='id_tipo_documento',
        db_comment="Llave foranea tabla tipos documento",
        verbose_name="id tipo documento usuario",
        related_name="id_tipo_documento_usuario",
        null=True
    )

    # Campo: Numero de documento
    num_doc = models.CharField(    
        max_length=15,
        db_comment="Numero de documento del usuario",
        verbose_name="numero documento",
        null=True,
        unique=True
    )

    # Campo: Numero Telefonico
    num_tel = models.CharField(
        max_length=15,
        db_comment="Numero telefonico del usuario",
        verbose_name="numero telefonico",
        null=True
    )

    # Campo: Fecha de nacimiento
    fecha_nacimiento = models.DateField(
        db_comment="Fecha de nacimiento del usuario",
        verbose_name="fecha nacimiento",
        null=True
    )

    # Foreing Key: Id Estado
    id_estado = models.ForeignKey(
        states,
        on_delete=models.CASCADE,
        db_column='id_estado',
        db_comment="Llave foranea tabla estados",
        verbose_name="id estado usuario",
        related_name="id_estado_usuario",
        null=True
    )

    # Campo: Fecha de creacion
    create_at = models.DateTimeField(
        auto_now_add=True,
        db_comment="Fecha de creacion",
        verbose_name="Fecha de creacion"
    )

    # Campo: Fecha de actualizacion
    updated_at = models.DateTimeField(
        auto_now=True,
        db_comment="Fecha de actualizacion",
        verbose_name="Fecha de actualizacion"
    )

    def __str__(self):
        return self.username
    
    # Metadatos de la tabla
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

        db_table = 'usuarios'
        ordering = ['id']

#Tabla: Direcciones
class addresses(models.Model):

    # Foreign Key tabla users (id_cliente)
    id_cliente = models.ForeignKey(
        settings.AUTH_USER_MODEL,
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