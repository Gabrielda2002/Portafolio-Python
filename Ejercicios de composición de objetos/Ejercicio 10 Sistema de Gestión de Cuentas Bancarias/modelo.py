class CuentaBancaria:
    def __init__(self, numero_cuenta, saldo, tipo_cuenta):
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo
        self.tipo_cuenta = tipo_cuenta

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            return True
        return False

    def retirar(self, monto):
        if monto > 0 and self.saldo >= monto:
            self.saldo -= monto
            return True
        return False

class Cliente:
    def __init__(self, nombre, identificacion):
        self.nombre = nombre
        self.identificacion = identificacion
        self.cuentas = []

    def agregar_cuenta(self, cuenta):
        self.cuentas.append(cuenta)

    def transferir(self, cuenta_origen, cuenta_destino, monto):
        if cuenta_origen in self.cuentas and cuenta_destino in self.cuentas:
            if cuenta_origen.retirar(monto):
                cuenta_destino.depositar(monto)
                return True
        return False

class Modelo:
    def __init__(self):
        self.clientes = []

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def verificar_saldo(self, cuenta):
        return cuenta.saldo
