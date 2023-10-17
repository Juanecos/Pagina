#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from App1.clasesensores import Manage_sensor
from multiprocessing import Process

# import datetime





def ejecutar(broker, port, Clientid,user,password,topic_list):
    nuevocliente = Manage_sensor(broker, port, Clientid, user, password, topic_list)
    nuevocliente.mqtt_deploy()


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mipaginaweb.settings")

    broker = "6eef623dbafd42238df342ee595d441a.s1.eu.hivemq.cloud"
    port = 8883
    user = "juan-camilo"
    password = "iNM123456789"
    user2 = "hivemq.webclient.1696257769493"
    password2 = "Q?1z.Y0ibLa47!eCD#Fc"
    Clientid = ""
    topic_list = [
        "sensor2",
        "temperatura1",
        "sensor3",
    ]  # sacar de la base de datos la topic list
    # list= Mimodelo.objects.get_all().filter(name)

    # mqtt_process = Process(target=ejecutar, args=(broker, port, Clientid,user,password,topic_list,))
    # mqtt_process.start()
    try:
        from django.core.management import execute_from_command_line
        

    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    
    main()

