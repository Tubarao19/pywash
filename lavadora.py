#proyecto de medicion de tiempo de uso de lavadoras teniendo en cuenta
#que cada hora cuesta $3000 y sabiendo que una vez se llegue a las 
#4h se le reduce en $1000 el precio total
#2- para la siguiente realizar una interfaz para la misma en la libreria tkinter

#libreria de tiempos
from os import system 
system("clear")
from datetime import datetime
price_hour = 3000
#datos a ingresar de entrada y salida

delivery_time = input('Tiempo de entrega de lavadora \n HH:MM am/pm\n>>>')
time_receipt = input('Tiempo de busqueda de lavadora \n HH:MM am/pm\n>>>')
#conversor de tiempos de formato 24h a 12h

delivery_time = datetime.strptime(delivery_time, "%I:%M %p")
time_receipt = datetime.strptime(time_receipt, "%I:%M %p")
usage_time = time_receipt - delivery_time
#conversor de horas a entero
usage_time = int(usage_time.total_seconds()/60/60)#/60(1h=60min)/60(1min=60seg)
#print(usage_time)
#condicionales
#buscar solucion cuando es am o cuando es pm (posiblemente deba recorrerse con ciclo for)
if(usage_time > 4):
    price_total = usage_time * price_hour
else:
    price_total = (usage_time * price_hour) - 1000

#variable de resultado resta

print(f'Tiempo de uso:\n {usage_time}h\n Total a pagar:\n ${price_total:,}')

#variable de resultado en costo
