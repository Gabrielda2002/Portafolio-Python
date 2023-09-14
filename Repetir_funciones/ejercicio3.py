def ingresar():
    print("Ingrese por favor un numero: ")
    num=input()
    dato_mensaje = mensaje(num)
    mostrar(dato_mensaje)
    
def mensaje(num):
    if num.isdigit() and len(num) == 5 and int(num) >0:
        Rmensaje = "El numero ingresado cumple con las condiciones"
    else:
        Rmensaje = "El numero no es valido, por favor ingrese un numero \npositivo y de 5 cifras."
    return Rmensaje
        

def mostrar(dato_mensaje):
    print(dato_mensaje)

ingresar()
