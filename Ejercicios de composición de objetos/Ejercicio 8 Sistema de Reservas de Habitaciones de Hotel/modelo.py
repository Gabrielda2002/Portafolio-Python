class Habitacion:
    def __init__(self, numero, tipo, precio, disponible=True):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.disponible = disponible

class Cliente:
    def __init__(self, nombre, numero_reserva, fecha_llegada):
        self.nombre = nombre
        self.numero_reserva = numero_reserva
        self.fecha_llegada = fecha_llegada

class Modelo:
    def __init__(self):
        self.habitaciones = []
        self.clientes = []

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def hacer_reserva(self, cliente, numero_habitacion):
        for habitacion in self.habitaciones:
            if habitacion.numero == numero_habitacion and habitacion.disponible:
                cliente.numero_reserva = numero_habitacion
                habitacion.disponible = False
                return True
        return False

    def calcular_costo_total(self, cliente):
        for habitacion in self.habitaciones:
            if habitacion.numero == cliente.numero_reserva:
                return habitacion.precio
        return 0

    def mostrar_disponibilidad(self):
        disponibles = [habitacion.numero for habitacion in self.habitaciones if habitacion.disponible]
        return disponibles
