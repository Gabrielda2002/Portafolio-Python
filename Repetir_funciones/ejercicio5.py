def ingresar():
    print("Por favor ingrese un numero:" )
    num1 = int(input())
    print("Por favor ingrese otro numero: ")
    num2 = int(input())
    return num1, num2
    
def suma(num1, num2):
    return num1 + num2


def main():
    while True:
        num1, num2 = ingresar()
        if num1 == 0 and num2 == 0: 
            print("Ha salido del programa con exito.")
            break
        else:
            suma = num1+num2
            print(f"La suma da un total de: {suma}")
if __name__ == "__main__":
    main()