def contar_numeros_repetidos(vector):
    contador = {}
    numeros_repetidos = []

    for numero in vector:
        if numero in contador:
            contador[numero] +=1
        else:
            contador[numero] = 1

    for numero, cantidad in contador.items():
        if cantidad > 1:
            numeros_repetidos.append(numero)

    return numeros_repetidos

print("Ingrese un vector de numeros separado por espacios: ")
entrada=input()

vector = [int(numero) for numero in entrada.split()]

numeros_repetidos = contar_numeros_repetidos(vector)

if numeros_repetidos:
    print(f"Los numeros repetidos del vector son: {', '.join(map(str, numeros_repetidos))}")
else:
    print("No hay numeros repetidos")
    
    
