import random

def numero_azar():
    #numeros al azar
    num1 = random.randint(0, 101)
    num2 = random.randint(0, 101)
    return num1, num2
def ingresar(num1, num2):
    #se pide al usuario que ingrse la respuesta correcta de la suma de los dos numeros al azar
    print(f"¿Cual es el resultado de la suma de el numero {num1} y {num2}? ")
    answer = int(input())
    return answer
# def validacion(answer):

def main():
    #ciclo que se repite si la respuesta de la suma no es correcta, se detiene hasta que se ingrese
    #la respuesta correcta
    while True:
        num1,num2 = numero_azar()
        answer =ingresar(num1,num2)
        suma_correcta = num1+num2
        if answer == suma_correcta :
            print(f"Es correcto! la suma es de: {answer}")
            break
        elif answer != suma_correcta:
            print("Ingrese la respuesta correcta")
if __name__=="__main__":
    main()
    
