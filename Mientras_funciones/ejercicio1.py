def ingresar():
    print("Por favor ingrese un numero (para terminar el programa ingrese 0): ")
    numero = float(input())
    return numero


def contadores(contador_negativos, suma_positivos ,numero):
    contador_negativos =0
    suma_positivos =0

    # if numero > 0:
    #     suma_positivos += numero
    # else:
    #     contador_negativos += 1
    
    return contador_negativos, suma_positivos

def main():
    # global suma_positivos, contador_negativos
    suma_positivos, contador_negativos = 0,0

    while True:
        numero = ingresar()
        if numero == 0:
            print("Ha finalizado el programa.")
            break
        if numero > 0:
            suma_positivos += numero
        else:
            contador_negativos += 1
        # else:
        #     contador_negativos, suma_positivos = contadores(numero, contador_negativos,suma_positivos)

    print(f"La suma de los numeros posivos que ha ingresado es: {suma_positivos}.")
    print(f"Hay {contador_negativos} numeros negativos.")

if __name__ == "__main__":
    main()



