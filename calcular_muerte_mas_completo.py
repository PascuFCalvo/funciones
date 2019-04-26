import datetime
import random
import msvcrt

#constantes

AVERAGE_LIFESPAN = 80

SMOKER_PENALTY = 1.5
DRINKER_PENALTY = 1
SEDENTARY_PENALTY = 0.5

def print_with_underscores(message):
    print(message)
    print(len(message) * "-")

#ahora vamos a asignar que la esperanza de vida no sea fija 80 importando random
#randint genera un entero aleatorio dentro del rango que le das

edad_media = random.randint((AVERAGE_LIFESPAN/1.25), AVERAGE_LIFESPAN)

#otra forma de hacerlo seria con random.random(), que te devuelve un numero aleatorio entre 0 y 1
#base_lifespan = random.random() * AVERAGE_LIFESPAN / 2 + AVERAGE_LIFESPAN / 2

print_with_underscores("Cuanto te queda de vida: ")
print("responde a estas preguntas: ")

birthdate = input("fecha nacimiento (formato: dd-mm-aaaa?): ")
birthdate = datetime.datetime.strptime(birthdate, "%d-%m-%Y")


penalizacion_fumador = 0
penalizacion_bebedor = 0
penalizacion_sedentario = 0



variable_fumador = int(input("¿Fumas: ? 1=No, 2=Muy poco, 3=A veces, 4=A menudo, 5=A diario, 6=Mucho: "))

if variable_fumador == 1:
    penalizacion_fumador = SMOKER_PENALTY
if variable_fumador == 2:
    penalizacion_fumador = SMOKER_PENALTY * 1.2
if variable_fumador == 3:
    penalizacion_fumador = SMOKER_PENALTY * 1.4
if variable_fumador == 4:
    penalizacion_fumador = SMOKER_PENALTY * 1.6
if variable_fumador == 5:
    penalizacion_fumador = SMOKER_PENALTY * 1.8
if variable_fumador == 6:
    penalizacion_fumador = SMOKER_PENALTY * 2

variable_bebedor = int(input("¿Bebes: ? 1=No, 2=Muy poco, 3=A veces, 4=A menudo, 5=A diario, 6=Mucho: "))

if variable_bebedor == 1:
    penalizacion_bebedor = DRINKER_PENALTY
if variable_bebedor == 2:
    penalizacion_bebedor = DRINKER_PENALTY * 1.2
if variable_bebedor == 3:
    penalizacion_bebedor = DRINKER_PENALTY * 1.4
if variable_bebedor == 4:
    penalizacion_bebedor = DRINKER_PENALTY * 1.6
if variable_bebedor == 5:
    penalizacion_bebedor = DRINKER_PENALTY * 1.8
if variable_bebedor == 6:
    penalizacion_bebedor = DRINKER_PENALTY * 2

variable_sedentario = int(input("Haces deporte: ? 1=No, 2= 1-2 veces por semana, 2= 3-4 veces por semana, 3= A diario, 4= Deportista intenso: "))

if variable_sedentario == 1:
    penalizacion_sedentario = SEDENTARY_PENALTY * 6
if variable_sedentario == 2:
    penalizacion_sedentario = SEDENTARY_PENALTY * 5
if variable_sedentario == 3:
    penalizacion_sedentario = SEDENTARY_PENALTY * 4
if variable_sedentario == 4:
    penalizacion_sedentario = SEDENTARY_PENALTY * 3
if variable_sedentario == 5:
    penalizacion_sedentario = SEDENTARY_PENALTY * 2
if variable_sedentario == 6:
    penalizacion_sedentario = SEDENTARY_PENALTY * 1

penalizacion_total = penalizacion_sedentario + penalizacion_bebedor + penalizacion_fumador
anosvida = edad_media - penalizacion_total

#diamuerte coge la fecha de naciemiento los dias qye te he dado el calcula anterior de anosvida mediante un timedelta

diamuerte = birthdate + datetime.timedelta(days=anosvida*365)
dias_pa_morir = diamuerte - datetime.datetime.now()

week_day = diamuerte.weekday()
dia_semana = ""

if week_day == 0:
        dia_semana = "lunes"
if week_day == 1:
        dia_semana = "martes"
if week_day == 2:
        dia_semana = "miercoles"
if week_day == 3:
        dia_semana = "jueves"
if week_day == 4:
        dia_semana = "viernes"
if week_day == 5:
        dia_semana = "sabado"
if week_day == 6:
        dia_semana = "domingo"

#diamuerte es una fecha, se formatea con strftime, y de dias_para_morir es un timedelta y le puedes pedir los dias , horas , minutos etc

print("Te vas a morir el {} {}, te quedan {} dias de vida".format(dia_semana, diamuerte.strftime("%d-%m-%Y"), dias_pa_morir.days))

#aaparte añadimos que se meta en un txt

archivo_muerte = open("lamuerte","w")
archivo_muerte.write("Te vas a morir el {} {}, te quedan {} dias de vida.\n".format(dia_semana, diamuerte.strftime("%d-%m-%Y"), dias_pa_morir.days))
archivo_muerte.close()

msvcrt.getch()








