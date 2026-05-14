contador1 = 0

while contador1<10:
    contador1+= 1
    print (contador1)
contador1+=1
while contador1>1:
    contador1 -= 1
    print (contador1) 
num = 0
while num<10:
    num +=2
    if num==10:
        print("10.")
    else:
        print(num,"mas 2 es:")

num1=int(input("coloque un numero: "))
num2=int(input("coloque otro numero: "))
num3=int(input("coloque el tercer numero: "))
num4=int(input("coloque el curto numero: "))
num5=int(input("ahora el ultimo numero: "))
print (f"ahora vamos a sumar {num1}, {num2}, {num3} ,{num4} ,{num5}")
suma_total = (num1+num2+num3+num4+num5)
print (suma_total, "suma total")
promedio=suma_total/5
print("el promedio es", promedio)

notas=0
nota=0
repes=0
while 2==2:
    nota=input("ingrese su nota o (fin): ")
    if nota=="fin":
        break
    else:
        notas += int(nota)
        repes += 1
promedio = notas/repes
print(f"El promedio de las {repes} notas da: {promedio}")
