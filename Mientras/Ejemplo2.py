while True:
    print("Por favor ingrese la suma total de dinero de los productos que llevara el cliente: ")
    total_neto = float(input())

    if total_neto >0 :
        descuento = total_neto-(total_neto*0.20)
        print(f"El total con descuento es de: {descuento}")

        agregar_iva = descuento+(descuento*0.10)
        print(f"El total a pagar incluyendo iva es de: {agregar_iva}")
        break
    elif total_neto == 0 :
        print("Se le pedira al usuario nuevamente")
