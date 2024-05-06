#Escriba un programa que pregunte al usuario la hora actual t del reloj y un número entero de horas h, que indique qué hora marcará el reloj dentro de h horas

horaActual = int(input("Por favor ingrese la hora actual, teniendo en cuenta el formato 24h: "))
hHoras = int(input("y dentro de cuántas horas quiere saber la hora que marcará el reloj, en números enteros:  "))

horaFuturo= (horaActual + hHoras)


while horaFuturo>24:
       horaFuturo-=24

horaReloj = (horaFuturo)

print ("En ", hHoras, " horas el reloj marcará ", horaReloj)