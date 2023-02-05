import datetime

# saber siempre la fecha y hora actual:
fechaHoraActual = datetime.datetime.now()
print(fechaHoraActual)
print(fechaHoraActual.hour)
print(fechaHoraActual.minute)
print(fechaHoraActual.second)

print("---------------------------------------------------------")

"""
ejercicio:
En una variable llamada minutos, almacena únicamente los minutos de la hora actual.

Por ejemplo, si se ejecutara a las 20:43:17 de la noche, 
la variable minutos debe almacenar el valor 43
"""

fecha_y_hora_actual = datetime.datetime.now()
minutos = fecha_y_hora_actual.minute
print(minutos)

print("---------------------------------------------------------")

# horas:
mi_hora = datetime.time(18, 35, 50) # reloj 24 horas
print(mi_hora) # 18:35:50
print(mi_hora.hour) # 18
print(mi_hora.minute) # 35
print(mi_hora.second) # 50
print(type(mi_hora)) # <class 'datetime.time'>u

print("---------------------------------------------------------")

# dias:
mi_dia = datetime.date(2023, 1, 29) # fecha, los meses deben tener 1 solo digito
print(mi_dia) # 2023-01-29
print(mi_dia.year) # 2023
print(mi_dia.month) # Enero
print(mi_dia.day) # 29
print(type(mi_dia)) # <class 'datetime.date'>

print(mi_dia.ctime()) # Sun Jan 29 00:00:00 2023
print(mi_dia.today()) # simepre muestre la fecha actual

print("---------------------------------------------------------")

from datetime import datetime, date

# fecha muy completa:
mi_fecha = datetime(2025, 5, 15, 22, 10, 15, 2500)
print(mi_fecha) # 2025-05-15 22:10:15.002500

# cambiando mes de la fecha anterior
mi_fecha = mi_fecha.replace(month = 11)
print(mi_fecha) # 2025-11-15 22:10:15.002500

print("---------------------------------------------------------")

# saber cuantos dia vivio una persona:
nacimiento = date(1995, 1, 20)
defuncion = date(2100, 1, 21)

diasVividos = defuncion - nacimiento
print("Dias Vivivos: ", diasVividos)

print("---------------------------------------------------------")

# saber cuantas horas estuvo despierta una persona:
despierta = datetime(2022, 10, 5, 7, 30)
duerme = datetime(2022, 10, 5, 23, 45)

vigilia = duerme - despierta
print(vigilia) # 16:15:00 horas
print(vigilia.seconds) # 58500 segundos despierto

# modulo datetime: https://www.udemy.com/course/python-total/learn/lecture/29023796?start=0#questions
