"""crear el administrador y correr"""
from django.contrib import admin

from .models import ModeloList, ModeloRealTime, ModeloHistory

# Register your models here.

admin.site.register(ModeloRealTime)
admin.site.register(ModeloHistory)
admin.site.register(ModeloList)

# py manage.py createsuperuser
# email: juanecos97@hotmail.com
# usuario = super //admin
# contraseña = 1234 //admin123
