class Departamento:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo
        self.empleados = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def calcular_salario_total(self):
        salario_total = sum(empleado.salario for empleado in self.empleados)
        return salario_total

class Empleado:
    def __init__(self, nombre, ID, salario, departamento):
        self.nombre = nombre
        self.ID = ID
        self.salario = salario
        self.departamento = departamento

class Modelo:
    def __init__(self):
        self.departamentos = []

    def agregar_departamento(self, departamento):
        self.departamentos.append(departamento)
