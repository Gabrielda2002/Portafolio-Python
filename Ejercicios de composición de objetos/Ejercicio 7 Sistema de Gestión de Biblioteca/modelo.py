class Libro:
    def __init__(self, titulo, autor, ejemplares, genero):
        self.titulo = titulo
        self.autor = autor
        self.ejemplares = ejemplares
        self.genero = genero

class Usuario:
    def __init__(self, nombre, identificacion):
        self.nombre = nombre
        self.identificacion = identificacion
        self.libros_prestados = []

    def prestar_libro(self, libro):
        if libro.ejemplares > 0:
            self.libros_prestados.append(libro)
            libro.ejemplares -= 1
            return True
        else:
            return False

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)
            libro.ejemplares += 1
            return True
        else:
            return False

class Modelo:
    def __init__(self):
        self.libros = []
        self.usuarios = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)
        