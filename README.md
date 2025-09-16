# Sistema de Gestión de Taller Automotriz (BioBio Motors)

Este proyecto implementa un sistema de gestión para un taller automotriz utilizando Django, siguiendo los requisitos de la Evaluación N°1 de Programación Back End (TI3041).

## Modelos Implementados

Se han definido los siguientes modelos ORM:

*   **Cliente**: `nombre`, `apellido`, `telefono`, `email` (opcional).
*   **Vehiculo**: `patente` (única), `marca`, `modelo`, `año`, `cliente` (ForeignKey).
*   **Servicio**: `nombre` (único), `precio`.
*   **OrdenReparacion**: `vehiculo` (ForeignKey), `servicios` (ManyToMany), `fecha_ingreso`, `fecha_salida` (opcional), `estado` (choices: 'ingresado', 'en_progreso', 'finalizado'), `monto_total`.

## Configuración y Ejecución del Proyecto

Sigue estos pasos para configurar y ejecutar el proyecto localmente:

1.  **Clonar el repositorio:**
    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd proyectotaller
    ```
    (Nota: Reemplaza `<URL_DEL_REPOSITORIO>` con la URL real de tu repositorio de GitHub).

2.  **Crear y activar un entorno virtual (opcional pero recomendado):**
    ```bash
    python -m venv venv
    # En Windows
    .\venv\Scripts\activate
    # En macOS/Linux
    source venv/bin/activate
    ```

3.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Aplicar migraciones de base de datos:**
    ```bash
    python proyectotaller/manage.py makemigrations gestion
    python proyectotaller/manage.py migrate
    ```

5.  **Generar datos de prueba (10 entradas para cada modelo):**
    ```bash
    python proyectotaller/manage.py generate_data
    ```

6.  **Ejecutar y registrar consultas en la Django Shell:**
    Los comandos para las consultas requeridas, junto con sus resultados, se encuentran en el archivo `shell_tests.txt`. Puedes ejecutar estos comandos en la shell de Django:
    ```bash
    python proyectotaller/manage.py shell
    # Luego, copia y pega los comandos de shell_tests.txt uno por uno.
    ```
    O puedes ejecutar los comandos directamente desde la línea de comandos:
    ```bash
    # Ejemplo de consulta (todos los comandos están en shell_tests.txt)
    python proyectotaller/manage.py shell --command "from gestion.models import Cliente; print(Cliente.objects.get(nombre='Cliente1').vehiculos.all())"
    ```

7.  **Iniciar el servidor de desarrollo:**
    ```bash
    python proyectotaller/manage.py runserver
    ```

8.  **Acceder a la interfaz web (CRUD completo):**
    Abre tu navegador y visita:
    *   `http://127.0.0.1:8000/gestion/clientes/` para gestionar Clientes.
    *   `http://127.0.0.1:8000/gestion/vehiculos/` para gestionar Vehículos.
    *   `http://127.0.0.1:8000/gestion/servicios/` para gestionar Servicios.
    *   `http://127.0.0.1:8000/gestion/ordenes/` para gestionar Órdenes de Reparación.


## Uso Simultáneo de la Terminal y la Interfaz Web

Puedes tener el servidor de desarrollo de Django ejecutándose en una terminal y abrir una **segunda terminal** en VS Code para interactuar con el ORM directamente a través de la Django Shell. Los cambios realizados en la shell se reflejarán en la interfaz web (y viceversa) ya que ambos interactúan con la misma base de datos.

## Estructura del Proyecto

```
.
├── proyectotaller/
│   ├── gestion/
│   │   ├── management/
│   │   │   └── commands/
│   │   │       └── generate_data.py
│   │   ├── migrations/
│   │   ├── templates/
│   │   │   └── gestion/
│   │   │       ├── base.html (Plantilla base extendida por todas las demás)
│   │   │       ├── home.html
│   │   │       ├── cliente_list.html
│   │   │       ├── cliente_form.html
│   │   │       ├── cliente_confirm_delete.html
│   │   │       ├── vehiculo_list.html
│   │   │       ├── vehiculo_form.html
│   │   │       ├── vehiculo_confirm_delete.html
│   │   │       ├── servicio_list.html
│   │   │       ├── servicio_form.html
│   │   │       ├── servicio_confirm_delete.html
│   │   │       ├── orden_reparacion_list.html
│   │   │       ├── orden_reparacion_form.html
│   │   │       └── orden_reparacion_confirm_delete.html
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── proyectotaller/
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   └── manage.py
├── ORM_usage_instructions.txt
├── requirements.txt
├── shell_tests.txt
├── TI3041 - Ev 1.pdf
└── README.md
