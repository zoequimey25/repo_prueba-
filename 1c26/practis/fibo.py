#f(n) = f(n-1) + f(n-2)
def secuencia_fibonacci(n):
    if n <= 1:
        return n
    else:
        return(secuencia_fibonacci(n-1) + secuencia_fibonacci(n-2))

secuencia = int(input("Ingrese un numero: "))
while True:
    if secuencia <= 0:
        secuencia = int(input("Ingrese un numero: "))
    else:
        print("Fibonacci secencia:" )
        for i in range(secuencia):
            # print(secuencia_fibonacci(i))
            print(f"F{secuencia} = {secuencia_fibonacci(i)}")
        break