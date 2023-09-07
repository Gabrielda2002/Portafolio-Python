print("Ingrese un numero: ")
num1=float(input())

print("Ingrese un segundo numero: ")
num2=float(input())


while True:
    

    print(f'''Ahora ingrese la opcion de la operacion que desea realizar con esos dos numeros: 
    1. suma.
    2. resta.
    3. multiplicacion
    4. division.
    5. salir''')
    option= input()



    if option == "1":
        resultado = num1+num2
        print(f"El resultado es: {resultado}")
        break
    elif option == "2":
        resultado = num1-num2
        print(f"El resultado es: {resultado}")
        break
    elif option == "3":
        resultado = num1*num2
        print(f"El resultado es: {resultado}")
        break
    elif option == "4":
        resultado = num1/num2
        print(f"El resultado es: {resultado}")
        break
    elif option == "5" :
        print("adios!")
        break
    else:
        print("Por favor ingrese una opcion valida")
