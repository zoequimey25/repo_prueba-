for n in range (1,11):
    print(n)

for n in range (10,0,-1):
    print(n)
numero= int(input("Ingrese un numero a contar: "))
for n in range(0,numero+1):
    print(n)
n=int(input("Ingrese un numero a multiplicar: "))
for j in range (0,11):
    print (f"{n} x {j} = {n*j}")

sum=0   
prom=0
for n in range (10):

    numero=input("Coloque un numero a sumar y promediar, o 0 para finalizar: ")
    sum+=int(numero)
    if numero=="0":
        break
prom=sum/n
print(f"La suma es: {sum}")
print(f"El promedio es: {prom}")

for n in range (1,11,1):
    if n%3 == 0:
        print (n ,"es multiplo de 3")

n = int(input("pon numero para piramide: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()


numero = int(input("Ingrese un numero: "))
contador_divisores = 0
for i in range(1, numero + 1):
    if numero % i == 0:
        print(i, end=" ")
        print("es divisor de", numero)
        contador_divisores += 1
        print()
print("La cantidad de divisores encontrados es:", contador_divisores)
