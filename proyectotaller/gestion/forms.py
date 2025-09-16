# gestion/forms.py
# Este archivo define los formularios de Django para los modelos de la aplicación 'gestion'.
# Estos formularios se utilizan para crear y actualizar instancias de los modelos
# a través de la interfaz web, proporcionando validación y renderizado de campos.

from django import forms
from .models import Cliente, Vehiculo, Servicio, OrdenReparacion

class ClienteForm(forms.ModelForm):
    """
    Formulario para el modelo Cliente.
    Permite la creación y edición de información de clientes.
    """
    class Meta:
        # Define el modelo asociado y los campos a incluir en el formulario.
        model = Cliente
        fields = ['nombre', 'apellido', 'telefono', 'email']
        # Define los widgets HTML para cada campo, aplicando clases CSS para estilo.
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class VehiculoForm(forms.ModelForm):
    """
    Formulario para el modelo Vehiculo.
    Permite la creación y edición de información de vehículos.
    """
    class Meta:
        # Define el modelo asociado y los campos a incluir en el formulario.
        model = Vehiculo
        fields = ['patente', 'marca', 'modelo', 'año', 'cliente']
        # Define los widgets HTML para cada campo, aplicando clases CSS para estilo.
        widgets = {
            'patente': forms.TextInput(attrs={'class': 'form-control'}),
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'año': forms.NumberInput(attrs={'class': 'form-control'}),
            'cliente': forms.Select(attrs={'class': 'form-control'}),
        }

class ServicioForm(forms.ModelForm):
    """
    Formulario para el modelo Servicio.
    Permite la creación y edición de información de servicios.
    """
    class Meta:
        # Define el modelo asociado y los campos a incluir en el formulario.
        model = Servicio
        fields = ['nombre', 'precio']
        # Define los widgets HTML para cada campo, aplicando clases CSS para estilo.
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'step': '1'}),
        }

class OrdenReparacionForm(forms.ModelForm):
    """
    Formulario para el modelo OrdenReparacion.
    Permite la creación y edición de órdenes de reparación.
    """
    class Meta:
        # Define el modelo asociado y los campos a incluir en el formulario.
        model = OrdenReparacion
        fields = ['vehiculo', 'servicios', 'fecha_ingreso', 'fecha_salida', 'estado']
        # Define los widgets HTML para cada campo, aplicando clases CSS para estilo.
        widgets = {
            'vehiculo': forms.Select(attrs={'class': 'form-control'}),
            'servicios': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'fecha_ingreso': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_salida': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
        }
