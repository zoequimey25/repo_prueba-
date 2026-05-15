def pedir_entero(n:int)->int:
    n=int(input("Ingrese un numero entero: "))
    return n
def pedir_flotante(n:float)->float:
    n=float(input("Ingrese un numero flotante: "))
    return n
def pedir_string(s:str)->str:
    s=input("Ingrese un texto: ")
    return s
def area_rectangulo(base:float, altura:float)->float:
    area=base*altura
    return area
def area_circulo(radio:float)->float:
    area=3.14*radio**2
    return area
def par_impar(n:int)->str:
    if n%2==0:
        print("par")
    else:
        print("impar")

def par_impar_bool(n:int)->bool:
    if n%2==0:
        return True
    else:
        return False
|