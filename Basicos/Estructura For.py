suma=0 #se crea la variable global
print("digite la cantidad de numeros para sumar")
cantidad = int(input())

for i in range(cantidad):
    print("Digite el numero" + str(i+1)+": ")
    numero=int(input())
    suma=suma+numero
    
print("La sumatoria total es de: ", str(suma))