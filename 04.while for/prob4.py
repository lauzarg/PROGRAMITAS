numeros = []

for i in range (4):
    numerosUsuario = int(input(f" {i+1} Ingrese un número entero por favor: "))
    numeros.append (numerosUsuario)

numerosPositivos = 0
sumaDeNumPositivos = 0

for numerosUsuario in numeros:
    if numerosUsuario>0:
        numerosPositivos += 1
        sumaDeNumPositivos += numerosUsuario


print ("La cantidad de números positivos fue", numerosPositivos)
print ("y la suma de esos números da ",sumaDeNumPositivos)
