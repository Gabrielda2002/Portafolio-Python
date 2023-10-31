class ProductoElectronico:
    def __init__(self, nombre, precio, stock, marca):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.marca = marca

class Cliente:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

class Venta:
    def __init__(self, cliente):
        self.cliente = cliente
        self.productos_vendidos = []
        self.total = 0

    def agregar_producto(self, producto, cantidad):
        if producto.stock >= cantidad:
            self.productos_vendidos.append((producto, cantidad))
            producto.stock -= cantidad
            self.total += producto.precio * cantidad
            return True
        else:
            return False

class Modelo:
    def __init__(self):
        self.productos = []
        self.clientes = []
        self.ventas = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def realizar_venta(self, venta):
        self.ventas.append(venta)
