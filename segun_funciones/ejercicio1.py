def ingresar():
    print("digite un numero de 1 a 7")
    num=int(input())
    return num

def logica(num):
    match num:
        case 1:
            print("Lunes")
            
        case 2:
            print("Martes")
            
        case 3:
            print("Miercoles")
            
        case 4:
            print("Jueves")
            
        case 5:
            print("Viernes")
            
        case 6:
            print("Sabado")
            
        case 7:
            print("Domingo")
            
        case defecto:
            print("Error! Ingrese una opcion valida")

def main():
    while True:
        num=ingresar()
        if 1 <= num  and num <= 7:
            logica(num)
            break
        else:
            print("Numero fuera de rango")
            logica(num)
if __name__ == "__main__":
    main()