import math
def ingresar():
    print("Ingrese el primer numero")
    numero1 = int(input())
    print("Por favor ingrese el segundo numero: ")
    numero2= int(input())
    return numero1, numero2
def calcular_mcm(numero1, numero2):
    mcd = math.gcd(numero1, numero2)
    mcm = abs(numero1*numero2) // mcd
    return mcm


def main():
    numero1, numero2 = ingresar()
    print(f"El minimo comun multiplo es de: {calcular_mcm(numero1, numero2)}.")
    
if __name__ == "__main__":
    main()