"""usar programacion orientada a objetos para manejar cada sensor"""
import paho.mqtt.client as paho
import ssl
import time
import numpy as np
import json

ultimo_mensaje_tiempo = 0

class Manage_sensor():
    def __init__(self,broker,port,addnewclient,user,password,topic_list): 
        self.client = paho.Client(addnewclient, clean_session=True, userdata=None, protocol=paho.MQTTv311)
        self.client.tls_set(ca_certs=None, certfile=None, keyfile=None, cert_reqs=ssl.CERT_REQUIRED,
        tls_version=ssl.PROTOCOL_TLS, ciphers=None)
        
        self.client.reconnect_delay_set(min_delay=1, max_delay=120)
        self.client.username_pw_set(user, password)
        self.client.on_connect = self.on_connect
        self.client.on_subscribe = self.on_subscribe
        self.client.on_message = self.on_message
        self.client.on_publish = self.on_publish
        self.topic_list = topic_list
        # self.arraytimes = np.ones(len(topic_list))*time.time()
        
        

        self.client.reconnect_delay_set(min_delay=1, max_delay=120)
        self.client.connect(broker,port,keepalive=60)
        

    def on_publish(self,client, userdata, mid):
        print(str(client))
        print(str(userdata))
        print("mid: "+str(mid))

    def on_subscribe(self,client, userdata, mid,granted_qos):
        print(str(client))
        print(str(userdata))
        print("mid: "+str(mid))

    def on_message(self,client, userdata, msg):
        # global ultimo_mensaje
        # ultimo_mensaje = time.time()

        if msg.topic in self.topic_list:
            position = self.topic_list.index(msg.topic)
            print("Mensaje recibido en el tema:", msg.topic)
            actualtopic = (msg.payload.decode())

            datos = json.loads(actualtopic)
            # print(datos)

            # topic = datos["Topico"]
            date = datos["Fecha"]
            hour = datos["Hora"]
            temperature = datos["Temperatura"]
            # humidity = datos["Humedad"]
            
            # #pressure = datos["Presion"]
            # print(topic)
            print(date)
            print(hour)
            print(temperature)
            # print(humidity)
            # print(position)
            

            # tiempomensaje = time.time()
            # tiempo_reducido = f"{tiempomensaje:.2f}"
            # self.arraytimes[position] = float(tiempo_reducido)
 
    def on_connect(self,client, userdata, flags, rc):
        print('CONNACK received with code %d.' % (rc))

    def pub(self,topic, msg, qos):
        self.client.publish(topic, msg, qos)

    def sub(self,topic,qos):
        self.client.subscribe(topic,qos)
    

    def mqtt_deploy(self):

        for topic in self.topic_list:
            self.client.subscribe(topic,qos=0)

        try:
            self.client.loop_forever()
        except KeyboardInterrupt:
            print("Disconnecting from MQTT broker and exiting.")
            self.client.client.loop_stop()
            self.client.disconnect()  
        except Exception as e:
            print("An error occurred:", str(e))
            print("Reconnecting to the MQTT broker in 5 seconds...")
            time.sleep(5)
            self.client.reconnect()

    # def start(self):
    #     self.client.loop_start()

    # def stop(self):
    #     self.client.loop_stop()
    # def loopfv(self):
    #     self.client.loop_forever()
    # def shut_down(self):
    #     self.client.disconnect()   
    # def reconnect(self):
    #     self.client.reconnect()



# broker = "6eef623dbafd42238df342ee595d441a.s1.eu.hivemq.cloud"
# port = 8883
# user = "juan-camilo"
# password = "iNM123456789"
# user2="hivemq.webclient.1696257769493"
# password2="Q?1z.Y0ibLa47!eCD#Fc"
# Clientid = ""

# topic_list=["sensor2","temperatura1","sensor3"]#sacar de la base de datos la topic list
# nuevocliente = Manage_sensor(broker,port,Clientid,user,password,topic_list)

# for topic in topic_list:
#     nuevocliente.sub(topic, qos=0)
#     time.sleep(1)

# nuevocliente.mqtt_deploy()