# gestion/apps.py
# Este archivo define la configuración de la aplicación 'gestion'.

from django.apps import AppConfig


class GestionConfig(AppConfig):
    """
    Configuración de la aplicación 'gestion'.

    Define el tipo de campo automático predeterminado para los modelos
    y el nombre de la aplicación.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gestion'
