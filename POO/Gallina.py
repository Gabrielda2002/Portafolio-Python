
from Animal import Animal
class Gallina(Animal):
    def __init__(self,color, nombre, cami_patas, tipo_pelaje, poner_huevos, tener_pico, aletear):
        super.__init__(color, nombre, cami_patas, tipo_pelaje)
        self.poner_huevos = poner_huevos
        self.tener_pico = tener_pico
        self.aletear = aletear
    
    # def pedir_datos(self):
    #     return super().pedir_datos()
    def caminar(self):
        print("El gallo puede caminar.")
        
        