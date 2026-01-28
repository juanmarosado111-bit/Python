# Rosado Trujillo, Juan Manuel

import os
os.system("cls")

try:
    num=int(input("Introduce un número entero positivo: "))

    for i in range(1,num+1):
        print(f"Tabla del {i}")
        for j in range(1,i+1):
            print(f"{j} x {i} = {j*i}")
            
except Exception as ex:
    print(f"Ha ocurrido un error, {ex}")
    
finally:
    print("La ejecución del codigo ha terminado")     

