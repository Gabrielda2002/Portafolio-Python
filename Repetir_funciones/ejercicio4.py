
    
def insertar_datos():
    #solicitando datos al usuario
    print("Por favor ingrese el numero de usuario: ")
    num_usuario = int(input())
    print("Por favor ingrese su contraseña: ")
    password_valido = int(input())
    return num_usuario, password_valido
def validacion(num_usuario, password_valido):
    #numero de usuario y contraseña validas
    num_valido = 1
    contraseña_valido = 1234
    
    if num_usuario == num_valido and password_valido == contraseña_valido:
        return True
    else:
        return False
        
        
        
def main():
    num_usuario, password_valido= insertar_datos()
    
    if validacion(num_usuario, password_valido):
        print("bienvenido!")
    else:
        print("El numero de usuario o contraseña no son correctos")
        print("Por favor valide si son correctos los datos ingresados.")
           
if __name__ == "__main__":
    main()








