# Generated by Django 4.2.4 on 2023-08-28 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoPqrs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15, unique=True, verbose_name='tipo_pqrs')),
            ],
        ),
        migrations.CreateModel(
            name='Pqrs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_pqrs', models.CharField(db_column='tituloPqrs', max_length=30, verbose_name='titulo_pqrs')),
                ('date_pqrs', models.DateField(db_column='fechaPqrs', default='2023-08-28', verbose_name='fecha_pqrs')),
                ('description', models.TextField(db_column='descripcion', verbose_name='desc_pqrs')),
                ('state_pqrs', models.CharField(choices=[('Pendiente', 'Pendiente'), ('Aprobado', 'Aprobado'), ('Rechazado', 'Rechazado')], db_column='estadoPqrs', default='Pendiente', max_length=12, verbose_name='estado_pqrrs')),
                ('answer_pqrs', models.TextField(db_column='respuesta', default='', null=True, verbose_name='resp_pqrs')),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('fk_id_TipoPqrs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pqrs.tipopqrs')),
                ('fk_id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pqrs_cliente', to='landing.users', verbose_name='fk_idCliente')),
                ('fk_id_estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landing.estado')),
                ('fk_id_trabajador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pqrs_trabajador', to='landing.users')),
            ],
        ),
    ]
