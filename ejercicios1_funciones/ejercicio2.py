def ingresar():
    print("Ingrese por favor un numero: ")
    num=input()
    dato_mensaje = mostrar(num)
    mostrar(dato_mensaje)
    
def mensaje(num):
    if num.isdigit() and len(num) == 3 and int(num) >0:
        Rmensaje = "El numero ingresado cumple con las condiciones"
    else:
        Rmensaje = "El numero no es valido, por favor ingrese un numero \npositivo y de 3 cifras."

def mostrar(dato_mensaje):
    print(dato_mensaje)

ingresar()






#solicitud par que el usuario ingrese el numero

#validacion con if
