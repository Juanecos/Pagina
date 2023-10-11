"""creacion del modelo"""
from django.db import models

class ModeloList(models.Model):
    """listado de sensores"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        fila = ("id: " + str(self.id)
                + "-" + " name: "+ str(self.name))
        return fila
    
    class Meta:
        """descripcion de la tabla"""
        db_table = "Lista_sensores"
        verbose_name = "Lista_sensor"
        verbose_name_plural = "Lista-sensores"


# Create your models here.
class ModeloRealTime(models.Model):
    """creacion de tabla sensores en tiempo real"""
    id = models.AutoField(primary_key=True)
    sensor = models.ForeignKey(ModeloList, on_delete=models.CASCADE,null=True)
    temperatura = models.FloatField(
        null=False, unique=False, verbose_name="temperatures", default=-0.0
    )
    humedad = models.FloatField(
        unique=False, verbose_name="Humidity%", default=-0.0
    )
    def __str__(self):
        fila = ("id: " + str(self.id)
                + "-" + " Sensor: "+ str(self.temperatura)
                + "-" + " Temperatura: "+ str(self.sensor)
                + "-" + " Humedad: " + str(self.humedad))
        return fila
    class Meta:
        """descripcion de la tabla"""

        db_table = "Tiempo_Real"
        verbose_name = "Dato_en_tiempo_real"
        verbose_name_plural = "Datos_en_tiempo_real"
class ModeloHistory(models.Model):
    """Para tener historial de temperatura y humedad"""
    id = models.AutoField(primary_key=True)
    sensor = models.ForeignKey(ModeloList, on_delete=models.CASCADE)
    temperatura = models.FloatField(null=False,
                                    unique=True,
                                    verbose_name="temperatures",
                                    default=-0.0)
    Humedad = models.FloatField(unique=True,
                                verbose_name="Humidity%",
                                default=-0.0)
    date = models.DateField(null=True, blank=True)
    hour = models.TimeField(null=True, blank=True)

    # fecha_hora_extension = models.DateTimeField(auto_now_add=True)
    # esta hora esta bien mentirosa y me sale el dia de mañana

    def __str__(self):
        fila = ("id: " + str(self.id)
        +"-" + " Topico: " + str(self.sensor)
        +"-" + " Temperatura: "+ str(self.sensor)
        +"-" + " Humedad: " + str(self.Humedad)
        +"-" + " Fecha: " + str(self.date)
        +"-" + " Hora: " + str(self.hour))
        return fila
    class Meta:
        """descripcion de la tabla"""
        db_table = "Historial"
        verbose_name = "Historial"
        verbose_name_plural = "Historial_de_datos"
        ordering =['sensor','-date']
