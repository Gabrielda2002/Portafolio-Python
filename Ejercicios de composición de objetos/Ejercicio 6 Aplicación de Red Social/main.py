import tkinter as tk
from user import Usuario
from post import Publicacion
from vista import InterfazUsuarioRedSocial

if __name__ == "__main__":
    ventana = tk.Tk()
    usuario = Usuario("usuario1", "contraseña1")  # Puedes inicializar con los datos que desees
    app = InterfazUsuarioRedSocial(ventana, usuario)
    ventana.mainloop()
