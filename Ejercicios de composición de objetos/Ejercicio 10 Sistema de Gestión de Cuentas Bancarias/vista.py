import tkinter as tk
from modelo import Modelo, Cliente, CuentaBancaria

class Vista:
    def __init__(self, root, modelo):
        self.root = root
        self.root.title("Sistema de Gestión de Cuentas Bancarias")
        self.modelo = modelo

        self.agregar_cliente_button = tk.Button(root, text="Agregar Cliente", command=self.agregar_cliente)
        self.agregar_cliente_button.pack()

        self.agregar_cuenta_button = tk.Button(root, text="Agregar Cuenta", command=self.agregar_cuenta)
        self.agregar_cuenta_button.pack()

        self.depositar_button = tk.Button(root, text="Depositar", command=self.depositar)
        self.depositar_button.pack()

        self.retirar_button = tk.Button(root, text="Retirar", command=self.retirar)
        self.retirar_button.pack()

        self.transferir_button = tk.Button(root, text="Transferir", command=self.transferir)
        self.transferir_button.pack()

        self.verificar_saldo_button = tk.Button(root, text="Verificar Saldo", command=self.verificar_saldo)
        self.verificar_saldo_button.pack()

    def agregar_cliente(self):
        nombre = "Cliente 1"  # Reemplaza con la entrada del usuario
        identificacion = "12345"  # Reemplaza con la entrada del usuario

        nuevo_cliente = Cliente(nombre, identificacion)
        self.modelo.agregar_cliente(nuevo_cliente)

        print(f"Cliente {nombre} agregado. Identificación: {identificacion}")

    def agregar_cuenta(self):
        cliente_nombre = "Cliente 1"  # Reemplaza con el nombre del cliente
        numero_cuenta = "C001"  # Reemplaza con el número de cuenta
        saldo = 1000.0  # Reemplaza con el saldo inicial
        tipo_cuenta = "Ahorro"  # Reemplaza con el tipo de cuenta

        cliente_encontrado = None
        for cliente in self.modelo.clientes:
            if cliente.nombre == cliente_nombre:
                cliente_encontrado = cliente
                break

        if cliente_encontrado:
            nueva_cuenta = CuentaBancaria(numero_cuenta, saldo, tipo_cuenta)
            cliente_encontrado.agregar_cuenta(nueva_cuenta)
            print(f"Cuenta {numero_cuenta} agregada al cliente {cliente_nombre}. Saldo: ${saldo:.2f}, Tipo: {tipo_cuenta}")
        else:
            print(f"El cliente {cliente_nombre} no existe.")

    def depositar(self):
        numero_cuenta = "C001"  # Reemplaza con el número de cuenta
        monto = 500.0  # Reemplaza con el monto a depositar

        cliente_encontrado = None
        cuenta_encontrada = None

        for cliente in self.modelo.clientes:
            for cuenta in cliente.cuentas:
                if cuenta.numero_cuenta == numero_cuenta:
                    cliente_encontrado = cliente
                    cuenta_encontrada = cuenta
                    break

        if cliente_encontrado and cuenta_encontrada:
            if cuenta_encontrada.depositar(monto):
                print(f"Depósito de ${monto:.2f} realizado en la cuenta {numero_cuenta}.")
            else:
                print(f"El monto a depositar debe ser mayor que 0.")
        else:
            if not cliente_encontrado:
                print(f"No se encontró el cliente para la cuenta {numero_cuenta}.")
            if not cuenta_encontrada:
                print(f"La cuenta {numero_cuenta} no existe.")

    def retirar(self):
        numero_cuenta = "C001"  # Reemplaza con el número de cuenta
        monto = 200.0  # Reemplaza con el monto a retirar

        cliente_encontrado = None
        cuenta_encontrada = None

        for cliente in self.modelo.clientes:
            for cuenta in cliente.cuentas:
                if cuenta.numero_cuenta == numero_cuenta:
                    cliente_encontrado = cliente
                    cuenta_encontrada = cuenta
                    break

        if cliente_encontrado and cuenta_encontrada:
            if cuenta_encontrada.retirar(monto):
                print(f"Retiro de ${monto:.2f} realizado en la cuenta {numero_cuenta}.")
            else:
                print(f"No se pudo realizar el retiro en la cuenta {numero_cuenta}. Verifique el monto y el saldo.")
        else:
            if not cliente_encontrado:
                print(f"No se encontró el cliente para la cuenta {numero_cuenta}.")
            if not cuenta_encontrada:
                print(f"La cuenta {numero_cuenta} no existe.")

    def transferir(self):
        cuenta_origen_numero = "C001"  # Reemplaza con el número de cuenta de origen
        cuenta_destino_numero = "C002"  # Reemplaza con el número de cuenta de destino
        monto = 300.0  # Reemplaza con el monto a transferir

        cliente_origen = None
        cliente_destino = None
        cuenta_origen = None
        cuenta_destino = None

        for cliente in self.modelo.clientes:
            for cuenta in cliente.cuentas:
                if cuenta.numero_cuenta == cuenta_origen_numero:
                    cliente_origen = cliente
                    cuenta_origen = cuenta
                if cuenta.numero_cuenta == cuenta_destino_numero:
                    cliente_destino = cliente
                    cuenta_destino = cuenta

        if cliente_origen and cuenta_origen and cliente_destino and cuenta_destino:
            if cliente_origen.transferir(cuenta_origen, cuenta_destino, monto):
                print(f"Transferencia de ${monto:.2f} realizada de la cuenta {cuenta_origen_numero} a la cuenta {cuenta_destino_numero}.")
            else:
                print(f"No se pudo realizar la transferencia. Verifique el monto y las cuentas.")
        else:
            print(f"No se encontraron las cuentas de origen y destino o los clientes asociados.")
    
    def verificar_saldo(self):
        numero_cuenta = "C001"  # Reemplaza con el número de cuenta

        cliente_encontrado = None
        cuenta_encontrada = None

        for cliente in self.modelo.clientes:
            for cuenta in cliente.cuentas:
                if cuenta.numero_cuenta == numero_cuenta:
                    cliente_encontrado = cliente
                    cuenta_encontrada = cuenta
                    break

        if cliente_encontrado and cuenta_encontrada:
            saldo = self.modelo.verificar_saldo(cuenta_encontrada)
            print(f"Saldo de la cuenta {numero_cuenta}: ${saldo:.2f}")
        else:
            if not cliente_encontrado:
                print(f"No se encontró el cliente para la cuenta {numero_cuenta}.")
            if not cuenta_encontrada:
                print(f"La cuenta {numero_cuenta} no existe.")

if __name__ == "__main__":
    root
