def ingresar():
    print("Ingrese un numero: ")
    num1=float(input())
    print("Ingrese un segundo numero: ")
    num2=float(input())
    return num1, num2

def ingresar_opcion():
    print(f'''Ahora ingrese la opcion de la operacion que desea realizar con esos dos numeros: 
        1. suma.
        2. resta.
        3. multiplicacion
        4. division.
        5. salir''')
    option= input()
    return option

def menu(option, num1, num2):
    if option == "1":
        resultado = num1+num2
        print(f"El resultado es: {resultado}")
        
    elif option == "2":
        resultado = num1-num2
        print(f"El resultado es: {resultado}")
        
    elif option == "3":
        resultado = num1*num2
        print(f"El resultado es: {resultado}")
        
    elif option == "4":
        resultado = num1/num2
        print(f"El resultado es: {resultado}")
        
    elif option == "5" :
        print("adios!")
        return True
    else:
        print("Por favor ingrese una opcion valida")


def main():
    while True:
        num1, num2 = ingresar()
        option= ingresar_opcion()
        if menu(option, num1, num2):
            break
if __name__ == "__main__":
    main()