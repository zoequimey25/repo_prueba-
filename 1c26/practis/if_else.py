#promedio generador
print( "hola bienvenido al generador de promedio",
"este caso para calcular 2 notas",
"tomando el 10 como maximo")
nota1 = float(input("Coloque en numero la nota 1: "))
nota2= float(input("Ahora coloque en numero la nota 2: "))
nota3= float(input("Por ultimo coloque la nota 3: "))
nota =( nota1+nota2+nota3)/3 
if nota >=6:
    print ("Promocion directa con nota",nota)
elif nota== 4 or nota== 5:
    print ("Aprobado, la nota es de", nota)
else:
    print("Desaprobaste con nota", nota)