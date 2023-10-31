import tkinter as tk
from modelo import Modelo, Plato, Pedido

class Vista:
    def __init__(self, root, modelo):
        self.root = root
        self.root.title("Sistema de Gestión de Restaurante")
        self.modelo = modelo

        self.agregar_plato_button = tk.Button(root, text="Agregar Plato al Menú", command=self.agregar_plato_al_menu)
        self.agregar_plato_button.pack()

        self.tomar_pedido_button = tk.Button(root, text="Tomar Pedido", command=self.tomar_pedido)
        self.tomar_pedido_button.pack()

        self.calcular_cuenta_button = tk.Button(root, text="Calcular Cuenta", command=self.calcular_cuenta)
        self.calcular_cuenta_button.pack()

    def agregar_plato_al_menu(self):
        nombre = "Plato del día"  
        precio = 15.0  
        descripcion = "Una deliciosa opción del chef"  

        nuevo_plato = Plato(nombre, precio, descripcion)
        self.modelo.agregar_plato_al_menu(nuevo_plato)

        print(f"Plato {nombre} agregado al menú. Precio: ${precio:.2f}")

    def tomar_pedido(self):
        pedido = self.modelo.tomar_pedido()
        print(f"Pedido número {pedido.numero_pedido} tomado.")

    def calcular_cuenta(self):
        numero_pedido = 1  
        pedido_encontrado = None

        for pedido in self.modelo.pedidos:
            if pedido.numero_pedido == numero_pedido:
                pedido_encontrado = pedido
                break

        if pedido_encontrado:
            total_pagar = self.modelo.calcular_cuenta(pedido_encontrado)
            print(f"Total a pagar para el pedido número {numero_pedido}: ${total_pagar:.2f}")
        else:
            print(f"El pedido número {numero_pedido} no existe.")

if __name__ == "__main__":
    root = tk.Tk()
    modelo = Modelo()
    vista = Vista(root, modelo)
    root.mainloop()
