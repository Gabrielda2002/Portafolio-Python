class Estudiante:
    def __init__(self, nombre, identificacion, carrera, promedio):
        self.nombre = nombre
        self.identificacion = identificacion
        self.carrera = carrera
        self.promedio = promedio

class Profesor:
    def __init__(self, nombre, identificacion, departamento, salario):
        self.nombre = nombre
        self.identificacion = identificacion
        self.departamento = departamento
        self.salario = salario

class Curso:
    def __init__(self, nombre, profesor):
        self.nombre = nombre
        self.profesor = profesor
        self.estudiantes = []

    def matricular_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

class Modelo:
    def __init__(self):
        self.estudiantes = []
        self.profesores = []
        self.cursos = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def agregar_profesor(self, profesor):
        self.profesores.append(profesor)

    def agregar_curso(self, curso):
        self.cursos.append(curso)
