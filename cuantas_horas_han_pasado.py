

import datetime

fecha_string = input("Introduce una fecha en este formato DD-MM-AAAA: ")
fecha_en_datetime = datetime.datetime.strptime(fecha_string, "%d-%m-%Y")
tiempo_pasado =  fecha_en_datetime - datetime.datetime.now()
horas = int(tiempo_pasado.total_seconds()/3600)


print("Han pasado {} horas desde la fecha que has dicho".format (abs(horas)))