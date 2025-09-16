"""
Configuración de URL para el proyecto proyectotaller.

La lista `urlpatterns` enruta las URLs a las vistas. Para más información, consulte:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Ejemplos:
Vistas basadas en funciones
    1. Agregue una importación: from my_app import views
    2. Agregue una URL a urlpatterns: path('', views.home, name='home')
Vistas basadas en clases
    1. Agregue una importación: from other_app.views import Home
    2. Agregue una URL a urlpatterns: path('', Home.as_view(), name='home')
Incluyendo otra URLconf
    1. Importe la función include(): from django.urls import include, path
    2. Agregue una URL a urlpatterns: path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from gestion import views # Importa las vistas de la aplicación 'gestion'

urlpatterns = [
    # Ruta para la interfaz de administración de Django.
    path('admin/', admin.site.urls),
    # Incluye las URLs de la aplicación 'gestion' bajo el prefijo 'gestion/'.
    path('gestion/', include('gestion.urls')),
    # Mapea la URL raíz del proyecto a la vista 'home' de la aplicación 'gestion'.
    path('', views.home, name='home'),
]
