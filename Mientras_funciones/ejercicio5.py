

def ingresar(indice):
    print(f"Ingrese numero {indice} : ")
    numero=float(input())
    return numero

def suma_numeros():
    suma = 0
    for i in range(10):
        numero = ingresar(i+1)
        suma+= numero
    return suma
def main():
    suma_total= suma_numeros()
    print(f"La suma de los 10 numeros es de: {suma_total}")

if __name__ == "__main__":
    main()



