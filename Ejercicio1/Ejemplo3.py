#solicitud par que el usuario ingrese el numero
print("Ingrese por favor un numero: ")
num=input()
#validacion con if
if num.isdigit() and len(num) == 5 and int(num) >0:
    print("El numero ingresado cumple con las condiciones")
else:
    print("El numero no es valido, por favor ingrese un numero \npositivo y de 5 cifras.")1