cont = 10
edad = 0
ia=0
rv/ra=0
oit=0

print("Hola, comencemos con la encuesta UTN Technologies  ")
while cont > 0:
    cont-=1
    nombre=input("Coloque su nombre:  ")
    edad=input("coloque su edad:  ")
    if edad <= "17":
        print("Debe ser mayor de 18, acceso denegado.")
        break 
    elif edad > "99":
        print("ingrese su edad real.")
        edad=input("Coloque su edad:  ")
    
    genero = input("Coloque el numero. Masculino 1, Femenino 2, Otro 3:  ")
    if genero <="0" or genero >="4":
        genero=input("Coloque un numero valido.")

    print ("Inteligencia Artificial (IA) = 1")
    print("Realidad Virtual/Aumentada (RV/RA) = 2")
    print("Internet de las Cosas (IOT) = 3")
    tecnologia=input("Registre su voto con el numero correcto.") 
    if tecnologia <="0" or tecnologia >="4":
        tecnologia=input("Coloque un numero valido.")
    if tecnologia == "1" and genero == "1":
        ia+=1
    elif tecnologia == "2":
        rv/ra+=1
    elif tecnologia == "3":
        oit+=1
