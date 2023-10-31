import tkinter as tk
from modelo import Modelo, Estudiante, Profesor, Curso

class Vista:
    def __init__(self, root, modelo):
        self.root = root
        self.root.title("Sistema de Gestión de Estudiantes y Profesores")
        self.modelo = modelo

        self.matricular_estudiante_button = tk.Button(root, text="Matricular Estudiante en Curso", command=self.matricular_estudiante)
        self.matricular_estudiante_button.pack()

        self.asignar_profesor_button = tk.Button(root, text="Asignar Profesor a Curso", command=self.asignar_profesor)
        self.asignar_profesor_button.pack()

        self.calcular_promedio_button = tk.Button(root, text="Calcular Promedio de Estudiante", command=self.calcular_promedio)
        self.calcular_promedio_button.pack()

    def matricular_estudiante(self):
        estudiante_nombre = "Jonathan Esteven"  
        estudiante_identificacion = "12345"  
        estudiante_carrera = "Informática"  
        estudiante_promedio = 9.0  

        nuevo_estudiante = Estudiante(estudiante_nombre, estudiante_identificacion, estudiante_carrera, estudiante_promedio)
        self.modelo.agregar_estudiante(nuevo_estudiante)

        print(f"Estudiante {estudiante_nombre} matriculado en la carrera {estudiante_carrera}.")

    def asignar_profesor(self):
        curso_nombre = "Informatica Basica"  
        profesor_nombre = "Cristiano Ronaldo"  
        profesor_identificacion = "67890"  
        profesor_departamento = "Informática"  
        profesor_salario = 60000  

        nuevo_profesor = Profesor(profesor_nombre, profesor_identificacion, profesor_departamento, profesor_salario)
        nuevo_curso = Curso(curso_nombre, nuevo_profesor)
        self.modelo.agregar_profesor(nuevo_profesor)
        self.modelo.agregar_curso(nuevo_curso)

        print(f"Profesor {profesor_nombre} asignado al curso {curso_nombre} en el departamento {profesor_departamento}.")

    def calcular_promedio(self):
        estudiante_nombre = "Jonathan Esteven" 
        estudiante_encontrado = None

        for estudiante in self.modelo.estudiantes:
            if estudiante.nombre == estudiante_nombre:
                estudiante_encontrado = estudiante
                break

        if estudiante_encontrado:
            promedio = estudiante_encontrado.promedio
            print(f"Promedio de {estudiante_nombre}: {promedio}")
        else:
            print(f"El estudiante {estudiante_nombre} no existe.")

if __name__ == "__main__":
    root = tk.Tk()
    modelo = Modelo()
    vista = Vista(root, modelo)
    root.mainloop()
