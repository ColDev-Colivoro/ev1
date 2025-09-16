# gestion/views.py
# Este archivo contiene las funciones de vista para la aplicación 'gestion'.
# Cada función maneja una solicitud HTTP específica, interactúa con los modelos
# y formularios, y renderiza una plantilla HTML para mostrar la respuesta al usuario.

from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, Vehiculo, Servicio, OrdenReparacion
from .forms import ClienteForm, VehiculoForm, ServicioForm, OrdenReparacionForm

# --- Vista de Inicio ---
def home(request):
    """
    Vista de la página de inicio.
    Renderiza la plantilla 'home.html' y pasa un título al contexto.
    """
    return render(request, 'gestion/home.html', {'titulo': 'Sistema de Gestión de Taller Automotriz'})

# --- Vistas para Cliente ---
def cliente_list(request):
    """
    Lista todos los clientes existentes.
    Recupera todos los objetos Cliente de la base de datos y los pasa a la plantilla.
    """
    clientes = Cliente.objects.all()
    return render(request, 'gestion/cliente_list.html', {'clientes': clientes, 'titulo': 'Listado de Clientes'})

def cliente_create(request):
    """
    Maneja la creación de un nuevo cliente.
    Si la solicitud es POST, procesa el formulario; de lo contrario, muestra un formulario vacío.
    """
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cliente_list') # Redirige a la lista de clientes después de guardar
    else:
        form = ClienteForm() # Crea un formulario vacío para GET
    return render(request, 'gestion/cliente_form.html', {'form': form, 'titulo': 'Crear Cliente'})

def cliente_update(request, pk):
    """
    Maneja la actualización de un cliente existente.
    Recupera el cliente por su clave primaria (pk) y pre-rellena el formulario.
    """
    cliente = get_object_or_404(Cliente, pk=pk) # Obtiene el cliente o devuelve un 404
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente) # Vincula el formulario con los datos POST y la instancia existente
        if form.is_valid():
            form.save()
            return redirect('cliente_list') # Redirige a la lista de clientes después de actualizar
    else:
        form = ClienteForm(instance=cliente) # Crea un formulario pre-rellenado para GET
    return render(request, 'gestion/cliente_form.html', {'form': form, 'titulo': 'Editar Cliente'})

def cliente_delete(request, pk):
    """
    Maneja la eliminación de un cliente.
    Muestra una página de confirmación y elimina el cliente si la solicitud es POST.
    """
    cliente = get_object_or_404(Cliente, pk=pk) # Obtiene el cliente o devuelve un 404
    if request.method == 'POST':
        cliente.delete() # Elimina el cliente de la base de datos
        return redirect('cliente_list') # Redirige a la lista de clientes
    return render(request, 'gestion/cliente_confirm_delete.html', {'cliente': cliente, 'titulo': 'Eliminar Cliente'})

# --- Vistas para Vehiculo ---
def vehiculo_list(request):
    """
    Lista todos los vehículos existentes.
    Recupera todos los objetos Vehiculo de la base de datos y los pasa a la plantilla.
    """
    vehiculos = Vehiculo.objects.all()
    return render(request, 'gestion/vehiculo_list.html', {'vehiculos': vehiculos, 'titulo': 'Listado de Vehículos'})

def vehiculo_create(request):
    """
    Maneja la creación de un nuevo vehículo.
    Si la solicitud es POST, procesa el formulario; de lo contrario, muestra un formulario vacío.
    """
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vehiculo_list') # Redirige a la lista de vehículos después de guardar
    else:
        form = VehiculoForm() # Crea un formulario vacío para GET
    return render(request, 'gestion/vehiculo_form.html', {'form': form, 'titulo': 'Crear Vehículo'})

def vehiculo_update(request, pk):
    """
    Maneja la actualización de un vehículo existente.
    Recupera el vehículo por su clave primaria (pk) y pre-rellena el formulario.
    """
    vehiculo = get_object_or_404(Vehiculo, pk=pk) # Obtiene el vehículo o devuelve un 404
    if request.method == 'POST':
        form = VehiculoForm(request.POST, instance=vehiculo) # Vincula el formulario con los datos POST y la instancia existente
        if form.is_valid():
            form.save()
            return redirect('vehiculo_list') # Redirige a la lista de vehículos después de actualizar
    else:
        form = VehiculoForm(instance=vehiculo) # Crea un formulario pre-rellenado para GET
    return render(request, 'gestion/vehiculo_form.html', {'form': form, 'titulo': 'Editar Vehículo'})

def vehiculo_delete(request, pk):
    """
    Maneja la eliminación de un vehículo.
    Muestra una página de confirmación y elimina el vehículo si la solicitud es POST.
    """
    vehiculo = get_object_or_404(Vehiculo, pk=pk) # Obtiene el vehículo o devuelve un 404
    if request.method == 'POST':
        vehiculo.delete() # Elimina el vehículo de la base de datos
        return redirect('vehiculo_list') # Redirige a la lista de vehículos
    return render(request, 'gestion/vehiculo_confirm_delete.html', {'vehiculo': vehiculo, 'titulo': 'Eliminar Vehículo'})

