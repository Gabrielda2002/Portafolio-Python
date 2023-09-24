
from Animal import Animal
class Gallina(Animal):
    def __str__(self,color, nombre, cami_patas, tipo_pelaje):
        super.__str__(color, nombre, cami_patas, tipo_pelaje)
        
    
    # def pedir_datos(self):
    #     return super().pedir_datos()
    # def caminar(self):
    #     print("El gallo puede caminar.")

    def sonido(self):
        return f"{self.nombre} hace 'kokoroko´"
        
        