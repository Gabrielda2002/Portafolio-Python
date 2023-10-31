import tkinter as tk
from modelo import Modelo, Producto, Compra

class Vista:
    def __init__(self, root, modelo):
        self.root = root
        self.root.title("Sistema de Administración de Productos")
        self.modelo = modelo

        self.agregar_producto_button = tk.Button(root, text="Agregar Producto", command=self.agregar_producto)
        self.agregar_producto_button.pack()

        self.agregar_al_carrito_button = tk.Button(root, text="Agregar al Carrito", command=self.agregar_al_carrito)
        self.agregar_al_carrito_button.pack()

        self.procesar_compra_button = tk.Button(root, text="Procesar Compra", command=self.procesar_compra)
        self.procesar_compra_button.pack()

    def agregar_producto(self):
        nombre = "Producto"  
        precio = 10.0  
        stock = 50  
        categoria = "Alimentos"  

        nuevo_producto = Producto(nombre, precio, stock, categoria)
        self.modelo.agregar_producto(nuevo_producto)

        print(f"Producto {nombre} agregado a la categoría {categoria}.")

    def agregar_al_carrito(self):
        producto_nombre = "Producto"  
        cantidad = 3  

        producto_encontrado = None

        for producto in self.modelo.productos:
            if producto.nombre == producto_nombre:
                producto_encontrado = producto
                break

        if producto_encontrado:
            compra_actual = self.modelo.compras[-1] if self.modelo.compras else None

            if not compra_actual or compra_actual.fecha != self.obtener_fecha_actual():
                compra_actual = Compra(self.obtener_fecha_actual())
                self.modelo.procesar_compra(compra_actual)

            if compra_actual.agregar_producto(producto_encontrado, cantidad):
                print(f"{cantidad} unidades de {producto_nombre} agregadas al carrito.")
            else:
                print(f"No hay suficiente stock de {producto_nombre}.")

        else:
            print(f"El producto {producto_nombre} no existe.")

    def procesar_compra(self):
        if self.modelo.compras:
            compra = self.modelo.compras[-1]
            print(f"Compra procesada el {compra.fecha}. Total: ${compra.total:.2f}")
        else:
            print("No hay compras para procesar.")

    def obtener_fecha_actual(self):
        
        return "2023-10-28"  

if __name__ == "__main__":
    root = tk.Tk()
    modelo = Modelo()
    vista = Vista(root, modelo)
    root.mainloop()
