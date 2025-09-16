# gestion/models.py
# Este archivo define los modelos de base de datos para la aplicación 'gestion'.
# Cada clase de modelo representa una tabla en la base de datos y define
# los campos y relaciones entre los datos.

from django.db import models

# Modelo Cliente
class Cliente(models.Model):
    """
    Representa a un cliente del taller automotriz.
    Cada cliente tiene un nombre, apellido, teléfono y un email opcional.
    """
    nombre = models.CharField(max_length=100, verbose_name="Nombre") # Nombre del cliente,verbose_name sirve para
    apellido = models.CharField(max_length=100, verbose_name="Apellido") # Apellido del cliente
    telefono = models.CharField(max_length=15, verbose_name="Teléfono") # Número de teléfono del cliente
    email = models.EmailField(blank=True, null=True, verbose_name="Email") # Email del cliente (opcional)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ['apellido', 'nombre'] # Ordenar clientes por apellido y luego por nombre

    def __str__(self):
        """
        Representación en cadena del objeto Cliente.
        """
        return f"{self.nombre} {self.apellido}"

# Modelo Vehiculo
class Vehiculo(models.Model):
    """
    Representa un vehículo propiedad de un cliente.
    Cada vehículo tiene una patente única, marca, modelo, año y está asociado a un cliente.
    """
    patente = models.CharField(max_length=10, unique=True, verbose_name="Patente") # Patente única del vehículo
    marca = models.CharField(max_length=50, verbose_name="Marca") # Marca del vehículo
    modelo = models.CharField(max_length=50, verbose_name="Modelo") # Modelo del vehículo
    año = models.IntegerField(verbose_name="Año") # Año de fabricación del vehículo
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name='vehiculos',
        verbose_name="Cliente"
    ) # Relación uno a muchos con el modelo Cliente

    class Meta:
        verbose_name = "Vehículo"
        verbose_name_plural = "Vehículos"
        ordering = ['patente'] # Ordenar vehículos por patente

    def __str__(self):
        """
        Representación en cadena del objeto Vehiculo.
        """
        return f"{self.marca} {self.modelo} ({self.patente})"

# Modelo Servicio
class Servicio(models.Model):
    """
    Representa un servicio ofrecido por el taller.
    Cada servicio tiene un nombre único y un precio.
    """
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Nombre del Servicio") # Nombre único del servicio
    precio = models.DecimalField(max_digits=10, decimal_places=0, verbose_name="Precio") # Precio del servicio

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
        ordering = ['nombre'] # Ordenar servicios por nombre

    def __str__(self):
        """
        Representación en cadena del objeto Servicio.
        """
        return f"{self.nombre} (${self.precio})"

# Modelo OrdenReparacion
class OrdenReparacion(models.Model):
    """
    Representa una orden de reparación para un vehículo.
    Incluye el vehículo, los servicios asociados, fechas de ingreso y salida,
    estado de la reparación y el monto total.
    """
    # Opciones para el campo 'estado' de la orden de reparación.
    ESTADO_CHOICES = [
        ('ingresado', 'Ingresado'),
        ('en_progreso', 'En Progreso'),
        ('finalizado', 'Finalizado'),
    ]

    vehiculo = models.ForeignKey(
        Vehiculo,
        on_delete=models.CASCADE,
        related_name='ordenes_reparacion',
        verbose_name="Vehículo"
    ) # Relación uno a muchos con el modelo Vehiculo
    servicios = models.ManyToManyField(
        Servicio,
        related_name='ordenes_reparacion',
        verbose_name="Servicios"
    ) # Relación muchos a muchos con el modelo Servicio
    fecha_ingreso = models.DateField(verbose_name="Fecha de Ingreso") # Fecha en que el vehículo ingresó al taller
    fecha_salida = models.DateField(blank=True, null=True, verbose_name="Fecha de Salida") # Fecha de salida del vehículo (opcional)
    estado = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        default='ingresado',
        verbose_name="Estado"
    ) # Estado actual de la orden de reparación
    monto_total = models.DecimalField(
        max_digits=10,
        decimal_places=0,
        default=0,
        verbose_name="Monto Total"
    ) # Monto total calculado de la reparación

    class Meta:
        verbose_name = "Orden de Reparación"
        verbose_name_plural = "Órdenes de Reparación"
        ordering = ['-fecha_ingreso'] # Ordenar órdenes por fecha de ingreso descendente

    def calcular_monto_total(self):
        """
        Calcula el monto total de la orden sumando los precios de los servicios asociados.
        Guarda el resultado en el campo 'monto_total'.
        """
        total = sum(servicio.precio for servicio in self.servicios.all())
        self.monto_total = total
        self.save()

    def __str__(self):
        """
        Representación en cadena del objeto OrdenReparacion.
        """
        return f"Orden N°{self.id} - {self.vehiculo.patente} - {self.estado}"
