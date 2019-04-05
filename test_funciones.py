
# Vamos a crear la variable confirmacion para
# evitar tener que repetir el proceso de confirmacion

#
#confirmacion = False

#while not confirmacion:

#    nombre = input("como te llamas?")
#    confirmar = input("Has dicho {}, estas seguro (si/no)".format(nombre))
#    if confirmar == "si":
#        confirmacion = True
#
#
#print("Has asegurado que tu nomnbre es {}".format(nombre))

#confirmacion = False

#while not confirmacion:
#
#    numero = input("Dime un numero")
#    confirmar = input("Has dicho {}, estas seguro (si/no)".format(numero))
#    if confirmar == "si":
#        confirmacion = True

#print("Has confirmado que el numero es {}".format(numero))



def input_confirmacion(pregunta):
    confirmacion = False
    while not confirmacion:
        valor =input(pregunta)
        confirmar = input("Has dicho {}, estas seguro (si/no)".format(valor))
        if confirmar == "si":
            confirmacion = True
    return valor

nombre = input_confirmacion("¿Como te llamas?")
print("{}".format(nombre))

numero = input_confirmacion("Dime un numero")
print("{}".format(numero))


