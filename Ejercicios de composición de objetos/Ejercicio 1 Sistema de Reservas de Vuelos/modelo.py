class Vuelo:
    def __init__(self, numero_vuelo, origen, destino, hora_salida, capacidad_maxima):
        self.numero_vuelo = numero_vuelo
        self.origen = origen
        self.destino = destino
        self.hora_salida = hora_salida
        self.capacidad_maxima = capacidad_maxima
        self.asientos_disponibles = capacidad_maxima
        self.pasajeros = []

    def reservar_asiento(self, pasajero):
        if self.asientos_disponibles > 0:
            self.pasajeros.append(pasajero)
            self.asientos_disponibles -= 1
            pasajero.asiento_asignado = len(self.pasajeros)
            return True
        else:
            return False

class Pasajero:
    def __init__(self, nombre, numero_pasaporte, asiento_asignado):
        self.nombre = nombre
        self.numero_pasaporte = numero_pasaporte
        self.asiento_asignado = asiento_asignado

class Modelo:
    def __init__(self):
        self.vuelos = []

    def agregar_vuelo(self, vuelo):
        self.vuelos.append(vuelo)
