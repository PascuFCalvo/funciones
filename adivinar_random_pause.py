import random
import time

while True:
    numero_maquina = random.randint(1, 3)

    numero_usuario = int(input("introduce un numero del 1 al 3: "))

    print("3,2,1...")

    time.sleep(3)

    if numero_maquina == numero_usuario:
            print("HAS GANADO!!!")
    elif numero_maquina != numero_usuario:
            print("Has perdido, estaba pensando en el {}".format(numero_maquina))
