class Menu:
    def __init__(self):
        self.menu = {
            "Hamburguesa": 15000,
            "Pizza": 65000,
            "Perros calientes": 13000
        }

    def mostrar_menu(self):
        print("MENU")
        for plato, precio in self.menu.items():
            print(f"{plato} --> ${precio}")

    def orden(self):
        print("Por favor seleccione un plato del menu.")
        seleccion = input()
        if seleccion in self.menu:
            print("Ingrese la cantidad deseada.")
            cantidad = int(input())
            return seleccion, cantidad
        else:
            print("Opcion no valida, por favor seleccione una opcion valida.")
            return None, 0

    def calculo_total(self, plato, cantidad):
        if plato in self.menu:
            precio_plato = self.menu[plato]
            total = precio_plato * cantidad
            print(f"El total de a pagar es de ${total:.2f}")
        else:
            print("No se pudo calcular el total a pagar.")

