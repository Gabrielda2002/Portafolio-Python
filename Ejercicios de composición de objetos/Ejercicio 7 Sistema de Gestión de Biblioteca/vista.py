import tkinter as tk
from modelo import Modelo, Libro, Usuario

class Vista:
    def __init__(self, root, modelo):
        self.root = root
        self.root.title("Sistema de Gestión de Biblioteca")
        self.modelo = modelo

        self.agregar_libro_button = tk.Button(root, text="Agregar Libro", command=self.agregar_libro)
        self.agregar_libro_button.pack()

        self.agregar_usuario_button = tk.Button(root, text="Agregar Usuario", command=self.agregar_usuario)
        self.agregar_usuario_button.pack()

        self.prestar_libro_button = tk.Button(root, text="Prestar Libro", command=self.prestar_libro)
        self.prestar_libro_button.pack()

        self.devolver_libro_button = tk.Button(root, text="Devolver Libro", command=self.devolver_libro)
        self.devolver_libro_button.pack()

        self.buscar_libro_autor_button = tk.Button(root, text="Buscar Libro por Autor", command=self.buscar_libro_por_autor)
        self.buscar_libro_autor_button.pack()

        self.buscar_libro_genero_button = tk.Button(root, text="Buscar Libro por Género", command=self.buscar_libro_por_genero)
        self.buscar_libro_genero_button.pack()

    def agregar_libro(self):
        titulo = "Libro A"  # Reemplaza con la entrada del usuario
        autor = "Autor X"  # Reemplaza con la entrada del usuario
        ejemplares = 5  # Reemplaza con la entrada del usuario
        genero = "Ficción"  # Reemplaza con la entrada del usuario

        nuevo_libro = Libro(titulo, autor, ejemplares, genero)
        self.modelo.agregar_libro(nuevo_libro)

        print(f"Libro {titulo} agregado a la biblioteca. Autor: {autor}, Género: {genero}.")

    def agregar_usuario(self):
        nombre = "Juan Pérez"  # Reemplaza con la entrada del usuario
        identificacion = "12345"  # Reemplaza con la entrada del usuario

        nuevo_usuario = Usuario(nombre, identificacion)
        self.modelo.agregar_usuario(nuevo_usuario)

        print(f"Usuario {nombre} agregado a la biblioteca. Identificación: {identificacion}.")

    def prestar_libro(self):
        usuario_nombre = "Juan Pérez"  # Reemplaza con el nombre del usuario
        libro_titulo = "Libro A"  # Reemplaza con el título del libro

        usuario_encontrado = None
        libro_encontrado = None

        for usuario in self.modelo.usuarios:
            if usuario.nombre == usuario_nombre:
                usuario_encontrado = usuario
                break

        for libro in self.modelo.libros:
            if libro.titulo == libro_titulo:
                libro_encontrado = libro
                break

        if usuario_encontrado and libro_encontrado:
            if usuario_encontrado.prestar_libro(libro_encontrado):
                print(f"{usuario_nombre} ha prestado el libro {libro_titulo}.")
            else:
                print(f"No hay ejemplares disponibles de {libro_titulo}.")
        else:
            if not usuario_encontrado:
                print(f"El usuario {usuario_nombre} no existe.")
            if not libro_encontrado:
                print(f"El libro {libro_titulo} no existe.")

    def devolver_libro(self):
        usuario_nombre = "Juan Pérez"  # Reemplaza con el nombre del usuario
        libro_titulo = "Libro A"  # Reemplaza con el título del libro

        usuario_encontrado = None
        libro_encontrado = None

        for usuario in self.modelo.usuarios:
            if usuario.nombre == usuario_nombre:
                usuario_encontrado = usuario
                break

        for libro in self.modelo.libros:
            if libro.titulo == libro_titulo:
                libro_encontrado = libro
                break

        if usuario_encontrado and libro_encontrado:
            if usuario_encontrado.devolver_libro(libro_encontrado):
                print(f"{usuario_nombre} ha devuelto el libro {libro_titulo}.")
            else:
                print(f"{usuario_nombre} no tiene prestado el libro")
