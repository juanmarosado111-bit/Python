# Este script le pide al usuario que vaya tecleando números enteros positivos hasta
# que el usuario ingrese el 0. En este caso el programa acaba mostrando el valor
# máximo y mínimo de los números tecleados. El usuario teclea la serie 4,2,3,5,0, El
# máximo es 5 y el mínimo es 2. Si teclea 2,2,2,0, máximo es 2 y mínimo es 2.

import os
os.system("cls")

try:
    numero=int(input("Introduce un numero positivo: "))
    maximo=numero
    minimo=numero

    
    while numero!=0:
        try:
            if numero>maximo:
                maximo=numero
            if numero<minimo:
                minimo=numero
            numero=int(input("Introduce un numero positivo: "))
        except Exception as ex:
            print(f"Ha ocurrido un error, {ex}")
            continue

    print(f"El máximo es {maximo} y el mínimo es {minimo}")
    
except Exception as ex:
    print(f"Ha ocurrido una excepción, {ex}")

