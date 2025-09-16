# gestion/tests.py
# Este archivo contiene las pruebas unitarias para la aplicación 'gestion'.
# Aquí se pueden escribir pruebas para los modelos, vistas, formularios, etc.,
# para asegurar que el código funciona como se espera.

from django.test import TestCase
from .models import Cliente, Vehiculo, Servicio, OrdenReparacion
from datetime import date, timedelta

class ClienteModelTest(TestCase):
    # Configuración inicial para las pruebas del modelo Cliente
    def setUp(self):
        # Crea un cliente de prueba que será usado en múltiples tests
        self.cliente = Cliente.objects.create(
            nombre="Juan",
            apellido="Perez",
            telefono="123456789",
            email="juan.perez@example.com"
        )

    def test_creacion_cliente(self):
        """Verifica que un cliente puede ser creado correctamente."""
        # Comprueba que los atributos del cliente coinciden con los valores proporcionados
        self.assertEqual(self.cliente.nombre, "Juan")
        self.assertEqual(self.cliente.apellido, "Perez")
        self.assertEqual(self.cliente.telefono, "123456789")
        self.assertEqual(self.cliente.email, "juan.perez@example.com")
        # Asegura que el objeto creado es una instancia del modelo Cliente
        self.assertTrue(isinstance(self.cliente, Cliente))

    def test_lectura_cliente(self):
        """Verifica que un cliente existente puede ser recuperado de la base de datos."""
        # Intenta obtener el cliente por su ID
        cliente_recuperado = Cliente.objects.get(id=self.cliente.id)
        # Comprueba que el nombre del cliente recuperado es el esperado
        self.assertEqual(cliente_recuperado.nombre, "Juan")

    def test_actualizacion_cliente(self):
        """Verifica que la información de un cliente puede ser actualizada y persistida."""
        # Modifica el nombre del cliente
        self.cliente.nombre = "Pedro"
        # Guarda los cambios en la base de datos
        self.cliente.save()
        # Recupera el cliente actualizado para verificar los cambios
        cliente_actualizado = Cliente.objects.get(id=self.cliente.id)
        # Comprueba que el nombre ha sido actualizado correctamente
        self.assertEqual(cliente_actualizado.nombre, "Pedro")

    def test_eliminacion_cliente(self):
        """Verifica que un cliente puede ser eliminado de la base de datos."""
        # Guarda el ID del cliente antes de eliminarlo
        cliente_id = self.cliente.id
        # Elimina el cliente
        self.cliente.delete()
        # Intenta recuperar el cliente eliminado y espera una excepción DoesNotExist
        with self.assertRaises(Cliente.DoesNotExist):
            Cliente.objects.get(id=cliente_id)

class VehiculoModelTest(TestCase):
    # Configuración inicial para las pruebas del modelo Vehiculo
    def setUp(self):
        # Crea un cliente de prueba para asociarlo con el vehículo
        self.cliente = Cliente.objects.create(
            nombre="Ana",
            apellido="Gomez",
            telefono="987654321",
            email="ana.gomez@example.com"
        )
        # Crea un vehículo de prueba asociado al cliente
        self.vehiculo = Vehiculo.objects.create(
            patente="XYZ789",
            marca="Honda",
            modelo="Civic",
            año=2022,
            cliente=self.cliente
        )

    def test_creacion_vehiculo(self):
        """Verifica que un vehículo puede ser creado y está correctamente vinculado a un cliente."""
        # Comprueba que los atributos del vehículo coinciden con los valores proporcionados
        self.assertEqual(self.vehiculo.patente, "XYZ789")
        self.assertEqual(self.vehiculo.marca, "Honda")
        self.assertEqual(self.vehiculo.modelo, "Civic")
        self.assertEqual(self.vehiculo.año, 2022)
        # Verifica que el vehículo está asociado al cliente correcto
        self.assertEqual(self.vehiculo.cliente, self.cliente)
        # Asegura que el objeto creado es una instancia del modelo Vehiculo
        self.assertTrue(isinstance(self.vehiculo, Vehiculo))

    def test_relacion_cliente_vehiculo(self):
        """Verifica la relación inversa desde el cliente hacia sus vehículos."""
        # Comprueba que el cliente tiene exactamente un vehículo asociado
        self.assertEqual(self.cliente.vehiculos.count(), 1)
        # Verifica que el vehículo asociado es el que se creó
        self.assertEqual(self.cliente.vehiculos.first(), self.vehiculo)

