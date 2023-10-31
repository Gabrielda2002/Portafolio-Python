import tkinter as tk
from modelo import Modelo, Departamento, Empleado

class Vista:
    def __init__(self, root, modelo):
        self.root = root
        self.root.title("Sistema de Gestión de Empleados")
        self.modelo = modelo

        self.agregar_empleado_button = tk.Button(root, text="Agregar Empleado", command=self.agregar_empleado)
        self.agregar_empleado_button.pack()

        self.calcular_salario_button = tk.Button(root, text="Calcular Salario Total del Departamento", command=self.calcular_salario_total)
        self.calcular_salario_button.pack()

        self.listar_empleados_button = tk.Button(root, text="Listar Empleados por Departamento", command=self.listar_empleados)
        self.listar_empleados_button.pack()

    def agregar_empleado(self):
        nombre = "Marlon"  
        ID = "12345" 
        salario = 50000  
        departamento_nombre = "Ventas"  

        departamento_existente = None
        for departamento in self.modelo.departamentos:
            if departamento.nombre == departamento_nombre:
                departamento_existente = departamento
                break

        if not departamento_existente:
            departamento_existente = Departamento(departamento_nombre, "D" + str(len(self.modelo.departamentos) + 1))
            self.modelo.agregar_departamento(departamento_existente)

        empleado = Empleado(nombre, ID, salario, departamento_existente)
        departamento_existente.agregar_empleado(empleado)

    def calcular_salario_total(self):
        departamento_nombre = "Ventas"  

        for departamento in self.modelo.departamentos:
            if departamento.nombre == departamento_nombre:
                salario_total = departamento.calcular_salario_total()
                print(f"El salario total del departamento {departamento.nombre} es: ${salario_total}")
                break

    def listar_empleados(self):
        departamento_nombre = "Ventas"  

        for departamento in self.modelo.departamentos:
            if departamento.nombre == departamento_nombre:
                print(f"Empleados en el departamento {departamento.nombre}:")
                for empleado in departamento.empleados:
                    print(f"Nombre: {empleado.nombre}, ID: {empleado.ID}, Salario: ${empleado.salario}")
                break

if __name__ == "__main__":
    root = tk.Tk()
    modelo = Modelo()
    vista = Vista(root, modelo)
    root.mainloop()
