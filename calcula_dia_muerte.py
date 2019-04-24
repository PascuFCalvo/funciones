

import datetime
import random

#constantes

AVERAGE_LIFESPAN = 80

SMOKER_PENALTY = 10
DRINKER_PENALTY = 10
SEDENTARY_PENALTY = 10

def print_with_underscores(message):
    print(message)
    print(len(message) * "-")

def ask_yes_or_not(message):
    response = None
    while response != "S" and response != "N":
        response = input (message + " [S/N]")
    return response == "S"

#ahora vamos a asignar que la esperanza de vida no sea fija 80 importando random
#randint genera un entero aleatorio dentro del rango que le das

base_lifespan = random.randint((AVERAGE_LIFESPAN / 1.5), AVERAGE_LIFESPAN)

#otra forma de hacerlo seria con random.random(), que te devuelve un numero aleatorio entre 0 y 1
#base_lifespan = random.random() * AVERAGE_LIFESPAN / 2 + AVERAGE_LIFESPAN / 2


print_with_underscores("Cuanto te queda de vida: ")
print("responde a estas preguntas: ")

birthdate = input("fecha nacimiento (formato: dd/mm/aaaa?: ")

#lo convierte a formato fecha es decir con strprtime le dices "te paso esta string con este formato, pasalo a fecha"

birthdate = datetime.datetime.strptime(birthdate, "%d/%m/%Y")

years_lost = 0


if  ask_yes_or_not("¿Fumas?"):
    years_lost += SMOKER_PENALTY
if ask_yes_or_not("¿Bebes?"):
    years_lost += DRINKER_PENALTY
if not ask_yes_or_not("¿Haces deporte?"):
    years_lost += SEDENTARY_PENALTY

lifespan = AVERAGE_LIFESPAN - years_lost
deathday = birthdate + datetime.timedelta(days=lifespan*365)

#datetime.datetime.now() es la fecha de hoy

days_to_death = deathday - datetime.datetime.now()

#strftime, te paso esta fecha, pasamela a este formato (la operacion inversa)

print("te vas a morir en  {}, te quedan {} dias:".format(deathday.strftime("%d/%m/%Y"), days_to_death.days))






