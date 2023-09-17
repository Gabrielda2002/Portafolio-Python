#se pide al usuario ingresar numeros positivos
def ingresar():
    print("Ingrese los numeros positivos que desea ingresar para acomular: ")
    numero = int(input())
    return numero

#variable donde se acomulan los numeros ingresados por el usuario
numeros_agregados=[]
#mostrar los numeros agregados por el usuario
def acomulador_numeros(numero):
    print("Los numeros positivos agregados por consola son:")
    for numero in numeros_agregados:
        print(numero)
#funcion main
def main():
    
    while True:
        numero= ingresar()
        #si el usuario ingresa un numeros negativo se rompe el ciclo y finaliza el progrema
        if numero <0:
            break
        numeros_agregados.append(numero)
        #aqui es donde se ingresan los numeros ingresados por el usurio y los acomula
        acomulador_numeros(numero)
        

if __name__ == "__main__":
    main()


# print("Los numeros agregados por consola son:")
# for numero in numeros_agregados:
#     print(numero)

# numeros_agregados = []
# while True:
#     print("Ingrese un numero: ")
#     numero = int(input())

#     if numero < 0:
#         break

#     numeros_agregados.append(numero)

# print("Los numeros ingresados son: ")
# for numero in numeros_agregados:
#     print(numero)