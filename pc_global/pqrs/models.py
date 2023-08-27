from django.db import models
from landing.models import Users, Estado
from datetime import datetime


class TipoPqrs(models.Model):
    nombre = models.CharField(max_length=15, verbose_name="tipo_pqrs", unique=True)

    def __str__(self):
        return self.nombre


class Pqrs(models.Model):
    fk_id_cliente = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name="fk_idCliente", related_name="pqrs_cliente")
    fk_id_trabajador = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="pqrs_trabajador")
    fk_id_estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    title_pqrs = models.CharField(max_length=30, null=False, blank=False, verbose_name="titulo_pqrs",
                                  db_column="tituloPqrs")
    date_pqrs = models.DateField(default=datetime.now().strftime('%Y-%m-%d'), verbose_name="fecha_pqrs",
                                 db_column="fechaPqrs")

    fk_id_TipoPqrs = models.ForeignKey(TipoPqrs, on_delete=models.CASCADE)
    description = models.TextField(verbose_name="desc_pqrs", db_column="descripcion", blank=False, null=False)
    # estados de pqrs, pendiente, respondido o en espera xd
    # (valor, etiqueta) el valor es el valor que se almacena en la base de datos y etiqueta es lo que aparece en la interfaz
    ESTADO_PQRS = [
        ('Pendiente', 'Pendiente'),
        ('Aprobado', 'Aprobado'),
        ('Rechazado', 'Rechazado'),
    ]
    # por defecto el estado que va a tomar el pqrs va a ser la primera tupla osea ('Pendiente', 'Pendiente')
    # por lo cual para acceder al primer valor para la bd se debera con ESTADO_PQRS[0][0], esto devolvera el primver valor de la tupla

    '''
     estado pqrs es el estado que tiene el pqrs si esta en espera de respuesta, si ya esta aprobado o rechazado
     , no si esta disponible o no o si esta borrado de la bd,
    '''

    state_pqrs = models.CharField(max_length=12, verbose_name="estado_pqrrs", choices=ESTADO_PQRS,
                                  default=ESTADO_PQRS[0][0], db_column="estadoPqrs")
    answer_pqrs = models.TextField(default="", verbose_name="resp_pqrs", db_column="respuesta", null=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title_pqrs
