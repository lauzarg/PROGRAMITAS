numeros = []
numerosPos = []
numerosNeg = []

for i in range (15):
    numerosUsuario = int(input (f"introduzca 15 números negativos, por favor. {i+1}° : "))
    numeros.append (numerosUsuario)
    
for numerosUsuario in numeros:
      if numerosUsuario<0:
        numerosNeg = numerosUsuario * (-1)
        numerosPos.append (numerosNeg)


print (numerosPos)