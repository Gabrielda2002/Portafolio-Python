from menu import ManejoDatos

datos = ManejoDatos()


while True:
    print(f'''Por favor seleccione un numero de acuerdo a lo que desea ralizar.
        1. asignar datos.
        2. actualizar datos.
        3. eliminar datos.
        4. salir.
    ''')
    option = input()

    if option == "1":
        datos.asignar_notas()
    elif option == "2":
        datos.modificar()
    elif option == "3":
        datos.eliminar()
    elif option == "4":
        print("Ha salido del programa.")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")

print("Los datos asignados son: ")
print(datos.notas)