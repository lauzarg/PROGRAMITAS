personasEdad = []
personasSexo = []

for i in range (3):
    usuarioEdad=int(input(f"Persona  {i+1}, Ingrese su edad por favor "))
    personasEdad.append (usuarioEdad)

for i in range (3):
    usuarioSexo=input(f"Ahora, persona {i+1} ingrese su sexo, [F] para mujer o [M] para hombre  :")
    personasSexo.append (usuarioSexo)

usuarioMayorEdad = 0
usuarioMenorEdad = 0
usuarioMujer = 0
usuarioVaron = 0

for usuarioEdad in personasEdad:
    if usuarioEdad>=18:
        usuarioMayorEdad +=1
    else:
        usuarioMenorEdad +=1

for usuarioSexo in personasSexo:
    if usuarioSexo.upper()=="F":
        usuarioMujer +=1
    elif usuarioSexo.upper()=="M":
        usuarioVaron +=1

print ("La cantidad de mayores de edad es ", usuarioMayorEdad)
print ("La cantidad de menores de edad es ", usuarioMenorEdad)
print ("La cantidad de Mujeres es ", usuarioMujer)
print ("La cantidad de Hombres es ", usuarioVaron)