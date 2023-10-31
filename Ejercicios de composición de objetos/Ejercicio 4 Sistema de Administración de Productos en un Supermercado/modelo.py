class Producto:
    def __init__(self, nombre, precio, stock, categoria):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.categoria = categoria

class Compra:
    def __init__(self, fecha):
        self.fecha = fecha
        self.productos_comprados = []
        self.total = 0

    def agregar_producto(self, producto, cantidad):
        if producto.stock >= cantidad:
            self.productos_comprados.append((producto, cantidad))
            producto.stock -= cantidad
            self.total += producto.precio * cantidad
            return True
        else:
            return False

class Modelo:
    def __init__(self):
        self.productos = []
        self.compras = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def procesar_compra(self, compra):
        self.compras.append(compra)
