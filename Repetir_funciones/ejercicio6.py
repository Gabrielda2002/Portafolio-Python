def ingresar():
    print('''Por favor ingrese una de las siguientes opciones:
          1. Sumar
          2. Multiplicar
          3. Salir''')
    option = int(input())
    return option
    
def main():
    while True:
        option = ingresar()

        if option == 1:
            suma = 1 + 1
            print(f"El resultado de la suma es: {suma}")
        elif option == 2:
            mul = 5 * 5
            print(f"El resultado de la multiplicación es {mul}")
        elif option == 3:
            print("Ha salido el programa. Vuelva pronto!")
            break
        else:
            print("Por favor ingrese una opción válida mostrada en el menú anterior.")
if __name__ == "__main__":
    main()