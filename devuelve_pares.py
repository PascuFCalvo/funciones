def devuelve_pares(valor):
    lista_pares = []
    posicion = 0
    while posicion < len(valor):
        if (int(valor[posicion])) % 2 == 0:
         lista_pares.append(valor[posicion])
         posicion += 1
        else:
            posicion += 1
    return lista_pares

fin = 0
while fin != 1:


    pares = []
    lista_rango = []

    lista_rango = input("dame una lista de numeros de la siguiente manera X X X X...: ")

    lista_rango = lista_rango.split()

    pares = devuelve_pares(lista_rango)


    print (pares)
    fin_usuario = input("Has terminado: si/no: ")
    if fin_usuario == "si":
        fin = 1