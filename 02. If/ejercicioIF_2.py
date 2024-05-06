forma_pago=int(input("Ingrese la forma en que desea pagar: 1 si es CONTADO, 2 si es TARJETA y 3 si es DÉBITO: " ))
importe=float(input("ahora ingrese el monto a pagar: "))

if forma_pago==1:
    montototal1= importe - (importe*0.1)
    print ("Lo que debe abonar es $ ", montototal1, "ya que tiene un descuento del 10%")

elif forma_pago==2:
    montototal2=importe+(importe*0.1)
    print ("Lo que debe abonar es $ ", montototal2, "ya que tiene un interés del 10%")

else: 
        montototal3=importe - (importe*0.05)
        print ("Lo que debe abonar es $ ", montototal3, "ya que tiene un descuento del 5%")