class ServicioModelTest(TestCase):
    # Configuración inicial para las pruebas del modelo Servicio
    def setUp(self):
        # Crea un servicio de prueba
        self.servicio = Servicio.objects.create(
            nombre="Cambio de Aceite",
            precio=50.00
        )

    def test_creacion_servicio(self):
        """Verifica que un servicio puede ser creado correctamente."""
        # Comprueba que los atributos del servicio coinciden con los valores proporcionados
        self.assertEqual(self.servicio.nombre, "Cambio de Aceite")
        self.assertEqual(self.servicio.precio, 50.00)
        # Asegura que el objeto creado es una instancia del modelo Servicio
        self.assertTrue(isinstance(self.servicio, Servicio))

class OrdenReparacionModelTest(TestCase):
    # Configuración inicial para las pruebas del modelo OrdenReparacion
    def setUp(self):
        # Crea un cliente de prueba
        self.cliente = Cliente.objects.create(
            nombre="Roberto",
            apellido="Diaz",
            telefono="112233445",
            email="roberto.diaz@example.com"
        )
        # Crea un vehículo de prueba asociado al cliente
        self.vehiculo = Vehiculo.objects.create(
            patente="ABC123",
            marca="Toyota",
            modelo="Corolla",
            año=2020,
            cliente=self.cliente
        )
        # Crea dos servicios de prueba
        self.servicio1 = Servicio.objects.create(
            nombre="Cambio de Frenos",
            precio=150.00
        )
        self.servicio2 = Servicio.objects.create(
            nombre="Revisión General",
            precio=100.00
        )
        # Crea una orden de reparación asociada al vehículo
        self.orden = OrdenReparacion.objects.create(
            vehiculo=self.vehiculo,
            fecha_ingreso=date.today(),
            estado="ingresado"
        )
        # Añade los servicios a la orden (relación ManyToMany)
        self.orden.servicios.add(self.servicio1)
        self.orden.servicios.add(self.servicio2)
        # Calcula y guarda el monto total de la orden
        self.orden.calcular_monto_total()

    def test_creacion_orden_reparacion(self):
        """Verifica que una orden de reparación puede ser creada correctamente."""
        # Comprueba que la orden está asociada al vehículo correcto
        self.assertEqual(self.orden.vehiculo, self.vehiculo)
        # Verifica el estado inicial de la orden
        self.assertEqual(self.orden.estado, "ingresado")
        # Comprueba que se han añadido dos servicios a la orden
        self.assertEqual(self.orden.servicios.count(), 2)
        # Asegura que el objeto creado es una instancia del modelo OrdenReparacion
        self.assertTrue(isinstance(self.orden, OrdenReparacion))

    def test_calculo_monto_total(self):
        """Verifica que el monto total de la orden se calcula correctamente."""
        # Calcula el total esperado sumando los precios de los servicios
        expected_total = self.servicio1.precio + self.servicio2.precio
        # Comprueba que el monto total de la orden coincide con el valor esperado
        self.assertEqual(self.orden.monto_total, expected_total)

    def test_actualizacion_estado_orden(self):
        """Verifica que el estado y la fecha de salida de una orden pueden ser actualizados."""
        # Actualiza el estado de la orden a "finalizado"
        self.orden.estado = "finalizado"
        # Establece una fecha de salida
        self.orden.fecha_salida = date.today() + timedelta(days=5)
        # Guarda los cambios en la base de datos
        self.orden.save()
        # Recupera la orden actualizada para verificar los cambios
        orden_actualizada = OrdenReparacion.objects.get(id=self.orden.id)
        # Comprueba que el estado ha sido actualizado
        self.assertEqual(orden_actualizada.estado, "finalizado")
        # Verifica que la fecha de salida no es nula
        self.assertIsNotNone(orden_actualizada.fecha_salida)

    def test_eliminacion_orden(self):
        """Verifica que una orden de reparación puede ser eliminada de la base de datos."""
        # Guarda el ID de la orden antes de eliminarla
        orden_id = self.orden.id
        # Elimina la orden
        self.orden.delete()
        # Intenta recuperar la orden eliminada y espera una excepción DoesNotExist
        with self.assertRaises(OrdenReparacion.DoesNotExist):
            OrdenReparacion.objects.get(id=orden_id)
