from django.urls import path
from . import views

urlpatterns = [
    # URLs para Cliente
    path('clientes/', views.cliente_list, name='cliente_list'),
    path('clientes/new/', views.cliente_create, name='cliente_create'),
    path('clientes/<int:pk>/edit/', views.cliente_update, name='cliente_update'),
    path('clientes/<int:pk>/delete/', views.cliente_delete, name='cliente_delete'),

    # URLs para Vehiculo
    path('vehiculos/', views.vehiculo_list, name='vehiculo_list'),
    path('vehiculos/new/', views.vehiculo_create, name='vehiculo_create'),
    path('vehiculos/<int:pk>/edit/', views.vehiculo_update, name='vehiculo_update'),
    path('vehiculos/<int:pk>/delete/', views.vehiculo_delete, name='vehiculo_delete'),

    # URLs para Servicio
    path('servicios/', views.servicio_list, name='servicio_list'),
    path('servicios/new/', views.servicio_create, name='servicio_create'),
    path('servicios/<int:pk>/edit/', views.servicio_update, name='servicio_update'),
    path('servicios/<int:pk>/delete/', views.servicio_delete, name='servicio_delete'),

    # URLs para OrdenReparacion
    path('ordenes/', views.orden_reparacion_list, name='orden_reparacion_list'),
    path('ordenes/new/', views.orden_reparacion_create, name='orden_reparacion_create'),
    path('ordenes/<int:pk>/edit/', views.orden_reparacion_update, name='orden_reparacion_update'),
    path('ordenes/<int:pk>/delete/', views.orden_reparacion_delete, name='orden_reparacion_delete'),
]
