print ("Bienvenido a viajando por el pais")
fecha = input("¿en que fecha va a viajar?" \
" INVIERNO, VERANO, OTOÑO, o PRIMAVERA.(responda en mayusculas)  ")
match fecha:
    case "INVIERNO":
        print("Se viaja a: Bariloche.")
        print ("no se viaja a: Mar del plata, Cataratas.")
    case "VERANO":
        print ("se viaja a Mar de plata, Cataratas.")
        print ("no se viaja a Bariloche.")
    case "OTOÑO":
        print ("Se viaja a Bariloche, Mar del plata, y Cataratas.")
    case "PRIMAVERA":
        print ("Se viaja a Mar del plata y cataratas.")
        print ("No se viaja a Bariloche.")
    case _: 
        print ("porfavor coloque una fecha valida")
        print ("en mayusculas y sin tildes.")