import random

#numeros al azar
num1 = random.randint(0, 101)
num2 = random.randint(0, 101)

suma_correcta = num1+num2

while True:
    print(f"¿Cual es el resultado de la suma de el numero {num1} y {num2}? ")
    answer = int(input())

    if answer == suma_correcta :
        print(f"Es correcto! la suma es de: {answer}")
        break
    elif answer != suma_correcta:
        print("Ingrese la respuesta correcta")
