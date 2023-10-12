from tkinter import messagebox
from Ejercicios_Interfaces.reserva_vuelos.accioon_vuelo import AccionVuelo
from Vuelo import Vuelo
from Cliente import Cliente

class SistemaReserva(AccionVuelo):
    def reservar_vuelo(self):
        numero_vuelo = self.flight_number.get()
        origen = self.origin.get()
        destino = self.destination.get()
        hora_salida = departure_time.get()
        capacidad_maxima = int(self.capacity.get())
        
        vuelo = Vuelo(numero_vuelo, origen, destino, hora_salida, capacidad_maxima)
        if vuelo.verificar_asiento():
            messagebox.showinfo("La reserva a sido exitosa.")
        else:
            messagebox.showinfo("Error al reservar el asiento, mo hay asientos disponibles en este vuelo.")
    def reservar_asiento(self, vuelo):
        
        
            
            