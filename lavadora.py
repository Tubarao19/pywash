#proyecto de medicion de tiempo de uso de lavadoras teniendo en cuenta
#que cada hora cuesta $3000 y sabiendo que una vez se llegue a las 
#4h se le reduce en $1000 el precio total
#2- para la siguiente realizar una interfaz para la misma en la libreria tkinter

#libreria de tiempos
from datetime import datetime
#datos a ingresar de entrada y salida
#conversor de tiempos de formato 24h a 12h
delivery_time = input('Tiempo de entrega de lavadora \n Ingrese de la sigt forma Hora:Min am/pm')
time_receipt = datetime.strptime(input('Tiempo de busqueda de lavadora \n Ingrese de la sigt forma Hora:Min am/pm'))

delivery_time = datetime.strptime(delivery_time, "%I:%M %p")
time_receipt = datetime.strptime(time_receipt, "%I:%M %p")
usage_time = delivery_time - time_receipt
#condicionales

#variable de resultado resta

print(f'Tiempo uso total:\n {usage_time}')
#variable de resultado en costo
