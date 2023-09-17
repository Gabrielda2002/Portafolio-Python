while True:

    print("digite un numero de 1 a 7")
    num=int(input())

    match num:
        case 1:
            print("Lunes")
            break
        case 2:
            print("Martes")
            break
        case 3:
            print("Miercoles")
            break
        case 4:
            print("Jueves")
            break
        case 5:
            print("Viernes")
            break
        case 6:
            print("Sabado")
            break
        case 7:
            print("Domingo")
            break
        case defecto:
            print("Error! Ingrese una opcion valida")
