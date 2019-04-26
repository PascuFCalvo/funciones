from time import sleep
import datetime

NIGHT_STARTS = 19
DAY_STARTS = 8
HOUR_DURATION = 1
input_dia_alarma = ""
input_dias_alarma = ""


def write_file_and_screen(text, file_name):
    with open(file_name, "a") as hours_file:
        hours_file.write("{}{}".format(text, "\n"))
        print(text)

opcion_usuario = int(input("Como quieres que suene la alarma: 1-Un dia concreto, 2-Una serie de dias, 3-Todos los dias:"))

if opcion_usuario == 1:
    input_dia_alarma = input("Dime la fecha con el formato dd-mm-aaaa:")
    dia_alarma = datetime.datetime.strptime(input_dia_alarma, "%d-%m-%Y")
elif opcion_usuario == 2:
    input_dias_alarma = input("dime que dias quieres que suene separados por comas aaaa, bbbb, cccc: ")
    input_dias_alarma = input_dias_alarma.split(", ")
    diasint = []

    for i in input_dias_alarma:
        if i == "lunes":
            diasint.append(0)
        if i == "martes":
            diasint.append(1)
        if i == "miercoles":
            diasint.append(2)
        if i == "jueves":
            diasint.append(3)
        if i == "viernes":
            diasint.append(4)
        if i == "sabado":
            diasint.append(5)
        if i == "domingo":
            diasint.append(6)

input_hora_alarma = input("A que hora (00h - 23h): ")


def main():
    hora_alarma = datetime.datetime.strptime(input_hora_alarma, "%H")
    current_time = datetime.datetime.now()
    is_night = False

    while True:
        sleep(HOUR_DURATION)
        current_time += datetime.timedelta(hours=1)
        light_changed = False

        if (current_time.hour >= NIGHT_STARTS or current_time.hour <= DAY_STARTS) and not is_night:
            is_night = True
            light_changed = True

        elif (current_time.hour > DAY_STARTS and current_time.hour < NIGHT_STARTS) and is_night:
            is_night = False
            light_changed = True

        if opcion_usuario == 3 and current_time.hour == hora_alarma.hour:
            write_file_and_screen("ALARMA!", "horas.txt")

        elif opcion_usuario == 1 and current_time.day == dia_alarma.day and current_time.hour == hora_alarma.hour:
            write_file_and_screen("ALARMA!", "horas.txt")

        elif opcion_usuario == 2 and current_time.weekday() in diasint and current_time.hour == hora_alarma.hour:
            write_file_and_screen("ALARMA!", "horas.txt")



        if light_changed:
            if is_night:
                write_file_and_screen("Se ha hecho de noche", "horas.txt")
            else:
                write_file_and_screen("Se ha hecho de día", "horas.txt")




        write_file_and_screen("La hora actual es {}".format(current_time), "horas.txt")


if __name__ == "__main__":
    main()


    #me falta añadir en un rango de dias