class ManejoDatos:
    def __init__(self):
        self.notas= {}

    def asignar_notas(self):
        while True:
            print("Ingresar el nombre del estudiante.")
            nombre = input()
            
            if nombre =="salir":
                break
            try:
                print("Por favor ingrese las calificaciones del estudiante.")
                calificacion = input()
            except ValueError:
                print("Por favor ingrese un numero valido para la calificacion.")
                continue
            self.notas[nombre]= calificacion
        print("se asigno correctamente.")
    
    def modificar(self):
        print("Por favor ingrese el nombre del estudiante cuya calificacion desea modificar.")
        nombre= input()
        if nombre in self.notas:
            print(f"La calificacion actual es {self.notas[nombre]}")
            try:
                print("Ingrese la nueva calificacion.")
                nueva_calificacion = float(input())
                self.notas[nombre] = nueva_calificacion
                print(f"La calificacion del estudiante {nombre} ha sido actualizado.")
            except ValueError:
                print(f"Ha ocurrido un error en la actualizacion de la calificacion de {nombre}")
            
        else:
            print("No se encontro el registro.")

    def eliminar(self):
        print("Ingrese el nombre del estudiante que desea eliminar.")
        nombre_eliminar =input()
        if nombre_eliminar in self.notas:
            del self.notas[nombre_eliminar]
            print(f"El estudiante {nombre_eliminar} ha sido eliminado.")
        else:
            print(f"El estudiante {nombre_eliminar} no se ha podido eliminar.")
