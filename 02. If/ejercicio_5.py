pregunta=input("Si desea cambiar dólares a pesos, escriba 1. Si desea cambiar pesos a dólares, escriba 2: ")

if pregunta=="1":
    dolares=int(input("¿Cuántos doláres desea cambiar?: "))
    pesos=dolares*1460
    print ("La cantidad de ", dolares, "equivale a ", pesos, "pesos" )

else:
    pesos=int(input("¿Cuántos pesos desea cambiar?: "))
    dolares=pesos/1460
    print ("La cantidad de ", pesos, "equivale a ", dolares, "dólares")