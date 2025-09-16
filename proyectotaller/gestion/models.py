from django.db import models

# Modelo Cliente
class Cliente(models.Model):
    """
    Representa a un cliente del taller automotriz.
    """
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True) # Email es opcional

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# Modelo Vehiculo
class Vehiculo(models.Model):
    """
    Representa un vehículo propiedad de un cliente.
    """
    patente = models.CharField(max_length=10, unique=True) # Patente debe ser única
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    año = models.IntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='vehiculos') # Relacionado a un Cliente

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.patente})"

# Modelo Servicio
class Servicio(models.Model):
    """
    Representa un servicio ofrecido por el taller.
    """
    nombre = models.CharField(max_length=100, unique=True) # Nombre del servicio debe ser único
    precio = models.DecimalField(max_digits=10, decimal_places=0)

    def __str__(self):
        return f"{self.nombre} (${self.precio})"

# Modelo OrdenReparacion
class OrdenReparacion(models.Model):
    """
    Representa una orden de reparación para un vehículo.
    """
    ESTADO_CHOICES = [
        ('ingresado', 'Ingresado'),
        ('en_progreso', 'En Progreso'),
        ('finalizado', 'Finalizado'),
    ]

    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, related_name='ordenes_reparacion') # Vehículo (FK)
    servicios = models.ManyToManyField(Servicio, related_name='ordenes_reparacion') # Servicios (Muchos a Muchos)
    fecha_ingreso = models.DateField()
    fecha_salida = models.DateField(blank=True, null=True) # Fecha de salida es opcional
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='ingresado') # Estado con choices
    monto_total = models.DecimalField(max_digits=10, decimal_places=0, default=0) # Monto total

    def calcular_monto_total(self):
        """
        Calcula el monto total de la orden sumando los precios de los servicios asociados.
        """
        total = sum(servicio.precio for servicio in self.servicios.all())
        self.monto_total = total
        self.save()

    def __str__(self):
        return f"Orden N°{self.id} - {self.vehiculo.patente} - {self.estado}"
