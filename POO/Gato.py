from Animal import Animal
class Gato(Animal):
    def __init__(self,color, nombre, cami_patas, tipo_pelaje, escalar, maullar, cazar):
        super.__init__(color, nombre, cami_patas, tipo_pelaje)
        self.escalar = escalar
        self.maullar = maullar
    # def pedir_datos(self):
    #     return super().pedir_datos()
    
    def caminar(self, dato_caminar):
        print("El gato puede caminar.")
    
    def nombre(self):
        print("pelucita")
        
    
    
        
    
    
    
        