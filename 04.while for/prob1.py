numeros=[]  # Lista vacia

for i in range (4):
    numeroAleatorio=int(input(f"ingrese un número {i+1}: ")) # Va a pedir 4 veces (el rango) al usuario que agregu elementos (numeros al azar)
    numeros.append (numeroAleatorio) # Agrega los elementos que dispone el usuario a la lista 

# Parte de los contadores en 0
numerosPares = 0
numerosImpares = 0
sumaDeNumerosPares = 0


for numeroAleatorio in numeros: #Para los numeros guardados en la lista
    if numeroAleatorio%2 == 0: # si son pares, es decir, el resto da 0
        numerosPares +=1 # agregar el elemento a los numeros pares
        sumaDeNumerosPares += numeroAleatorio #y se los va agregando a la suma

    else:
        numerosImpares += 1 # si no son pares, se agregan a la lista de impares

# muestra de resultados
print ("La cantidad de pares es", numerosPares)
print ("La cantidad de impares es ", numerosImpares )
print ("La suma de los pares da por resultado ", sumaDeNumerosPares)