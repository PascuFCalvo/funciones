from time import sleep
import random

frases_random = ["Dios mio que calvario", "por que yo", "ooootra vez no", "guayomini de la selva", "padres miopes"]

INTERVALO = 3

while True:
    sleep(INTERVALO)
    print(random.choice(frases_random))
