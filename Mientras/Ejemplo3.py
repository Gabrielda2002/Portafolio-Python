numeros_agregados = []
while True:
    print("Ingrese un numero: ")
    numero = int(input())

    if numero < 0:
        break

    numeros_agregados.append(numero)

print("Los numeros ingresados son: ")
for numero in numeros_agregados:
    print(numero)