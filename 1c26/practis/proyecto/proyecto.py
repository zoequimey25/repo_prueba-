usuario = ""
clave = ""
opcion = ""


print ("bienvenido")
  
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")

  
sugerido = nombre[0] + apellido
print("Usuario sugerido:", sugerido)

opcion = input("¿Querés usar este usuario? (s/n): ")
if opcion == "s":
        usuario = sugerido
else:
    usuario = input("Cree un nombre de usuario: ")
    clave = int(input("cree una clave numerica: "))

clave1 = int(input(f"ingrese su clave {usuario}:  "))
  
while clave != clave1:
    print ("error clave incorrecta")
    clave1 =  input(f"ingrese su clave {usuario}:  ")
print ("Acceso correcto",usuario)

while opcion != "6":
    print("Proyectos 1")
    print("Tablas 2")
    print("Variables 3")
    print("Mostrar 4")
    print("Estadistica 5")
    print("Salir 6")
    
    opcion = input("Coloque el numero de la opcion que corresponda: ")
    match opcion:
        case "1":
            print("Proyectos")
        case "2":
            print("Tablas")
        case "3":
            print("Variables")
        case "4":
            print("datos")
        case "5":
            print("Estadísticas")
        case "6":
            print("Ejecutando salir")
        case _:
            print("error de opcion")

