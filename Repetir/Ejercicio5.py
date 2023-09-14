while True:
    print("Por favor ingrese un numero:" )
    num1 = int(input())
    print("Por favor ingrese otro numero: ")
    num2 = int(input())

    if num1 == 0 and num2 == 0: 
        print("Ha salido del programa con exito.")
        break
    else:
        suma = num1+num2
        print(f"La suma da un total de: {suma}")