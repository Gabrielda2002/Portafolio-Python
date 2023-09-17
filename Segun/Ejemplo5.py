while True:
    print('''Por favor ingrese el numero dependiendo de la accion que quieras realizar
          1. Hallar numero primo.
          2. verificar si es par o impar
          3. el dia de la semana correspodiente a un numero de 1 a 7.
          4. Acomodar 3 numeros de mayor a menor.
          5. Acomodar 3 numeros de menor a mayor.
          6. mostrar numeros de menor a mayor en distintas lineas y si hay numeros iguales se pintan en la misma linea.
          7. Que pida una letra y detecte si es una Vocal.''')
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
                        return False
                    i+=0
                return True
            def principal():
                print("Ingrse un numero del 1 al 5")
                numero = int(input())
                if 1 <= numero and numero <= 5:
                    if es_primo(numero):
                        print(f"{numero} Es un numero primo")
                    else:
                        print(f"{numero} No es un numero primo.")
                else:
                    print("Por favor ingrese un numero valido del 1 al 5.")
                
            principal()
            break
        case 2:
            def numero_par(numero):
                return numero %2 ==0
            def principal2():
                print("Ingrese un numero.")
                numero=int(input())
                if numero_par(numero):
                    print(f"{numero } es un numero par.")
                else:
                    print(f"{numero} no es par.")
            principal2()
            break
        case 3:
            while True:

                print("digite un numero de 1 a 7")
                num=int(input())
                match num:
                    case 1:
                        print("Lunes")
                        break
                    case 2:
                        print("Martes")
                        break
                    case 3:
                        print("Miercoles")
                        break
                    case 4:
                        print("Jueves")
                        break
                    case 5:
                        print("Viernes")
                        break
                    case 6:
                        print("Sabado")
                        break
                    case 7:
                        print("Domingo")
                        break
                    case defecto:
                        print("Error! Ingrese una opcion valida")
            break
        case 4:
            def principal3():
                print("Por favor ingrese un numero.")
                num1=float(input())
                print("Por favor ingrese un segundo numero.")
                num2=float(input())
                print("Por favor ingrese un tercer numero.")
                num3=float(input())

                numeros_ordenados = sorted([num1, num2, num3], reverse=True)
                print("Los numeros ordenados de mayor a menor:")
                for numero in numeros_ordenados:
                    print(numero)
            principal3()
            break
        case 5:
            def principal4():
                print("Por favor ingrese un numero.")
                num1=float(input())
                print("Por favor ingrese un segundo numero.")
                num2=float(input())
                print("Por favor ingrese un tercer numero.")
                num3=float(input())

                numeros_ordenados = sorted([num1, num2, num3], reverse=True)
                print("Los numeros ordenados de mayor a menor:")
                for numero in numeros_ordenados:
                    print(numero)
            principal4()
            break
        case 6:
            def principal5():
                print("Ingrese una serie de números separados por espacios:")
                numeros = input().split()
                
                # Convertir la entrada en una lista de números enteros
                numeros = [int(numero) for numero in numeros]
                
                # Ordenar la lista de números de menor a mayor
                numeros.sort()
                
                # Inicializar una lista para agrupar números iguales
                numeros_agrupados = []
                
                # Iterar sobre la lista de números ordenados
                for numero in numeros:
                    if not numeros_agrupados or numero != numeros_agrupados[-1][-1]:
                        numeros_agrupados.append([numero])
                    else:
                        numeros_agrupados[-1].append(numero)
                
                # Mostrar los números agrupados en líneas separadas
                for grupo in numeros_agrupados:
                    linea = " ".join(map(str, grupo))
                    print(linea)
            principal5()
            break
        case 7:
            def verificar_vocal(letra):
                vocales = ['a','e','i','o','u']

                if letra.lower() in vocales:
                    return True
                else:
                    return False
            def principal6():
                print("Por favor ingrese una letra.")
                letra = input().strip()
                if len(letra) == letra.isalpha():
                    if verificar_vocal(letra):
                        print(f"{letra} es una vocal.")
                    else:
                        print(f"{letra} no es una vocal.")
                else:
                    print("Por favor ingrese una letra.")
            principal6()
            break
        case defecto:
            print("Por favor ingrese una opcion valida.")
        




            
