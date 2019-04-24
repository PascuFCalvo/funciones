

import datetime

#la fecha actual te queda en la variable x con hora fecha y segundos

x = datetime.datetime.now()

#fecha.strftime('%A')
#te devuelve el nombre del dia lunes martes etc pero en ingles asi que le asignamos un valor en español en un diccionario

dicdias = {'MONDAY': 'Lunes', 'TUESDAY': 'Martes', 'WEDNESDAY': 'Miercoles', 'THURSDAY': 'Jueves','FRIDAY': 'Viernes', 'SATURDAY': 'Sabado', 'SUNDAY': 'Domingo'}
ano = x.year
mes = x.month
dia = x.day

fecha = datetime.date(ano, mes, dia)

five_ago = datetime.datetime.now()-datetime.timedelta(days=5)
five_ago = five_ago.strftime("%d del %m de %Y")
week_day = datetime.date.weekday(datetime.datetime.now()-datetime.timedelta(days=5))
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

print("Hace 5 dias era {} y cae en {}".format((five_ago), dia_semana))
