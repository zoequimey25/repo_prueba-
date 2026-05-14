bandera =1
vuelta = 0
cant_masc_ia = 0
cant_no_ia=0
empleado_mayor_edad = "0"
empleado_mayor_edad_nombre = ""
empleado_mayor_edad_tecnologia = ""  
while vuelta < 10:
    vuelta+=1
    nombre = input("Coloque su nombre:  ")
    while bandera == 1:
        edad = input("coloque su edad:  ")
        edad = edad.replace(" ", "")
        if edad < "17" or edad > "99":
            print("Debe ser mayor de 18, acceso denegado.")
        else:
            print("Edad válida. " , edad)
            bandera=0
    while bandera == 0:
        genero = input("Coloque el numero. Masculino 1, Femenino 2, Otro 3:  ")
        genero = genero.replace(" ", "")
        if genero <="0" or genero >="4":
            print("Coloque un numero valido.")
        else:
            print("Genero válido. " , genero)
            bandera=1
    while bandera ==1:
        tecnologia_elegida = input("Registre su voto con el numero correcto. Inteligencia Artificial (IA) = 1, Realidad Virtual/Aumentada (RV/RA) = 2, Internet de las Cosas (IOT) = 3:  ")
        tecnologia_elegida = tecnologia_elegida.replace(" ", "")
        if tecnologia_elegida <="0" or tecnologia_elegida >="4":
            print("Coloque un numero valido.")
        else:
            print("Tecnología válida. " , tecnologia_elegida)
            bandera=0
    if genero==1 and (tecnologia_elegida == "1" or tecnologia_elegida == "3") and (edad >= "25" and edad <= "50"):
        cant_masc_ia+=1
    if genero!=2 and (edad >"33" and edad < "40") and tecnologia_elegida != "1":
        cant_no_ia+=1
    if edad > empleado_mayor_edad:
        empleado_mayor_edad = edad
        empleado_mayor_edad_nombre = nombre
        if tecnologia_elegida == "1":
            empleado_mayor_edad_tecnologia = "Inteligencia Artificial (IA)"
        elif tecnologia_elegida == "2":
            empleado_mayor_edad_tecnologia = "Realidad Virtual/Aumentada (RV/RA)"
        elif tecnologia_elegida == "3":
            empleado_mayor_edad_tecnologia = "Internet de las Cosas (IOT)"
    bandera=1

print("Cantidad de hombres entre 25 y 50 años que eligieron IA o IOT: ", cant_masc_ia)
print("Cantidad de personas que no son mujeres, entre 33 y 40 años, que no eligieron IA: ", (cant_no_ia*100/10)   , "%")
print("Empleado de mayor edad: ", empleado_mayor_edad_nombre, " con ", empleado_mayor_edad, " años, eligio la tecnologia: ", empleado_mayor_edad_tecnologia)