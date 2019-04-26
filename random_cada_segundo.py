from time import sleep
import random

frase_alegres = ["hola bebe", "bien", "yuju", "yupi"]
nombres_de_muebles = ["mesa","silla","comoda","armario"]
nombres_de_bebidas = ["vodka","cola","fanta","agua"]
nombres_de_comidas = ["pizza", "pasta", "carne", "pescado"]
frases_de_odio = ["mentira", "meeeeentiroso", "te odio"]
frase_absurdas = ["que calvario","modernoooo","ai dios miooo"]
nombres_animales = ["tigre","leon","vaca","pollo"]
frase_motivacionales = ["tu puedes","eres mejor que ayer","mrwonderfull"]
sonidos_animales = ["muuu", "miau", "guau guau", "cua cua cua"]
frases_tristes = ["vas a morir", "cancer de sida", "llueve y es puente"]

INTERVALO = 1
contador_segundos = 0


while True:


    segundos_string = str(contador_segundos)
    unidades = segundos_string[-1]
    intunidades = int(unidades)


    sleep(INTERVALO)

    contador_segundos += 1

    if intunidades == 0:
        print(random.choice(frase_alegres))
    if intunidades == 1:
        print(random.choice(nombres_de_muebles))
    if intunidades == 2:
        print(random.choice(nombres_de_bebidas))
    if intunidades == 3:
        print(random.choice(nombres_de_comidas))
    if intunidades == 4:
        print(random.choice(frases_de_odio))
    if intunidades == 5:
        print(random.choice(frase_absurdas))
    if intunidades == 6:
        print(random.choice(nombres_animales))
    if intunidades == 7:
        print(random.choice(frase_motivacionales))
    if intunidades == 8:
        print(random.choice(sonidos_animales))
    if intunidades == 9:
        print(random.choice(frases_tristes))




