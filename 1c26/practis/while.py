positivo_suma = 0
positivo_cont =0
positivo_mayor=0

negativosuma=0
negativocont=0
ingresos=0


continuar = "s"
while continuar == "s":
    num = int(input("ingrese un numero: "))
    if num>0: 
        positivo_cont+=1
        if positivo_cont == 0 or num> positivo_mayor:
            positivo_mayor=num
    elif num>=0:
        negativocont+=1    
        





continuar= input("continuamos? (s/n)") 