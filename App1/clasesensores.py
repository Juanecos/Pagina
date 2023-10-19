"""usar programacion orientada a objetos para manejar cada sensor"""
import paho.mqtt.client as paho
import ssl
import time
import numpy as np
import json
# from .models import ModeloRealTime,ModeloHistory,ModeloList





class Manage_sensor:
    def __init__(self, broker, port, addnewclient, user, password, topic_list):
        
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
        # self.tablarealtime= tablaRealTime

        self.client.reconnect_delay_set(min_delay=1, max_delay=120)
        self.client.connect(broker, port, keepalive=60)
        self.variable_global = None
        

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
            mensaje_global="Hola"

        self.actualizar_variable_global(datos)
        time.sleep(0.1)
        self.actualizar_variable_global(None)

    def actualizar_variable_global(self, mensaje):
        # Actualiza aquí tu variable global con el mensaje recibido
        
        self.variable_global = mensaje

        
    def obtener_variable_global(self):
        return self.variable_global

        
            # print(data1)

            # for element in self.tablarealtime:
            #     print(element)

            # mensaje_mqtt = ModeloRealTime()
            # mensaje_mqtt.save()
            # for element in self.tablarealtime:
            #     try:
            #         e = ModeloRealTime.objects.get(id=element)
            #         print(e)
            #         print(element)
            #     except ModeloRealTime.DoesNotExist:
            #         # Maneja la excepción si el objeto no existe
            #         pass
  
            # print(a)

            # # #pressure = datos["Presion"]
            # print(topic)
            # print(date)
            # print(hour)
            # print(temperature)
            # print(humidity)
            # print(position)

            # tiempomensaje = time.time()
            # tiempo_reducido = f"{tiempomensaje:.2f}"
            # self.arraytimes[position] = float(tiempo_reducido)    

    def on_connect(self, client, userdata, flags, rc):
        print("CONNACK received with code %d." % (rc))

    def pub(self, topic, msg, qos):
        self.client.publish(topic, msg, qos)

    def sub(self, topic, qos):
        self.client.subscribe(topic, qos)
    
    def shutdown(self):
        self.client.loop_stop()
        self.client.disconnect()

    def reconnectcl(self):
        self.client.reconnect()


    def mqtt_deploy(self):
        # while True:
        
        # try:
        self.client.loop_start()
            
        variable_global = self.obtener_variable_global()
        # Utiliza la variable global como desees
        if variable_global is not None:
            variable2=variable_global
            variable_global= None
            
            return(variable2)
        
    
        # except KeyboardInterrupt:
        #     print("Disconnecting from MQTT broker and exiting.")
        #     self.client.loop_stop()
        #     self.client.disconnect()
        #     # break
        # except Exception as e:
        #     print("An error occurred:", str(e))
        #     print("Reconnecting to the MQTT broker in 5 seconds...")
        #     time.sleep(5)
        #     self.client.reconnect()

def performance(broker,port,Clientid,user,password,topic_list,q):
    import time
    nuevocliente = Manage_sensor(broker, port, Clientid, user, password, topic_list)

    for topic in topic_list:
        nuevocliente.sub(topic, qos=0)
        time.sleep(1)

    while True:
        try:
            mensaje = nuevocliente.mqtt_deploy()
            if mensaje is not None:
                # hacer update de la base de datos
                print(mensaje)
                time.sleep(0.3)
                
                
                

        except KeyboardInterrupt:
            print("Disconnecting")

            break

if __name__ =='__main__':


            
    from multiprocessing import Process, Queue


    broker = "6eef623dbafd42238df342ee595d441a.s1.eu.hivemq.cloud"
    port = 8883
    user = "juan-camilo"
    password = "iNM123456789"
    user2 = "hivemq.webclient.1696257769493"
    password2 = "Q?1z.Y0ibLa47!eCD#Fc"
    Clientid = ""



    topic_list = [
        "AR001",
        "temperatura1",
        "sensor3",
    ]  # sacar de la base de datos la topic list


    q = Queue()
    mqtt_process = Process(
        target=performance,
        args=(broker,port,Clientid,user,password,topic_list,q)
    )
    mqtt_process.start()
    print(q.get())  # prints "[42, None, 'hello']"


    time.sleep(1)

    



