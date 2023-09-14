while True:
    print('''Por favor ingrese el numero dependiendo de la accion que quieras realizar
          1. Hallar numero primo.
          2. verificar si es par o impar
          3. el dia de la semana correspodiente a un numero de 1 a 7.
          4. El mes del año correcpodiente a un numero entre 1 y 12
          5. Acomodar 3 numeros de menor a mayor.
          6. Acomodar 3 numeros de mayor a menor.
          7. mostrar numeros de menor a mayor en distintas lineas y si hay numeros iguales se pintan en la misma linea.
          8. Que pida una letra y detecte si es una Vocal.''')
    option=int(input())
    match option:
        case 1:
            def es_primo(numero):
                if numero <= 1:
                    return False
                elif numero <= 3:
                    return True
                elif numero%2 == 0 or numero %3 ==0:
                    return False
                i = 5
                while i * i <= numero:
                    if numero % i == 0 or numero %(i+2) ==0: