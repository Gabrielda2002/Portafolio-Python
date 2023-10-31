from post import Publicacion

class Usuario:
    def __init__(self, nombre_usuario, contraseña):
        self.nombre_usuario = nombre_usuario
        self.contraseña = contraseña
        self.amigos = []

    def agregar_amigo(self, amigo):
        self.amigos.append(amigo)
        print(f'{self.nombre_usuario} agregó a {amigo.nombre_usuario} como amigo.')

    def crear_publicacion(self, contenido):
        return Publicacion(self, contenido)
