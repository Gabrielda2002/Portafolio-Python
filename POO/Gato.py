from Animal import Animal
class Gato(Animal):
    def __str__(self,color, nombre, cantidad_patas, tipo_pelaje):
        super.__str__(color, nombre, cantidad_patas, tipo_pelaje)
        
    # def pedir_datos(self):
    #     return super().pedir_datos()
    
    # def caminar(self, dato_caminar):
    #     print("El gato puede caminar.")
    
    def sonido(self):
        return f"{self.nombre} hace 'Miau!'"
        
    
    
        
    
    
    
        