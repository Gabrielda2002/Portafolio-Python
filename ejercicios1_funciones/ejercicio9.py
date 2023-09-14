def ingresar():
    print("Ingrese un numero: ")
    numero=int(input())
    return numero

def es_perfecto(numero):
    suma_divisores = 0
    for i in range(1, numero):
        if numero % i==0:
            suma_divisores +=i
    return suma_divisores == numero

def main():
    
    numero =ingresar()
    if es_perfecto(numero):
        print(f"El numero {numero}, es perfecto.")
    else:
        print(f"EL numero {numero}, no es perfecto")    
        
if __name__ == "__main__":
    main()
    




