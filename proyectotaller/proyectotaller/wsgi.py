"""
Configuración WSGI para el proyecto proyectotaller.

Este archivo expone el invocable WSGI como una variable a nivel de módulo llamada ``application``.

Para más información sobre este archivo, consulte
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Establece la configuración de Django para el módulo de ajustes del proyecto.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyectotaller.settings')

# Obtiene la aplicación WSGI de Django.
application = get_wsgi_application()
