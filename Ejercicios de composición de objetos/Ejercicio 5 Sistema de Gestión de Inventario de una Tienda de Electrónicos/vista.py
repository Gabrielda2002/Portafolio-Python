import tkinter as tk
from modelo import Modelo, ProductoElectronico, Cliente, Venta

class Vista:
    def __init__(self, root, modelo):
        self.root = root
        self.root.title("Sistema de Gestión de Inventario")
        self.modelo = modelo

        self.agregar_producto_button = tk.Button(root, text="Agregar Producto", command=self.agregar_producto)
        self.agregar_producto_button.pack()

        self.agregar_cliente_button = tk.Button(root, text="Agregar Cliente", command=self.agregar_cliente)
        self.agregar_cliente_button.pack()

        self.realizar_venta_button = tk.Button(root, text="Realizar Venta", command=self.realizar_venta)
        self.realizar_venta_button.pack()


    def agregar_producto(self):
        nombre = "Producto A"  
        precio = 100.0  
        stock = 50  
        marca = "Marca X"  

        nuevo_producto = ProductoElectronico(nombre, precio, stock, marca)
        self.modelo.agregar_producto(nuevo_producto)

        print(f"Producto {nombre} agregado al inventario. Marca: {marca}.")

    def agregar_cliente(self):
        nombre = "Tatan"  
        direccion = "123 Main St"  
        telefono = "555-1234"  

        nuevo_cliente = Cliente(nombre, direccion, telefono)
        self.modelo.agregar_cliente(nuevo_cliente)

        print(f"Cliente {nombre} agregado. Dirección: {direccion}, Teléfono: {telefono}.")

    def realizar_venta(self):
        cliente_nombre = "Tatan" 
        producto_nombre = "Producto A" 
        cantidad = 2  

        cliente_encontrado = None
        producto_encontrado = None

        for cliente in self.modelo.clientes:
            if cliente.nombre == cliente_nombre:
                cliente_encontrado = cliente
                break

        for producto in self.modelo.productos:
            if producto.nombre == producto_nombre:
                producto_encontrado = producto
                break

        if cliente_encontrado and producto_encontrado:
            venta_actual = self.modelo.ventas[-1] if self.modelo.ventas else None

            if not venta_actual:
                venta_actual = Venta(cliente_encontrado)
                self.modelo.realizar_venta(venta_actual)

            if venta_actual.agregar_producto(producto_encontrado, cantidad):
                print(f"Venta realizada a {cliente_nombre}. Total: ${venta_actual.total:.2f}")
            else:
                print(f"No hay suficiente stock de {producto_nombre}.")

        else:
            if not cliente_encontrado:
                print(f"El cliente {cliente_nombre} no existe.")
            if not producto_encontrado:
                print(f"El producto {producto_nombre} no existe.")

if __name__ == "__main__":
    root = tk.Tk()
    modelo = Modelo()
    vista = Vista(root, modelo)
    root.mainloop()
