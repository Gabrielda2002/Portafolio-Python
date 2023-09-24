from Animal import Animal
from Gato import Gato
from Gallina import Gallina


# se le solicita al usuario los datos de el animal (Gato y Gallina)
print("Por favor ingrese el nombre de el gato.")
nombre_gato = input()
print("Por favor ingrese el nombre de la Gallina.")
nombre_gallina = input()
print("por favor ingrese el color de el Gato.")
color_gato = input()
print("por favor ingrese el color de la gallina.")
color_gallina = input()
print("por favor ingrese el tipo de pelaje de el Gato.")
tipo_de_pelaje = input()
print("por favor ingrese el tipo de pelaje de la Gallina.")
pelaje_gallina = input()


#se instancia la clase Gato para asignarle los parametros del constructor y mostrarlos en pantalla
gato1 = Gato(color_gato, nombre_gato, "4", tipo_de_pelaje)
print(f'''
El nombre de el Gato es: {gato1.nombre}.
El color de el gato es de: {gato1.color}.
El gato camina en {gato1.cantidad_patas} patas.
El tipo de pelaje de el gato es {gato1.tipo_pelaje}''')

print(gato1.sonido())


gallo1 = Gallina(color_gallina, nombre_gallina, "2", pelaje_gallina)
print(f'''
El nombre de el Gato es: {gallo1.nombre}.
El color de el gato es de: {gallo1.color}.
El gato camina en {gallo1.cantidad_patas} patas.
El tipo de pelaje de el gato es {gallo1.tipo_pelaje}''')

print(gallo1.sonido())
