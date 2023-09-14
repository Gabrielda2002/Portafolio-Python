def ingresar_datos():
    print("Ingrese el numero que desea validar")
    num=int(input())
    dato_mensaje = mensaje(num)
    mostrar(dato_mensaje)

def mensaje(num):
    if num == 0:
        Rmensaje = "El numero es neutro"
    elif num<0:
        Rmensaje = "El numero es negativo"
    else:
        Rmensaje = "El numero es positivo"
    return Rmensaje
        
    
def mostrar(dato_mensaje):
    print(dato_mensaje)

ingresar_datos()










