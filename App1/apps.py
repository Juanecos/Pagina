from django.apps import AppConfig

from .clasesensores import Manage_sensor



def performance(broker, port, Clientid, user, password, topic_list, q):
    import time

    nuevocliente = Manage_sensor(broker, port, Clientid, user, password, topic_list)

    for topic in topic_list:
        nuevocliente.sub(topic, qos=0)

    while True:
        # try:
        mensaje = nuevocliente.mqtt_deploy()
        if mensaje is not None:
            # hacer update de la base de datos
            datos = (mensaje)
            topic = datos["Topico"]
            date = datos["Fecha"]
            hour = datos["Hora"]
            temperature = datos["Temperatura"]
            humidity = datos["Humedad"]
            q.put(datos)
            time.sleep(1)
            break

    # print(f"T:{topic}, F:{date}, h:{hour}, temp:{temperature}, hum:{humidity}")
    # print(datos)

    # q.put(datos)

        

 

    # try:
    #     mensaje = nuevocliente.mqtt_deploy()
    #     if mensaje is not None:
    #         # hacer update de la base de datos
    #         datos = (mensaje)
    #         topic = datos["Topico"]
    #         date = datos["Fecha"]
    #         hour = datos["Hora"]
    #         temperature = datos["Temperatura"]
    #         humidity = datos["Humedad"]

    # print(f"T:{topic}, F:{date}, h:{hour}, temp:{temperature}, hum:{humidity}")
    # print(datos)

    # q.put(datos)

    # time.sleep(0.2)
    # except KeyboardInterrupt:
    #     print("Disconnecting from MQTT broker and exiting.aaaaaaaaaaaaa")
    #     nuevocliente.shutdown()

    # except Exception as e:
    #     print("An error occurred:", str(e))
    #     print("Reconnecting to the MQTT broker in 5 seconds...aaaaaaaaaaaaaaaaa")
    #     time.sleep(5)
    #     nuevocliente.reconnectcl()


class App1Config(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "App1"

    def ready(self):
        # Importa los modelos y carga la base de datos aquí
        from .models import ModeloList, ModeloRealTime, ModeloHistory
        from .clasesensores import Manage_sensor
        import time
        import sys

        from multiprocessing import Process, Queue

        broker = "6eef623dbafd42238df342ee595d441a.s1.eu.hivemq.cloud"
        port = 8883
        user = "juan-camilo"
        password = "iNM123456789"
        user2 = "hivemq.webclient.1696257769493"
        password2 = "Q?1z.Y0ibLa47!eCD#Fc"
        Clientid = "cliente-python"

        # tablaRealTime = ModeloRealTime.objects.all()

        # for objeto in tablaRealTime:
        #     id_del_objeto = objeto.id
        #     enviarIDRealTime.append(id_del_objeto)

        # resultado_queue = multiprocessing.Queue()
        
        # except KeyboardInterrupt:
        #     print("Disconnecting F")
        #     # nuevocliente.shutdown()
        #     break
        # resultado = resultado_queue.get()  # Obtiene el resultado desde la cola
        # print("Resultado obtenido:", resultado)
        if 'runserver' in sys.argv:
            print("El servidor de desarrollo de Django está en ejecución")
            lista = ModeloList.objects.values_list("name", flat=True)
            topic_list = list(lista)
            print(topic_list)
            # while True:
            #     try:
            q = Queue()
            mqtt_process = Process(
                target=performance,
                args=(broker,port,Clientid,user,password,topic_list,q)
            )
            mqtt_process.start()
            print(q.get())  # prints "[42, None, 'hello']"
            mqtt_process.join()

            time.sleep(1)
            # y la aplicación se está cargando.
            # Puedes agregar aquí el código que deseas ejecutar en este caso.
        else:
            # El servidor de desarrollo no está en ejecución,
            # por lo que este código se ejecutará cuando se realicen
            # otras operaciones, como migraciones de base de datos, tests, etc.
            pass


# {"Topico":"temperatura1","Fecha":"2023-18-10","Hora":"9:46:55","Temperatura":"15.5","Humedad":"30"}
