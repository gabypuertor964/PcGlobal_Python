# Generated by Django 4.2.4 on 2023-08-28 00:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id_categorias')),
                ('nombre_categoria', models.CharField(db_comment='Nombre de la Categoría', max_length=50, unique=True, verbose_name='nombre_categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Marcas',
            fields=[
                ('id', models.AutoField(db_comment='Llave Primaria', primary_key=True, serialize=False, verbose_name='id_marcas')),
                ('nombre', models.CharField(db_comment='Nombre Marca', max_length=50, unique=True, verbose_name='nombre_marca')),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id_categorias')),
                ('modelo', models.CharField(max_length=55, unique=True, verbose_name='modelo')),
                ('imagen_producto', models.TextField(db_column='imagen', db_comment='Imagen del Producto', verbose_name='imagen_producto')),
                ('descripcion', models.TextField(db_comment='Descripcion del Producto', verbose_name='descripcion')),
                ('precio', models.CharField(db_comment='Precio unitario del producto', max_length=10, verbose_name='precio')),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('fk_id_categorias', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.categorias', verbose_name='id_categorias')),
                ('fk_id_marcas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.marcas', verbose_name='id_marcas')),
            ],
        ),
        migrations.CreateModel(
            name='UnidadesProductos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id_unidades_productos')),
                ('serial', models.CharField(db_comment='Serial Unidad del producto', max_length=255, null='False', unique=True, verbose_name='serial')),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('fk_id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.productos')),
            ],
            options={
                'db_table': 'unidades_producto',
            },
        ),
    ]
