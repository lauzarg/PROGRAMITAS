
numeros = []

for i in range (10):
    numeroAleat=int(input(f"Ingrese un numero {i+1} : "))
    numeros.append(numeroAleat)

numeroMasCien = 0
numeroMenosCien = 0

for numeroAleat in numeros:
    if numeroAleat<100:
        numeroMenosCien += 1

    else:
        numeroMasCien += 1

print ("La cantidad de números mayores a 100 es ", numeroMasCien)
print ("La cantidad de números menores a 100 es ", numeroMenosCien)