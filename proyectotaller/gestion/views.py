from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, Vehiculo, Servicio, OrdenReparacion
from .forms import ClienteForm, VehiculoForm, ServicioForm, OrdenReparacionForm

# --- Vista de Inicio ---
def home(request):
    """
    Vista de la página de inicio.
    """
    return render(request, 'gestion/home.html', {'titulo': 'Sistema de Gestión de Taller Automotriz'})

# --- Vistas para Cliente ---
def cliente_list(request):
    """
    Lista todos los clientes.
    """
    clientes = Cliente.objects.all()
    return render(request, 'gestion/cliente_list.html', {'clientes': clientes, 'titulo': 'Listado de Clientes'})

def cliente_create(request):
    """
    Crea un nuevo cliente.
    """
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')
    else:
        form = ClienteForm()
    return render(request, 'gestion/cliente_form.html', {'form': form, 'titulo': 'Crear Cliente'})

def cliente_update(request, pk):
    """
    Actualiza un cliente existente.
    """
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'gestion/cliente_form.html', {'form': form, 'titulo': 'Editar Cliente'})

def cliente_delete(request, pk):
    """
    Elimina un cliente.
    """
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('cliente_list')
    return render(request, 'gestion/cliente_confirm_delete.html', {'cliente': cliente, 'titulo': 'Eliminar Cliente'})

# --- Vistas para Vehiculo ---
def vehiculo_list(request):
    """
    Lista todos los vehículos.
    """
    vehiculos = Vehiculo.objects.all()
    return render(request, 'gestion/vehiculo_list.html', {'vehiculos': vehiculos, 'titulo': 'Listado de Vehículos'})

def vehiculo_create(request):
    """
    Crea un nuevo vehículo.
    """
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vehiculo_list')
    else:
        form = VehiculoForm()
    return render(request, 'gestion/vehiculo_form.html', {'form': form, 'titulo': 'Crear Vehículo'})

def vehiculo_update(request, pk):
    """
    Actualiza un vehículo existente.
    """
    vehiculo = get_object_or_404(Vehiculo, pk=pk)
    if request.method == 'POST':
        form = VehiculoForm(request.POST, instance=vehiculo)
        if form.is_valid():
            form.save()
            return redirect('vehiculo_list')
    else:
        form = VehiculoForm(instance=vehiculo)
    return render(request, 'gestion/vehiculo_form.html', {'form': form, 'titulo': 'Editar Vehículo'})

def vehiculo_delete(request, pk):
    """
    Elimina un vehículo.
    """
    vehiculo = get_object_or_404(Vehiculo, pk=pk)
    if request.method == 'POST':
        vehiculo.delete()
        return redirect('vehiculo_list')
    return render(request, 'gestion/vehiculo_confirm_delete.html', {'vehiculo': vehiculo, 'titulo': 'Eliminar Vehículo'})

# --- Vistas para Servicio ---
def servicio_list(request):
    """
    Lista todos los servicios.
    """
    servicios = Servicio.objects.all()
    return render(request, 'gestion/servicio_list.html', {'servicios': servicios, 'titulo': 'Listado de Servicios'})

def servicio_create(request):
    """
    Crea un nuevo servicio.
    """
    if request.method == 'POST':
        form = ServicioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('servicio_list')
    else:
        form = ServicioForm()
    return render(request, 'gestion/servicio_form.html', {'form': form, 'titulo': 'Crear Servicio'})

def servicio_update(request, pk):
    """
    Actualiza un servicio existente.
    """
    servicio = get_object_or_404(Servicio, pk=pk)
    if request.method == 'POST':
        form = ServicioForm(request.POST, instance=servicio)
        if form.is_valid():
            form.save()
            return redirect('servicio_list')
    else:
        form = ServicioForm(instance=servicio)
    return render(request, 'gestion/servicio_form.html', {'form': form, 'titulo': 'Editar Servicio'})

def servicio_delete(request, pk):
    """
    Elimina un servicio.
    """
    servicio = get_object_or_404(Servicio, pk=pk)
    if request.method == 'POST':
        servicio.delete()
        return redirect('servicio_list')
    return render(request, 'gestion/servicio_confirm_delete.html', {'servicio': servicio, 'titulo': 'Eliminar Servicio'})

# --- Vistas para OrdenReparacion ---
def orden_reparacion_list(request):
    """
    Lista todas las órdenes de reparación.
    """
    ordenes = OrdenReparacion.objects.all().order_by('-fecha_ingreso')
    return render(request, 'gestion/orden_reparacion_list.html', {'ordenes': ordenes, 'titulo': 'Listado de Órdenes de Reparación'})

def orden_reparacion_create(request):
    """
    Crea una nueva orden de reparación.
    """
    if request.method == 'POST':
        form = OrdenReparacionForm(request.POST)
        if form.is_valid():
            orden = form.save(commit=False)
            orden.save()
            form.save_m2m() # Guarda la relación ManyToMany
            orden.calcular_monto_total() # Calcula el monto total después de guardar los servicios
            return redirect('orden_reparacion_list')
    else:
        form = OrdenReparacionForm()
    return render(request, 'gestion/orden_reparacion_form.html', {'form': form, 'titulo': 'Crear Orden de Reparación'})

def orden_reparacion_update(request, pk):
    """
    Actualiza una orden de reparación existente.
    """
    orden = get_object_or_404(OrdenReparacion, pk=pk)
    if request.method == 'POST':
        form = OrdenReparacionForm(request.POST, instance=orden)
        if form.is_valid():
            orden = form.save(commit=False)
            orden.save()
            form.save_m2m() # Guarda la relación ManyToMany
            orden.calcular_monto_total() # Recalcula el monto total
            return redirect('orden_reparacion_list')
    else:
        form = OrdenReparacionForm(instance=orden)
    return render(request, 'gestion/orden_reparacion_form.html', {'form': form, 'titulo': 'Editar Orden de Reparación'})

def orden_reparacion_delete(request, pk):
    """
    Elimina una orden de reparación.
    """
    orden = get_object_or_404(OrdenReparacion, pk=pk)
    if request.method == 'POST':
        orden.delete()
        return redirect('orden_reparacion_list')
    return render(request, 'gestion/orden_reparacion_confirm_delete.html', {'orden': orden, 'titulo': 'Eliminar Orden de Reparación'})
