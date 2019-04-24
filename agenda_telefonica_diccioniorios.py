

salida = False
#añadiendo el diccionario
agenda = dict()


while not salida:
    nombre = ""
    numero = ""
    accion = input("¿Que quieres hacer) [Añadir numero(A) / Consular numero (C)] / Salir (S)]:  ")

    #accion añadir
    if accion == "A":
        print("Vamos a añadir un numero de telefono:")
        nombre = input("Nombre: ")
        numero = input("Numero: ")
        agenda[nombre] = numero

    #accion consultar
    elif accion == "C":
        print("Vamos a consultar un numero:")
        nombre = input("De quien quieres saber el numero: ")
        print(agenda[nombre])

    #accion salir
    elif accion == "S":
        salida = True