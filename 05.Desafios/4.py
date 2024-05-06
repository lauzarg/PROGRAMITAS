# Tiempo de viaje. Un viajero desea saber cuánto tiempo tomó un viaje que realizó. Él tiene la duración en minutos de cada uno de los tramos del viaje. 
# Desarrolle un programa que permita ingresar los tiempos de viaje de los tramos y entregue como resultado el tiempo total de viaje en formato horas:minutos.
# El programa deja de pedir tiempos de viaje cuando se ingresa un 0.

minViaje = []

while True:
    tiempoViaje= int(input("Ingrese la cantidad de minutos de viaje. Ingrese 0 para terminar: "))
    minViaje.append(tiempoViaje)

    if tiempoViaje == 0:
        break

minutosViaje = 0


for tiempoViaje in minViaje:
    if tiempoViaje>0:
        minutosViaje += tiempoViaje

if minutosViaje>1:
    horas = minutosViaje // 60
    minutos = minutosViaje - (60*horas)

print ("El tiempo total de viaje es", horas,":", minutos, "horas")