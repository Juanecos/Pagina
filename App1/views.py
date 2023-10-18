"""definir vistas"""
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import ModeloRealTime, ModeloHistory, ModeloList
from django.template import loader

def updatetopiclist():
    listado =list( ModeloList.objects.values_list('name', flat=True))
    print(listado)
    

def home(request):
    """acceder a la pagina de inicio"""
    lista = ModeloList.objects.values_list('name', flat=True)
    print(list(lista))
    
    return render(request, "paginas/home.html")


def about(request):
    """acceder a la pagina de acerca de"""
    return render(request, "paginas/about.html")


def reviews(request):
    """acceder a la pagina para hacer una observacion"""
    return render(request, "paginas/reviews.html")


def view(request):
    """acceder a la pagina de visualizacion"""
    return render(request, "paginas/view.html")


def dataview(request):
    """acceder a la pagina de tiempo real dentro de visualizacion"""
    datos = ModeloRealTime.objects.all()
    sensorlistado = ModeloList.objects.all()

    updatetopiclist()
    
    return render(request, "paginas/dataview.html", {"datosl":sensorlistado,"datos": datos})


def registrarsensor(request):
    """acceder aregistrar sensor"""
    nuevosensor = request.POST['txtnombresensor']
    nuevosensor_list = ModeloList.objects.create(name=nuevosensor)
    
    ModeloRealTime.objects.create(sensor=nuevosensor_list, temperatura=0.0, humedad=0.0)

    #actualizar lista de topicos


    return redirect('/visualizacion/viewdata/')

def eliminar_sensor(request, modelo_id):
    """funcion para eliminar una fila de la tabla"""
    modelo = ModeloList.objects.get(id = modelo_id)
    print(modelo)
    modelo.delete()
    #actualizar lista de topicos
    
    

    return redirect('/visualizacion/viewdata/')

def editar_sensor(request, modelo_id):
    codigo = ModeloList.objects.get(id = modelo_id)

    return render(request, 'paginas/edicion_sensor.html',{"codigo":codigo})

def editar_select(request,modelo_id):
    nombre = request.POST['txtnombresensor']
    modelo = ModeloList.objects.get(id=modelo_id)
    print(modelo)
    modelo.name = nombre
    modelo.save()
    #actualizar lista de topicos
    

    return redirect('/visualizacion/viewdata/')
