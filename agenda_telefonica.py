

salida = False
agenda = []


while not salida:
    accion = input("¿Que quieres hacer) [Añadir numero(A) / Consular numero (C)] / Salir (S)]:  ")

    #accion añadir
    if accion == "A":
        print("Vamos a añadir un numero de telefono:")
        nombre = input ("Nombre: ")
        numero = numero ("Numero: ")
        agenda.append([nombre, numero])

    #accion consultar
    elif accion == "C":
        print("Vamos a consultar un numero:")
        nombre = input("De quien quieres saber el numero: ")
        for nombre_numero in agenda:
            if nombre_numero[0] == nombre:
                print(nombre_numero[1])

    #accion salir
    elif accion == "S":
        salida = True