from tkinter import Tk
from tkinter import Frame
from tkinter import Label
from tkinter import Entry
from tkinter import StringVar
from tkinter import Button

ventana = Tk()
ventana.title("Aplicacion")
User_name = StringVar()
Last_name = StringVar()
year = StringVar()
Gender = StringVar()
n_identidad = StringVar()
funcionalidad_general = StringVar()
problemas = StringVar()
funcion_monitor = StringVar()
experiencia = StringVar()
utilidad = StringVar()



contenedor = Frame()
# contenedor.grid(column=0,row=0)
contenedor.pack()
contenedor.config(bg="pink")

contenedor2 = Frame()
# contenedor.grid(column=0,row=0)
contenedor2.pack()
contenedor2.config(bg="white")

contenedor3=Frame()
contenedor3.pack()
contenedor3.config(bg="white")

contenedor4=Frame()
contenedor4.pack()
contenedor4.config(bg="white")

contenedor5=Frame()
contenedor5.pack()
contenedor5.config(bg="white")

contenedor6=Frame()
contenedor6.pack()
contenedor6.config(bg="white")

contenedor7=Frame()
contenedor7.pack()
contenedor7.config(bg="white")

contenedor8=Frame()
contenedor8.pack()
contenedor8.config(bg="white")

contenedor9=Frame()
contenedor9.pack()
contenedor9.config(bg="white")

contenedor10=Frame()
contenedor10.pack()
contenedor10.config(bg="white")

# contenedor3=Frame()
# contenedor3.pack()
# contenedor3.config(bg="white")



p1 = Label(contenedor, text="Nombre" )
p2 = Label(contenedor2, text="Apellido")
p3 = Label(contenedor3,text="Edad")
p4 = Label(contenedor4, text="Genero")
p5 = Label(contenedor5, text="N. Identidad")
p6 = Label(contenedor6, text="¿el PC funciona correctamente?")
p7 = Label(contenedor7, text="¿Ha tenido problemas con el producto?")
p8 = Label(contenedor8, text="¿El monitor a presentado alguna falla?")
p9 = Label(contenedor9, text="¿Cual es su experiencia con el productor?")
p10 = Label(contenedor10, text="¿Para que utiliza el producto?")
p1.pack()
p2.pack()
p3.pack()
p4.pack()
p5.pack()
p6.pack()
p7.pack()
p8.pack()
p9.pack()
p10.pack()
p1.config(bg="pink")




R1 = Entry(contenedor)
R1.pack()
R2= Entry(contenedor2)
R2.pack()
R3 = Entry(contenedor3)
R3.pack()
R4 = Entry(contenedor4)
R4.pack()
R5 = Entry(contenedor5)
R5.pack()
R6 = Entry(contenedor6)
R6.pack()
R7 = Entry(contenedor7)
R7.pack()
R8 = Entry(contenedor8)
R8.pack()
R9 = Entry(contenedor9)
R9.pack()
R10 = Entry(contenedor10)
R10.pack()
p1.config(bg="pink")

def tomar_datos():
    pass

boton = Button(text="Enviar", command=tomar_datos)
# boton.grid(column=0, row=1)
boton.pack()

def Datos():
    Rnombre = User_name.get()
    Rapellido = Last_name.get()
    Raños = year.get()
    Rgenero = Gender.get()
    Rn_identidad = n_identidad.get()
    Rfuncionalidad = funcionalidad_general.get()
    Rfuncion_monitor = funcion_monitor.get()
    Rproblemas = problemas.get()
    Rexperiencia = experiencia.get()
    Rutilidad = utilidad.get()

def Datos():
    Rnombre = User_name.set()
    Rapellido = Last_name.set()
    Raños = year.set()
    Rgenero = Gender.set()
    Rn_identidad = n_identidad.set()
    Rfuncionalidad = funcionalidad_general.set()
    Rfuncion_monitor = funcion_monitor.set()
    Rproblemas = problemas.set()
    Rexperiencia = experiencia.set()
    Rutilidad = utilidad.set()

ventana.mainloop()