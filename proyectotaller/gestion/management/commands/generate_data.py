# gestion/management/commands/generate_data.py
# Este archivo define un comando de administración personalizado de Django.
# Su propósito es generar datos de ejemplo para los modelos de la aplicación 'gestion',
# lo cual es útil para pruebas y desarrollo.

from django.core.management.base import BaseCommand
from gestion.models import Cliente, Vehiculo, Servicio, OrdenReparacion
from datetime import date, timedelta
import random

class Command(BaseCommand):
    """
    Comando de Django para generar datos de ejemplo.
    """
    help = 'Genera 10 entradas de datos de ejemplo para los modelos Cliente, Vehiculo, Servicio y OrdenReparacion.'

    def handle(self, *args, **kwargs):
        """
        Lógica principal del comando para generar datos.
        """
        self.stdout.write(self.style.SUCCESS('Eliminando datos existentes...'))
        # Elimina todos los registros existentes de cada modelo para asegurar un estado limpio.
        Cliente.objects.all().delete()
        Vehiculo.objects.all().delete()
        Servicio.objects.all().delete()
        OrdenReparacion.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Datos existentes eliminados.'))

        self.stdout.write(self.style.SUCCESS('Generando 10 clientes y 10 vehículos...'))
        clientes = []
        vehiculos = []
        # Bucle para crear 10 clientes y 10 vehículos asociados.
        for i in range(1, 11):
            cliente = Cliente.objects.create(
                nombre=f'Cliente{i}',
                apellido=f'Apellido{i}',
                telefono=f'9{random.randint(10000000, 99999999)}',
                email=f'cliente{i}@example.com' if i % 2 == 0 else None # Email opcional
            )
            clientes.append(cliente)
            vehiculo = Vehiculo.objects.create(
                patente=f'PAT{i:02d}00',
                marca=random.choice(['Toyota', 'Nissan', 'Ford', 'Chevrolet', 'BMW']),
                modelo=random.choice(['Corolla', 'Versa', 'Focus', 'Cruze', 'X5']),
                año=random.randint(2010, 2023),
                cliente=cliente # Asocia el vehículo al cliente creado
            )
            vehiculos.append(vehiculo)
        self.stdout.write(self.style.SUCCESS('10 clientes y 10 vehículos generados.'))

        self.stdout.write(self.style.SUCCESS('Generando 10 servicios...'))
        servicios = []
        nombres_servicios = [
            'Cambio de Aceite', 'Revisión General', 'Cambio de Frenos', 'Alineación',
            'Balanceo', 'Cambio de Neumáticos', 'Diagnóstico Motor', 'Reparación Eléctrica',
            'Cambio de Batería', 'Lavado Detallado'
        ]
        # Precios en pesos chilenos 
        precios_servicios = [35000, 60000, 120000, 45000, 30000, 200000, 80000, 150000, 70000, 40000]

        # Bucle para crear 10 servicios con nombres y precios predefinidos.
        for i in range(10):
            servicio = Servicio.objects.create(
                nombre=nombres_servicios[i],
                precio=precios_servicios[i]
            )
            servicios.append(servicio)
        self.stdout.write(self.style.SUCCESS('10 servicios generados.'))

        self.stdout.write(self.style.SUCCESS('Generando 10 órdenes de reparación...'))
        ordenes = []
        estados = ['ingresado', 'en_progreso', 'finalizado']
        # Bucle para crear 10 órdenes de reparación.
        for i in range(10):
            vehiculo_elegido = random.choice(vehiculos) # Selecciona un vehículo al azar
            fecha_ingreso = date(2025, 9, 1) + timedelta(days=i) # Fecha de ingreso incremental
            estado_elegido = random.choice(estados) # Estado aleatorio
            fecha_salida = None
            if estado_elegido == 'finalizado':
                fecha_salida = fecha_ingreso + timedelta(days=random.randint(1, 7)) # Fecha de salida si está finalizado

            orden = OrdenReparacion.objects.create(
                vehiculo=vehiculo_elegido,
                fecha_ingreso=fecha_ingreso,
                fecha_salida=fecha_salida,
                estado=estado_elegido
            )
            servicios_asociados = random.sample(servicios, random.randint(1, 3)) # Asocia 1 a 3 servicios al azar
            orden.servicios.set(servicios_asociados)
            orden.calcular_monto_total() # Calcula el monto total de la orden
            ordenes.append(orden)
        self.stdout.write(self.style.SUCCESS('10 órdenes de reparación generadas.'))

        self.stdout.write(self.style.SUCCESS('Generación de datos de ejemplo completada.'))