# --- Vistas para Servicio ---
def servicio_list(request):
    """
    Lista todos los servicios existentes.
    Recupera todos los objetos Servicio de la base de datos y los pasa a la plantilla.
    """
    servicios = Servicio.objects.all()
    return render(request, 'gestion/servicio_list.html', {'servicios': servicios, 'titulo': 'Listado de Servicios'})

def servicio_create(request):
    """
    Maneja la creación de un nuevo servicio.
    Si la solicitud es POST, procesa el formulario; de lo contrario, muestra un formulario vacío.
    """
    if request.method == 'POST':
        form = ServicioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('servicio_list') # Redirige a la lista de servicios después de guardar
    else:
        form = ServicioForm() # Crea un formulario vacío para GET
    return render(request, 'gestion/servicio_form.html', {'form': form, 'titulo': 'Crear Servicio'})

def servicio_update(request, pk):
    """
    Maneja la actualización de un servicio existente.
    Recupera el servicio por su clave primaria (pk) y pre-rellena el formulario.
    """
    servicio = get_object_or_404(Servicio, pk=pk) # Obtiene el servicio o devuelve un 404
    if request.method == 'POST':
        form = ServicioForm(request.POST, instance=servicio) # Vincula el formulario con los datos POST y la instancia existente
        if form.is_valid():
            form.save()
            return redirect('servicio_list') # Redirige a la lista de servicios después de actualizar
    else:
        form = ServicioForm(instance=servicio) # Crea un formulario pre-rellenado para GET
    return render(request, 'gestion/servicio_form.html', {'form': form, 'titulo': 'Editar Servicio'})

def servicio_delete(request, pk):
    """
    Maneja la eliminación de un servicio.
    Muestra una página de confirmación y elimina el servicio si la solicitud es POST.
    """
    servicio = get_object_or_404(Servicio, pk=pk) # Obtiene el servicio o devuelve un 404
    if request.method == 'POST':
        servicio.delete() # Elimina el servicio de la base de datos
        return redirect('servicio_list') # Redirige a la lista de servicios
    return render(request, 'gestion/servicio_confirm_delete.html', {'servicio': servicio, 'titulo': 'Eliminar Servicio'})

# --- Vistas para OrdenReparacion ---
def orden_reparacion_list(request):
    """
    Lista todas las órdenes de reparación existentes.
    Recupera todas las órdenes de reparación y las ordena por fecha de ingreso descendente.
    """
    ordenes = OrdenReparacion.objects.all().order_by('-fecha_ingreso')
    return render(request, 'gestion/orden_reparacion_list.html', {'ordenes': ordenes, 'titulo': 'Listado de Órdenes de Reparación'})

def orden_reparacion_create(request):
    """
    Maneja la creación de una nueva orden de reparación.
    Si la solicitud es POST, procesa el formulario; de lo contrario, muestra un formulario vacío.
    Calcula el monto total después de guardar los servicios.
    """
    if request.method == 'POST':
        form = OrdenReparacionForm(request.POST)
        if form.is_valid():
            orden = form.save(commit=False) # Guarda la instancia del modelo sin guardar en la base de datos aún
            orden.save() # Guarda la instancia del modelo
            form.save_m2m() # Guarda la relación ManyToMany (servicios)
            orden.calcular_monto_total() # Calcula el monto total después de guardar los servicios
            return redirect('orden_reparacion_list') # Redirige a la lista de órdenes de reparación
    else:
        form = OrdenReparacionForm() # Crea un formulario vacío para GET
    return render(request, 'gestion/orden_reparacion_form.html', {'form': form, 'titulo': 'Crear Orden de Reparación'})

def orden_reparacion_update(request, pk):
    """
    Maneja la actualización de una orden de reparación existente.
    Recupera la orden por su clave primaria (pk) y pre-rellena el formulario.
    Recalcula el monto total después de actualizar los servicios.
    """
    orden = get_object_or_404(OrdenReparacion, pk=pk) # Obtiene la orden de reparación o devuelve un 404
    if request.method == 'POST':
        form = OrdenReparacionForm(request.POST, instance=orden) # Vincula el formulario con los datos POST y la instancia existente
        if form.is_valid():
            orden = form.save(commit=False) # Guarda la instancia del modelo sin guardar en la base de datos aún
            orden.save() # Guarda la instancia del modelo
            form.save_m2m() # Guarda la relación ManyToMany (servicios)
            orden.calcular_monto_total() # Recalcula el monto total
            return redirect('orden_reparacion_list') # Redirige a la lista de órdenes de reparación
    else:
        form = OrdenReparacionForm(instance=orden) # Crea un formulario pre-rellenado para GET
    return render(request, 'gestion/orden_reparacion_form.html', {'form': form, 'titulo': 'Editar Orden de Reparación'})

def orden_reparacion_delete(request, pk):
    """
    Maneja la eliminación de una orden de reparación.
    Muestra una página de confirmación y elimina la orden si la solicitud es POST.
    """
    orden = get_object_or_404(OrdenReparacion, pk=pk) # Obtiene la orden de reparación o devuelve un 404
    if request.method == 'POST':
        orden.delete() # Elimina la orden de reparación de la base de datos
        return redirect('orden_reparacion_list') # Redirige a la lista de órdenes de reparación
    return render(request, 'gestion/orden_reparacion_confirm_delete.html', {'orden': orden, 'titulo': 'Eliminar Orden de Reparación'})
