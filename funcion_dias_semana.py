input_dias_alarma = input("dime que dias quieres que suene separados por comas aaaa, bbbb, cccc: ")
input_dias_alarma = input_dias_alarma.split(", ")
diasint = []

print(input_dias_alarma)

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

print(diasint)