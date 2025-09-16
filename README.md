# Sistema de Gestión de Taller Automotriz (BioBio Motors)

Este proyecto implementa un sistema de gestión para un taller automotriz utilizando Django, siguiendo los requisitos de la Evaluación N°1 de Programación Back End (TI3041).

**Repositorio:** [https://github.com/ColDev-Colivoro/ev1.git](https://github.com/ColDev-Colivoro/ev1.git)

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
    git clone https://github.com/ColDev-Colivoro/ev1.git
    cd ev1
    ```

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
    python proyectotaller/manage.py shell --command "from gestion.models import Cliente; print(Cliente.objects.get(nombre='''Cliente1''').vehiculos.all())"
    ```

7.  **Iniciar el servidor de desarrollo:**
    ```bash
    python proyectotaller/manage.py runserver
    ```

8.  **Acceder a la Interfaz de Usuario Web (CRUD Completo):**
 
    Abre tu navegador y visita `http://127.0.0.1:8000/` para acceder a la página de inicio del proyecto. Desde allí, puedes navegar a las siguientes secciones para la gestión CRUD completa:
    *   `http://127.0.0.1:8000/gestion/clientes/` para gestionar Clientes.
    *   `http://127.0.0.1:8000/gestion/vehiculos/` para gestionar Vehículos.
    *   `http://127.0.0.1:8000/gestion/servicios/` para gestionar Servicios.
    *   `http://127.0.0.1:8000/gestion/ordenes/` para gestionar Órdenes de Reparación.


## Uso del ORM de Django

Este apartado proporciona una guía sobre cómo interactuar con los modelos ORM de Django definidos para el sistema.

### Acceso a la Django Shell

Para interactuar con el ORM, abre la Django Shell desde la raíz de tu proyecto (donde se encuentra `manage.py`):

```bash
python proyectotaller/manage.py shell
```

Una vez dentro de la shell, puedes importar tus modelos:

```python
from gestion.models import Cliente, Vehiculo, Servicio, OrdenReparacion
from datetime import date, timedelta
```

### Operaciones CRUD Básicas

#### 1. Crear Registros

```python
# Crear un Cliente
cliente_nuevo = Cliente.objects.create(
    nombre='''Carlos''',
    apellido='''Ruiz''',
    telefono='''998877665''',
    email='''carlos.ruiz@example.com'''
)
print(f"Cliente creado: {cliente_nuevo}")

# Crear un Vehiculo para el cliente_nuevo
vehiculo_nuevo = Vehiculo.objects.create(
    patente='''XYZ789''',
    marca='''Honda''',
    modelo='''Civic''',
    año=2022,
    cliente=cliente_nuevo
)
print(f"Vehículo creado: {vehiculo_nuevo}")

# Crear un Servicio
servicio_nuevo = Servicio.objects.create(
    nombre='''Cambio de Bujías''',
    precio=75.00
)
print(f"Servicio creado: {servicio_nuevo}")

# Crear una Orden de Reparacion
orden_nueva = OrdenReparacion.objects.create(
    vehiculo=vehiculo_nuevo,
    fecha_ingreso=date.today(),
    estado='''ingresado'''
)
# Añadir servicios a la orden (relación ManyToMany)
orden_nueva.servicios.add(servicio_nuevo)
# Si hay más servicios, puedes añadirlos así:
# otro_servicio = Servicio.objects.get(nombre='''Cambio de Aceite''')
# orden_nueva.servicios.add(otro_servicio)

# Calcular y guardar el monto total de la orden
orden_nueva.calcular_monto_total()
print(f"Orden de Reparación creada: {orden_nueva}")
```

#### 2. Leer Registros

```python
# Obtener todos los clientes
todos_clientes = Cliente.objects.all()
for c in todos_clientes:
    print(c)

# Obtener un cliente por su ID
cliente_por_id = Cliente.objects.get(id=1)
print(f"Cliente por ID: {cliente_por_id}")

# Obtener un vehículo por su patente
vehiculo_por_patente = Vehiculo.objects.get(patente='''PAT0100''')
print(f"Vehículo por patente: {vehiculo_por_patente}")

# Filtrar órdenes por estado
ordenes_en_progreso = OrdenReparacion.objects.filter(estado='''en_progreso''')
for o in ordenes_en_progreso:
    print(o)

# Filtrar órdenes sin fecha de salida
ordenes_sin_salida = OrdenReparacion.objects.filter(fecha_salida__isnull=True)
for o in ordenes_sin_salida:
    print(o)

# Acceder a relaciones inversas (related_name)
# Vehículos de un cliente
cliente_ejemplo = Cliente.objects.get(nombre='''Cliente1''')
vehiculos_cliente = cliente_ejemplo.vehiculos.all()
print(f"Vehículos de {cliente_ejemplo.nombre}: {vehiculos_cliente}")

# Órdenes de un vehículo
vehiculo_ejemplo = Vehiculo.objects.get(patente='''PAT0100''')
ordenes_vehiculo = vehiculo_ejemplo.ordenes_reparacion.all()
print(f"Órdenes de {vehiculo_ejemplo.patente}: {ordenes_vehiculo}")

# Servicios asociados a una orden
orden_ejemplo = OrdenReparacion.objects.get(id=1)
servicios_orden = orden_ejemplo.servicios.all()
print(f"Servicios de la orden {orden_ejemplo.id}: {servicios_orden}")
```

#### 3. Actualizar Registros

```python
# Actualizar el teléfono de un cliente
cliente_a_actualizar = Cliente.objects.get(nombre='''Carlos''')
cliente_a_actualizar.telefono = '''999111222'''
cliente_a_actualizar.save()
print(f"Cliente actualizado: {cliente_a_actualizar}")

# Actualizar el estado y fecha de salida de una orden
orden_a_finalizar = OrdenReparacion.objects.get(id=orden_nueva.id)
orden_a_finalizar.estado = '''finalizado'''
orden_a_finalizar.fecha_salida = date.today() + timedelta(days=2)
orden_a_finalizar.save()
print(f"Orden finalizada: {orden_a_finalizar}")
```

#### 4. Eliminar Registros

```python
# Eliminar un servicio
servicio_a_eliminar = Servicio.objects.get(nombre='''Cambio de Bujías''')
servicio_a_eliminar.delete()
print(f"Servicio eliminado: {servicio_a_eliminar}")

# Eliminar un cliente (esto también eliminará sus vehículos y órdenes asociadas debido a CASCADE)
cliente_a_eliminar = Cliente.objects.get(nombre='''Carlos''')
cliente_a_eliminar.delete()
print(f"Cliente eliminado: {cliente_a_eliminar}")
```

### Consideraciones Adicionales

*   **`calcular_monto_total()`**: Recuerda llamar a `orden.calcular_monto_total()` después de añadir o quitar servicios a una `OrdenReparacion` para actualizar el `monto_total`.
*   **`related_name`**: Se han utilizado `related_name` en las relaciones `ForeignKey` y `ManyToManyField` para facilitar el acceso inverso desde los modelos relacionados (ej. `cliente.vehiculos.all()`).
*   **`get_estado_display()`**: Para obtener la representación legible del campo `estado` de `OrdenReparacion`, usa `orden.get_estado_display()`.

## Uso Simultáneo de la Terminal y la Interfaz Web

Puedes tener el servidor de desarrollo de Django ejecutándose en una terminal y abrir una **segunda terminal** en VS Code para interactuar con el ORM directamente a través de la Django Shell. Los cambios realizados en la shell se reflejarán en la interfaz web (y viceversa) ya que ambos interactúan con la misma base de datos.

## Estructura del Proyecto

![Diagrama de la raíz](diagrama%20django%20ev1.png)

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
├── requirements.txt
├── shell_tests.txt
└── README.md
```
