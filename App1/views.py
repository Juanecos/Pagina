
'''difinir vistas'''
from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'paginas/home.html')


def about(request):
    return render(request, 'paginas/about.html')


def reviews(request):
    return render(request, 'paginas/reviews.html')

def view(request):
    return render(request, 'paginas/view.html')

def hora(request):
    
    return render(request, 'paginas/hora.html')