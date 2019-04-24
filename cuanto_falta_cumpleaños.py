
import datetime

fecha_string = input("Introduce una fecha en este formato DD-MM-AAAA: ")
fecha_en_datetime = datetime.datetime.strptime(fecha_string, "%d-%m-%Y")
falta_cumple = fecha_en_datetime - datetime.datetime.now()
week_day = fecha_en_datetime.weekday()
dia_semana = ""

if week_day == 0:
        dia_semana = "Lunes"
if week_day == 1:
        dia_semana = "Martes"
if week_day == 2:
        dia_semana = "Miercoles"
if week_day == 3:
        dia_semana = "Jueves"
if week_day == 4:
        dia_semana = "Viernes"
if week_day == 5:
        dia_semana = "Sabado"
if week_day == 6:
        dia_semana = "Domingo"


print("Para tu cumpleaños faltan {} dias y caera en {}".format(falta_cumple, dia_semana))