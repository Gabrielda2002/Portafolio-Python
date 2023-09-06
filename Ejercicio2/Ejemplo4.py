print("Ingrese un numero: ")
num1= int(input())
print("Por favor ingrese un segundo numero: ")
num2 = int(input())

if num1 > num2:
    num1, num2 = num2, num1 #aqui se intercambian las variables en caso de que num 2 sea menor a num 1 se intercambian para que quedene de manera ascendente


print("Los numeros que hay entre los dos numeros ingresados son: ")

for numero in range(num1, num2 + 1):
    print(numero)