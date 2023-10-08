from menu import Menu

menu = Menu()
menu.mostrar_menu()
plato, cantidad = menu.orden()
menu.calculo_total(plato, cantidad)
