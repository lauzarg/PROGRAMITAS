contador = 0

while contador<5:
    print (contador)
    contador +=1


for i in range(10):
    if i==5:
        break
    print (i)

for i in range(10):
    if i==5:
        continue
    print (i)


for i in range (5):
    print (i)
else:
    print ("El bucle ha terminado sin interrupeciones")
    