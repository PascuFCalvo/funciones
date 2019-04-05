

def rango(primero,minimo,maximo):

    if primero >= minimo and primero <= maximo:
        esta_en_rango = True
    else:
        esta_en_rango = False

    return esta_en_rango

fin = 0
while fin != 1:

    lista_rango = []
    lista_rango = input("dame numero y rango y rango en el que lo quieres buscar ej:X Y Z. ")

    lista_rango = lista_rango.split()

    print("Quieres saber si {} esta entre {} y {}".format(lista_rango[0], lista_rango[1], lista_rango[2]))

    rank = rango(int(lista_rango[0]), int(lista_rango[1]), int(lista_rango[2]))


    print ("Esta en rango = {}".format(rank))
    fin_usuario = input("Has terminado: si/no: ")
    if fin_usuario == "si":
        fin = 1