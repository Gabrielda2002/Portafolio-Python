    # Definir un diccionario con información sobre los días y festivos de cada mes
meses = {
    'enero': {'dias': 31, 'festivos': 2},
    'febrero': {'dias': 28, 'festivos': 0},
    'marzo': {'dias': 31, 'festivos': 1},
    'abril': {'dias': 28, 'festivos': 2},
    'mayo': {'dias': 31, 'festivos': 2},
    'junio': {'dias': 30, 'festivos': 2},
    'julio': {'dias': 31, 'festivos': 2},
    'agosto': {'dias': 31, 'festivos': 2},
    'septiembre': {'dias': 29, 'festivos': 0},
    'octubre': {'dias': 31, 'festivos': 1},
    'noviembre': {'dias': 30, 'festivos': 1},
    'diciembre': {'dias': 31, 'festivos': 2}
}

def ingresar():
    print("Ingrese el nombre o carácter de un mes (o 'salir' para terminar): ")
    mes = input().lower()
    return mes
def logica(mes):
    if mes == 'salir':
        print("Ha salido del programa con exito.")
        return True
    if mes in meses:
        info_mes = meses[mes]
        print(f"{mes.capitalize()} tiene {info_mes['dias']} días y {info_mes['festivos']} festivos.")
        
    else:
        print("Mes no válido. Inténtelo nuevamente.")
        return False
def main():
    while True:
        mes = ingresar()
        if logica(mes):
            
            break
        # elif logica(mes) == 'salir':
        #     break
        # elif logica == False:
        #     print("Intente nuevamente.")
if __name__ == "__main__":
    main()
