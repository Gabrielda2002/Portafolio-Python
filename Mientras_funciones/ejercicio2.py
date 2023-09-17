def ingresar():
    print("Por favor ingrese la suma total de dinero de los productos que llevara el cliente: ")
    total_neto = float(input())
    return total_neto

# def calcular_descuento(total_neto):
    
#     return descuento

def calcular(total_neto):
    descuento = total_neto-(total_neto*0.20)
    agregar_iva = descuento+(descuento*0.10)
    return agregar_iva, descuento

def main():
    while True:
        total_neto = ingresar()
        agregar_iva, descuento = calcular(total_neto)
        if total_neto >0:
            calcular(descuento)
            print(f"El total con descuento es de: {descuento}")
            calcular(agregar_iva)
            print(f"El total a pagar incluyendo iva es de: {agregar_iva}")
            break
        elif total_neto ==0:
            print("Se le pedira al usuario nuevamente")
if __name__ == "__main__":
    main()



# while True:
    
#     if total_neto >0 :
#         descuento = total_neto-(total_neto*0.20)
#         print(f"El total con descuento es de: {descuento}")

#         agregar_iva = descuento+(descuento*0.10)
#         print(f"El total a pagar incluyendo iva es de: {agregar_iva}")
#         break
#     elif total_neto == 0 :
#         print("Se le pedira al usuario nuevamente")
