

#crear la funcion para calcular el largo de una lista imaginando que no existe len
#parametro nuevo "def" para definir una funcion

#y los metemos dentro de la funcion utilizando def con nombre largo y el parametro (lista)
#el parametro de dentro del parentesis puedes llamarlo como quieras
# return devuelve a quien sea que haya llamado a la funcion a largo, el resultado

def largo(lista):
    largo = 0
    for item in lista:
        largo += 1
    return largo

listanums = [2,3,4,5]

print(largo(listanums))







