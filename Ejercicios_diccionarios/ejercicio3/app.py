from Verificar import Letras

print(f"Por favor ingrese un vector.")
vector = input()
print(f"Por favor ingrese una palabra.")
palabra = input()

verificar = Letras(vector, palabra)
verificar.verificar_capicua()
verificar.verificar_palindromo()
