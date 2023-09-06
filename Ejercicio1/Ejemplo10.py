def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib1, fib2 = 0, 1
        for _ in range(2, n + 1):
            fib1, fib2 = fib2, fib1 + fib2
        return fib2

n = int(input("Ingrese el valor de n para obtener el término n-ésimo de Fibonacci: "))
resultado = fibonacci(n)
print(f"El término {n}-ésimo de la serie Fibonacci es {resultado}")
