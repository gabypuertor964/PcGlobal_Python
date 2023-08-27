"""
En este archivo de models principalmente se haran los modelos orm para las tablas que tengan que
ver con los usuarios y el login
"""

from django.db import models
# esta libreria nos ayuda a crear por ejemplo los campos de updated_at y created_at, ademas para crear defaults
from datetime import datetime
# esta libreria validators nos sirve para agregar mas funciones para validar datos
from django.core.validators import MaxValueValidator

# print(datetime.now().strftime('%Y'))

'''
    verbose_name: nos da una variable para usar en la interfaz
    
'''


class Sexos(models.Model):
    id = models.AutoField(primary_key=True, db_comment="Llave Primaria")
    nombre = models.CharField(max_length=10, unique=True, db_comment="Nombre del sexo", verbose_name="nombre",
                              null=True)

    def __str__(self):
        return self.nombre


class TipoDocumento(models.Model):
    id = models.AutoField(primary_key=True, db_comment="Llave Primaria")
    nombre = models.CharField(max_length=40, unique=True, db_comment="Nombre tipo de documento",
                              verbose_name="nombre")
    siglas = models.CharField(max_length=3, unique=True, db_comment="Abreviatura/Sigla del Tipo Documento")

    def __str__(self):
        return self.nombre


class Areas(models.Model):
    nombre = models.CharField(max_length=20, unique=True, db_comment="nombre Area", verbose_name="nombre_areas")

    def __str__(self):
        return self.nombre


class Estado(models.Model):
    nombre = models.CharField(max_length=20, unique="True", db_comment="Nombre Estado", verbose_name="nombre_estado")
    fk_id_area = models.ForeignKey(Areas, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Users(models.Model):
    # Seccion de los nombres de usuarios
    name_user = models.CharField(max_length=30, blank=False, null=False, verbose_name="nombres", db_comment="Nombres",
                                 db_column="nombres")
    surnames = models.CharField(max_length=30, blank=False, null=False, verbose_name="Apellidos",
                                db_comment="Apellidos",
                                db_column="apellidos")

    fk_id_sexo = models.ForeignKey(Sexos, on_delete=models.CASCADE, null=False, verbose_name="id_sexo")
    fk_id_tip_doc = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE, null=False, verbose_name="id_tip_doc")

    num_doc = models.CharField(max_length=15, unique=True, db_comment="Id tipo de documento",
                               verbose_name="num_doc", null=False, blank=False)
    num_tel = models.CharField(max_length=10, unique=True, db_comment="Numero telefonico", null=False, blank=False,
                               verbose_name="num_tel")

    birth_date = models.DateField(validators=[MaxValueValidator(datetime.now().strftime('%Y'))],
                                  db_comment="Fecha de Nacimiento", blank=False, verbose_name="fecha_nacimiento",
                                  null=False, db_column="fecha_nacimiento")

    email = models.EmailField(unique=True, db_comment="Correo electronico", verbose_name="email", null=False,
                              blank=False)
    password = models.CharField(max_length=255, db_comment="Contraseña hasheada", verbose_name="password", null=False,
                                blank=False)
    email_verified_at = models.DateField(null=True, db_comment="Fecha y hora de validacion de correo electronico")
    remember_token = models.CharField(max_length=100, verbose_name="token_recuerdame", db_comment="token 'recuerdame'",
                                      null=True)
    fk_id_estado = models.ForeignKey(Estado, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
