lado1=float(input("Hola! vamos a analizar qué tipo de triángulo estás viendo. ¿Cuánto mide el primer lado? "))
lado2=float(input("Ahora, decime cuánto mide el segundo lado: "))
lado3=float(input("Por último, decime cuánto mide el tercer lado: "))

if lado1==lado2==lado3:
        print ("El tríangulo es equilátero porque tiene los tres lados iguales")

else:
        if lado1==lado2 and lado1!=lado3:
            print ("Este es un triángulo isósceles porque hay dos lados iguales")
        
        elif lado1==lado3 and lado1!=lado2:
            print ("Este es un triángulo isósceles porque hay dos lados iguales")
        
        elif lado2==lado3 and lado1!=lado2:
            print ("Este es un triángulo isósceles porque hay dos lados iguales")

        elif lado1!=lado2!=lado3:
              print ("Este es un triángulo escaleno porque todos los lados son diferentes")