cont = 10
edad = 0
print("Hola, comencemos con la encuesta UTN Technologies  ")
while cont > 0:
    cont-=1
    nombre=input("Coloque su nombre:  ")
    edad=input("coloque su edad:  ")
    if edad <= "17":
        print("Debe ser mayor de 18, acceso denegado.")
    elif edad> "99" :
        print("ingrese su edad real.")
        edad=input("Coloque su edad:  ")
  
    genero = input("Coloque el numero. Masculino 1, Femenino 2, Otro 3:  ")
    print ("Inteligencia Artificial (IA) = 1")
    print("Realidad Virtual/Aumentada (RV/RA) = 2")
    print("Internet de las Cosas (IOT) = 3")
    tecnologia=input("Registre su voto con el numero correcto.") \
    