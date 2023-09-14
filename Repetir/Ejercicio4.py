#numero de usuario y contraseña validas
num_valido = 1
contraseña_valido = 1234
#solicitando datos al usuario
print("Por favor ingrese el numero de usuario: ")
num_usuario = int(input())
print("Por favor ingrese su contraseña: ")
password_valido = int(input())

if num_usuario == num_valido and password_valido == contraseña_valido:
    print("Ha ingresado con exito")
else:
    print("El numero de usuario o contraseña no son correctos")
    print("Por favor valide si son correctos los datos ingresados.")