class Vuelo:
    def __init__(self, flight_number, origin, destination, departure_time, capacity):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.departure_time = destination
        self.capacity = capacity
        self.seat = capacity
        
    def verificar_asiento(self):
        return self.seat >0 
    def reservar_asiento(self):
        if self.seat >0:
            self.seat -= 1
            return True
        else:
            return False
        
    
        