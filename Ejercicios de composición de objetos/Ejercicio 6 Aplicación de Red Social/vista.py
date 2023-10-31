import tkinter as tk


class InterfazUsuarioRedSocial:
    def __init__(self, ventana, usuario):
        self.ventana = ventana
        self.ventana.title("Red Social")
        self.usuario_actual = usuario

        self.etiqueta = tk.Label(ventana, text="Bienvenido a la Red Social")
        self.etiqueta.pack()

        self.boton_amigo = tk.Button(ventana, text="Agregar Amigo", command=self.agregar_amigo)
        self.boton_amigo.pack()

        self.boton_publicacion = tk.Button(ventana, text="Crear Publicación", command=self.crear_publicacion)
        self.boton_publicacion.pack()

        self.boton_like = tk.Button(ventana, text="Dar Like", command=self.dar_like)
        self.boton_like.pack()

        self.boton_comentario = tk.Button(ventana, text="Comentar", command=self.comentar)
        self.boton_comentario.pack()

    def agregar_amigo(self):
        amigo = input("Introduce el nombre del amigo: ")
        self.usuario_actual.agregar_amigo(amigo)

    def crear_publicacion(self):
        contenido = input("Introduce el contenido de la publicación: ")
        publicacion = self.usuario_actual.crear_publicacion(contenido)
        print(f'Has creado una nueva publicación: "{contenido}".')

    def dar_like(self):
        print("Has dado like a la publicación.")

    def comentar(self):
        comentario = input("Introduce tu comentario: ")
        print(f'Has comentado: "{comentario}".')

if __name__ == "__main__":
    ventana = tk.Tk()
    usuario = Usuario("usuario1", "contraseña1")  # Puedes inicializar con los datos que desees
    app = InterfazUsuarioRedSocial(ventana, usuario)
    ventana.mainloop()
