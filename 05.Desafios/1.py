#Escriba un programa que pida al usuario un entero de tres dígitos, y entregue el número con los dígitos en orden inverso

numeroTresDig = int(input("Por favor, escriba un número de tres diígitos:  "))

miNum = [int (numero) for numero in str(numeroTresDig)]

print (miNum[-1],miNum[-2],miNum[-3]) 
