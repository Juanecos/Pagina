
'''definir vistas'''
from django.shortcuts import render
from .models import MiModelo
# from django.http import HttpResponse
# Create your views here.

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

