
#le das un numero, y un rango y te comprueba que esta dentro


def rango(primero, segundo, tercero):
    esta_en_rango = ""

    if primero >= segundo and primero <= tercero:
        esta_en_rango = "si, el numero esta en rango"
    else:
        esta_en_rango = "no, el numero no esta en rango"

    return esta_en_rango


fin = 0
while fin != 1:

    numero_buscar= int(input("dame numero a buscar en el rango:"))
    primer_rango = int(input("dame el primer numero del rango:"))
    segundo_rango = int(input("dame el segundo numero del rango:"))

    rank = rango(numero_buscar,primer_rango,segundo_rango)

    print (rank)
    fin_usuario = input("Has terminado_ Si/No: ")
    if fin_usuario == "Si":
        fin = 1