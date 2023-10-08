class Letras:
    def __init__(self, vector, palabra):
        self.vector = vector
        self.palabra =palabra

    # def ingresar(self):
    #     print("Por favor ingrese un vector.")
    #     self.vector = input()
    #     print("Por favor ingrese una palabra.")
    #     self.palabra = input()
    #     return self.vector, self.palabra
    
    def verificar_capicua(self):
        self.vector = str(self.vector)
        vector_original = list(self.vector)
        vector_revertido = list(reversed(self.vector))
        if vector_original == vector_revertido:
            print(f"el vector {self.vector} es un Capicua")
        else:
            print("No es un Capicua.")

    def verificar_palindromo(self):
        self.palabra = self.palabra.lower()
        self.palabra = self.palabra.replace(" ","")
        palabra_original = list(self.palabra)
        palabra_revertida = list(reversed(self.palabra))

        if palabra_original == palabra_revertida:
            print(f"La palabra {self.palabra} es Palindromo.")
        else:
            print(f"La palabra ingresada no es Palindromo.")
