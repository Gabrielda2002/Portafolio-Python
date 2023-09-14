import math

def ingresar():
    print("Por favor ingrese un numero: ")
    num1=int(input())
    print("Por favor ingrese otro numero: ")
    num2=int(input())
    return num1, num2
def minimocd(num1, num2):
    mcd = math.gcd(num1, num2)
    return mcd
    
def main():
    num1, num2 = ingresar()
    print(f"El maximo comun divisor de los numeros {num1}, {num2} es {minimocd(num1, num2)}.")
    
if __name__ == "__main__":
    main()
    
    
    







