# gestion/urls.py
# Este archivo define las rutas URL para la aplicación 'gestion'.
# Cada ruta mapea una URL a una vista específica en views.py,
# permitiendo la navegación y el acceso a las diferentes funcionalidades de la aplicación.

from django.urls import path
from . import views

urlpatterns = [
    # URLs para la gestión de Clientes
    path('clientes/', views.cliente_list, name='cliente_list'), # Lista todos los clientes
    path('clientes/new/', views.cliente_create, name='cliente_create'), # Crea un nuevo cliente
    path('clientes/<int:pk>/edit/', views.cliente_update, name='cliente_update'), # Edita un cliente existente por su ID
    path('clientes/<int:pk>/delete/', views.cliente_delete, name='cliente_delete'), # Elimina un cliente existente por su ID

    # URLs para la gestión de Vehículos
    path('vehiculos/', views.vehiculo_list, name='vehiculo_list'), # Lista todos los vehículos
    path('vehiculos/new/', views.vehiculo_create, name='vehiculo_create'), # Crea un nuevo vehículo
    path('vehiculos/<int:pk>/edit/', views.vehiculo_update, name='vehiculo_update'), # Edita un vehículo existente por su ID
    path('vehiculos/<int:pk>/delete/', views.vehiculo_delete, name='vehiculo_delete'), # Elimina un vehículo existente por su ID

    # URLs para la gestión de Servicios
    path('servicios/', views.servicio_list, name='servicio_list'), # Lista todos los servicios
    path('servicios/new/', views.servicio_create, name='servicio_create'), # Crea un nuevo servicio
    path('servicios/<int:pk>/edit/', views.servicio_update, name='servicio_update'), # Edita un servicio existente por su ID
    path('servicios/<int:pk>/delete/', views.servicio_delete, name='servicio_delete'), # Elimina un servicio existente por su ID

    # URLs para la gestión de Órdenes de Reparación
    path('ordenes/', views.orden_reparacion_list, name='orden_reparacion_list'), # Lista todas las órdenes de reparación
    path('ordenes/new/', views.orden_reparacion_create, name='orden_reparacion_create'), # Crea una nueva orden de reparación
    path('ordenes/<int:pk>/edit/', views.orden_reparacion_update, name='orden_reparacion_update'), # Edita una orden de reparación existente por su ID
    path('ordenes/<int:pk>/delete/', views.orden_reparacion_delete, name='orden_reparacion_delete'), # Elimina una orden de reparación existente por su ID
]
