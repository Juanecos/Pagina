# Generated by Django 4.2.4 on 2023-10-10 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0002_alter_modelohistory_options_alter_modelolist_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modelorealtime',
            name='Humedad',
        ),
        migrations.AlterField(
            model_name='modelorealtime',
            name='temperatura',
            field=models.FloatField(default=-0.0, verbose_name='temperatures'),
        ),
        migrations.AddField(
            model_name='modelorealtime',
            name='humedad',
            field=models.FloatField(default=-0.0, verbose_name='Humidity%'),
        ),
    ]