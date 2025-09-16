"""
Configuración ASGI para el proyecto proyectotaller.

Este archivo expone el invocable ASGI como una variable a nivel de módulo llamada ``application``.

Para más información sobre este archivo, consulte
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# Establece la configuración de Django para el módulo de ajustes del proyecto.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyectotaller.settings')

# Obtiene la aplicación ASGI de Django.
application = get_asgi_application()
