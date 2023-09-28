
'''definir vistas'''
from django.shortcuts import render
from django.http import HttpResponse
from .models import MiModelo
from django.template import loader

# import pyrebase
# # Create your views here.

# # test-c3d8b proyecto
# config = {
#   'apiKey': "AIzaSyDbBnEESS4GhltvSzEwp-CaKJMhWgaFkZE",
#   'authDomain': "test-c3d8b.firebaseapp.com",
#   'projectId': "test-c3d8b",
#   'storageBucket': "test-c3d8b.appspot.com",
#   'messagingSenderId': "86425367004",
#   'appId': "1:86425367004:web:22edc939bea12ee383df19"
# };

# # Initialize Firebase
# firebase=pyrebase.initialize_app(config);

def home(request):
    '''acceder a la pagina de inicio'''
    return render(request, 'paginas/home.html')


def about(request):
    '''acceder a la pagina de acerca de'''
    return render(request, 'paginas/about.html')


def reviews(request):
    '''acceder a la pagina para hacer una observacion'''
    return render(request, 'paginas/reviews.html')

def view(request):
    '''acceder a la pagina de visualizacion'''
    return render(request, 'paginas/view.html')

def temperatura(request):
    '''acceder a la pagina de tiempo real dentro de visualizacion'''
    datos = MiModelo.objects.all()

    return render(request, 'paginas/temperature.html', {'datos':datos})

def sensores(request,id):
    '''acceder a un sensor en especifico'''

    p= MiModelo.objects.get(id=id)
    print(f"hola {p}")
    #falta perfeccionarlo
    return render(request, 'paginas/sensorgraph.html', {'datos':datos})

