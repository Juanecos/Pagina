"""crear el administrador y correr"""
from django.contrib import admin
from .models import MiModelo

# Register your models here.

admin.site.register(MiModelo)


# py manage.py createsuperuser
# email: juanecos97@hotmail.com
# usuario = super
# contraseña = 1234
