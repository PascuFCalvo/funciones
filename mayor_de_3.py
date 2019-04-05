

def mayor_de_tres(primero, segundo, tercero):
    mayor = 0

    if primero > mayor:
        mayor = primero
    if segundo > mayor:
        mayor = segundo
    if tercero > mayor:
        mayor = tercero

    return mayor


fin = 0
while fin != 1:

    uno = int(input("dame el primer numero:"))
    dos = int(input("dame el segundo numero:"))
    tres = int(input("dame el tercer numero:"))

    numero_mayor = mayor_de_tres(uno, dos, tres)

    print (numero_mayor)
    fin_usuario = input("Has terminado_ Si/No: ")
    if fin_usuario == "Si":
        fin = 1




