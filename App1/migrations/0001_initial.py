# Generated by Django 4.2.4 on 2023-09-14 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MiModelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificador', models.CharField(max_length=100, unique=True, verbose_name='identificador')),
                ('temperatura', models.FloatField(max_length=10)),
            ],
            options={
                'verbose_name': 'Dato_en_tiempo_real',
                'verbose_name_plural': 'Datos_en_tiempo_real',
                'db_table': 'Real_time',
                'ordering': ['id'],
            },
        ),
    ]