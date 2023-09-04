from django.db import models

#Tabla: Areas
class Areas(models.Model):

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
class States(models.Model):

    # Campo Nombre
    nombre = models.CharField(
        max_length=20
    )

    # Llave Foranea tabla areas
    id_area = models.ForeignKey(
        Areas,
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