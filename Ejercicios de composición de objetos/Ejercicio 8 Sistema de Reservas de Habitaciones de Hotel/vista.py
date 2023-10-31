import tkinter as tk
from modelo import Modelo, Habitacion, Cliente

class Vista:
    def __init__(self, root, modelo):
        self.root = root
        self.root.title("Sistema de Reservas de Habitaciones")
        self.modelo = modelo

        self.agregar_habitacion_button = tk.Button(root, text="Agregar Habitación", command=self.agregar_habitacion)
        self.agregar_habitacion_button.pack()

        self.agregar_cliente_button = tk.Button(root, text="Agregar Cliente", command=self.agregar_cliente)
        self.agregar_cliente_button.pack()

        self.hacer_reserva_button = tk.Button(root, text="Hacer Reserva", command=self.hacer_reserva)
        self.hacer_reserva_button.pack()

        self.calcular_costo_button = tk.Button(root, text="Calcular Costo", command=self.calcular_costo)
        self.calcular_costo_button.pack()

        self.mostrar_disponibilidad_button = tk.Button(root, text="Mostrar Disponibilidad", command=self.mostrar_disponibilidad)
        self.mostrar_disponibilidad_button.pack()

    def agregar_habitacion(self):
        numero = 101  
        tipo = "Doble"  
        precio = 150.0  

        nueva_habitacion = Habitacion(numero, tipo, precio)
        self.modelo.agregar_habitacion(nueva_habitacion)

        print(f"Habitación {numero} agregada. Tipo: {tipo}, Precio por noche: ${precio:.2f}")

    def agregar_cliente(self):
        nombre = "Juan Pérez"  
        numero_reserva = 101  
        fecha_llegada = "2023-10-28"  

        nuevo_cliente = Cliente(nombre, numero_reserva, fecha_llegada)
        self.modelo.agregar_cliente(nuevo_cliente)

        print(f"Cliente {nombre} registrado. Número de reserva: {numero_reserva}, Fecha de llegada: {fecha_llegada}.")

    def hacer_reserva(self):
        numero_reserva = 101  
        cliente_nombre = "Juan Pérez"  

        cliente_encontrado = None
        for cliente in self.modelo.clientes:
            if cliente.nombre == cliente_nombre:
                cliente_encontrado = cliente
                break

        if cliente_encontrado and self.modelo.hacer_reserva(cliente_encontrado, numero_reserva):
            print(f"Reserva realizada para {cliente_nombre} en la habitación {numero_reserva}.")
        else:
            print(f"No se pudo hacer la reserva para {cliente_nombre} en la habitación {numero_reserva}.")

    def calcular_costo(self):
        cliente_nombre = "Juan Pérez"  

        cliente_encontrado = None
        for cliente in self.modelo.clientes:
            if cliente.nombre == cliente_nombre:
                cliente_encontrado = cliente
                break

        if cliente_encontrado:
            costo = self.modelo.calcular_costo_total(cliente_encontrado)
            if costo:
                print(f"Costo total para {cliente_nombre}: ${costo:.2f}")
            else:
                print(f"{cliente_nombre} no tiene una habitación reservada.")
        else:
            print(f"El cliente {cliente_nombre} no existe.")

    def mostrar_disponibilidad(self):
        habitaciones_disponibles = self.modelo.mostrar_disponibilidad()
        if habitaciones_disponibles:
            print(f"Habitaciones disponibles: {', '.join(map(str, habitaciones_disponibles))}")
        else:
            print("No hay habitaciones disponibles.")

if __name__ == "__main__":
    root = tk.Tk()
    modelo = Modelo()
    vista = Vista(root, modelo)
    root.mainloop()
