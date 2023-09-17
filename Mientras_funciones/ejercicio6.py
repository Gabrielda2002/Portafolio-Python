def ingresar():
    print("Ingrese la contraseña: ")
    password = input()
    return password

def logica(password):
    if password != "1234":
        return False
    elif password == "1234":
        return True

def main():
    while True:
        password = ingresar()
        if logica(password):
            print("Bienvenido ha ingresado al sistema con exito!")
            break
        else:
            print()

if __name__ == "__main__":
    main()
    