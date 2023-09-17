def ingresar():
    print("A continuacion ingrese una de las opciones de acuerdo a la bumba que necesita: ")
    print('''Ingrese:
        1. Bomba de agua.
        2. Bomba de gasolina.
        3. Bomba de hormigon.
        4. Pasta alimenticia.
        5. salir.''')
    option= int(input())
    return option
def menu(option):
        match option:
            case 0:
                print("No establecio un numero para el este tipo de bomba.")
                
            case 1:
                print("La bomba es una bomba de agua")
                
            case 2:
                print("La bomba es una bomba de gasolina")
                
            case 3:
                print("La bomba es una bomba de pasta hormigon.")
                
            case 4:
                print("La bomba es una bomba alimenticia.")
            case 5:
                print("Ha salido del programa.")
                return True
            case defecto:
                print("Error! El numero ingresado no es valido, por favor intente nuevamente.")


def main():
    while True:
        option=ingresar()
        if menu(option):
            break
if __name__=="__main__":
    main()
