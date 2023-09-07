while True:
    print("A continuacion ingrese una de las opciones de acuerdo a la bumba que necesita: ")
    print('''Ingrese:
        1. Bomba de agua.
        2. Bomba de gasolina.
        3. Bomba de hormigon.
        4. Pasta alimenticia.''')
    option= int(input())
    match option:
        case 0:
            print("No establecio un numero para el este tipo de bomba.")
            
        case 1:
            print("La bomba es una bomba de agua")
            break
        case 2:
            print("La bomba es una bomba de gasolina")
            break
        case 3:
            print("La bomba es una bomba de pasta hormigon.")
            break
        case 4:
            print("La bomba es una bomba alimenticia.")
            break
        case defecto:
            print("Error! El numero ingresado no es valido, por favor intente nuevamente.")