


frase_a_contar = input("Escribe una frase: ")
frase_a_contar = list(frase_a_contar.split())

aparece_palabra = dict()
for posicion in frase_a_contar:
    if posicion in aparece_palabra:
        aparece_palabra[posicion] += 1
    else:
        aparece_palabra[posicion] = 1


for i in aparece_palabra:
    print("la palabra {} aparece {} veces: ".format((i),(aparece_palabra[i])))



