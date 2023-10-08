class Calculos:
    def __init__(self, numeros):
        self.numeros = numeros

    def calculos(self):
        suma = sum(self.numeros)
        promedio = suma // len(self.numeros)
        print(f"La suma total de los numeros es de: {suma}")
        print(f"El promedio de los numeros es de: {promedio}")
        return suma, promedio
    
        