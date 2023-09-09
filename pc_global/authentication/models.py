from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from landing.models import States

# Tabla: Tipos de Documento
class DocTypes(models.Model):

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
class Genders(models.Model):
  
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

# Tabla: Usuarios
class UserCustom(AbstractUser):

    # Foreign Key: id genero
    id_genero = models.ForeignKey(
        Genders,
        on_delete=models.CASCADE,
        db_column='id_genero',
        db_comment="Llave foranea tabla generos",
        verbose_name="id genero usuario",
        related_name="id_genero_usuario",
        null=True
    )

    # Foreign key: Id tipo documento
    id_tipo_documento = models.ForeignKey(
        DocTypes,
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

    # Campo: Email
    email = models.EmailField(
        max_length=50,
        db_comment="Email del usuario",
        verbose_name="email",
        null=True,
        unique=True
    )

    # Campo: Fecha de nacimiento
    fecha_nacimiento = models.DateField(
        db_comment="Fecha de nacimiento del usuario",
        verbose_name="fecha nacimiento",
        null=True
    )

    # Foreing Key: Id Estado
    id_estado = models.ForeignKey(
        States,
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

    # Reemplazo email x username en el login
    USERNAME_FIELD='email'

    REQUIRED_FIELDS = ['username']

    def __str__(self):

        # Si no tiene nombre ni apellido, se mostrara el username
        if(self.first_name == "" and self.last_name == ""):
            return self.username
        else:
            return f"{self.first_name} {self.last_name}"
    
    # Metadatos de la tabla
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

        db_table = 'usuarios'
        ordering = ['id']

#Tabla: Direcciones
class Addresses(models.Model):

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
        return str(self.id_cliente)
    
    # Metadatos de la tabla
    class Meta:
        verbose_name = 'Direccion'
        verbose_name_plural = 'Direcciones'

        db_table = 'direcciones'
        ordering = ['id']