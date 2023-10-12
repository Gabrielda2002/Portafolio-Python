from abc import ABC, abstractclassmethod
# from Vuelo import Vuelo


class AccionVuelo(abc):
    @abstractclassmethod
    def reserva_asiento(self, vuelo):
        pass
    
    @abstractclassmethod
    def asignar_asiento(self, vuelo, cliente):
        pass
    
    