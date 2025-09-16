"""
Utilidad de línea de comandos de Django para tareas administrativas.

Este archivo es el punto de entrada para ejecutar varias tareas administrativas
como iniciar el servidor de desarrollo, migrar la base de datos, etc.
"""
import os
import sys


def main():
    """
    Ejecuta tareas administrativas.

    Esta función establece el módulo de configuración predeterminado de Django y luego
    ejecuta el comando desde los argumentos de la línea de comandos.
    También maneja el ImportError si Django no está instalado correctamente.
    """
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyectotaller.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "No se pudo importar Django. ¿Está seguro de que está instalado y "
            "disponible en su variable de entorno PYTHONPATH? ¿Olvidó "
            "activar un entorno virtual?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    # Este bloque asegura que main() se llama cuando el script se ejecuta directamente.
    main()
