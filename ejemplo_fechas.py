import datetime

year = int(input ("Dime el año: "))
month = int(input("Dime el mes: "))
day = int(input("Dime el dia: "))

user_date = datetime.datetime(year=year, month=month, day=day)

time_remaining = user_date - datetime.datetime.now()

print("Faltan {} dias y {} horas".format(time_remaining.days, int(time_remaining.seconds / 3600 )))



#Hasta aqui el programa tu le das una fecha y te dice cuanto falta


print(datetime.datetime.now() + time_remaining)

#En esta linea imprime el dia que sale de sumar el momento actual + lo que falta para el dia que le has dado
#Es decir, que imprime el dia que el usuario le ha puesto

print("Mañana es {}".format(datetime.datetime.now() + datetime.timedelta(days=1)))

#Imprime por pantalla que dia es mañana sumandole el timedelta


manana = datetime.datetime.now() + datetime.timedelta(days=1)
manana_medianoche = datetime.datetime(year= manana.year, month = manana.month, day = manana.day)
hoy = datetime.datetime.now()
falta_para_manana = manana_medianoche - hoy

print("mañana es {}".format(manana))
print("Faltan {} horas para mañana".format(int(falta_para_manana.total_seconds() / 3600)))

#En este trozo, guardamos variables, para que te diga cuanto tiempo falta para mañana a medianoche

print("Mañana es {}".format(manana.strftime("%d del %m de %Y")))

#formateando la fecha con strftime