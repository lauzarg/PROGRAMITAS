# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.

numeroUsuario = int(input("Ingrese un número: "))

if numeroUsuario>3 and (numeroUsuario%2==0 or numeroUsuario%3==0 or numeroUsuario%4==0 or numeroUsuario%5==0):
    print (numeroUsuario, " no es primo: ")
    
elif numeroUsuario%1 == 0 and numeroUsuario/numeroUsuario ==1 :
     print ( numeroUsuario, "es un número primo")
