import tkinter as tk
from tkinter import messagebox
from abc import ABC, abstractmethod

class Vuelo:
    def __init__(self, numero_vuelo, origen, destino, hora_salida, capacidad_maxima):
        self.numero_vuelo = numero_vuelo
        self.origen = origen
        self.destino = destino
        self.hora_salida = hora_salida
        self.capacidad_maxima = capacidad_maxima
        self.asientos_disponibles = capacidad_maxima

    def verificar_disponibilidad(self):
        return self.asientos_disponibles > 0

    def reservar_asiento(self):
        if self.asientos_disponibles > 0:
            self.asientos_disponibles -= 1
            return True
        else:
            return False

class Pasajero:
    def __init__(self, nombre, numero_pasaporte, asiento_asignado):
        self.nombre = nombre
        self.numero_pasaporte = numero_pasaporte
        self.asiento_asignado = asiento_asignado

class AccionesVuelo(ABC):
    @abstractmethod
    def reservar_asiento(self, vuelo, pasajero):
        pass

    @abstractmethod
    def asignar_pasajero(self, vuelo, pasajero):
        pass

class SistemaReservas(AccionesVuelo):
    def reservar_vuelo(self):
        numero_vuelo = self.numero_vuelo.get()
        origen = self.origen.get()
        destino = self.destino.get()
        hora_salida = self.hora_salida.get()
        capacidad_maxima = int(self.capacidad_maxima.get())

        vuelo = Vuelo(numero_vuelo, origen, destino, hora_salida, capacidad_maxima)

        if vuelo.verificar_disponibilidad():
            messagebox.showinfo("Reserva exitosa", "El vuelo ha sido reservado exitosamente.")
        else:
            messagebox.showerror("Error de reserva", "No hay asientos disponibles en este vuelo.")

    def reservar_asiento(self, vuelo):
        if vuelo.verificar_disponibilidad():
            pasajero_nombre = self.pasajero_nombre.get()
            pasajero_numero_pasaporte = self.pasajero_numero_pasaporte.get()
            pasajero = Pasajero(pasajero_nombre, pasajero_numero_pasaporte, None)

            if vuelo.reservar_asiento():
                messagebox.showinfo("Reserva exitosa", f"El asiento {vuelo.capacidad_maxima - vuelo.asientos_disponibles} ha sido reservado para el pasajero {pasajero.nombre}.")
            else:
                messagebox.showerror("Error de reserva", "No hay asientos disponibles en este vuelo.")
        else:
            messagebox.showerror("Error de reserva", "No hay asientos disponibles en este vuelo.")

    def asignar_pasajero(self, vuelo, pasajero):
        if vuelo.asientos_disponibles > 0:
            pasajero.asiento_asignado = vuelo.capacidad_maxima - vuelo.asientos_disponibles
            vuelo.asientos_disponibles -= 1
            messagebox.showinfo("Asignación exitosa", f"Se ha asignado el asiento {pasajero.asiento_asignado} al pasajero {pasajero.nombre}.")

class ReservaVueloFormulario:
    def __init__(self, master):
        self.master = master
        master.title("Reserva de Vuelo")

        self.label_numero_vuelo = tk.Label(master, text="Número de vuelo:")
        self.label_numero_vuelo.pack()

        self.numero_vuelo = tk.Entry(master)
        self.numero_vuelo.pack()

        self.label_origen = tk.Label(master, text="Origen:")
        self.label_origen.pack()

        self.origen = tk.Entry(master)
        self.origen.pack()

        self.label_destino = tk.Label(master, text="Destino:")
        self.label_destino.pack()

        self.destino = tk.Entry(master)
        self.destino.pack()

        self.label_hora_salida = tk.Label(master, text="Hora de salida:")
        self.label_hora_salida.pack()

        self.hora_salida = tk.Entry(master)
        self.hora_salida.pack()

        self.label_capacidad_maxima = tk.Label(master, text="Capacidad máxima de pasajeros:")
        self.label_capacidad_maxima.pack()

        self.capacidad_maxima = tk.Entry(master)
        self.capacidad_maxima.pack()

        self.reservar_button = tk.Button(master, text="Reservar Vuelo", command=self.reservar_vuelo)
        self.reservar_button.pack()

    def reservar_vuelo(self):
        numero_vuelo = self.numero_vuelo.get()
        origen = self.origen.get()
        destino = self.destino.get()
        hora_salida = self.hora_salida.get()
        capacidad_maxima = int(self.capacidad_maxima.get())

        vuelo = Vuelo(numero_vuelo, origen, destino, hora_salida, capacidad_maxima)
        sistema_reservas = SistemaReservas()

        sistema_reservas.reservar_asiento(vuelo)

root = tk.Tk()
formulario = ReservaVueloFormulario(root)
root.mainloop()
