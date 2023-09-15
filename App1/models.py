'''creacion del modelo'''
from django.db import models

# Create your models here.


class MiModelo(models.Model):
    """creacion del modelo"""
    id = models.AutoField(primary_key=True)
    temperatura = models.FloatField(max_length=10, null=False, unique=True, verbose_name='temperatures')

    def __str__(self): 
        fila= "Id: " + str(self.id) + "-" + "Temperatura: " + str(self.temperatura)
        return fila

    class Meta:
        '''descripcion de la tabla'''
        db_table = 'Real_time'
        verbose_name = 'Dato_en_tiempo_real'
        verbose_name_plural = 'Datos_en_tiempo_real'
        
