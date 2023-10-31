class Plato:
    def __init__(self, nombre, precio, descripcion):
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion

class Pedido:
    def __init__(self, numero_pedido):
        self.numero_pedido = numero_pedido
        self.platos = []
        self.total_pagar = 0

    def agregar_plato(self, plato):
        self.platos.append(plato)
        self.total_pagar += plato.precio

class Modelo:
    def __init__(self):
        self.menu = []
        self.pedidos = []
        self.numero_pedido_actual = 1

    def agregar_plato_al_menu(self, plato):
        self.menu.append(plato)

    def tomar_pedido(self):
        pedido = Pedido(self.numero_pedido_actual)
        self.pedidos.append(pedido)
        self.numero_pedido_actual += 1
        return pedido

    def calcular_cuenta(self, pedido):
        return pedido.total_pagar
