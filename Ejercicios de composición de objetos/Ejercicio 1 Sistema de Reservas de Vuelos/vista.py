import tkinter as tk
from modelo import Modelo, Vuelo, Pasajero

class Vista:
    def __init__(self, root, modelo):
        self.root = root
        self.root.title("Sistema de Reservas de Vuelos")
        self.modelo = modelo

        self.reservar_button = tk.Button(root, text="Reservar Asientos", command=self.reservar_asientos)
        self.reservar_button.pack()

        self.asignar_button = tk.Button(root, text="Asignar Pasajeros a Vuelos", command=self.asignar_pasajeros_a_vuelo)
        self.asignar_button.pack()

        self.verificar_button = tk.Button(root, text="Verificar Disponibilidad de Asientos", command=self.verificar_disponibilidad)
        self.verificar_button.pack()

    def reservar_asientos(self):
        vuelo_numero = "ABC123"  

        for vuelo in self.modelo.vuelos:
            if vuelo.numero_vuelo == vuelo_numero:
                vuelo_encontrado = vuelo
                break

        if vuelo_encontrado:
            nuevo_pasajero = Pasajero("John Doe", "12345", -1)
            if vuelo_encontrado.reservar_asiento(nuevo_pasajero):
                print(f"Reserva realizada para el vuelo {vuelo_numero}. Asiento asignado: {nuevo_pasajero.asiento_asignado}")
            else:
                print(f"No hay asientos disponibles en el vuelo {vuelo_numero}.")
        else:
            print(f"El vuelo {vuelo_numero} no existe.")

    def asignar_pasajeros_a_vuelo(self):
        vuelo_numero = "ABC123"  
        pasajero_nombre = "Alice Smith"  
        pasajero_numero_pasaporte = "67890" 

        vuelo_encontrado = None
        for vuelo in self.modelo.vuelos:
            if vuelo.numero_vuelo == vuelo_numero:
                vuelo_encontrado = vuelo
                break

        if vuelo_encontrado:
            nuevo_pasajero = Pasajero(pasajero_nombre, pasajero_numero_pasaporte, -1)
            if vuelo_encontrado.reservar_asiento(nuevo_pasajero):
                print(f"Pasajero {nuevo_pasajero.nombre} asignado al vuelo {vuelo_numero}. Asiento asignado: {nuevo_pasajero.asiento_asignado}")
            else:
                print(f"No hay asientos disponibles en el vuelo {vuelo_numero}.")
        else:
            print(f"El vuelo {vuelo_numero} no existe.")

    def verificar_disponibilidad(self):
        vuelo_numero = "ABC123"  
        vuelo_encontrado = None

        for vuelo in self.modelo.vuelos:
            if vuelo.numero_vuelo == vuelo_numero:
                vuelo_encontrado = vuelo
                break

        if vuelo_encontrado:
            disponibilidad = vuelo_encontrado.asientos_disponibles
            print(f"Asientos disponibles en el vuelo {vuelo_numero}: {disponibilidad}")
        else:
            print(f"El vuelo {vuelo_numero} no existe.")

if __name__ == "__main__":
    root = tk.Tk()
    modelo = Modelo()
    vuelo = Vuelo("ABC123", "New York", "Los Angeles", "14:00", 100)
    modelo.agregar_vuelo(vuelo)
    vista = Vista(root, modelo)
    root.mainloop()
