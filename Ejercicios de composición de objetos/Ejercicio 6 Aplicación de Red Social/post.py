
class Publicacion:
    def __init__(self, usuario, contenido):
        self.usuario = usuario
        self.contenido = contenido
        self.likes = 0
        self.comentarios = []

    def dar_like(self):
        self.likes += 1
        print(f'{self.usuario.nombre_usuario} dio like a la publicación: "{self.contenido}".')

    def comentar(self, comentario):
        self.comentarios.append(comentario)
        print(f'{self.usuario.nombre_usuario} comentó en la publicación: "{self.contenido}": "{comentario}".')
