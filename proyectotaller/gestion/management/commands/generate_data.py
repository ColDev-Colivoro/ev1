from django.core.management.base import BaseCommand
from gestion.models import Cliente, Vehiculo, Servicio, OrdenReparacion
from datetime import date, timedelta
import random

class Command(BaseCommand):
    help = 'Generates 10 sample data entries for Cliente, Vehiculo, Servicio, and OrdenReparacion models.'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Deleting existing data...'))
        Cliente.objects.all().delete()
        Vehiculo.objects.all().delete()
        Servicio.objects.all().delete()
        OrdenReparacion.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Existing data deleted.'))

        self.stdout.write(self.style.SUCCESS('Generating 10 clients and 10 vehicles...'))
        clientes = []
        vehiculos = []
        for i in range(1, 11):
            cliente = Cliente.objects.create(
                nombre=f'Cliente{i}',
                apellido=f'Apellido{i}',
                telefono=f'9{random.randint(10000000, 99999999)}',
                email=f'cliente{i}@example.com' if i % 2 == 0 else None
            )
            clientes.append(cliente)
            vehiculo = Vehiculo.objects.create(
                patente=f'PAT{i:02d}00',
                marca=random.choice(['Toyota', 'Nissan', 'Ford', 'Chevrolet', 'BMW']),
                modelo=random.choice(['Corolla', 'Versa', 'Focus', 'Cruze', 'X5']),
                año=random.randint(2010, 2023),
                cliente=cliente
            )
            vehiculos.append(vehiculo)
        self.stdout.write(self.style.SUCCESS('10 clients and 10 vehicles generated.'))

        self.stdout.write(self.style.SUCCESS('Generating 10 services...'))
        servicios = []
        nombres_servicios = [
            'Cambio de Aceite', 'Revisión General', 'Cambio de Frenos', 'Alineación',
            'Balanceo', 'Cambio de Neumáticos', 'Diagnóstico Motor', 'Reparación Eléctrica',
            'Cambio de Batería', 'Lavado Detallado'
        ]
        # Precios en pesos chilenos (sin centavos y con valores más realistas)
        precios_servicios = [35000, 60000, 120000, 45000, 30000, 200000, 80000, 150000, 70000, 40000]

        for i in range(10):
            servicio = Servicio.objects.create(
                nombre=nombres_servicios[i],
                precio=precios_servicios[i]
            )
            servicios.append(servicio)
        self.stdout.write(self.style.SUCCESS('10 services generated.'))

        self.stdout.write(self.style.SUCCESS('Generating 10 repair orders...'))
        ordenes = []
        estados = ['ingresado', 'en_progreso', 'finalizado']
        for i in range(10):
            vehiculo_elegido = random.choice(vehiculos)
            fecha_ingreso = date(2025, 9, 1) + timedelta(days=i)
            estado_elegido = random.choice(estados)
            fecha_salida = None
            if estado_elegido == 'finalizado':
                fecha_salida = fecha_ingreso + timedelta(days=random.randint(1, 7))

            orden = OrdenReparacion.objects.create(
                vehiculo=vehiculo_elegido,
                fecha_ingreso=fecha_ingreso,
                fecha_salida=fecha_salida,
                estado=estado_elegido
            )
            servicios_asociados = random.sample(servicios, random.randint(1, 3))
            orden.servicios.set(servicios_asociados)
            orden.calcular_monto_total()
            ordenes.append(orden)
        self.stdout.write(self.style.SUCCESS('10 repair orders generated.'))

        self.stdout.write(self.style.SUCCESS('Sample data generation complete.'))
