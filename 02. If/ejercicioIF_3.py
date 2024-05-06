numero1=int(input("ingrese un número: "))
numero2=int(input("ingrse otro número: "))
numero3=int(input("ingrese otro número más:"))

if numero1>numero2 and numero2>numero3:
   if numero1 % 2==0:
      print ("El número mayor es ", numero1, " y es par")
   else:
      print ("El numero mayor es", numero1, "y es impar")  
      
if numero2>numero1 and numero2>numero3:
   if numero2 % 2 ==0:
      print ("El número mayor es ", numero2, "y es par")
   else:
      print ("El número mayor es ", numero2, "y es impar")

if numero3>numero1 and numero3>numero2:
   if numero3 %2 ==0:
      print ("El número mayor es: ", numero3, "y es par")
   else:
      print ("El número mayor es ", numero3, " y es impar")


