"""importacion de librerias"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="inicio" ),
    path('acerca_de/', views.about, name="acerca-de"),
    path('observaciones/', views.reviews, name="observaciones"),
    path('visualizacion/', views.view, name="visualizacion"),
    path('visualizacion/temperatura/', views.temperatura, name="temperatura"),

]