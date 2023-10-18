from django.apps import AppConfig

# from .clasesensores import Manage_sensor
from multiprocessing import Process

import paho.mqtt.client as paho
import ssl
import time
import numpy as np
import json


class App1Config(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "App1"

    def ready(self):
        # Importa los modelos y carga la base de datos aquí
        from .models import ModeloList, ModeloRealTime, ModeloHistory

        lista = ModeloList.objects.values_list("name", flat=True)
        topicos = list(lista)
        print(topicos)

        broker = "6eef623dbafd42238df342ee595d441a.s1.eu.hivemq.cloud"
        port = 8883
        user = "juan-camilo"
        password = "iNM123456789"
        user2 = "hivemq.webclient.1696257769493"
        password2 = "Q?1z.Y0ibLa47!eCD#Fc"
        Clientid = ""
        topic_list = topicos
        tablaRealTime = ModeloRealTime.objects.all()
        enviarIDRealTime = []

        for objeto in tablaRealTime:
            id_del_objeto = objeto.id
            enviarIDRealTime.append(id_del_objeto)

        mqtt_process = Process(
            target=ejecutar,
            args=(broker, port, Clientid, user, password, topicos, enviarIDRealTime),
        )
        mqtt_process.start()


# {"Topico":"temperatura1","Fecha":"2023-18-10","Hora":"9:46:55","Temperatura":"15.5","Humedad":"30"}
def ejecutar(broker, port, Clientid, user, password, topic_list, tablaRealTime):
    nuevocliente = Manage_sensor(
        broker, port, Clientid, user, password, topic_list, tablaRealTime
    )
    nuevocliente.mqtt_deploy()


class Manage_sensor:
    def __init__(
        self, broker, port, addnewclient, user, password, topic_list, tablaRealTime
    ):
        self.client = paho.Client(
            addnewclient, clean_session=True, userdata=None, protocol=paho.MQTTv311
        )
        self.client.tls_set(
            ca_certs=None,
            certfile=None,
            keyfile=None,
            cert_reqs=ssl.CERT_REQUIRED,
            tls_version=ssl.PROTOCOL_TLS,
            ciphers=None,
        )

        self.client.reconnect_delay_set(min_delay=1, max_delay=120)
        self.client.username_pw_set(user, password)
        self.client.on_connect = self.on_connect
        self.client.on_subscribe = self.on_subscribe
        self.client.on_message = self.on_message
        self.client.on_publish = self.on_publish
        self.topic_list = topic_list
        self.tablarealtime = tablaRealTime

        self.client.reconnect_delay_set(min_delay=1, max_delay=120)
        self.client.connect(broker, port, keepalive=60)
        

    def on_publish(self, client, userdata, mid):
        print(str(client))
        print(str(userdata))
        print("mid: " + str(mid))

    def on_subscribe(self, client, userdata, mid, granted_qos):
        print(str(client))
        print(str(userdata))
        print("mid: " + str(mid))

    def on_message(self, client, userdata, msg):

        if msg.topic in self.topic_list:
            position = self.topic_list.index(msg.topic)
            print("Mensaje recibido en el tema:", msg.topic)
            actualtopic = msg.payload.decode()
            
            datos = json.loads(actualtopic)
            topic = datos["Topico"]
            date = datos["Fecha"]
            hour = datos["Hora"]
            temperature = datos["Temperatura"]
            humidity = datos["Humedad"]
            # modelo=ModeloRealTime.object.all()
            # print(modelo)
            # print(datos)
            
            # print(self.datos)
            return(datos)
        
    def on_connect(self, client, userdata, flags, rc):
        print("CONNACK received with code %d." % (rc))

    def pub(self, topic, msg, qos):
        self.client.publish(topic, msg, qos)

    def sub(self, topic, qos):
        self.client.subscribe(topic, qos)

    def mqtt_deploy(self):


        for topic in self.topic_list:
            self.client.subscribe(topic, qos=0)
        try:
            msg = self.on_message
            print(msg)
            self.client.loop_forever()
        except KeyboardInterrupt:
            print("Disconnecting from MQTT broker and exiting.")
            self.client.loop_stop()
            self.client.disconnect()
        except Exception as e:
            print("An error occurred:", str(e))
            print("Reconnecting to the MQTT broker in 5 seconds...")
            time.sleep(5)
            self.client.reconnect()
