#Crear una lista de 5 números al azar entre el 0 y el 9, que estén ordenados y no repetidos
import random #TRAE DE LA LIBRERIA

lista = []

numero = random.randint (0,9)

while len(lista)<5:
    if numero not in lista:
        lista.append(numero)
    numero = random.randint (0,9)

lista.sort()

print(lista)

