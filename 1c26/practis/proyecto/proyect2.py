def ingreso(usuarios):
    print("bienvenido")

    usuario = input("Ingrese usuario: ")

    if usuario in usuarios:
       
        clave = int(input("Ingrese su clave: "))
        return validar_clave(usuario, clave, usuarios)
    else:
        print("usuario no existe, crear uno nuevo")

        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")

        sugerido = nombre[0] + apellido
        print("Usuario sugerido:", sugerido)

        opcion = input("¿Querés usar este usuario? (s/n): ")

        if opcion == "s":
            usuario = sugerido
        else:
            usuario = input("Cree un nombre de usuario: ")

        clave = int(input("Cree una clave numérica: "))
        usuarios[usuario] = clave

        print("Usuario creado")

        return usuario


def validar_clave(usuario, clave, usuarios):
    if usuarios[usuario] == clave:
        print("Acceso correcto", usuario)
        return usuario
    else:
        print("error clave incorrecta")
        clave = int(input("Ingrese su clave: "))
        return validar_clave(usuario, clave, usuarios)  # 👈 recursividad


def menu(usuario):
    opcion = ""

    while opcion != "6":
        print("bienvenida", usuario)
        print("Proyectos 1")
        print("Tablas 2")
        print("Variables 3")
        print("Mostrar 4")
        print("Estadistica 5")
        print("Salir 6")

        opcion = input("Coloque el numero de la opcion: ")

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
                print("Saliendo...")
            case _:
                print("error de opcion")



usuarios = {}

usuario = ingreso(usuarios)
menu(usuario)