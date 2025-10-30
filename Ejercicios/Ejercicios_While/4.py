# Determinar si el número que teclea el usuario es primo o no. Recordar que un
# número primo es el que solo puede dividirse por sí mismo y por la unidad. Si el
# usuario teclea el 3: dirá que 3 es primo. Si teclea el 4 dirá que 4 no es primo.

import os
os.system("cls")

numero=int(input("Introduce un numero: "))
contador=2
primo=True

try:
    while numero>contador:
        if (numero%contador)==0:
            primo=False
        contador+=1


    if primo:
        print("El numero es primo")
    else:
        print("El numero no es primo")

except Exception as ex:
    print(f"Ha ocurrido un error, {ex}")
    
