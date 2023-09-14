import math

print("Por favor ingrese un numero: ")
num1=int(input())
print("Por favor ingrese otro numero: ")
num2=int(input())

mcd = math.gcd(num1, num2)

print(f"El maximo comun divisor de los numeros {num1}, {num2} es {mcd}.")