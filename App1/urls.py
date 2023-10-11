"""importacion de librerias"""
# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="inicio"),
    path("acerca_de/", views.about, name="acerca-de"),
    path("observaciones/", views.reviews, name="observaciones"),
    path("visualizacion/", views.view, name="visualizacion"),
    path("visualizacion/viewdata/", views.dataview, name="viewdata"),
    path("visualizacion/viewdata/registrarsensor/", views.registrarsensor, name="registrarsensor"),
    # path('visualizacion/viewdata//<int:modelo_id>/', views.editar_modelo, name='editar_modelo'),
    path('visualizacion/viewdata/eliminar/<int:modelo_id>/', views.eliminar_sensor, name='eliminar_sensor'),
    path('visualizacion/viewdata/editar/<int:modelo_id>/', views.editar_sensor, name='editar_sensor'),
    path('visualizacion/viewdata/editarsensorselct//<int:modelo_id>/', views.editar_select, name='editarsensorselct'),
    #path('visualizacion/viewdata/editarsensorselct/', views.editarselecsensor, name ="editarselecsensor")
    #path('visualizacion/temperatura/<int:id>',views.sensores, name="sensor-id")
]
