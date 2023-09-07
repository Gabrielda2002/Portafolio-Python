contador_negativos = 0
suma_positivos = 0

while True:
    print("Por favor ingrese un numero (para terminar el programa ingrese 0): ")
    numero = float(input())
    
    
    if numero == 0:
        print("Ha finalizado el programa!")
        break
    elif numero > 0:
        suma_positivos += numero
    else:
        contador_negativos += 1

print(f"La suma de los numeros posivos que ha ingresado es: {suma_positivos}.")
print(f"Hay {contador_negativos} numeros negativos.")