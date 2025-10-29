# Usando un bucle while escribir un script que pida un valor entero y cree una lista
# con los números desde el 0 al valor tecleado. Luego deberá sacar esa lista con un
# alert. Los números se separarán por comas. Si le doy el número 5 pues deberá
# contar 0,1,2,3,4,5

import os
os.system("cls")

numero=int(input("Introduce un numero: "))
contador=0

print("Bucle While:")

try:
    while contador<=numero:
        if contador<numero:
            print(contador, end=", ")
            contador+=1
        else:
            print(contador)
            break
except Exception as excepcion:
    print(f"Ha habido una excepcion, {excepcion}")
finally:
    print("La ejecucion del programa ha finalizado")


print("")    
print("-----------------------------------------------------------------------------------")
print("")


print("Bucle For:")

try:
    for num in range(0,numero+1):
        if num<numero:
            print(num, end=", ")
        else:
            print(num)
except Exception as excepcion:
    print(f"Ha habido una excepcion, {excepcion}")
finally:
    print("La ejecucion del programa ha finalizado")
        
