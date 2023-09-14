import math

def calcular_mcm(a, b):
    mcd = math.gcd(a,b)
    mcm = abs(a*b) // mcd
    return mcm

print("Ingrese el primer numero")
numero1 = int(input())

print("Por favor ingrese el segundo numero: ")
numero2= int(input())

mcm = calcular_mcm(numero1, numero2)

print(f"El minimo comun multiplo es de: {mcm}.")